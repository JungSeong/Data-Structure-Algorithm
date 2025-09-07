#include <iostream>
#include <string>
#include <set>

using namespace std;

int main()
{
    int N, cnt=0;
    string str;
    set<string> mySet;
    cin >> N;

    cin.ignore(); // 버퍼 비우기

    for (int i=0; i<N; i++)
    {
        getline(cin, str);
        if (str.compare("ENTER") != 0)
        {
            mySet.insert(str);
        }
        else
        {
            cnt += mySet.size();
            mySet.clear();
        }
    }
    cnt += mySet.size();

    cout << cnt;
}