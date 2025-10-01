#include <iostream>

using namespace std;

int N, M;
int arr[9];

void BackTracking(int k)
{
	if (k == M)
	{
		for (int i=1; i<=M; i++)
        {
            cout << arr[i] << ' ';
        }
        cout << '\n';
        return;
	}
	for (int i=1; i<=N; i++)
	{
        if (arr[k] <= i)
        {
            arr[k+1] = i;
            BackTracking(k+1);	
        }
	}
}

int main()
{
	cin >> N >> M;
	BackTracking(0);
}