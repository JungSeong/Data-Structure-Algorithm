/*
long double powl( long double x, long double y );
*/

#include <iostream>
#include <cmath>

int main()
{
    long n;
    std::cin >> n;

    std::cout << (long) powl(n,2) << '\n' << 2 << std::endl;
}