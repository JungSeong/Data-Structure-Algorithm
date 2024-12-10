#include <iostream>
#include <vector>

int main()
{
    int M, N, answer = 0;
    std::cin >> N >> M;

    int arr[N];
    std::vector<int> sum;

    for (int i=0; i<N; i++)
    {
        std::cin >> arr[i];
    }

    for (int i=0; i<N-2; i++)
    {
        for (int ii=i+1; ii<N-1; ii++)
        {
            for (int iii=ii+1; iii<N; iii++)
            {
                sum.push_back(arr[i] + arr[ii] + arr[iii]);
            }
        }
    }

    for (int i=0; i<sum.size(); i++)
    {
        if (sum[i] <= M && answer < sum[i])
        {
            answer = sum[i];
        }
    }

    std::cout << answer;
}