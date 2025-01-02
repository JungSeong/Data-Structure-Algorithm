#include <iostream>
#include <stack>
using namespace std;

int main(void) {

	stack<int> st;
	stack<int> st2;

	st.push(1);
	st.push(2);
	st.push(3);

	st2.push(10);
	st2.push(20);
	st2.push(30);

	swap(st, st2);

	while (!st.empty()) {
		cout << st.top() << endl;
		st.pop();
	}

	return 0;
}