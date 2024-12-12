/*
str_comp.find("string")에서 만약 string을 찾는다면 찾는 문자의 첫번째 인덱스 값을 반환한다.
그렇지 못하다면 string::npos (쓰레기 값)을 리턴하게 된다.
*/

#include <iostream>
#include <string>
#define True (1)

int main()
{
    int N, start = 666, comp = start, cnt = 0, idx = 0;
    std::cin >> N;

    while (True)
    {
        std::string str_comp = std::to_string(comp);

        if (str_comp.find("666") != std::string::npos)
        {
            idx++;

            if (idx == N)
            {
                std::cout << comp << std::endl;
                break;
            }
        }

        comp++;
    }

    return 0;
}