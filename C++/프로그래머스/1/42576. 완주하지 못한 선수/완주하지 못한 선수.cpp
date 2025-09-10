#include <string>
#include <vector>
#include <unordered_map>
#include <iostream>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    unordered_map<string, int> p;
    unordered_map<string, int> c;
    
    for (const auto& elem : participant)
    {
        p[elem]++;
    }
    
    for (const auto& elem : completion)
    {
        c[elem]++;
    }
    
    string answer = "";
    
    for (const auto& [key, value] : c)
    {
        if (auto search = p.find(key); search != p.end())
        {
            p[key]-=value;
        }
    }
    
    for (const auto& [key, value] : p)
        if (value != 0) {answer = key;}
    
    return answer;
}