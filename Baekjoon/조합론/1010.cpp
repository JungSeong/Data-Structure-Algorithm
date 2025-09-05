#include <iostream>

using namespace std;

int main()
{
    int T, N, M;
    cin >> T;

    for (int idx = 0; idx < T; idx++)
    {
        cin >> N >> M;

        // 오버플로우를 방지하는 방식으로 조합 계산
        unsigned long long int result = 1;
        for (int i = 1; i <= N; i++)
        {
            result = result * (M - i + 1) / i;
        }

        cout << result << '\n';
    }
    
    return 0;
}