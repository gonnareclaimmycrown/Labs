#include <iostream>
#include "stack.h"
#include "calculator.cpp"
int main() {
    stack<int> s;
    cout << s.isEmpty() << endl;
    for (int i = 0; i < 5; i++){
        s.push(i*(i+1));
    }
    cout << s.peek() << endl;
    while (!s.isEmpty()){
        cout << s.pop() << " ";
    }
    cout << endl;
    cout << evaluate("3 + 4 + 5") << endl; //12
    cout << evaluate("3 * 4 + 5") << endl; //17
    cout << evaluate("3 + 4 * 5") << endl; // 23
    cout << evaluate("(3 + 4) * 5") << endl; // 35
    return 0;
}
