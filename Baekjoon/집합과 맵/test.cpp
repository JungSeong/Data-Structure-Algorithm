#include <iostream>
#include <string>

using namespace std;

int main()
{
    string str1 = "happy";
    string str2 = "25";

    for (int idx=0; idx<str1.length(); idx++)
    {
        if (isdigit(str1[idx]) == 0)
        {
            cout << '0';
        }
        else
        {
            cout << '1';
        }
    }
}