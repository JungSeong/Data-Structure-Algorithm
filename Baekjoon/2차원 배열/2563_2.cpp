#include <iostream>
#include <algorithm>

int main()
{
    int arr[100][100] = {0, };
    int N, x, y, size = 0;

    std::cin >> N;

    for (int i=0; i<N; i++)
    {
        std::cin >> x >> y;
        
        for (int ii=x; ii<x+10; ii++)
        {
            std::fill(&arr[ii][y], &arr[ii][y+10], 1);
        }
    }

    for (int i=0; i<100; i++)
    {
        for (int ii=0; ii<100; ii++)
        {
            size += arr[i][ii];
        }
    }

    std::cout << size;
}