#include <bits/stdc++.h>

using namespace std;

int main()
{
    string name;
    int cnt = 0;
    getline(cin, name);
    
    for (auto ch : name)
    {
        if (ch == ' ') {cnt++;}
    }
    
    if (name.front() == ' ') {cnt--;}
    if (name.back() == ' ') {cnt--;}
    
    cout << cnt+1;
}