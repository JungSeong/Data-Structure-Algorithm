#include <iostream>
#include <vector>
#include <cmath>
#include <numeric>
#include <algorithm>

using namespace std;

int main()
{
    int N, arg, cnt=0;
    long int l=0;
    vector<int> v;
    cin >> N;

    for (int i=0; i<N; i++)
    {
        cin >> arg;
        v.push_back(arg);
    }

    sort(v.begin(), v.end());

    for (int i=1; i<=v.size(); i++)
    {
        if ((int)pow(v.front(), i) == *(v.begin()+i-1))
        {
            cnt++;
        }
    }

    if (cnt == v.size()) cout << (int)pow(*(v.begin()), cnt+1);
    else
    {
        for (auto it=v.begin(); it!=v.end()-1; it++)
        {
            l = lcm(*it, *(it+1));
            *(it+1) = l;
        }
        cout << l;
    }
}