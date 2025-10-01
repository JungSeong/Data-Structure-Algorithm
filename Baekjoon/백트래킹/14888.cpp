#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> result;
vector<int> num;
int oper[4], N;

void operation(int k, int idx)
{
    if (oper[0] + oper[1] + oper[2] + oper[3] == 0)
    {
        result.push_back(k);
        return;
    }

    for (int i=0; i<4; i++)
    {
        int next_k = k;
        if (oper[i] > 0)
        {
            if (i==0) {next_k += num[idx];}
            else if (i==1) {next_k -= num[idx];}
            else if (i==2) {next_k *= num[idx];}
            else
            {
                next_k /= num[idx];
            }
            oper[i]--;
            operation(next_k, idx+1);
            oper[i]++;
        }
    }
}

int main()
{
    int elem;
    cin >> N;

    for (int i=0; i<N; i++)
    {
        cin >> elem;
        num.push_back(elem);
    }

    for (int i=0; i<4; i++)
    {
        cin >> elem;
        oper[i] = elem;
    }

    operation(num[0], 1);
    sort(result.begin(), result.end());

    cout << result.back() << '\n' << result.front();
}