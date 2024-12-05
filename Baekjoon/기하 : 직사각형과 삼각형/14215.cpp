/* 
삼각형의 조건 : 가장 긴 변의 길이보다 나머지 두 변의 길이의 합이 더 길어야 한다.
*/

#include <iostream>

int main()
{
    int arr[3];
    std::cin >> arr[0] >> arr[1] >> arr[2];
    int max = arr[0], idx = 0;

    for (int i=0; i<3; i++)
    {
        if (max < arr[i])
        {
            max = arr[i];
            idx = i;
        }    
    }

    if (max >= arr[0] + arr[1] + arr[2] - arr[idx])
    {
        arr[idx] = arr[0] + arr[1] + arr[2] - arr[idx] - 1;
    }

    std::cout << arr[0] + arr[1] + arr[2];
}