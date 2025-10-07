#include <bits/stdc++.h>

using namespace std;

vector<int> solution(vector<string> name, vector<int> yearning, vector<vector<string>> photo) {
    unordered_map<string, int> info;
    vector<int> answer;
    
    for (int i=0; i<name.size(); i++)
    {
        info[name[i]] = yearning[i];
    }
    
    for (int i=0; i<photo.size(); i++)
    {
        int score = 0;
        for (int j=0; j<photo[i].size(); j++)
        {
            if (info[photo[i][j]])
            {
                score += info[photo[i][j]];
            }
        }
        answer.push_back(score);
    }
    
    return answer;
}