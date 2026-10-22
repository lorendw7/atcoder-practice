#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    // Describe the approach and complexity before implementing it.
    int n;
    cin >> n;

    vector<int> a(n);

    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    int alice = 0;
    int bob = 0;
    sort(a.begin(), a.end(), greater<int>());

    for (int i = 0; i < n; ++i) {
        if (i % 2 == 0) {
            alice += a[i];
        } else {
            bob += a[i];
        }
    }

    cout << alice - bob << '\n';
    return 0;
}
