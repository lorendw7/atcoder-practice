#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    // Describe the approach and complexity before implementing it.
    int c[3][3];
    bool ok = true;

    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 3; ++j) {
            cin >> c[i][j];
        }
    }
    for (int i = 1; i < 3; ++i) {
        int diff = c[i][0] - c[i - 1][0];
        for (int j = 0; j < 3; ++j) {
            int a = c[i][j] - c[i - 1][j];
            if (diff != a) {
                ok = false;
            }
        }
    }

    if (ok) {
        cout << "Yes\n";
    } else {
        cout << "No\n";
    }
    return 0;
}
