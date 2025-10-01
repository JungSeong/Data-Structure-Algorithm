#include <string>
#include <vector>
#include <utility>

using namespace std;

vector<pair<char, int>> chr{{'A',0},{'E',0},{'I',0},{'O',0},{'U',0}};
int answer = 0;
bool Isfound = false;

void vocabulary(string& str, string word, int pos)
{
    if (str.compare(word) == 0)
    {
        Isfound = true;
        return;
    }

    if (str.size() == 5) {return;}

    for (int i=0; i<5; i++)
    {
        if (Isfound) {return;}
        
        str.push_back(chr[i].first);
        chr[i].second++;
        answer++;
        vocabulary(str, word, pos+1);
        chr[i].second--;
        str.pop_back();
    }
}

int solution(string word)
{
    string str = "";
    vocabulary(str, word, 0);

    return answer;
}