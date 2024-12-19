/* 
2차원 배열을 정렬하기 위해서는 vector을 사용해야 한다.
pair 클래스 : 2차원 좌표 저장에 유용하게 사용됨, #include <utility>를 통해 불러올 수 있음

생성 : pair <type1, type2> pv
초기화 : make_pair(pv_x, pv_2)

인자의 첫 번째 값 : pv_x.first
인자의 두 번째 값 : pv_x.second

오름차순 정렬은 기본, sort(pv.begin(), pv.end()) 하면 된다 -> first 값을 기준으로 오름차순 정렬,
first 값이 같으면 second 값을 기준으로 정렬해 준다
내림차순 정렬을 원하면 sort(pv.begin(), pv.end(), greater<pair<int, int>>()) 로 선언
*/

#include <iostream>
#include <vector>
#include <algorithm> // sort 함수를 불러 오는 라이브러리
#include <utility> // pair 클래스를 불러 오는 라이브러리

using namespace std;

bool cmp(pair<int, int> a, pair<int, int> b)
{
    if (a.second != b.second) // y 좌표가 다르면
    {
        return a.second < b.second; // y 좌표를 기준으로 오름차순 정렬
    }
    else
    {
        return a.first < b.first; // x 좌표를 기준으로 오름차순 정렬
    }
}

int main()
{
    int N, pv_x, pv_y;
    cin >> N;

    vector<pair<int, int>> pv;
    
    for (int i=0; i<N; i++)
    {
        cin >> pv_x >> pv_y;
        pv.push_back(make_pair(pv_x, pv_y));
    }

    sort(pv.begin(), pv.end(), cmp);

    for (int i=0; i<N; i++)
    {
        cout << pv[i].first << ' ' << pv[i].second << '\n';
    }

    return 0;
}