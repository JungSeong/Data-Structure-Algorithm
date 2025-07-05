#include <iostream>
#include <unordered_set>
#include <vector>

using namespace std;

int main()
{
    int lenA, lenB, input;
    cin >> lenA >> lenB;

    unordered_set<int> A;
    unordered_set<int> B;

    for (int idx=0; idx<lenA; idx++)
    {
        cin >> input;
        A.insert(input);
    }

    for (int idx=0; idx<lenB; idx++)
    {
        cin >> input;
        B.insert(input);
    }

    vector<int> A_B;
    vector<int> B_A;

    for (auto it=A.begin(); it != A.end(); it++)
    {
        if (auto search = B.find(*it); search != B.end())
            continue;
        else
            A_B.push_back(*it);
    }

    for (auto it=B.begin(); it != B.end(); it++)
    {
        if (auto search = A.find(*it); search != A.end())
            continue;
        else
            B_A.push_back(*it);
    }

    cout << A_B.size() + B_A.size();
}