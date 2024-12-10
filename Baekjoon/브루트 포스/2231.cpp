#include <iostream>
#define True (1)

int main()
{
    int N, I, comp, cnt = 1;
    std::cin >> N;

    for (int i=1; i<N; i++)
    {
        I = i;
        comp += I;

        while(True)
        {
            comp += I % 10;
            I /= 10;

            if (I == 0)
            {
                break;
            }
        }

        if (comp == N)
        {
            std::cout << i;
            break;
        }
        else
        {
            comp = 0;
            cnt ++;
        }
    }

    if (cnt == N)
    {
        std::cout << 0;
    }
}