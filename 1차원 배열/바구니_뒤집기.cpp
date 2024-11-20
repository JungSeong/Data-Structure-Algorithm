/* 
배열에서 특정 범위의 원소를 역순으로 정렬하는 문제이다.
더 좋은 방법이 있을 듯 하다.
*/

#include <iostream>

int main()
{
    int N, M, i, j, temp;
    int I, J;

    std::cin >> N >> M;

    int arr[N];

    for (int p=0; p<N; p++)
    {
        arr[p] = p + 1;
    }

    for (int p=0; p<M; p++)
    {
        std::cin >> i >> j;
        I = i;
        J = j;

        for (int pp=0; pp<(j-i)/2+1; pp++)
        {
            temp = arr[I-1];
            arr[I-1] = arr[J-1];
            arr[J-1] = temp;

            I++;
            J--;
        }
    }

    for (int p=0; p<N; p++)
    {
        std::cout << arr[p] << ' ';
    }
}