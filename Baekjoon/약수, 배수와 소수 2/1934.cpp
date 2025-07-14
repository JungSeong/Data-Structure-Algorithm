#include <iostream>

using namespace std;

int main()
{
    cin.tie(NULL);
    cout.tie(NULL);

    int T, A, B, cnt = 0, multiple = 1;
    cin >> T;

    for (int idx=0; idx<T; idx++)
    {
        cin >> A >> B;
        int smaller = A < B ? A : B;
        int larger = A > B ? A : B;
        multiple = 1;

        for (int i=1; i<=smaller; i++)
        {
            cnt = 0;

            for (int ii=1; ii<=i; ii++)
            {
                if (i % ii == 0) {cnt++;}
            }

            if (cnt == 2 && smaller % i == 0)
            {
                while (smaller % i == 0 && larger % i == 0)
                {
                    smaller /= i;
                    larger /= i;
                    multiple *= i;
                }
            }
        }
        cout << multiple * smaller * larger << '\n';
    }
}