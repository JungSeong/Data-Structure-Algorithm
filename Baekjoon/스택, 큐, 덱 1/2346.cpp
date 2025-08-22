#include <iostream>
#include <deque>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N, e, front, len;
    int front_idx;
    deque<int> d;
    deque<int> id;
    cin >> N;

    for (int i=0; i<N; i++)
    {
        cin >> e;
        d.push_back(e);
        id.push_back(i+1);
    }

    while (!d.empty())
    {
        if (d.front() > 0)
        {
            front = d.front();
            front_idx = id.front();
            cout << front_idx << ' ';
            d.pop_front();
            id.pop_front();
            if (d.empty())
            {
                break;
            }
            len = d.size();
            len = (front-1) % len;

            for (int i=0; i<len; i++)
            {
                front = d.front();
                d.pop_front();
                d.push_back(front);

                front_idx = id.front();
                id.pop_front();
                id.push_back(front_idx);
            }
        }
        else
        {
            front = d.front() * -1;
            front_idx = id.front();
            cout << front_idx << ' ';
            d.pop_front();
            id.pop_front();
            if (d.empty())
            {
                break;
            }
            len = d.size();
            len = len - (front % len);

            for (int i=0; i<len; i++)
            {
                front = d.front();
                d.pop_front();
                d.push_back(front);

                front_idx = id.front();
                id.pop_front();
                id.push_back(front_idx);
            }
        }
    }
}