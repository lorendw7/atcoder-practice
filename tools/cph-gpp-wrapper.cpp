#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <process.h>
#include <string>
#include <vector>

int main(int argc, char* argv[]) {
    constexpr char compiler[] = "C:\\msys64\\ucrt64\\bin\\g++.exe";
    constexpr char compiler_dir[] = "C:\\msys64\\ucrt64\\bin";

    const char* old_path = std::getenv("PATH");
    std::string path = compiler_dir;
    if (old_path != nullptr && *old_path != '\0') {
        path += ";";
        path += old_path;
    }
    if (_putenv_s("PATH", path.c_str()) != 0) {
        std::cerr << "Failed to prepare PATH for MSYS2 UCRT64 GCC.\n";
        return 127;
    }

    std::vector<const char*> compiler_args;
    compiler_args.reserve(static_cast<std::size_t>(argc) + 1);
    compiler_args.push_back(compiler);
    for (int i = 1; i < argc; ++i) {
        compiler_args.push_back(argv[i]);
    }
    compiler_args.push_back(nullptr);

    const intptr_t result =
        _spawnv(_P_WAIT, compiler, compiler_args.data());
    if (result == -1) {
        std::perror("Failed to start MSYS2 UCRT64 GCC");
        return 127;
    }
    return static_cast<int>(result);
}
