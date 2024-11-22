#include <iostream>

int main()
{
    int N;
    std::cin >> N;

    for (int i=0; i<2*N-1; i++)
    {   
        if (i < N)
        {
            for (int ii=N-i-1; ii>0; ii--)
            {
                std::cout << ' ';
            }
            for (int ii=0; ii<2*i+1; ii++)
            {
                std::cout << '*';
            }
        }
        else
        {
            for (int ii=i-N+1; ii>0; ii--)
            {
                std::cout << ' ';
            }
            for (int ii=4*N-2*i-3; ii>0; ii--)
            {
                std::cout << '*';
            }
        }

        std::cout << std::endl;
    }
}