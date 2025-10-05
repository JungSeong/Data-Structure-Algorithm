#include <iostream>

using namespace std;

int main()
{
    int N;
    cin >> N;
    
    int ppl[N];
    for (int i=0; i<N; i++) {cin >> ppl[i];}
    
    int B, C;
    cin >> B >> C;
    
    long long cnt = 0;
    
    for (auto& elem : ppl)
    {
        elem -= B;
        cnt++;

        if (elem >= 1) // 부 감독관도 필요
        {
            cnt += elem / C;
            if (elem % C != 0)
            {
                cnt++;
            }
        }
    }
    
    cout << cnt;
}