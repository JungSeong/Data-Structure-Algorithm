#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;
int main() {
    vector<vector<int>> lines = {{0,1}, {3,9}, {2,5}};

    for (const auto& elem : lines)
    {
        cout << elem[0] << ' ' << elem[1] << '\n';
    }
    
    return 0;
}