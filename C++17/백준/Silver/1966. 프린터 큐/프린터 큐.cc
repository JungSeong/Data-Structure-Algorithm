#include <iostream>
#include <deque>
#include <utility>
#include <vector>
using namespace std;
int main()
{
    int T;
    cin >> T;
    int N, M, elem;
    for (int i=0; i<T; i++)
    {
        vector<pair<int, int>> importance; // importance, idx
        cin >> N >> M; // M : idx
        for (int j=0; j<N; j++)
        {
            cin >> elem; // importance
            importance.push_back({elem, j});
        }
        deque<pair<int, int>> dq(importance.begin(), importance.end());
        int cnt = 1;
        while (true)
        {
            auto cur = dq.front();
            dq.pop_front();
            bool HasHigher = false;
            for (const auto& elem : dq) // for문 내에서 dq를 조작하는 로직이 있으면 위험함
            {
                if (cur.first < elem.first) {HasHigher = true; break;}
            }
            if (HasHigher) {dq.push_back(cur);}
            else
            {
                if (cur.second == M)
                {
                    cout << cnt << '\n';
                    break;
                }
                cnt++;
            }
        }
    }
}