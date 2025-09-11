#include <string>
#include <vector>

using namespace std;

int solution(vector<vector<int>> lines) {
    int arr[201] = {0};
    int answer = 0;
    
    for (const auto& it : lines)
    {
        for (int i=it[0]; i<it[1]; i++)
        {
            arr[i+100]++;
        }
    }
    
    for (int i=0; i<200; i++)
    {
        if (arr[i]>=2)
        {
            answer++;
        }
    }
    return answer;
}