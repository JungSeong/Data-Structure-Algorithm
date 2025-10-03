#include <bits/stdc++.h>

using namespace std;

int solution(vector<vector<int>> board) {
    int N = board.size();
    int answer = N*N;
    
    for (int i=0; i<N; i++)
    {
        for (int j=0; j<N; j++)
        {
            if (board[i][j] == 1)
            {
                for (int ii=i-1; ii<=i+1; ii++)
                {
                    for (int jj=j-1; jj<=j+1; jj++)
                    {
                        if ((ii>=0 && ii<N) && (jj>=0 && jj<N) && (board[ii][jj] == 0))
                        {
                            board[ii][jj] = 2;
                        }
                    }
                }
            }
        }
    }
    
    for (int i=0; i<N; i++)
    {
        for (int j=0; j<N; j++)
        {
            if (board[i][j]) {answer--;}
        }
    }
    
    return answer;
}