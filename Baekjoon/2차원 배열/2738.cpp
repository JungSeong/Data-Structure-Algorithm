#include <iostream>

int main()
{
    int N, M;
    std::cin >> N >> M;

    int A[N][M], B[N][M], S[N][M];

    for (int i=0; i<N; i++)
    {
        for (int ii=0; ii<M; ii++)
        {
            std::cin >> A[i][ii];
        }
    }

    for (int i=0; i<N; i++)
    {
        for (int ii=0; ii<M; ii++)
        {
            std::cin >> B[i][ii];
        }
    }

    for (int i=0; i<N; i++)
    {
        for (int ii=0; ii<M; ii++)
        {
            S[i][ii] = A[i][ii] + B[i][ii];
        }
    }

    for (int i=0; i<N; i++)
    {
        for (int ii=0; ii<M; ii++)
        {
            std::cout << S[i][ii] << ' ';
        }
        std::cout << std::endl;
    }
}