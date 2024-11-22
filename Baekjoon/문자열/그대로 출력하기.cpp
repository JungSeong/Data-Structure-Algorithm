/* 
C++ 에서는 std::cin을 통해서 공백을 입력받을 수 없음
따라서 <iostream>에 내장된 std::cin.getline() 함수를 사용해야 한다.
*/

#include <iostream>

int main()
{
    char str[1001];

    for (int i=0; i<100; i++)
    {
        std::cin.getline(str, 1001);
        std::cout << str << std::endl;
    }
}