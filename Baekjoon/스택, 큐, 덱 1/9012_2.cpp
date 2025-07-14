#include <iostream>
#include <stack>
#include <string>

using namespace std;

#define TRUE 1
#define FALSE 0

int main()
{
    string str;
    int T;
    bool isOkay = TRUE;
    cin >> T;
    cin.ignore();

    for (int idx=0; idx<T; idx++)
    {
        stack<char> myStack;
        isOkay = TRUE;
        getline(cin, str);

        for (char chr : str)
        {
            if (chr == '(')
            {
                myStack.push(chr);
            }
            else
            {
                if (myStack.empty() == 1 || myStack.top() != '(')
                {
                    isOkay = FALSE;
                    break;
                }
                myStack.pop();
            }
        }
        if (myStack.empty() != 1) {isOkay = FALSE;}
        if (isOkay == TRUE) {cout << "YES" << '\n';}
        else {cout << "NO" << '\n';}
    }
}