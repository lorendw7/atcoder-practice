#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    // Describe the approach and complexity before implementing it.
    int a, b, c, x;

    cin >> a >> b >> c >> x;

    int ans = 0;

    for (int i = 0; i <= a; ++i) {
        for (int j = 0; j <= b; ++j) {
            for (int k = 0; k <= c; ++k) {
                int s = i * 500 + 100 * j + k * 50;
                if (s == x) {
                    ans++;
                }
            }
        }
    }

    cout << ans << '\n';
    return 0;
}
