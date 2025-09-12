#include <string>
#include <stack>
#include <iostream>

using namespace std;

bool solution(string s)
{
    stack<char> myStack;
    bool answer = true;
    
    for (auto it=s.begin(); it!=s.end(); it++)
    {
        if (*it == '(')
        {
            myStack.push(*it);
        }
        else
        {
            if (!myStack.empty() && myStack.top() == '(')
            {
                myStack.pop();
            }
            else
            {
                answer = false;
                return answer;
            }
        }
    }

    if (!myStack.empty()) {answer = false;}
    return answer;
}