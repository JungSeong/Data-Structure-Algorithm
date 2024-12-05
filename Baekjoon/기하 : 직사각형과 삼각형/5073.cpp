#include <iostream>
#define True (1)

int main()
{
    while(True)
    {
        int arr[3];
        std::cin >> arr[0] >> arr[1] >> arr[2];

        if (arr[0] == 0 && arr[1] == 0 && arr[2] == 0)
        {
            break;
        }
        
        int max = arr[0], idx = 0;

        for (int i=0; i<3; i++)
        {
            if(max < arr[i])
            {
                max = arr[i];
                idx = i;
            }
        }

        if (max >= arr[0] + arr[1] + arr[2] - arr[idx])
        {
            std::cout << "Invalid" << std::endl;
        }
        else if (arr[0]==arr[1] && arr[1]==arr[2] && arr[2]==arr[0])
        {
            std::cout << "Equilateral" << std::endl;
        }
        else if (arr[0]==arr[1] || arr[1]==arr[2] || arr[2]==arr[0])
        {
            std::cout << "Isosceles" << std::endl;
        }
        else if (arr[0]!=arr[1] && arr[1]!=arr[2] && arr[2]!=arr[0])
        {
            std::cout << "Scalene" << std::endl;
        }
    }
}