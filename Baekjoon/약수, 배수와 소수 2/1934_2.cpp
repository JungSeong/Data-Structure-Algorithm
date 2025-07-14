#include <numeric>
#include <iostream>

using namespace std;

int main()
{
    int T, A, B;
    cin >> T;

    for (int i=0; i<T; i++)
    {
        cin >> A >> B;
        cout << lcm(A, B) << '\n';
    }
}