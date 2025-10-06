#include <bits/stdc++.h>

using namespace std;

vector<string> hanoi_process;

void hanoi(int N, string from, string to, string passby)
{
    if (N == 1){
        hanoi_process.push_back(from + " " + to);
        return;
    }
    hanoi(N-1, from, passby, to);
    hanoi_process.push_back(from + " " + to);
    hanoi(N-1, passby, to, from);
}

int main()
{
    int N;
    cin >> N;
    
    hanoi(N, "1", "3", "2");
    
    cout << hanoi_process.size() << '\n';
    for (auto& elem : hanoi_process)
    {
        cout << elem << '\n';
    }
}