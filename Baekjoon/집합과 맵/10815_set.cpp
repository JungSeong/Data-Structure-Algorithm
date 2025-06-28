#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_set>

using namespace std;

int main()
{
    int N, M, card_num;
    cin >> N;
    
    unordered_set<int> Cards;
    for (int idx=0; idx<N ; idx++)
    {
        cin >> card_num;
        Cards.insert(card_num);
    }

    cin >> M;

    vector<int> myCards;
    for (int idx=0; idx<M; idx++)
    {
        cin >> card_num;
        myCards.push_back(card_num);
    }

    for (auto iter = myCards.begin(); iter != myCards.end(); iter++)
    {
        if (auto it = Cards.find(*iter); it != Cards.end())
        {
            cout << "1 ";
        }
        else
        {
            cout << "0 ";
        }
    }
}