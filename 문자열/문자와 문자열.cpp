/* 
문자열의 경우 마지막에 NULL이 들어가기 때문에 1000자 제한이면 1001로 배열을 선언해야 한다.
*/

#include <iostream>

int main()
{
    char str[1001];
    int i;

    std::cin >> str;
    std::cin >> i;

    std::cout << str[i-1];
}