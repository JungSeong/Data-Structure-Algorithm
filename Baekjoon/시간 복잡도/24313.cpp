#include <iostream>

int main()
{
    int a_1, a_0, c, n_0;
    double n;
    std::cin >> a_1 >> a_0;
    std::cin >> c;
    std::cin >> n_0;

    if (a_1 == c)
    {
        if (a_0 > 0)
        {
            std::cout << 0;
        }
        else
        {
            std::cout << 1;
        }
    }

    else if (a_1 > c)
    {
        std::cout << 0;
    }

    else
    {
        n = a_0 / (c - a_1);

        if (n > n_0)
        {
            std::cout << 0;
        }
        else
        {
            std::cout << 1;
        }
    }

}