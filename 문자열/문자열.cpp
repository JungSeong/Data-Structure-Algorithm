#include <iostream>
#include <cstring>

int main()
{
    char str[1001];

    int T;
    std::cin >> T;

    for (int i=0; i<T; i++)
    {
        std::cin >> str;
        std::cout << str[0] << str[strlen(str)-1] << std::endl;
    }
}