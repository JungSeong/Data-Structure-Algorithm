#include <iostream>
#include <unordered_map>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

#define pp pair<string,int>

bool customSort(const pp& a, const pp& b) {
    if (a.second == b.second)
    {
        if (a.first.size() == b.first.size())
        {
            return a.first < b.first; // 사전 순으로 정렬
        }
        return a.first.size() > b.first.size(); // 단어의 길이 순으로 내림차순 정렬
    }
    return a.second > b.second; // 자주 나오는 빈도로 내림차순 정렬
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M;
    string str;
    unordered_map<string, int> myMap;
    cin >> N >> M;
    
    cin.ignore();

    for (int i=0; i<N; i++)
    {
        cin >> str;
        if (str.length() >= M)
        {
            myMap[str]++;
        }
    }

    vector<pp> vec(myMap.begin(), myMap.end());
    sort(vec.begin(), vec.end(), customSort);

    for (auto it : vec) {
		cout << it.first << '\n';
	}
}