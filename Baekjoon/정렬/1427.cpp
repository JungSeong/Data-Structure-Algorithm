/*
문자열의 길이 : num.length()
벡터의 크기 : v.size()

문자를 숫자로 : char - '0'
내림차순으로 sort -> compare() 함수 구현 후 sort에 compare 넣기
*/

#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>

using namespace std;

bool compare(int a, int b){
    return a > b;
}

int main()
{
    string num;

    cin >> num;
    vector<int> v(num.length());

    for (int i=0; i<num.length(); i++)
    {
        v[i] = num[i] - '0';
    }

    sort(v.begin(), v.end(), compare);

    for (int i=0; i<num.length(); i++)
    {
        cout << v[i];
    }

    return 0;
}