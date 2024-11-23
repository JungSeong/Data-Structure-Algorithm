#include <iostream>
#include <cstring>

int main()
{
    char str[101];
    int cnt = 0;

    std::cin >> str;
    for (int i=0; i<strlen(str)/2; i++)
    {
        if (str[i] != str[strlen(str)-i-1])
        {
            std::cout << 0;
            exit(0);
        }
    }

    std::cout << 1;
}