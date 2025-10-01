#include <string>
#include <vector>
#include <iostream>
#include <queue>
#include <cmath>

using namespace std;

vector<int> answer;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    int remain;
    queue<int> q;
    for (int i=0; i<progresses.size(); i++)
    {
        remain = (int)ceil((100 - progresses[i])/speeds[i]);
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

int main()
{
    answer = solution({1, 99, 1}, {5, 1, 5});

    for (const auto&it : answer)
    {
        cout << it << ' ';
    }
}