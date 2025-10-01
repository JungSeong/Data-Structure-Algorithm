#include <iostream>
#include <vector>

using namespace std;

int Fibocnt = 0;
int FiboDycnt = 0;

int n;

int Fibo(int n)
{
    if (n==1 || n==2) {Fibocnt++; return 1;}
    else {return Fibo(n-1) + Fibo(n-2);}
}

int Fibo_Dy(int n, vector<int>& memo) {
    if (memo[n]) return memo[n];
    if (n <= 2) return memo[n] = 1;
    FiboDycnt++; // dp 덧셈 1회
    return memo[n] = Fibo_Dy(n-1, memo) + Fibo_Dy(n-2, memo);
}

int main()
{
    cin >> n;
    vector<int> memo(n+1, 0);

    Fibo(n);
    Fibo_Dy(n, memo);

    cout << Fibocnt << ' ' << FiboDycnt;
}