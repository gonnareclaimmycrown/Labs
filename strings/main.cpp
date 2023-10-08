#include <iostream>
#include "iomanip"
using namespace std;

int strcmp(char *str1, const char *str2){
    int i(0), summ(0), first, last;
    while (str1[i] != '\0'){
        summ += int(str1[i]);
        i++;
    }
    first = summ;
    summ = 0;
    i = 0;
    while (str2[i] != '\0') {
        summ += int(str2[i]);
        i++;
    }
    last = summ;
    if (first == last){
        return 0;
    }
    if (first < last){
        return -1;
    }
    if (first > last){
        return 1;
    }
}

int main() {
    char comparative[] = "apples";
    int size;
    cin >> size;
    char compar[size];
    cin >> compar;
    cout << strcmp(compar, comparative);
    return 0;
}
