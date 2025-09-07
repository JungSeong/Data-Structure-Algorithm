#include <iostream>
#include <set>
#include <string>

using namespace std;

int main()
{
    int N, cnt=0;
    string str1, str2;
    set<string> mySet;
    cin >> N;

    cin.ignore();

    for (int idx=0; idx<N; idx++)
    {
        cin >> str1 >> str2;
        if (str1.compare("ChongChong") == 0 || str2.compare("ChongChong") == 0)
        {
            mySet.insert(str1);
            mySet.insert(str2);
        }
        else
        {
            if (mySet.count("ChongChong") != 0)
            {
                if (mySet.count(str1) != 0 || mySet.count(str2) != 0)
                {
                    mySet.insert(str1);
                    mySet.insert(str2);
                }
            }
        }
    }

    cout << mySet.size();
}