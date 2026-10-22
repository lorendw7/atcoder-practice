#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    // Describe the approach and complexity before implementing it.
    int n, m;
    cin >> n >> m;

    vector<vector<char>> grid(n, vector<char>(m));

    int ans = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            cin >> grid[i][j];
            if (grid[i][j] == '.') {
                ans++;
            }
        }
    }
    vector<vector<int>> dist(n, vector<int>(m, -1));
    queue<pair<int, int>> q;

    q.push({0, 0});
    dist[0][0] = 0;

    int dr[4] = {-1, 1, 0, 0};
    int dc[4] = {0, 0, -1, 1};

    while (!q.empty()) {
        auto cell = q.front();
        q.pop();

        auto r = cell.first;
        auto c = cell.second;

        for (int i = 0; i < 4; ++i) {
            int nr = r + dr[i];
            int nc = c + dc[i];

            if (nr < 0 || nr >= n || nc < 0 || nc >= m) {
                continue;
            }

            if (dist[nr][nc] != -1 || grid[nr][nc] == '#') {
                continue;
            }

            dist[nr][nc] = dist[r][c] + 1;
            q.push({nr, nc});
        }
    }

    if (dist[n - 1][m - 1] != -1) {
        ans = ans - dist[n - 1][m - 1] - 1;
        cout << ans << '\n';
    } else {
        cout << -1 << '\n';
    }

    return 0;
}
