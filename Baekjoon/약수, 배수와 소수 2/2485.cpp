#include <iostream>
#include <numeric>
#include <vector>

using namespace std;

int main()
{
    int N, input;
    cin >> N;
    vector<int> list, dist_list, dist_list_copy;

    for (int idx=0; idx<N; idx++)
    {
        cin >> input;
        list.push_back(input);
    }
    
    for (int idx=0; idx<N-1; idx++)
    {
        dist_list.push_back(list[idx+1] - list[idx]);
    }

    int gcd_final = 0;
    copy(dist_list.begin(), dist_list.end(), back_inserter(dist_list_copy));

    for (int idx=0; idx<N-2; idx++)
    {
        gcd_final = gcd(dist_list_copy[idx], dist_list_copy[idx+1]);
        dist_list_copy[idx+1] = gcd_final;
    }

    int result = 0;

    for (auto it = dist_list.begin(); it != dist_list.end(); it++)
    {
        result += (*it)/gcd_final - 1;
    }

    cout << result;
} 