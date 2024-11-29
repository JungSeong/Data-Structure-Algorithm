#include <iostream>
#include <math.h>

int main()
{
    double T = 5.00;

    std::cout << T/0.25;
    T = fmod(T, 0.25);

    std::cout << ' ' << T;
}