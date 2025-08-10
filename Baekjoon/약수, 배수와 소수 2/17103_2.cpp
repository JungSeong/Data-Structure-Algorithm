#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

vector<bool> GetEratosTable(int N)
{
    vector<bool> EratosTable(N+1, true);
    EratosTable[0] = false;
    EratosTable[1] = false;

    for (int idx=2; idx<=N; idx++)
    {
        EratosTable[idx] = true; //init
    }

    for (int idx=2; idx<=sqrt(N); idx++)
    {
        if (EratosTable[idx] == true)
        {
            for (int j = idx*idx; j<=N; j+=idx)
            {
                if (j%idx == 0)
                {
                    EratosTable[j] = false;
                }
            }
        }
    }

    return EratosTable;
}

int main()
{
    int T, N, cnt;
    cin >> T;

    vector<bool> EratosTable = GetEratosTable(1000000);

    for (int idx=0; idx<T; idx++)
    {
        cnt = 0;
        cin >> N;

        for (int i=2; i<=N/2; i++)
        {
            if(EratosTable[i] == true && EratosTable[N-i] == true)
            {
                cnt++;
            }
        }

        cout << cnt << '\n';
    }
}