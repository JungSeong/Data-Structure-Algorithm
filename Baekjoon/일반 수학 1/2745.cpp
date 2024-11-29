#include <iostream>
#include <cstring>
#include <cmath>

int main()
{
    std::string N;
    int B, result = 0;

    std::cin >> N >> B;
    
    int length = N.length()-1;

    for (int i=0 ; i<N.length(); i++)
    {
        if (int(N.at(i)) >= 48 && int(N.at(i)) <= 57)
        {
            result += (int(N.at(i))-48) * pow(B, length);
            length--;
        }

        if (int(N.at(i)>=65 && int(N.at(i)) <= 90))
        {
            result += (int(N.at(i))-55) * pow(B, length);
            length--;
        }
    }

    std::cout << result;
}