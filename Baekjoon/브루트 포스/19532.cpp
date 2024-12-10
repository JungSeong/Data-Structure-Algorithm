#include <iostream>

int main()
{
    int a, b, c, d, e, f;
    int x, y;
    std::cin >> a >> b >> c >> d >> e >> f;

    int arr[2][2], crr[2][1];
    int det = a*e - b*d;

    arr[0][0] = e;
    arr[0][1] = -b;
    arr[1][0] = -d;
    arr[1][1] = a;

    crr[0][0] = c;
    crr[0][1] = f;

    x = (arr[0][0] * crr[0][0] + arr[0][1] * crr[0][1]) / det;
    y = (arr[1][0] * crr[0][0] + arr[1][1] * crr[0][1]) / det;

    std::cout << x << ' ' <<  y;
}