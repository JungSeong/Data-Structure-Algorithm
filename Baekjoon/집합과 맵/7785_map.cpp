#include <iostream>
#include <algorithm>
#include <map>
#include <string>

using namespace std;

int main()
{
    int n;
    string name, is_in;
    map<string, string, greater<string>> member;

    cin >> n;

    for (int idx=0; idx<n; idx++)
    {
        cin >> name >> is_in;
        member[name] = is_in;
    }

    for (auto iter = member.begin(); iter != member.end(); iter++)
    {
        if (iter->second == "enter")
        {
            cout << iter->first << '\n';
        }
    }
}