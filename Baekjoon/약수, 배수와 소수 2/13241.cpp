#include <iostream>

using namespace std;

int main()
{
    long long int A, B, temp = 0;
    cin >> A >> B;

    long long int larger = A > B ? A : B;
    long long int smaller = A < B ? A : B;
    
    while (larger % smaller != 0)
    {
        temp = larger % smaller;
        larger = smaller;
        smaller = temp;
    }

    cout << smaller * (A / smaller) * (B / smaller);
}