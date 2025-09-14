#include <iostream>
#include <vector>
#include <set>

using namespace std;

int solution(vector<int> nums)
{
    set<int> s;
    for (int i=0; i<nums.size(); i++)
    {
        s.insert(nums[i]);
    }
    int answer;
    if (s.size() >= nums.size()/2) {answer = nums.size()/2;}
    else {answer = s.size();}
    return answer;
}