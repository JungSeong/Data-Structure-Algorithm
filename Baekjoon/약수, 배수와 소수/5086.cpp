/* 
C++에서 상수를 define 할 때 상수는 항상 괄호로 감싸준다.
#define NUM (1)
*/

#include <iostream>
#define True (1)

int main()
{
    int A=-1, B=1;
    
    while(True)
    {
        std::cin >> A >> B;

        if (A==0 && B==0)
        {
            break;
        }

        if (B % A == 0)
        {
            std::cout << "factor" << std::endl;
        }

        else if (A % B == 0)
        {
            std::cout << "multiple" << std::endl;
        }

        else
        {
            std::cout << "neither" << std::endl;
        }
    }
}