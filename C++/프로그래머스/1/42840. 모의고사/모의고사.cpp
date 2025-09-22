#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> answers) {
    int person1[5] = {1,2,3,4,5};
    int person2[8] = {2,1,2,3,2,4,2,5};
    int person3[10] = {3,3,1,1,2,2,4,4,5,5};
    
    int correct[3] = {0,0,0};
    
    for (int i=0; i<answers.size(); i++)
    {
        if (person1[i%5] == answers[i]) {correct[0]++;}
        if (person2[i%8] == answers[i]) {correct[1]++;}
        if (person3[i%10] == answers[i]) {correct[2]++;}
    }
    
    int max=0;
    
    for (int i=0; i<3; i++)
    {
        if (correct[i] > max)
        {
            max = correct[i];
        }
    }
    
    vector<int> answer;
    
    for (int i=0; i<3; i++)
    {
        if (correct[i] == max)
        {
            answer.push_back(i+1);
        }
    }
    
    return answer;
}