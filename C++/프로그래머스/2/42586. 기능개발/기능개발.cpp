#include <string>
#include <vector>
#include <iostream>
#include <queue>
#include <cmath>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    int remain;
    queue<int> q;
    vector<int> answer;
    for (int i=0; i<progresses.size(); i++)
    {
        remain = (int)ceil((100.0 - progresses[i])/speeds[i]);
        q.push(remain);
    }
    
    int i=1;
    while(!q.empty())
    {
        int cnt=0;
        if (q.front() <= i)
        {
            while (!q.empty() && q.front() <= i)
            {
                q.pop();
                cnt++;
            }
            answer.push_back(cnt);
        }
        i++;
    }
    
    return answer;
}