#include <string>
#include <vector>

using namespace std;

int solution(vector<vector<int>> sizes) {
    for (int i=0; i<sizes.size(); i++)
    {
        if (sizes[i][0] < sizes[i][1])
        {
            int it = sizes[i][0];
            sizes[i][0] = sizes[i][1];
            sizes[i][1] = it;
        }
    }
    
    int w_max=0, h_max=0;
    
    for (auto elem : sizes)
    {
        if (w_max < elem[0]) {w_max = elem[0];}
        if (h_max < elem[1]) {h_max = elem[1];}
    }
    
    int answer = w_max * h_max;
    return answer;
}