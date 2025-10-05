#include <bits/stdc++.h>

using namespace std;

int main()
{
    int arr[8];
    for (int i=0; i<8; i++) {cin >> arr[i];}
    
    bool isAsc = true;
    bool isDec = true;
    
    for (int i=0; i<7; i++)
    {
        if (arr[i] < arr[i+1]) {isDec = false;}
        if (arr[i] > arr[i+1]) {isAsc = false;}
    }
    
    if (isAsc) {cout << "ascending";}
    if (isDec) {cout << "descending";}
    
    if (!isAsc && !isDec) {cout << "mixed";}
}