#include <iostream>
#include <cmath>

using namespace std;

bool isPrime(int num)
{
    if (num == 1) return false;
    if (num == 2) return true;
    if (num % 2 == 0) return false;
    for (int n=3; n<=sqrt(num); n++)
    {
        if (num % n == 0) return false;
    }
    return true;
}

int main()
{
    cin.tie(NULL);
    cout.tie(NULL);

    int T, N, cnt=0;
    cin >> T;

    for (int i=0; i<T; i++)
    {
        cnt = 0;
        cin >> N;

        for (int i=2; i<=N/2; i++)
        {
            if (isPrime(i) == true && isPrime(N-i) == true)
            {
                cnt++;
            }
        }

        cout << cnt << '\n';
    }
}