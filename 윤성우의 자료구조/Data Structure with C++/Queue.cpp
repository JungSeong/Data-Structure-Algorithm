#include <iostream>
#include <queue>
using namespace std;

int main()
{ 
    queue<int> q1;
    queue<int> q2;

    q1.push(1);
    q1.push(2);
    q1.push(3);

    q2.push(10);
    q2.push(20);
    q2.push(30);

    swap(q1, q2);

    while (!q1.empty())
    {
        cout << q1.front() << endl;
        q1.pop();
    }

    return 0;
}