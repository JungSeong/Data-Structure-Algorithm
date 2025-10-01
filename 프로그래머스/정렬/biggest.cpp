#include <string>
#include <vector>
#include <iostream>
#include <cstdlib>
#include <algorithm>

using namespace std;

bool rule(string num1, string num2)
{
    if (num1+num2 > num2+num1) {return num1 > num2;}
    else {return num2 > num1;}
}

string solution(vector<int> numbers) {
    vector<string> numbers_str;
    
    for (auto& elem : numbers)
    {
        numbers_str.push_back(to_string(elem));
    }
    
    sort(numbers_str.begin(), numbers_str.end(), greater<string>());
    sort(numbers_str.begin(), numbers_str.end(), rule);

    string answer = "";
    
    for (const auto& elem : numbers_str)
    {
        answer += elem;
    }
    
    return answer;
}

int main()
{
    cout << solution({3, 38, 30, 5, 9});
}