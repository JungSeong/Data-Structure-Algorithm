/* 
삽입 정렬 : 2 번째 원소부터 시작해서 앞의 이미 정렬된 원소들과 비교하여 자신의 위치를 결정해주는 알고리즘이다.
시간 복잡도 : O(n^2)
*/

#include <iostream>

int main()
{
    int arr[8] = {1,3,4,2,5,9,0,10};
    int temp;

    for (int i=0; i<sizeof(arr)/sizeof(int)-1; i++)
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

    for (int i=0; i<sizeof(arr)/sizeof(int); i++)
    {
        std::cout << arr[i] << ' ';
    }

    return 0;
}