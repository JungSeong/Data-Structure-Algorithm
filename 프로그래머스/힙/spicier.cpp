#include <string>
#include <vector>
#include <queue>
#include <iostream>

using namespace std;

int solution(vector<int> scoville, int K) {
    int answer = 0;
    priority_queue pq(scoville.begin(), scoville.end(), greater<int>());

    while (!pq.empty() && pq.top() < K)
    {
        if (pq.size() == 1)
        {
            answer = -1;
            return answer;
        }

        auto k1 = pq.top();
        pq.pop();
        auto k2 = pq.top();
        pq.pop();
        pq.push(k1+2*k2);
        answer++;
    }

    return answer;
}

int main()
{
    cout << solution({1, 2, 3, 9, 10, 12}, 7);
}