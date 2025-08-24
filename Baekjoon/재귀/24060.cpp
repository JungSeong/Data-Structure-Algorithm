#include <iostream>
#include <vector>

using namespace std;

int cnt = 0;
bool isin = false;

void merge(vector<int>& v, int p, int q, int r, int K);

void merge_sort(vector<int>& v, int p, int r, int K)
{
    int q;

    if (p < r)
    {
        q = (p + r) / 2;
        merge_sort(v, p, q, K);
        merge_sort(v, q+1, r, K);
        merge(v, p, q, r, K);
    }
}

void merge(vector<int>& v, int p, int q, int r, int K)
{
    int i=p, j=q+1, t=0;
    vector<int> temp;
    while(i<=q && j<=r)
    {
        if (v[i] <= v[j])
        {
            temp.push_back(v[i++]);
        }
        else
        {
            temp.push_back(v[j++]);
        }
    }
    while (i<=q)
    {
        temp.push_back(v[i++]);
    }
    while (j<=r)
    {
        temp.push_back(v[j++]);
    }

    i=p; t=0;

    while (i <= r)
    {
        cnt++;
        v[i] = temp[t];

        if (cnt == K)
        {
            cout << temp[t];
            isin = true;
        }

        i++; t++;
    }
}

int main()
{
    int N, K, input;
    cin >> N >> K;

    vector<int> v;
    for (int i=0; i<N; i++)
    {
        cin >> input;
        v.push_back(input);
    }

    merge_sort(v, 0, v.size()-1, K);

    if (!isin)
    {
        cout << -1;
    }
    
    // for (auto it=v.begin(); it!=v.end(); it++)
    // {
    //     cout << *it << ' ';
    // }
}