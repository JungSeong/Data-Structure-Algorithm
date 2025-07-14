#include <iostream>
#include <string>
#include <stack>

using namespace std;

int main()
{
    int T, cnt=0;
    string str;

    cin >> T;
    cin.ignore();

    for (int idx=0; idx<T; idx++)
    {
        stack<char> myStack;
        cnt = 0;

        getline(cin, str);
        for (auto it = str.begin(); it != str.end(); it++)
        {
            myStack.push(*it);
        }

        while(myStack.empty() != 1)
        {
            if (myStack.top() == ')')
            {
                myStack.pop();
                cnt++;
            }
            else if (myStack.top() == '(')
            {
                myStack.pop();
                cnt--;

                if (cnt < 0)
                { 
                    cout << "NO" << '\n';
                    break;
                }
            }
        }

        if (cnt == 0)
        {
            cout << "YES" << '\n';
        }
        else if (cnt > 0)
        {
            cout << "NO" << '\n';
        }
    }
}