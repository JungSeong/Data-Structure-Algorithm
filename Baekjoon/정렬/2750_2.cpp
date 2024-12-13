/* 
버블 정렬 : 이웃하는 두 원소씩 차례대로 정렬하는 작업을 반복한다.
시간 복잡도 : O(n^2)
*/

#include <iostream>

int main()
{
    int N;
    std::cin >> N;

    int arr[N];
    
    for (int i=0; i<N; i++)
    {
        std::cin >> arr[i];
    }

    int temp;

    for (int i=0; i<sizeof(arr)/sizeof(int)-1; i++)
    {
        for (int ii=0; ii<sizeof(arr)/sizeof(int)-1; ii++)
        {
            if (arr[ii] > arr[ii+1])
            {
                temp = arr[ii];
                arr[ii] = arr[ii+1];
                arr[ii+1] = temp;
            }
        }
    }

    for (int i=0; i<N; i++)
    {
        std::cout << arr[i] << std::endl;
    }
}