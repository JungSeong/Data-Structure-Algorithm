#include <iostream>
#include <queue>
#include <stack>
#include <vector>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M, T;
    queue<int> q;
    vector<int> v;

    cin >> N;
    for (int i=0; i<N; i++)
    {
        cin >> M;
        v.push_back(M);
    }

    for (int i=0; i<N; i++)
    {
        cin >> M;
        if (v[i] == 0)
        {
            q.push(M);
        }
        else
        {
            s.push(M);
        }
    }

    cin >> T;
    for (int i=0; i<T; i++)
    {
        cin >> M;
        for (int ii=0; ii<N; ii++)
        {
            if (v[ii]==0)
            {
                q.push(M);
                M = q.front();
                q.pop();
            }
        }

        cout << M << ' ';
    }
}
