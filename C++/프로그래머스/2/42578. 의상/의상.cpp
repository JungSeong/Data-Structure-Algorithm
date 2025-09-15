#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

int solution(vector<vector<string>> clothes) {
    unordered_map<string, int> clothmap;
    for (int i=0; i<clothes.size(); i++)
    {
        clothmap[clothes[i][1]]++;
    }
    
    int answer = 1;
    
    for (const auto& [key, value] : clothmap)
    {
        answer *= (value+1);
    }

    return answer-1;
}