#include <iostream>
#include <cmath>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

int main()
{
    int N, input;

    vector<int> v, compv;
    map<int, int> myMap;
    cin >> N;

    for (int i=0; i<N; i++)
    {
        cin >> input;
        v.push_back(input);
    }

    float sum = 0;
    int m2, m3, m4, maxv=-4001;

    sort(v.begin(), v.end());
    
    for (auto it=v.begin(); it!=v.end(); it++)
    {
        sum += *it;
        myMap[*it]++;
    }

    for (const auto& [key, value] : myMap)
    {
        if (value >= maxv)
        {
            maxv = value;
        }
    }

    for (const auto& [key, value] : myMap)
    {
        if (value == maxv)
        {
            compv.push_back(key);
        }
    }

    if (compv.size() != 1)
    {
        sort(compv.begin(), compv.end());
        m3 = compv[1];
    }
    else
    {
        m3 = compv[0];
    }

    double mean = (double)sum / N;
    m2 = v[N/2];
    m4 = v.back() - v.front();

    cout << (int)round(mean) << '\n' << m2 << '\n' << m3 << '\n' << m4;
}