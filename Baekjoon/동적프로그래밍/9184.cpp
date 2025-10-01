#include <iostream>
#include <vector>

using namespace std;

int weight(int a, int b, int c, vector<vector<vector<int>>> & w)
{
    if (a<=0 || b<=0 || c<=0)
    {
        return w[a+50][b+50][c+50] = 1;
    }
    if (a>20 || b>20 || c>20)
    {
        return w[a+50][b+50][c+50] = weight(20, 20, 20, w);
    }
    if (a<b && b<c)
    {
        if (w[a+50][b+50][c+50])
        {
            return w[a+50][b+50][c+50];
        }
        return w[a+50][b+50][c+50] = weight(a, b, c-1, w) + weight(a, b-1, c-1, w) - weight(a, b-1, c, w);
    }
    if (w[a+50][b+50][c+50])
    {
        return w[a+50][b+50][c+50];
    }
    return w[a+50][b+50][c+50] = weight(a-1, b, c, w) + weight(a-1, b-1, c, w) + weight(a-1, b, c-1, w) - weight(a-1, b-1, c-1, w);
}

int main()
    {
    int a, b, c;
    // vector<vector<int>> w1(101, vector<int>(101, 0));
    vector<vector<vector<int>>> w(101, vector<vector<int>>(101, vector<int>(101,0)));
    while (true)
    {
        cin >> a >> b >> c;
        if (a==-1 && b==-1 && c==-1) {break;}
        cout << "w(" << a << ", " << b << ", " << c << ") = " << weight(a,b,c,w) << '\n';
    }
}