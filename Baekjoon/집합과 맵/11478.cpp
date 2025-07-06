#include <iostream>
#include <unordered_set>
#include <string>
#include <iterator>

using namespace std;

int main()
{
    string str, sub_str;
    getline(cin, str);

    unordered_set<string> parsed_str_set;

    int N = 0;

    for (int idx = 0; idx < str.length(); idx++)
    {
        for (int N = str.length() - idx; N >= 0; N--)
        {
            sub_str = str.substr(idx, N);
            parsed_str_set.insert(sub_str);
        }
    }

    cout << parsed_str_set.size() - 1;
}