#include <string>
#include <vector>
#include <numeric>

using namespace std;

vector<int> solution(int numer1, int denom1, int numer2, int denom2) {
    int div = lcm(denom1, denom2);
    int mul1 = div / denom1;
    int mul2 = div / denom2;
    
    int numer = mul1 * numer1 + mul2 * numer2;
    int gc = gcd(numer, div);
    
    vector<int> answer;
    
    answer.push_back(numer / gc);
    answer.push_back(div / gc);

    return answer;
}