#include <iostream>
#include <stack>
#include <vector>

using namespace std;

int main()
{
    int K, N, current=1;
    stack<int> myStack;
    bool isOkay = true;

    cin >> K;
    vector<int> line;

    for (int idx=0; idx<K; idx++)
    {
        cin >> N;
        line.push_back(N);
    }

    for (int idx=0; idx<K; idx++)
    {
        while (myStack.empty() != 1 && myStack.top() == current)
        {
            current++;
            myStack.pop();
        }

        if (line[idx] == current)
        {
            current++;
        }
        else
        {
            myStack.push(line[idx]);
        }
    }

    while(myStack.empty() != 1)
    {
        if (myStack.top() == current)
        {
            current++;
            myStack.pop();
        }
        else
        {
            isOkay = false;
            break;
        }
    }

    if (isOkay) cout << "Nice";
    else cout << "Sad";
} 