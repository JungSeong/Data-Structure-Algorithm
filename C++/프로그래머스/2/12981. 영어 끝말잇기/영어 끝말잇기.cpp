#include <bits/stdc++.h>

using namespace std;

vector<int> solution(int n, vector<string> words) {
    vector<int> answer;
    bool isDiff = false;
    bool isIn = false;
    int idx1=101, idx2=101, idx;
    
    for (int i=0; i<words.size()-1; i++)
    {
        if (words[i].back() != words[i+1].front())
        {
            isDiff = true;
            idx1 = i+1;
            break;
        }
    }
    
    unordered_map<string, int> sentence;
    
    for (int i=0; i<words.size(); i++)
    {
        if (!sentence.empty() && sentence[words[i]] == 1) // 이미 있는 경우
        {
            isIn = true;
            idx2 = i;
            break;
        }
        sentence[words[i]]++;
    }
    
    if (!isDiff && !isIn)
    {
        answer = {0, 0};
    }
    else
    {
        idx = min(idx1, idx2);
        answer = {idx%n+1, idx/n+1};
    }

    return answer;
}