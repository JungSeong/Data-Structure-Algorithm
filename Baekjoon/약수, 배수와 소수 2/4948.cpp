#include <iostream>
#include <cmath>

#define true 1

using namespace std;

bool isBool(int n)
{
    if (n == 1) return false;
    if (n == 2) return true;
    if (n % 2 == 0) return false;
    for (int i=3; i<=sqrt(n); i++)
    {
        if (n % i == 0) return false;
    }
    return true;
}

int main()
{
    while (true)
    {
        int n, cnt=0;
        cin >> n;

        if (n == 0) break;

        for (int idx=n+1; idx<=2*n; idx++)
        {
            if (isBool(idx) == true)
            {
                // cout << idx << '\n';
                cnt++;
            }
        }

        cout << cnt << '\n';
    }
}