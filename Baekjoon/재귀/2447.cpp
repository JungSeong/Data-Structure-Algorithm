#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

char pattern[3][3] = {{'*','*','*'},{'*',' ','*'},{'*','*','*'}};

void definePattern(int row, int col, int length, vector<vector<bool>>& isBlank)
{
    if (length > 3)
    {
        for (int i=row; i<row+length/3; i++)
        {
            for (int ii=col; ii<col+length/3; ii++)
            {
                isBlank[i][ii] = true;
            }
        }

        for (int i=0; i<3; i++)
        {
            for (int ii=0; ii<3; ii++)
            {
                definePattern(i*3, ii*3, length/3, isBlank);
            }
        }
    }
}

int main()
{
    int N; 
    cin >> N;

    vector<vector<bool>> isBlank(N, vector<bool>(N, false));
    definePattern(N/3, N/3, N, isBlank);

    for (int i=0; i<N; i++)
    {
        for (int ii=0; ii<N; ii++)
        {
            cout << isBlank[i][ii];
        }
        cout << '\n';
    }
}