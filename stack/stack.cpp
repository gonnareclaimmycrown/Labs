//
// Created by я on 02.01.2024.
//
#include "stdexcept"
#include "stack.h"
template <class T>
void stack<T>::push (T item){
    if (NeedToResize()){
        resize();
    }
    data[top] = item;
    top++;
}

template <class T>
T stack<T>::peek() {
    if (top <= 0){
        throw std::out_of_range("Attempted to peek an empty stack.");
    }
    return data[top -1];
}

template <class T>
T stack<T>::pop() {
    if (top <= 0){
        throw std::out_of_range("Attempted to peek an empty stack.");
    }
    top--;
    return data[top-1];
}

template <class T>
bool stack<T>::NeedToResize() {
    return (top == size);
}

template <class T>
void stack<T>::resize() {
    T* newdata = new T[2*size];
    for (int i = 0; i < size; i++){
        newdata[i] = data[i];
    }
    data = newdata;;
    size *= 2;
}

template <class T>
bool stack<T>::isEmpty() {
    return (top == 0);
}


/*
Stack() {
    storage_ = new T[capacity_];
    capacity_ = 1;
    n_ = 0;
    ~Stack();
    {
        delete[] storage_;
    }
}

bool is_empty() {
    if (capacity_==0) {
        return true;
    } else {
        return false;
    }
}

void resize(int capacity) {
    T *temp = new T[capacity];
    for (int i = 0; i < n_; ++i) {
        temp[i] = storage_[i];
    }
    delete[]storage_;
    storage_ = temp;
    capacity_ = capacity;
}

void operator<<(T item) { // push method
    if (n_ == capacity_) {
        resize(capacity_ * 2);
    }
    storage_[n_++] = item;
};

T pop() { // pop method
    is_empty();
    T item = storage_[--n_];
    if (n_ > 0 && n_ == capacity_ / 4) {
        resize(capacity_ / 2);
    }
    return item;
}

bool operator>(Stack X) {
if (capacity_ > X.capacity_) {
return true;
} else {
return false;
}
}

bool operator>=(Stack X) {
if (capacity_ >= X.capacity_) {
return true;
} else {
return false;
}
}

bool operator==(Stack X) {
if (capacity_ == X.capacity_) {
return true;
} else {
return false;
}
}

bool operator<(Stack X) {
if (capacity_ < X.capacity_) {
return true;
} else {
return false;
}
}

bool operator<=(Stack X) {
if (capacity_ <= X.capacity_) {
return true;
} else {
return false;
}
}

void operator=(const T &X) {
    storage_ = new T[X.capacity];
    for (int i = 0; i < X.capacity - 1; i++) {
        storage_[i] = X.storage_[i];
    }
    capacity_ = X.capacity;
}
*/