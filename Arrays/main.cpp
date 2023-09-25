#include <iostream>
#include "cstdlib"
#include <ctime>
using namespace std;

int main() {
    int leftmeas, rightmeas, summ (0), last, prod (1), value, count(0);
    double first;
    int h1(0), h2(0);
    int* theonlyone = new int[value];
    cout << "Enter measurements" << endl;
    cin >> leftmeas >> rightmeas;
    cout << "Enter the number of elements in array" << endl;
    cin >> value;
    srand(time(NULL));
    cout << "first version of array: ";
    for (int i = 0; i < value; i++){
        theonlyone[i] = rand() % (leftmeas - rightmeas) + leftmeas;
    }
    for (int i = 0; i < value; i++){
        cout << theonlyone[i] << " ";
    }
    for (int i = 0; i < value; i++){
        if (i % 2 != 0) {
            summ = summ + theonlyone[i];
        }
    }
    for (int i = 0; i < value; i++){
        if (theonlyone[i] < 0){
            first = i;
            h1 = i;
            break;
        }
    }
    for (int i = value - 1; i >= 0; i--){
        if (theonlyone[i] < 0){
            last = i;
            h2 = i;
            break;
        }
    }
    while (h1 < (h2 - 1)){
        prod = prod * theonlyone[h1+1];
        h1++;
    }
    for (int i = 0; i < (value - count); i++){
        if (abs(theonlyone[i]) <= 1){
            for (int j = i; j < (value - 1); j++ ){
                theonlyone[j] = theonlyone[j+1];
            }
            i--;
            count = count + 1;
        }
    }
    for (int i = value - 1; i >= (value - count); i--){
        theonlyone[i] = 0;
    }
    cout << endl;
    cout << "Summ of all uneven elements equals: " << summ << endl;
    if (first == last){
        cout << "there are no elements between two negative numbers" << endl;
    }
    else if (first == last + 1){
        cout << "there are no elements between two negative numbers" << endl;
    }
    else{
        cout << "product of all elements between first negative and last one equals: " << prod << endl;
    }
    for (int i = 0; i < value; i++){
        cout << theonlyone[i] << " ";
    }
    cout << "- this is a version of array where all |elements| <= 1 are now zeros";
    delete[]theonlyone;
    return 0;
}
