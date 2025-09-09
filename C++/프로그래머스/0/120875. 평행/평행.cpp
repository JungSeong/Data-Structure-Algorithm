#include <iostream>
#include <string>
#include <vector>

using namespace std;

int solution(vector<vector<int>> dots) {
    int dx1, dy1, dx2, dy2;

    for (int i=1; i<=3; i++)
    {
        vector<vector<int>> pv;
        for (int ii=1; ii<=3; ii++)
        {
            if (ii != i)
            {
                pv.push_back(dots[ii]);
            }
        }
        dx1 = dots[i][0] - dots[0][0];
        dy1 = dots[i][1] - dots[0][1];
        dx2 = pv[1][0] - pv[0][0];
        dy2 = pv[1][1] - pv[0][1];

        if (dx1 * dy2 == dy1 * dx2) {return 1;}
    }
    return 0;
}