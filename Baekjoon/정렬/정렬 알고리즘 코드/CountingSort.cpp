#include <iostream>
#include <vector>

using namespace std;

int main()
{
    vector<int> v = {3,1,2,2,4,5};
    vector<int> sorted_v(v.size());

    int max = v[0], idx, c_idx;

    for (int i=0; i<v.size();i++) // 원 배열의 MAX 값 구하기
    {
        if (max < v[i])
        {
            max = v[i];
        }
    }

    vector<int> cv(max+1); // (MAX값+1)의 크기로 카운팅 배열 만들기
    int j = 0;

    for (int i=0; i<v.size(); i++) // 카운팅 배열에 원 배열의 각 원소의 개수 대입하기
    {
        cv[v[i]]++;
    }

    for (int i=1; i<cv.size(); i++) // 누적합을 다음 원소에 대입해 가기
    {
        cv[i] = cv[i-1] + cv[i];
    }

    for (int i=0; i<v.size(); i++) // 입력 배열과 동일한 크기의 배열을 생성하고, 새로운 배열에 정렬된 값을 대입해 나간다.
    {
        c_idx = v[i];
        idx = cv[c_idx] - 1;
        sorted_v[idx] = c_idx;
        
        for (int j=0; j<sorted_v.size(); j++)
        {
            cout << sorted_v[j] << ' ';
        }
        cout << '\n';

        cv[c_idx]--;
    }

    for (int i=0; i<v.size(); i++)
    {
        cout << sorted_v[i] << ' ';
    }

    return 0;
}