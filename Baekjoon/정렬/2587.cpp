#include <iostream>

int main()
{
    int arr[5], avg = 0, mid, temp;

    for (int i=0; i<5; i++)
    {
        std::cin >> arr[i];
        avg += arr[i];
    }

    // for (int i=0; i<5-1; i++) // BubbleSort로 해결
    // {
    //     for (int ii=0; ii<5-1-i; ii++)
    //     {
    //         if (arr[ii] > arr[ii+1])
    //         {
    //             temp = arr[ii];
    //             arr[ii] = arr[ii+1];
    //             arr[ii+1] = temp;
    //         }
    //     }
    // }

    for (int i=0; i<5-1; i++) // InsertSort로 해결
    {
        for (int ii=i+1; ii>0; ii--)
        {
            if (arr[ii] < arr[ii-1])
            {
                temp = arr[ii-1];
                arr[ii-1] = arr[ii];
                arr[ii] = temp;
            }
        }
    }

    mid = arr[2];
    avg /= 5;

    std::cout << avg << '\n' << mid;
}