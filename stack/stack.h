//
// Created by я on 10.12.2023.
//

#ifndef STACK_STACK_H
#define STACK_STACK_H

#include <vector>
#include <cstring>
#include <iostream>
#include <new>
using namespace std;

template <class T>
class stack {
private:
    int size;
    int top;
    T* data;
    void resize();
    bool NeedToResize();
public:
    stack(){
        size = 5;
        data = new T(size);
        top = 0;
    }
    void push(T item);
    T peek();
    T pop();
    bool isEmpty();
};
#include "stack.cpp"
#endif //STACK_STACK_H
