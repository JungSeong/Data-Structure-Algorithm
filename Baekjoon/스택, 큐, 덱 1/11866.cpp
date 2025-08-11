#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int main()
{
    int N, K, top;
    cin >> N >> K;

    queue<int> q;
    vector<int> v;
    
    for (int i=1; i<=N; i++)
    {
        q.push(i);
    }

    for (int i=0; i<N; i++)
    {
        for (int ii=0; ii<K-1; ii++)
        {
            top = q.front();
            q.pop();
            q.push(top);
        }
        v.push_back(q.front());
        q.pop();
    }

    cout << "<";
    for (auto it=v.begin(); it!=v.end()-1; it++)
    {
        cout << *it << ", ";
    }

    auto it=v.end()-1;
    cout << *it << ">";
}