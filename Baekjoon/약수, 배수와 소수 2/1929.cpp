#include <iostream>
#include <cmath>

using namespace std;

bool isPrime(int idx)
{
    if (idx == 1)
    {
        return false;
    }
    if (idx == 2)
    {
        return true;
    }
    if (idx % 2 == 0)
    {
        return false;
    }
    for (int n=3; n<=sqrt(idx); n++)
    {
        if (idx % n == 0)
        {
            return false;
        }
    }
    return true;
}

int main()
{
    int M, N;
    cin >> M >> N;

    for (int idx=M; idx<=N; idx++)
    {
        if (isPrime(idx) == true)
        {
            cout << idx << '\n';
        }
    }
}