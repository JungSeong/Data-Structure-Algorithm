/*
배열의 사이즈가 1,000,000이 되자 Segmentation fault 에러가 떴음. 배열의 크기를 너무 크게 하면 안되는 것으로 보이며, <vector> 자료구조를 사용해야 하는 것으로 보인다.<br>
std::sort 자료구조의 경우 시간 복잡도가 **nlogn**이 된다.<br>
std::endl의 경우 줄 바꿈 뿐만 아니라 스트림의 버퍼를 비운는 Flush 작업도 수행하게 되는데, 이 때문에 시간이 더 소요되는 문제가 생긴다. 이는 **스트림을 통한 입출력**이 많은 경우 특히 문제가 도드라지게 된다.<br>
이 문제의 경우 시간 복잡도가 nlogn인 알고리즘으로 해결이 가능하다. 이 알고리즘의 구현도 한 번쯤 해봐야 할 지는? 잘 모그렜다.
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