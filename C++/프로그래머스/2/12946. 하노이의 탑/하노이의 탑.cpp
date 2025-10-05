#include <bits/stdc++.h>

using namespace std;

vector<vector<int>> answer;

void hanoi(int n, int from_pos, int to_pos, int aux_pos)
{
    if (n == 1)
    {
        answer.push_back({from_pos, to_pos});
        return;
    }
    hanoi(n-1, from_pos, aux_pos, to_pos);
    answer.push_back({from_pos, to_pos});
    hanoi(n-1, aux_pos, to_pos, from_pos);
}

vector<vector<int>> solution(int n) {
    hanoi(n, 1, 3, 2);
    
    return answer;
}