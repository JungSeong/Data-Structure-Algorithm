#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
#include <unordered_set>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
	cin.tie(0);
    cout.tie(0);
    
    int N, M;
    string name, comp;
    cin >> N >> M;

    unordered_map<string, int> name2num;
    unordered_map<int, string> num2name;

    for (int idx=0; idx<N; idx++)
    {
        cin >> name;
        name2num[name] = idx+1;
        num2name[idx] = name;
    }

    size_t pos{};

    for (int idx=0; idx<M; idx++)
    {
        cin >> comp;

        if (isdigit(comp[0]) == 0) // english
        {
            cout << name2num[comp] << '\n';
        }
        else // digit
        {
            cout << num2name[stoi(comp, &pos)-1] << '\n'; 
        }
    }
}