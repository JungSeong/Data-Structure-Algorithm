#include <iostream>
#include <vector>
#define True (1)

int main()
{
    int M, N, cnt_0 = 0, cnt_1 = 0;
    std::cin >> M >> N;

    char chess[M][N];
    char chess_1[8] = {'B','W','B','W','B','W','B','W'};
    char chess_2[8] = {'W','B','W','B','W','B','W','B'};
    
    std::vector<int> sum;

    for (int i=0; i<M; i++)
    {
        for (int ii=0; ii<N; ii++)
        {
            std::cin >> chess[i][ii];
        }
    }

    for (int row_s=0; row_s<(M-7); row_s++)
    {
        for (int col_s=0; col_s<(N-7) ; col_s++)
        {
            for (int iii=0; iii<8; iii++)
            {
                for (int iv=0; iv<8; iv++)
                {
                    if (iii % 2 == 0)
                    {
                        if (chess[iii+row_s][iv+col_s] != chess_1[iv])
                        {
                            cnt_0++;
                        }
                    }
                    else
                    {
                        if (chess[iii+row_s][iv+col_s] != chess_2[iv])
                        {
                            cnt_0++;
                        }
                    }
                }
            }
            
            for (int iii=0; iii<8; iii++)
            {
                for (int iv=0; iv<8; iv++)
                {
                    if (iii % 2 == 0)
                    {
                        if (chess[iii+row_s][iv+col_s] != chess_2[iv])
                        {
                            cnt_1++;
                        }
                    }
                    else
                    {
                        if (chess[iii+row_s][iv+col_s] != chess_1[iv])
                        {
                            cnt_1++;
                        }
                    }
                }
            }

            if (cnt_0 > cnt_1)
            {
                sum.push_back(cnt_1);
            }
            else
            {
                sum.push_back(cnt_0);
            }

            cnt_0 = 0;
            cnt_1 = 0;
        }
    }

    int min = sum[0];

    for (int i=0; i<sum.size(); i++)
    {
        if (min > sum[i])
        {
            min = sum[i];
        }
    }

    std::cout << min;
}