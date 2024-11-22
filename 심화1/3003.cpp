#include <iostream>

int main()
{
    int answer[6] = {1, 1, 2, 2, 2, 8};
    int found[6] = {0};

    for (int i=0; i<6; i++)
    {
        std::cin >> found[i];
    }

    for (int i=0; i<6; i++)
    {
        std::cout << answer[i] - found[i] << ' ';
    }
}