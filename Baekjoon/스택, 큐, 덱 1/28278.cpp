#include <iostream>
#include <stack>
#include <string>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    
    int N;
    cin >> N;

    string command;
    stack<int> my_stack;
    // size_t pos{}; // ?

    for (int idx=0; idx<=N; idx++)
    {
        getline(cin, command);

        if (command.length() > 1) // 1 X
        {
            string::size_type position = command.find(" ");
            int q_input = stoi(command.substr(position+1));
            my_stack.push(q_input);
        }
        else
        {
            if (command == "2")
            {
                if (my_stack.empty())
                {
                    cout << "-1" << '\n';
                }
                else
                {
                    cout << my_stack.top() << '\n';
                    my_stack.pop();
                }
            }
            else if (command == "3")
            {
                cout << my_stack.size() << '\n';
            }
            else if (command == "4")
            {
                if (my_stack.empty())
                {
                    cout << "1" << '\n';
                }
                else
                {
                    cout << "0" << '\n';
                }
            }
            else if (command == "5")
            {
                if (my_stack.empty())
                {
                    cout << "-1" << '\n';
                }
                else
                {
                    cout << my_stack.top() << '\n';
                }
            }    
        }
    }
}