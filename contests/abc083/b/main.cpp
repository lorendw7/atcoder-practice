#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    int a, b;
    cin >> a >> b;

    int ans = 0;

    for (int i = 1; i <= n; ++i) {
        int num = i;
        int sum = 0;
        while (num > 0) {
            sum += num % 10;
            num /= 10;
        }

        if (sum <= b && sum >= a) {
            ans += i;
        }
    }

    cout << ans << '\n';

    return 0;
}
