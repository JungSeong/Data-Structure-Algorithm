#include <iostream>
#include <deque>
#include <string>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M;
    string str;
    deque<int>d;

    cin >> N;
    cin.ignore();

    for (int idx=0; idx<N; idx++)
    {
        getline(cin, str);

        if (str[0] == '1')
        {
            M = stoi(str.substr(2));
            d.push_front(M);
        }
        else if (str[0] == '2')
        {
            M = stoi(str.substr(2));
            d.push_back(M);
        }
        else if (str[0] == '3')
        {
            if (!d.empty())
            {
                cout << d.front() << '\n';
                d.pop_front();
            }
            else
            {
                cout << -1 << '\n';
            }
        }
        else if (str[0] == '4')
        {
            if (!d.empty())
            {
                cout << d.back() << '\n';
                d.pop_back();
            }
            else
            {
                cout << -1 << '\n';
            }
        }
        else if (str[0] == '5')
        {
            cout << d.size() << '\n';
        }
        else if (str[0] == '6')
        {
            if (d.empty())
            {
                cout << 1 << '\n';
            }
            else
            {
                cout << 0 << '\n';
            }
        }
        else if (str[0] == '7')
        {
            if (!d.empty())
            {
                cout << d.front() << '\n';
            }
            else
            {
                cout << -1 << '\n';
            }
        }
        else if (str[0] == '8')
        {
            if (!d.empty())
            {
                cout << d.back() << '\n';
            }
            else
            {
                cout << -1 << '\n';
            }
        }
    }
}