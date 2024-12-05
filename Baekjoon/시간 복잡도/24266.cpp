/*
long double powl( long double x, long double y );
*/

#include <iostream>
#include <cmath>

int main()
{
    long n;
    std::cin >> n;

    std::cout << (long) powl(n,3) << '\n' << 3 << std::endl;
}