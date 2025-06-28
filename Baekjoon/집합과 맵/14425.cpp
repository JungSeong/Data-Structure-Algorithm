#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <unordered_set>

using namespace std;

int main()
{
    int N, M, cnt=0;
    string str;
    cin >> N >> M;

    unordered_set<string> str_set;
    
    for (int idx=0; idx<N; idx++)
    {
        cin >> str;
        str_set.insert(str);
    }

    vector<string> str_comp_vec;

    for (int idx=0; idx<M; idx++)
    {
        cin >> str;
        str_comp_vec.push_back(str);
    }

    for (auto iter = str_comp_vec.begin(); iter != str_comp_vec.end(); iter++)
    {
        if (auto iiter = str_set.find(*iter); iiter != str_set.end())
        {
            cnt++;
        }
    }

    cout << cnt;
}