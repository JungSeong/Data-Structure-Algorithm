#include <iostream>
#include <cstdlib>
#include <vector>
#include <set>

using namespace std;

int N;
vector<vector<int>> arr;
set<int> answer;
bool TeamStart[10] = {false};

void Balancing(int k, int recent)
{
    if (k == N/2)
    {
        vector<int> teamStart;
        vector<int> teamLink;
        int result=0, start_s=0, link_s=0;

        for (int i=0; i<N; i++)
        {
            if (TeamStart[i] == true)
            {
                teamStart.push_back(i);
            }
            else
            {
                teamLink.push_back(i);
            }
        }

        for (int i=0; i<N/2-1; i++)
        {
            for (int ii=i+1; ii<N/2; ii++)
            {
                start_s += arr[teamStart[i]][teamStart[ii]] + arr[teamStart[ii]][teamStart[i]];
                link_s += arr[teamLink[i]][teamLink[ii]] + arr[teamLink[ii]][teamLink[i]];
            }
        }
        answer.insert(abs(start_s - link_s));
    }

    for (int i=0; i<N; i++)
    {
        if (TeamStart[i]==false && i>recent)
        {
            TeamStart[i] = true;
            Balancing(k+1, i);
            TeamStart[i] = false;
        }
    }
}

int main()
{
    int elem;
    cin >> N;
    arr.reserve(N);

    for (int i=0; i<N; i++)
    {
        for (int ii=0; ii<N; ii++)
        {
            cin >> elem;
            arr[i].push_back(elem);
        }
    }

    Balancing(0, 0);

    cout << *(answer.begin());
}