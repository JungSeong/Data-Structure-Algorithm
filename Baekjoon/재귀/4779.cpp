#include <iostream>
#include <cmath>

int N;
bool doPrint[540000] = {false};

using namespace std;

void cantore(int idx, int length)
{
    for (int i=idx+length/3; i<idx+length/3*2; i++)
    {
        doPrint[i] = false;
    }
    if (length != 1)
    {
        cantore(idx, length/3);
        cantore(idx+length/3*2, length/3);
    }
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    while (cin >> N)
    {
        for (int i=0; i<pow(3,N); i++)
        {
            doPrint[i] = true;
        }

        cantore(0, pow(3,N));

        for (int i=0; i<pow(3,N); i++)
        {
            if (doPrint[i] == true)
            {
                cout << "-";
            }
            else
            {
                cout << " ";
            }
        }

        cout << '\n';
    }
}