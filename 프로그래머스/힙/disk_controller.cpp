#include <iostream>
#include <string>
#include <vector>
#include <queue>

using namespace std;

bool customSort(vector<vector<int>> &a, vector<vector<int>>> &b)
{
    return a[]
}

int solution(vector<vector<int>> jobs) {
    int answer = 0, idx=0, cur_time=0;
    vector<vector<vector<int>>> vjob;
    for (int i=0; i<jobs.size(); i++)
    {
        vjob[i][0] = jobs[i][0];
        vjob[i][1] = jobs[i][1];
        vjob[i][2] = idx;
        idx++;
    }

    priority_queue pq(vjob.begin(), vjob.end(), customSort);

    return answer;
}

int main()
{
    solution{{{0,3}, {1,9}, {3,5}}};
}