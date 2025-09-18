#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
    vector<int> answer;
    
    for (const auto& elem : commands)
    {
        vector<int> parsed;
        for (int i=elem[0]-1; i<=elem[1]-1; i++)
        {
            parsed.push_back(array[i]);
        }
        sort(parsed.begin(), parsed.end());
        answer.push_back(parsed[elem[2]-1]);
    }
    
    return answer;
}