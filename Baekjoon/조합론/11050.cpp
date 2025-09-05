#include <iostream>

using namespace std;

int main()
{
    int N, K, result=1;
    cin >> N >> K;

    if (K == 0) cout << 1;
    else
    {
        for (int i=1; i<=K; i++)
        {
            result = result * (N-i+1)/i;
        }
    
        cout << result;
    }
}