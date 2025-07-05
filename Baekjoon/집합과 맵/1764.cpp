#include <iostream>
#include <string>
#include <unordered_set>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int N, M;
    string name;
    cin >> N >> M;

    cin.ignore();

    unordered_set<string> not_heard_before;
    unordered_set<string> not_seen_before;

    for (int idx=0; idx<N; idx++)
    {
        getline(cin, name);
        not_heard_before.insert(name);
    }

    for (int idx=0; idx<M; idx++)
    {
        getline(cin, name);
        not_seen_before.insert(name);
    }

    vector<string> result;

    for (auto it = not_heard_before.begin(); it != not_heard_before.end(); it++)
    {
        if (auto search = not_seen_before.find(*it); search != not_seen_before.end())
        {
            result.push_back(*search);
        }
    }

    sort(result.begin(), result.end());

    cout << result.size() << '\n';

    for (auto it = result.begin(); it != result.end(); it++)
    {
        cout << *it << '\n';
    }
}