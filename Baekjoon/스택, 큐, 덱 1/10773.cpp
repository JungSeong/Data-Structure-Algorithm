#include <iostream>
#include <stack>

using namespace std;

int main()
{
    int K, num;
    stack<int> myStack;
    cin >> K;

    for (int idx=0; idx<K; idx++)
    {
        cin >> num;
        if (num == 0)
        {
            myStack.pop();
        }
        else
        {
            myStack.push(num);
        }
    }

    int sum = 0;

    while(myStack.size() != 0)
    {
        sum += myStack.top();
        myStack.pop();
    }

    cout << sum;
}