#include <string>
#include <vector>
#include <iostream>
#include <deque>

using namespace std;

int solution(vector<int> priorities, int location) {
    deque<pair<int, int>> dq;
    int i=0, front, answer = 0;;
    
    for (const auto& it : priorities)
    {
        dq.push_back({it,i});
        i++;
    }
    
    while (!dq.empty())
    {
        auto cur = dq.front();
        bool isOkay = true;
        dq.pop_front();
        
        for (const auto& it : dq)
        {
            if (it.first > cur.first)
            {
                isOkay = false;
                dq.push_back(cur);
                break;
            }
        }
        
        if (isOkay)
        {
            answer++;
            if (cur.second == location)
            {
                return answer;
            }
        }    
    }
}