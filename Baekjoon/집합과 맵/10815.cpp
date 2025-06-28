#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N, M, input;
    cin >> N;

    vector<int> vec;

    for (int idx=0; idx<N; idx++)
    {
        cin >> input;
        vec.push_back(input);
    }

    cin >> M;
    vector<int> vec2;

    for (int idx=0; idx<M; idx++)
    {
        cin >> input;
        vec2.push_back(input);
    }

    sort(vec.begin(), vec.end());

    for (auto iter = vec2.begin(); iter != vec2.end(); iter++)
    {
        if (binary_search(vec.begin(), vec.end(), *iter))
        {
            cout << "1 ";
        }
        else
        {
            cout << "0 ";
        }
    }
}