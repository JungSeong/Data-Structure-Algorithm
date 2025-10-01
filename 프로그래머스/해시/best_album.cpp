#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

int sortByPlays(const pair<string, int>& a, const pair<string, int>&b)
{
    return a.second > b.second;
}

int main()
{
    vector<string> genres = {"classic", "pop", "classic", "classic", "pop", "jazz"};
    vector<int> plays = {500, 600, 150, 800, 2500, 4000};

    map<string, int> m;
    map<string, vector<int>> music;

    for (int i=0; i<genres.size(); i++)
    {
        m[genres[i]] += plays[i];
        music[genres[i]].push_back(plays[i]);
    }

    vector<pair<string, int>> mv(m.begin(), m.end());
    sort(mv.begin(), mv.end(), sortByPlays);

    for (const auto& it : mv)
    {
        for (const auto& [key, value] : music)
        {
            
        }
    }

    // for (const auto& [key, value] : music)
    // {
    //     cout << key << ' ';
    //     for (const auto& it : value)
    //     {
    //         cout << it << ' ';
    //     }
    //     cout << '\n';
    // }
}