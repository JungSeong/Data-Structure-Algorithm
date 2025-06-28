#include <iostream>
#include <algorithm>
#include <unordered_map>
#include <vector>

using namespace std;

int main()
{
    ios::sync_with_stdios(false);
    cin.tie(0);
    cout.tie(0);

    int N, M, cardNum;
    cin >> N;

    unordered_map<int, int> my_Cards;

    for (int idx=0; idx<N; idx++)
    {
        cin >> cardNum;
        my_Cards[cardNum]++;
    }

    // for (auto it = my_Cards.begin(); it != my_Cards.end(); it++)
    // {
    //     cout << it->first << " " << it->second << '\n';
    // }

    cin >> M;
    vector<int> comp_Cards;

    for (int idx=0; idx<M; idx++)
    {
        cin >> cardNum;
        comp_Cards.push_back(cardNum);
    }

    for (auto it = comp_Cards.begin(); it != comp_Cards.end(); it++)
    {
        cout << my_Cards[*it] << " ";
    }
}