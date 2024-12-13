#include <iostream>

int main()
{
    int N, k, temp;
    std::cin >> N >> k;

    int arr[N];

    for (int i=0; i<N; i++)
    {
        std::cin >> arr[i];
    }

    for (int i=0; i<N-1; i++) // BubbleSort로 해결
    {
        for (int ii=0; ii<N-1-i; ii++)
        {
            if (arr[ii] < arr[ii+1])
            {
                temp = arr[ii+1];
                arr[ii+1] = arr[ii];
                arr[ii] = temp;
            }
        }
    }

    // for (int i=0; i<5-1; i++) // InsertSort로 해결
    // {
    //     for (int ii=i+1; ii>0; ii--)
    //     {
    //         if (arr[ii] < arr[ii-1])
    //         {
    //             temp = arr[ii-1];
    //             arr[ii-1] = arr[ii];
    //             arr[ii] = temp;
    //         }
    //     }
    // }

    std::cout << arr[k-1];
    return 0;
}