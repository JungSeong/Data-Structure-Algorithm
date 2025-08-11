#include <iostream>
#include <queue>

using namespace std;

int main()
{
    int N, front;
    cin >> N;

    queue<int> q;

    for (int idx=1; idx<=N; idx++)
    {
        q.push(idx);
    }

    while (q.size()>1)
    {
        q.pop();
        front = q.front();
        q.pop();
        q.push(front);
    }

    cout << q.front();
}