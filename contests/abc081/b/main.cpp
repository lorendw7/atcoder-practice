#include <bits/stdc++.h>
using namespace std;

// Independently written during practice. Simulate each simultaneous division.
// Time: O(N log(max(A))); space: O(N).
int main() {
    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    int ans = 0;
    bool flag = true;
    while (flag) {
        for (int i = 0; i < n; ++i) {
            if (a[i] % 2 != 0) {
                flag = false;
            }
        }
        if (flag) {
            for (int i = 0; i < n; ++i) {
                a[i] /= 2;
            }
            ans++;
        }
    }
    cout << ans << '\n';
    return 0;
}
