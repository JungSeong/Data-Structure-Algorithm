#include <string>
#include <vector>

using namespace std;

int answer[8] = {0};
int max_cnt = 0;

void enter_dungeon(int k, int cnt, vector<vector<int>>& dungeons)
{
    bool canJoin = false;

    for (int i=0; i<dungeons.size(); i++)
    {
        if (k >= dungeons[i][0] && answer[i]) {canJoin = true; break;}
    }

    if (!canJoin)
    {
        max_cnt = max(max_cnt, cnt);
        return;
    }

    for (int i=0; i<dungeons.size(); i++)
    {
        if (k >= dungeons[i][0] && answer[i]>0)
        {
            answer[i]=0;
            enter_dungeon(k-dungeons[i][1], cnt+1, dungeons);
            answer[i]=1;
        }
    }
}

int solution(int k, vector<vector<int>> dungeons) {
    for (int i=0; i<dungeons.size(); i++)
    {
        answer[i] = 1;
    }

    enter_dungeon(k, 0, dungeons);

    return max_cnt;
}