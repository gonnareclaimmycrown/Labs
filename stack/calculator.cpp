//
// Created by я on 02.01.2024.
//
#include "stack.h"
#include "iostream"
#include "string"
using namespace std;
bool isDigit(char c){
    return (c >= '0' && c <= '9');
}

bool isOperator(char c){
    return (c == '+' || c== '-' || c == '*' || c == '/' || c == '(' || c == ')');
}
int getPrecendence (char c){
    switch (c) {
        case '+':
        case '-': return 1;
        case '*':
        case '/': return 2;
        case '(':
        case ')': return 3;
        default: return -1;
    }
}
int operate (int val1, int val2, char op){
    if (op == '+') return val1 + val2;
    if (op == '-') return val1 - val2;
    if (op == '*') return val1 * val2;
    return val1 / val2;
}
int evaluate (string s){
    stack<int> vals;
    stack<char> ops;

    int val = 0;
    int pos = 0;
    char op = 0;

    while (pos < s.length()){
        char spot = s[pos];
        if (isDigit(spot)){
            val = (val * 10) + (int)(spot - '0');
        }
        else if (isOperator(spot)) {
            if (spot == '(') {
            ops.push(spot);
            val = 0;
        }
            else if (vals.isEmpty()){
                vals.push(val);
                ops.push(spot);
                val = 0;
            }
            else if (spot == ')'){
                vals.push(val);
                while (ops.peek() != '('){
                    spot = ops.pop();
                    val = vals.pop();
                    int prev = vals.pop();
                    val = operate(prev, val, spot);
                    vals.push(val);
                }
                ops.pop();
                vals.pop();
            }
            else{
                char prev = ops.peek();
                if (getPrecendence(spot) > getPrecendence(prev)){
                    vals.push(val);
                    ops.push(spot);
                    val = 0;
                }
                else{
                    int prevVal = vals.pop();
                    int prevOp = ops.pop();
                    prevVal = operate(prevVal, val, prevOp);
                    vals.push(prevVal);
                    ops.push(spot);
                    val = 0;
                }
            }
        }
        pos++;
    }
    while (!ops.isEmpty()){
        int prev = vals.pop();
        char spot = ops.pop();
        val = operate(prev, val, spot);
    }
    return val;
}