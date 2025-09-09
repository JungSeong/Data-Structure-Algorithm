#include <string>
#include <vector>

using namespace std;

int solution(vector<string> babbling) {
    int answer = 0;
    for (auto it=babbling.begin(); it!=babbling.end(); it++)
    {
        while(true)
        {
            if (it->empty()) {answer++; break;}
            if (it->find("aya")==0 || it->find("woo")==0)
            {
                *it = it->substr(3);
            }
            else if (it->find("ye")==0 || it->find("ma")==0)
            {
                *it = it->substr(2);
            }
            else
            {
                break;
            }
        }
    }
    return answer;
}