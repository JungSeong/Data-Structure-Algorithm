/* 
버블 정렬 : 이웃하는 두 원소씩 차례대로 정렬하는 작업을 반복한다. + 이미 정렬이 된 원소들은 고려하지 않는다.
시간 복잡도 : O(n^2)
*/

#include <iostream>

int main()
{
    int arr[8] = {1,3,4,2,5,9,0,10};
    int temp;

    for (int i=0; i<sizeof(arr)/sizeof(int)-1; i++)
    {
        for (int ii=0; ii<sizeof(arr)/sizeof(int)-1-i; ii++)
        {
            if (arr[ii] > arr[ii+1])
            {
                temp = arr[ii];
                arr[ii] = arr[ii+1];
                arr[ii+1] = temp;
            }
        }
    }

    for (int i=0; i<8; i++)
    {
        std::cout << arr[i] << ' ';
    }
}