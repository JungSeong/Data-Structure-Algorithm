#include <iostream>
#include <deque>
#include <vector>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M, T, cnt=0;
    deque<int> dq;
    vector<int> v;

    cin >> N;
    for (int i=0; i<N; i++)
    {
        cin >> M;
        v.push_back(M);
        if (M == 0)
        {
            cnt++;
        }
    }

    for (int i=0; i<N; i++)
    {
        cin >> M;
        if (v[i] == 0)
        {
            dq.push_back(M);
        }
    }

    cin >> T;
    for (int i=0; i<T; i++)
    {
        cin >> M;
        dq.push_front(M);
        cout << dq.back() << ' ';
        dq.pop_back();
    }
}
