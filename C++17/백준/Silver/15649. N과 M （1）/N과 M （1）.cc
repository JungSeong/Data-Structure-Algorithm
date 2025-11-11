#include <iostream>

using namespace std;

int N, M;
int arr[9];
bool isUsed[9] = {false};

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
        if (isUsed[i] == false)
        {
            arr[k+1] = i;
            isUsed[i] = true;
            BackTracking(k+1);
            isUsed[i] = false;
        }		
	}
}

int main()
{
	cin >> N >> M;
	BackTracking(0);
}