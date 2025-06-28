#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <unordered_set>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
	cin.tie(0);
    cout.tie(0);

    int n;
    string name, is_in;

    cin >> n;
    unordered_set<string> member;

    for (int idx=0; idx<n; idx++)
    {
        cin >> name >> is_in;
        if (is_in == "enter")
        {
            member.insert(name);
        }
        else
        {
            member.erase(name);
        }
    }

    vector member_vec(member.begin(), member.end());
    sort(member_vec.begin(), member_vec.end(), greater<string>());

    for (auto iter = member_vec.begin(); iter != member_vec.end(); iter++)
    {
        cout << *iter << '\n';
    }
}