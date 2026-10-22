"""Small Windows-first wrapper around GCC and online-judge-tools."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shlex
import shutil
import subprocess
import sys
import tempfile
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]


def run(args, **kwargs):
    print('+ ' + subprocess.list2cmdline([str(a) for a in args]), flush=True)
    subprocess.run([str(a) for a in args], check=True, **kwargs)


def oj():
    path = Path(sys.executable).parent / ('oj.exe' if os.name == 'nt' else 'oj')
    if not path.is_file():
        raise ValueError('Install requirements.txt into .venv first; see README.md.')
    return path


def compiler_env():
    env = os.environ.copy()
    # uv's Python home must not leak into GDB's embedded MSYS2 Python.
    env.pop('PYTHONHOME', None)
    env.pop('PYTHONPATH', None)
    fallback = Path('C:/msys64/ucrt64/bin')
    if os.name == 'nt' and fallback.is_dir():
        env['PATH'] = str(fallback) + os.pathsep + env.get('PATH', '')
    compiler = env.get('CXX') or shutil.which('g++', path=env.get('PATH'))
    if not compiler:
        raise ValueError('GCC not found. Install MSYS2 UCRT64 GCC or set CXX to g++.')
    return compiler, env


def source_path(value):
    path = Path(value).resolve()
    if not path.is_file() or path.suffix != '.cpp':
        raise ValueError(f'Expected an existing .cpp file: {path}')
    if not path.is_relative_to(ROOT):
        raise ValueError('Keep practice sources inside this repository.')
    return path


def metadata(source):
    path = source.parent / 'problem.json'
    return json.loads(path.read_text(encoding='utf-8')) if path.exists() else {}


def sample_pairs(source):
    inputs = sorted((source.parent / 'test').glob('*.in'))
    if not inputs:
        raise ValueError('No samples. Download them or create test/custom-1.in and .out.')
    pairs = []
    for inp in inputs:
        out = inp.with_suffix('.out')
        if not out.is_file():
            raise ValueError(f'Missing expected output: {out}')
        pairs.append((inp, out))
    return pairs


def export_cph(source):
    pairs = sample_pairs(source)
    data = metadata(source)
    folder = source.parent / '.cph'
    folder.mkdir(exist_ok=True)
    # VS Code may normalize the Windows drive letter to lowercase.
    paths = {str(source)}
    if os.name == 'nt':
        paths.add(str(source)[0].lower() + str(source)[1:])
        paths.add(str(source)[0].upper() + str(source)[1:])
    for src in paths:
        digest = hashlib.md5(src.encode()).hexdigest()
        target = folder / f'.{source.name}_{digest}.prob'
        if target.exists():
            print(f'Keeping existing CPH cases: {target}')
            continue
        problem = dict(name=data.get('task', source.stem), url=data.get('url', ''),
                       interactive=False, memoryLimit=1024, timeLimit=3000,
                       group=data.get('contest', 'Local'), srcPath=src,
                       tests=[dict(id=i, input=a.read_text(encoding='utf-8'),
                                   output=b.read_text(encoding='utf-8'))
                              for i, (a, b) in enumerate(pairs, 1)])
        target.write_text(json.dumps(problem, indent=2) + '\n', encoding='utf-8')
    print('CPH cases ready. Open the source and press Ctrl+Alt+B.')


def download(source):
    destination = source.parent / 'test'
    if destination.exists() and any(destination.iterdir()):
        print('Keeping existing test files (no overwrites).')
        export_cph(source)
        return
    url = metadata(source).get('url')
    if not url:
        raise ValueError('No problem URL. Use the new command first.')
    # Download to a temporary directory so failed requests leave no partial samples.
    with tempfile.TemporaryDirectory(prefix='.samples-', dir=source.parent) as tmp:
        fresh = Path(tmp) / 'test'
        run([oj(), 'download', url, '--directory', fresh], timeout=120)
        if not list(fresh.glob('*.in')):
            raise ValueError('No public samples found. See the browser fallback in README.')
        destination.mkdir(exist_ok=True)
        for item in fresh.iterdir():
            if item.is_file():
                shutil.copy2(item, destination / item.name)
    export_cph(source)


def new_problem(url):
    parsed = urlparse(url)
    match = re.fullmatch(r'/contests/([a-zA-Z0-9_-]+)/tasks/([a-zA-Z0-9_-]+)/?', parsed.path)
    if parsed.scheme != 'https' or parsed.netloc != 'atcoder.jp' or not match:
        raise ValueError('Use an https://atcoder.jp/contests/CONTEST/tasks/TASK URL.')
    contest, task = match.groups()
    label = task[len(contest) + 1:] if task.startswith(contest + '_') else task
    folder = ROOT / 'contests' / contest / label
    folder.mkdir(parents=True, exist_ok=True)
    source = folder / 'main.cpp'
    if not source.exists():
        shutil.copy2(ROOT / 'templates/main.cpp', source)
    info = folder / 'problem.json'
    if not info.exists():
        info.write_text(json.dumps(dict(contest=contest, task=task,
                        url=f'https://atcoder.jp/contests/{contest}/tasks/{task}'), indent=2) + '\n',
                        encoding='utf-8')
    print(f'Source: {source}', flush=True)
    download(source)


def build(source, debug=False):
    compiler, env = compiler_env()
    executable = source.with_suffix('.exe' if os.name == 'nt' else '.bin')
    args = [compiler, '-std=c++20', '-Wall', '-Wextra', '-Wshadow']
    args += ['-O0', '-g', '-D_GLIBCXX_ASSERTIONS'] if debug else ['-O2']
    if os.name == 'nt':
        args += ['-static']
    run(args + [source, '-o', executable], env=env)
    return executable, env


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    sub.add_parser('new', help='Create a task and download public samples').add_argument('url')
    for name in ('download', 'cph', 'build', 'run', 'test'):
        cmd = sub.add_parser(name)
        cmd.add_argument('source', help='Path to main.cpp')
        if name in ('build', 'run', 'test'):
            cmd.add_argument('--debug', action='store_true')
        if name == 'test':
            cmd.add_argument('--time-limit', type=float, default=3)
            cmd.add_argument('--error', type=float, help='Floating-point absolute/relative tolerance')
    sub.add_parser('doctor', help='Check compiler, debugger, and oj')
    args = parser.parse_args()
    if args.command == 'new':
        new_problem(args.url)
    elif args.command == 'doctor':
        compiler, env = compiler_env()
        run([compiler, '--version'], env=env)
        debugger = shutil.which('gdb', path=env['PATH'])
        if not debugger:
            raise ValueError('GDB not found.')
        run([debugger, '--version'], env=env)
        run([oj(), '--version'])
    else:
        source = source_path(args.source)
        if args.command == 'download':
            download(source)
        elif args.command == 'cph':
            export_cph(source)
        else:
            if args.command == 'test':
                sample_pairs(source)
            executable, env = build(source, args.debug)
            if args.command == 'run':
                run([executable], cwd=source.parent, env=env)
            elif args.command == 'test':
                command = (subprocess.list2cmdline([str(executable)]) if os.name == 'nt'
                           else shlex.quote(str(executable)))
                argv = [oj(), 'test', '-c', command, '-d', source.parent / 'test',
                        '-t', str(args.time_limit)]
                if args.error is not None:
                    argv += ['-e', str(args.error)]
                run(argv, env=env)


if __name__ == '__main__':
    try:
        main()
    except (ValueError, OSError, subprocess.TimeoutExpired) as exc:
        print(f'ERROR: {exc}', file=sys.stderr)
        sys.exit(1)
    except subprocess.CalledProcessError as exc:
        print('Command failed; no success is recorded. See the output above.', file=sys.stderr)
        sys.exit(exc.returncode if 0 < exc.returncode < 256 else 1)
