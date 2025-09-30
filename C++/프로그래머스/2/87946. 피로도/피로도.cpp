#include <string>
#include <vector>
#include <unordered_map>
#include <algorithm>
#include <iostream>

using namespace std;

vector<int> enter_list;

void exploration(int k, int cnt, unordered_map<string, int>& info)
{
    bool canEnter = false;

    for (auto [key, val] : info)
    {
        auto min_health = stoi(key.substr(0, key.find("_")));

        if (k >= min_health && val > 0)
        {
            canEnter = true;
            break;
        }
    }

    if (!canEnter)
    {
        enter_list.push_back(cnt);
        return;
    }

    for (auto& [key, val]: info)
    {
        auto min_health = stoi(key.substr(0, key.find("_")));
        auto minus_health = stoi(key.substr(key.find("_")+1));
        if (k >= min_health && val>0)
        {
            k -= minus_health;
            val--;
            exploration(k, cnt+1, info);
            val++;
            k += minus_health;
        }
    }
}

int solution(int k, vector<vector<int>> dungeons) {
    unordered_map<string, int> info;    

    for (auto elem : dungeons)
    {
        string element = to_string(elem[0])+"_"+to_string(elem[1]);
        info[element]++;
    }

    exploration(k, 0, info);

    sort(enter_list.begin(), enter_list.end());

    return enter_list.back();
}