/* 
lower_bound() 함수 : <algorithm>에 정의된 함수, 찾고자 하는 key 값보다 같거나 큰 숫자가 배열의 몇 번째에서 처음으로 등장하는지 반환
실제로 몇 번째 인덱스인지 알고 싶으면, lower_bound 값에서 배열의 첫 번째 주소를 가르키는 배열의 이름을 빼주면 된다.
*/

#include <iostream>
#include <vector>
#include <algorithm>
#include <utility>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false); // cin, cout의 동기화 해제 -> I/O 속도가 빨라진다는 특징을 가진다
    cin.tie(NULL); // 입출력 (cin / cout) 의 연결을 끊어 성능을 향상 시킨다
    cout.tie(NULL); // cout을 다른 스트림에 연결하지 않게 함으로써 속도를 향상시킨다.
    
    int N, cnt = 0;
    double X;
    cin >> N;

    vector<double> v, cv;

    for (int i=0; i<N; i++)
    {
        cin >> X;
        v.push_back(X);
    }

    cv = v;
    sort(cv.begin(), cv.end());

    cv.erase(unique(cv.begin(), cv.end()), cv.end());

    for (int i=0; i<N; i++)
    {
        auto idx = lower_bound(cv.begin(), cv.end(), v[i]);
        cout << idx - cv.begin() << ' ';
    }

    return 0;
}