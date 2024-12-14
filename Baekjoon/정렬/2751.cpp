/*

*/

#include <iostream>
#include <algorithm>
#include <vector>

int main()
{
    int N;
    std::cin >> N;

    std::vector <int> v(N);

    for (int i=0; i<N; i++)
    {
        std::cin >> v[i];
    }

    std::sort(v.begin(), v.end());

    for (int i=0; i<N; i++)
    {
        std::cout << v[i] << '\n';
    }
}