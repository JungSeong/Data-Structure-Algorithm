#include <string>
#include <vector>
#include <map>
#include <unordered_set>
#include <cmath>

using namespace std;

bool isPrime(int elem)
{
    if (elem == 1) {return false;}
    if (elem == 2) {return true;}
    if (elem % 2 == 0) {return false;}
    for (int i=3; i<=sqrt(elem); i++)
    {
        if (elem % i == 0) {return false;}
    }
    return true;
}

void buildNum(map<char, int>& num, string& str, int len, unordered_set<int>& bag)
{
    if (str.size() == len)
    {
        bag.insert(stoi(str));
        return;
    }
    for (auto& kv : num)
    {
        char k = kv.first;
        int& v = kv.second;
        if (v == 0) continue;
        v--;
        str.push_back(k);
        buildNum(num, str, len, bag);
        v++;
        str.pop_back();
    }
}

int solution(string numbers)
{
    int answer = 0;
    map<char, int> num;
    for (auto elem : numbers)
    {
        num[elem]++;
    }
    
    unordered_set<int> bag;
    string str;

    for (int i=1; i<=numbers.size(); i++)
    {
        buildNum(num, str, i, bag);
    }

    for (auto elem : bag)
    {
        if(isPrime(elem)) {answer++;}
    }
    
    return answer;
}