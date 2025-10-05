#include <unordered_map>
#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    string num;
    cin >> num;
    
    unordered_map<char, int> info;

    for (char i = '0'; i <= '9'; i++)
    {
        info[i] = 0;
    }
    
    for (auto ch : num)
    {
        info[ch]++;
    }

    auto cur = ceil(float(info['6']+info['9'])/2);
    info['6'] = cur;

    int required = info['0'];

    for (char i = '1'; i <= '8'; i++)
    {
        required = max(required, info[i]);
    }
    
    cout << required;
}