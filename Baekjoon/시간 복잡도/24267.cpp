/* 
일단 위 문제의 시간 복잡도는 n(n-1)(n-2)/6 으로 구해진다고 한다.
만약 n이 int형이면 answer을 구하는데 에러가 발생한다. 따라서 n도 long 형으로 선언해야 한다.
*/

#include <iostream>

int main()
{
    long n;
    std::cin >> n;

    long answer = n*(n-1)*(n-2)/6;

    std::cout << answer << '\n' << 3 << std::endl;
}