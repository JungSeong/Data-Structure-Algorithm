#include <iostream>
#include <string>

int main()
{
    // std::string str;
    // std::cin >> str;
    // std::cout << str.at(0) << std::endl;

    std::string str2[3];
    
    for (int i=0; i<3; i++)
    {
        std::cin >> str2[i];
    }

    for (int i=0; i<3; i++)
    {
        std::cout << str2[i] << std::endl;
    }

    std::string str = str2[0];
    std::cout << str.length() << std::endl;
    return 0;
}