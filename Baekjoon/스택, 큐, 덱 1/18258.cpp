#include <iostream>
#include <queue>
#include <string>
#include <stdlib.h>

using namespace std;

int main()
{
    cin.tie(NULL);
    cout.tie(NULL);

    int N;
    string str;
    cin >> N;
    cin.ignore();

    queue<int> q;

    for (int idx=0; idx<N; idx++)
    {
        getline(cin, str);
        
        if (str == "pop")
        {
            if (q.empty())
            {
                cout << -1 << '\n';
            }
            else
            {
                cout << q.front() << '\n';
                q.pop();
            }
        }
        else if (str == "size")
        {
            cout << q.size() << '\n';
        }
        else if (str == "empty")
        {
            if (q.empty()) cout << 1 << '\n';
            else cout << 0 << '\n';
        }
        else if (str == "front")
        {
            if (q.empty()) cout << -1 << '\n';
            else cout << q.front() << '\n';
        }
        else if (str == "back")
        {
            if (q.empty()) cout << -1 << '\n';
            else cout << q.back() << '\n';
        }
        else
        {
            size_t pos = str.find(" ");
            string substr = str.substr(pos+1);
            q.push(stoi(substr));
        }
    }
}