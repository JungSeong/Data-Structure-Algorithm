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
    int M, N;
    cin >> M >> N;

    vector<bool> EratosTable = GetEratosTable(N);

    for (int i=M; i<=N; i++)
    {
        if (EratosTable[i])
        {
            cout << i << '\n';
        }
    }
}