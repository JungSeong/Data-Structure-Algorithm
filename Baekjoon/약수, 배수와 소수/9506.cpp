#include <iostream>
#define True (1)

int main()
{
    int n, comp = 0;

    while(True)
    {
        std::cin >> n;

        if (n == -1)
        {
            break;
        }

        for (int i=1; i<n; i++)
        {
            if (n % i == 0)
            {
                comp += i;
            }
        }

        if (comp != n)
        {
            std::cout << n << " is NOT perfect." << std::endl;
        }

        else
        {
            std::cout << n << " = ";
            comp = 0;
            
            for (int i=1; i<n; i++)
            {
                if (n % i == 0)
                {
                    comp += i;

                    if (comp != n)
                    {
                        std::cout << i << " + ";
                    }
                    else
                    {
                        std::cout << i;
                    }
                }
            }
            std::cout << std::endl;
        }

        comp = 0;
    }

}