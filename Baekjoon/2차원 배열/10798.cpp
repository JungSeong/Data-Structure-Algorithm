/* 
std::cin으로 문자열을 입력받을 때 가장 마지막에는 '\0' (널 문자)가 들어가게 된다.
*/

#include <iostream>

int main()
{
    char arr[5][16] = {};

    for (int i=0; i<5; i++)
    {
        std::cin >> arr[i];
    }

    for (int col=0; col<15; col++)
    {
        for (int row=0; row<5; row++)
        {
            if (arr[row][col] != '\0')
            {
                std::cout << arr[row][col];
            }
        }
    }
}