#include <iostream>
#include <stack>
#include <string>

#define TRUE 1
#define FALSE 0

using namespace std;

int main()
{
    string str;

    while (TRUE)
    {
        getline(cin, str);
        stack<char>myStack;
        bool isOkay = TRUE;

        if (str == ".")
        {
            break;
        }
        for (auto it = str.begin(); it != str.end(); it++)
        {
            if (*it == '(' || *it == '[')
            {
                myStack.push(*it);
            }
            else if (*it == ')')
            {
                if (myStack.empty() == 1 || myStack.top() == '[')
                {
                    isOkay = FALSE;
                    break;
                }
                myStack.pop();
            }
            else if (*it == ']')
            {
                if (myStack.empty() == 1 || myStack.top() == '(')
                {
                    isOkay = FALSE;
                    break;
                }
                myStack.pop();
            }
        }

        if (!myStack.empty()) isOkay = false;

        if (isOkay) cout << "yes" << '\n';
        else cout << "no" << '\n';
    }
}