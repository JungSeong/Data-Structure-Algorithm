#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> arr) 
{
    vector<int> answer;
    
    for (auto it=arr.begin(); it!=arr.end()-1; it++)
    {
        if (*it != *(it+1))
        {
            answer.push_back(*it);
        }
    }
    
    answer.push_back(arr.back());

    return answer;
}