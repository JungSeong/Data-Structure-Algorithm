#include <iostream>

using namespace std;

long Fibo(int n)
{
    if (n == 0) return 0;
    else if (n == 1) return 1;
    else return Fibo(n-2) + Fibo(n-1);
}

int main()
{
    int n;
    cin >> n;

    cout << Fibo(n);
}