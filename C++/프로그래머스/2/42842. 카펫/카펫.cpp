#include <string>
#include <vector>
#include <cmath>

using namespace std;

vector<int> solution(int brown, int yellow) {
    vector<int> answer;
    int j;
    for (int i=1; i<=sqrt(yellow); i++)
    {
        if (yellow % i == 0)
        {
            j = yellow / i;
        }
        if ((i+2)*(j+2) - i*j == brown)
        {
            answer.push_back(j+2);
            answer.push_back(i+2);
            return answer;
        }
    }
}