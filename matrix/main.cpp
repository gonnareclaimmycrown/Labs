#include "vector"
#include "time.h"
#include "cmath"
#include <iostream>
using namespace std;
int main() {
    srand(time(NULL));
    int size, lowerbound, upperbound, sum(0), prod(1), lim(0), max;
    start:
    cout << "enter the size of square matrix (0-10)" << endl;
    cin >> size;
    if (size > 10){
        cout << "unlucky this time, try later" << endl;
        goto start;
    }
    cout << "enter the lower boundary and the upper boundary of elements for matrix" << endl;
    cin >> lowerbound >> upperbound;
    max = lowerbound;
    vector<vector<int> > v3(size, vector<int>(size));
    for (int i = 0; i < size; i++){
        for (int j = 0; j < size; j++){
            v3[i][j] = rand() % (upperbound - lowerbound) + lowerbound;
        }
    }
    for (int i = 0; i < size; i++){
        cout << endl;
        for (int j = 0; j < size; j++){
            cout << v3[i][j] << " ";
        }
    }
    cout << endl;
    for (int i = 0; i < size; i++){
        for (int j = 0; j < size; j++){
            if ((i+j) % 2 != 0){
                v3[i][j] = 1;
            }
        }
    }
    cout << endl;
    cout << "v3[i][j] = 1 if i+j is uneven:";
    for (int i = 0; i < size; i++){
        cout << endl;
        for (int j = 0; j < size; j++){
            cout << v3[i][j] << " ";
        }
    }
    cout << endl;
    for (int i = 0; i < size; i++){
        if (i > 0){
            sum = 0;
            }
        for (int j = 0; j < size; j++){
            if (v3[i][j] == 0){
                cout << i << " row does have zero in it" << endl;
                sum = 0;
                break;
            }
            else if (v3[i][j] != 0){
                sum = sum + v3[i][j];
            }
            if (j == (size - 1)){
                cout << "summ of elements in row " << i << ":" << " " << sum << endl;
            }
        }
    }
    int l = 0;
    int num2;
    int i(0), j(size - 1), xd, row2(1), row;
    xd = (size);
    while (j > i){
                while (row2 != xd){
                l++;
                num2 = (size - l);
                row = 0;
                    for (int num = (size - 1); num > (size - l - 1); num--){
                        prod *= v3[row][num2];
                        num2++;
                        row++;
                    }
                    if (max < prod){
                    max = prod;
                    }
                row2++;
                prod = 1;
            }
        j--;
    }
    xd = size;
    l = 0;
    i = (size - 1);
    j = 0;
    row2 = 1;
    while (j < i){
        while(row2 != xd){
        num2 = l;
        l++;
        row = (size - 1);
            for (int num = (size - 1); num > (size - l - 1); num--){
                prod *= v3[row][num2];
                num2--;
                row--;
            }
            if (max < prod){
            max = prod;
        }
        row2++;
        prod = 1;
        }
    i--;
    }
    cout << endl;
    cout << "The biggest product of elements in diagonals parallel to the main one is " << max;
    return 0;
}
