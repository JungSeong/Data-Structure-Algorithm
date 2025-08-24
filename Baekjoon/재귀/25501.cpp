#include <iostream>
#include <string>
#include <utility>

using namespace std;

pair<int, int> recursion(string& s, int l, int r, int cnt){
    if (l >= r) return make_pair(1, cnt+1);
    else if(s[l] != s[r]) return make_pair(0, cnt+1);
    else return recursion(s, l+1, r-1, cnt+1);
}

// int cnt_recursion(string s, int l, int r, int cnt)
// {
//     if(l >= r) return cnt+1;
//     else if(s[l] != s[r]) return cnt+1;
//     else return cnt_recursion(s, l+1, r-1, cnt+1);
// }

void isPalindrome(string& s){
    pair<int, int> isPal = recursion(s, 0, s.length()-1, 0);

    cout << isPal.first << ' ' << isPal.second << '\n';
}

int main()
{
    ios::sync_with_stdio(false);
    // cin.tie(NULL);

    int T;
    string str;

    cin >> T;
    cin.ignore();

    for (int i=0; i<T; i++)
    {
        getline(cin, str);
        isPalindrome(str);
    }
}