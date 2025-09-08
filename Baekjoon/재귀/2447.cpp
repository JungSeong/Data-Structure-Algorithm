#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

char pattern[3][3] = {{'*','*','*'},{'*',' ','*'},{'*','*','*'}};

void RecursivePattern(int idx, int length, int full, vector<vector<bool>>& isBlank)
{
    if (length > 3)
    {
        for (int i=idx; i<idx+length/3; i++)
        {
            for (int ii=idx; ii<idx+length/3; ii++)
            {
                isBlank[i][ii] = true;
            }
        }

        RecursivePattern(idx-length/9*2, length/3, full, isBlank);
        RecursivePattern(idx+length/9, length/3, full, isBlank);
        RecursivePattern(idx+length/3+length/9, length/3, full, isBlank);
    }
}

int main()
{
    int N;
    cin >> N;
    
    double length = pow(3,N);
    double full = length;

    vector<vector<bool>> isBlank(length, vector<bool>(length, false));
    RecursivePattern(length/3, length, full, isBlank);

    for (int i=0; i<length; i++)
    {
        for (int ii=0; ii<length; ii++)
        {
            cout << isBlank[i][ii];
        }
        cout << '\n';
    }
}