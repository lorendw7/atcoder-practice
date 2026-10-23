#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    // Describe the approach and complexity before implementing it.
    int n;
    cin >> n;

    int k;
    cin >> k;

    vector<int> h(n + 1);

    for (int i = 1; i <= n; ++i) {
        cin >> h[i];
    }

    const int inf = numeric_limits<int>::max();
    vector<int> dp(n + 1, inf);

    dp[1] = 0;
    for (int i = 2; i <= n; ++i) {
        for (int d = 1; d <= k && i - d >= 1; ++d) {
            int j = i - d;
            dp[i] = min(dp[i], dp[j] + abs(h[i] - h[j]));
        }
    }

    cout << dp[n] << '\n';

    return 0;
}
