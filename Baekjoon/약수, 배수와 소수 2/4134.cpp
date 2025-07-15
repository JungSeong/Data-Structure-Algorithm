#include <iostream>
#include <cmath>

using namespace std;

bool isPrime(long n)
{
    if (n < 2) return false;
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
    cin.tie(NULL);
    cout.tie(NULL);

    int T;
    long num;
    cin >> T;

    for (int idx=0; idx<T; idx++)
    {
        cin >> num;

        while(true)
        {
            if (isPrime(num) == false) num++;
            else
            {
                cout << num << '\n';
                break;
            }
        }
    }
}