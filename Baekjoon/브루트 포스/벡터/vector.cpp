#include <iostream>
#include <vector>
using namespace std;

int main(){
    vector<int> v;
    v.push_back(10);
    cout << "v.back() <added> : " << v.back() << "\n";  // v.back() <added> : 10
    
    cout << "v.size() : " << v.size() << "\n";  // v.size() : 4
    v.push_back(12);
    v.push_back(14);
    v.push_back(16);
    v.push_back(18);
    cout << "v.size() <added> : " << v.size() << "\n";  // v.size() <added> : 8

    v.pop_back();
    cout << "v.size() <pop-1> : " << v.size() << "\n";  // v.size() <pop-1> : 7
    cout << "v.back() <pop-1> : " << v.back() << "\n";  // v.back() <pop-1> : 16
    v.pop_back();
    cout << "v.size() <pop-2> : " << v.size() << "\n";  // v.size() <pop-2> : 6
    cout << "v.back() <pop-2> : " << v.back() << "\n";  // v.back() <pop-2> : 14
    v.pop_back();
    cout << "v.size() <pop-3> : " << v.size() << "\n";  // v.size() <pop-3> : 5
    cout << "v.back() <pop-3> : " << v.back() << "\n";  // v.back() <pop-3> : 12
}
