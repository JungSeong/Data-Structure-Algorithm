#include <iostream>
#include <cmath>

int main()
{
    int N, B, result = 0;

    std::cin >> N >> B;

    int length = 0;
    int n= N;

    // 자릿수 계산을 위한 반복문
    while(n != 0)
    {
        n /= B;
        length++;
    }

    char st[length];
    int l = length-1;

    while(N != 0)
    {  
        if (N % B <10)
        {
            st[l] = char(N%B + '0');
        }

        else
        {
            st[l] = char(N%B + 55);
        }

        N /= B;
        l--;
    }

    for (int i=0; i<length; i++)
    {
        std::cout << st[i];
    }
}