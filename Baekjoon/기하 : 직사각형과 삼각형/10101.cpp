#include <iostream>

int main()
{
    int A, B, C;
    std::cin >> A;
    std::cin >> B;
    std::cin >> C;

    if (A==60 && B==60 && C==60)
    {
        std::cout << "Equilateral";
    }
    else if (A+B+C == 180 && (A==B || B==C || C==A))
    {
        std::cout << "Isosceles";
    }
    else if (A+B+C == 180 && A!=B && B!=C && C!=A)
    {
        std::cout << "Scalene";
    }
    else if (A+B+C != 180)
    {
        std::cout << "Error";
    }

    return 0;
}