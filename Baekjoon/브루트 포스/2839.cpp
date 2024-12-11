#include <iostream>
#include <vector>

int main()
{
    int N;
    std::cin >> N;

    int n = N, repeat = N/5;

    std::vector<int> cnt;

    for (int i=0; i<=repeat; i++)
    {
        n -= 5 * i;

        if (n % 3 == 0)
        {
            cnt.push_back(i + n/3);
        }

        n = N;
    }

    if (cnt.size() == 0)
    {
        std::cout << -1;
    }
    else
    {
        int min = cnt[0];

        for (int i=0; i<cnt.size(); i++)
        {
            if (min > cnt[i])
            {
                min = cnt[i];
            }
        }

        std::cout << min;
    }
    
    return 0;
}