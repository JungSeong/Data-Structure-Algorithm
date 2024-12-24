/* 
bool cmp (string str1, string str2)
{
    if (str1.length() != str2.length())
    {
        return str1.length() < str2.length(); // 문자열의 길이가 다르면, 문자열의 길이를 기준으로 오름차순 정렬 한다.
    }
    else
    {
        return str1 < str2; // 문자열의 길이가 같으면, 벡터를 사전 순서대로 정렬 한다.
    }
}

std::unique -> algorithm 헤더에 존재, 배열에서 중복되지 않는 원소들을 앞에서부터 채워나가되,중복되는 요소는 그 이후로 존재하게끔 한다. 이후 새로운 끝 위치 (=중복된 원소들이 있는 첫 위치)를 반환하게 된다.
vector::erase -> vector에서 특정 원소들을 삭제하는 함수
*/

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

bool cmp (string str1, string str2)
{
    if (str1.length() != str2.length())
    {
        return str1.length() < str2.length();
    }
    else
    {
        return str1 < str2;
    }
}

int main()
{
    int N;
    std::cin >> N;

    string str;
    vector<string> vec;

    for (int i=0; i<N; i++)
    {
        cin >> str;
        vec.push_back(str);
    }

    sort(vec.begin(), vec.end(), cmp);

    vec.erase(std::unique(vec.begin(), vec.end()), vec.end());

    for (int i=0; i<vec.size(); i++)
    {
        std::cout << vec[i] << '\n';
    }

    return 0;
}