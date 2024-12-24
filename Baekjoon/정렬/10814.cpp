#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <utility>

using namespace std;

bool cmp(pair<int, int> pv1, pair<int, int> pv2)
{
    if (pv1.first != pv2.first)
    {
        return pv1.first < pv2.first;
    }
    else
    {
        return pv1.second < pv2.second;
    }
}

int main()
{
    int N, pv_age, pv_idx = 0;
    string name;
    cin >> N;
    
    vector<pair<int, int>> pv;
    vector<string> v_name;

    for (int i=0; i<N; i++)
    {
        cin >> pv_age >> name;
        pv.push_back(make_pair(pv_age, pv_idx));
        v_name.push_back(name);

        pv_idx++;
    }

    sort(pv.begin(), pv.end(), cmp);

    for (int i=0; i<N; i++)
    {
        cout << pv[i].first << ' ' << v_name[pv[i].second] << '\n';
    }

    return 0;
}