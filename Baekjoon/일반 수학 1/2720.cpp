/* 
나머지 출력 : fmod(A, B) -> A를 B로 나눈 나머지를 출력한다.
*/

#include <iostream>
#include <math.h>

int main()
{
    int T, C;
    std::cin >> T;

    int quarter = 0, dime = 0, nickel = 0, penny = 0;

    for (int i=0; i<T; i++)
    {
        std::cin >> C;

        quarter = C / 25;
        C = fmod(C, 25);

        dime = C / 10;
        C = fmod(C, 10);

        nickel = C / 5;
        C = fmod(C, 5);

        penny = C / 1;

        std::cout << quarter << ' ' << dime << ' ' << nickel << ' ' << penny << std::endl;
    }
}