#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <utility>

using namespace std;

bool sortByPlayed(const pair<string, int>&a, const pair<string, int>&b)
{
    return a.second > b.second;
}

bool sortByNum(const pair<int, int>&a, const pair<int, int>&b)
{
    if (a.first == b.first)
    {
        return a.second < b.second;
    }
    return a.first > b.first;
}

vector<int> solution(vector<string> genres, vector<int> plays) {
    map<string, int> m;
    map<string, vector<pair<int, int>>> music;
    vector<int> answer;
    
    for (int i=0; i<genres.size(); i++)
    {
        m[genres[i]] += plays[i];
        music[genres[i]].push_back(make_pair(plays[i], i));
    }
    
    vector<pair<string, int>> mv(m.begin(), m.end());
    sort(mv.begin(), mv.end(), sortByPlayed);
    
    for (const auto& genre : mv)
    {
        vector<pair<int, int>> musicv(music[genre.first].begin(), music[genre.first].end());
        sort(musicv.begin(), musicv.end(), sortByNum);
        
        answer.push_back(musicv[0].second);
        if (musicv.size() > 1) {answer.push_back(musicv[1].second);}
    }

    return answer;
}