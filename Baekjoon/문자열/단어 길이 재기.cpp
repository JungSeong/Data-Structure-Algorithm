/* 
문자열 배열의 크기 : <cstring> 라이브러리의 strlen() 함수 사용
*/

#include <iostream>
#include <cstring>

int main()
{
    char str[101];
    std::cin >> str;

    std::cout << strlen(str);
}