#include <iostream>

int main()
{
    int A[9][9];
    int idx_row, idx_col;

    for (int i=0; i<9; i++)
    {
        for (int ii=0; ii<9; ii++)
        {
            std::cin >> A[i][ii];
        }
    }

    int max = A[0][0];

    for (int i=0; i<9; i++)
    {
        for (int ii=0; ii<9; ii++)
        {
            if (max <= A[i][ii])
            {
                max = A[i][ii];
                idx_row = i;
                idx_col = ii; 
            }
        }
    }

    std::cout << max << std::endl << idx_row +1 << ' ' << idx_col + 1;
}