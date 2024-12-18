/* 
1MB = 1024KB,
1KB = 1024B
int형 = 4B

8 MB = 8 * 1024 * 1024 = 4 * x
-> x는 2,097,152로 10,000,000개의 읿력을 받아야 하는데 이걸 못 한다. 
따라서 각 원소가 몇 개 있는지 확인하는 '카운팅 정렬'을 사용하여야 한다.
*/

#include <iostream>
#include <vector>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false); // cin, cout의 동기화 해제 -> I/O 속도가 빨라진다는 특징을 가진다
    cin.tie(NULL); // 입출력 (cin / cout) 의 연결을 끊어 성능을 향상 시킨다
    cout.tie(NULL); // cout을 다른 스트림에 연결하지 않게 함으로써 속도를 향상시킨다.

    int N;
    cin >> N;

    int input, idx, c_idx;
    vector<int> cv;

    for (int i=0; i<N; i++)
    {   
        cin >> input;

        if (input > cv.size())
        {
            cv.resize(input);
        }

        cv[input-1]++;
    }

    for (int i=1; i<=cv.size(); i++)
    {
        for (int ii=0; ii<cv[i-1]; ii++)
        {
            cout << i << '\n';
        }
    }

    return 0;
}