#include <iostream>

int main()
{
    int n;
    unsigned long sum = 0;
    std::cin >> n;

    for (int i=n-1; i>0; i--)
    {
        sum += i;
    }

    std::cout << sum << '\n' << 2 << std::endl;
}