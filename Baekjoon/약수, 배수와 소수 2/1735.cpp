#include <iostream>
#include <numeric>

using namespace std;

int main()
{
    int A1, B1, A2, B2;
    cin >> A1 >> B1;
    cin >> A2 >> B2;

    int gcd1 = gcd(A1, B1);
    int gcd2 = gcd(A2, B2);

    A1 /= gcd1;
    B1 /= gcd1;
    A2 /= gcd2;
    B2 /= gcd2;

    int divide = lcm(B1, B2);
    int multi1 = divide / B1, multi2 = divide / B2;
    int divided = multi1 * A1 + multi2 * A2;

    int gcd3 = gcd(divide, divided);
    divide /= gcd3;
    divided /= gcd3;

    cout << divided << ' ' << divide;
}