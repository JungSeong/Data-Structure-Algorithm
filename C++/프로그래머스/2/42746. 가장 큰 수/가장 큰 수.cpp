#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool rule(string num1, string num2)
{
    return num1+num2 > num2+num1;
}

string solution(vector<int> numbers) {
    vector<string> numbers_str;
    
    for (auto& elem : numbers)
    {
        numbers_str.push_back(to_string(elem));
    }
    
    sort(numbers_str.begin(), numbers_str.end(), rule);
    
    string answer = "";
    
    for (const auto& elem : numbers_str)
    {
        answer += elem;
    }
    
    if (answer == string(answer.length(), '0'))
    {
        answer = "0";
    }
    
    return answer;
}