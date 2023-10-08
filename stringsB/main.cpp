#include <iostream>

using namespace std;

int main() {
    int xd = 20;
    char main[xd];
    int count(0), count1 (0), i(0);
    cout << "enter text" << endl;
    cin.getline(main, sizeof(main));
    while (i < xd){
        if (int(main[i]) > 58 || int(main[i]) < 48){
            do {
                i++;
            } while (int(main[i]) != 32);
        }
        else {
            for (int j = i; int(main[j]) != 32; j++){
                count++;
                main[j-1] = main[j];
                if (int(main[j]) > 58 || int(main[j]) < 48 ){
                    while (count != 0){
                        main[j] = main[j+1];
                        j++;
                        count--;
                    }
                    for (int k = 0; int(main[k]) != 32; k++){
                        count = 0;
                        count1++;
                    }
                }
                i += count1;
                count1 = 0;
            }
            /* do {
                i++;
                count++;
                if (int(main[i]) > 58 || int(main[i]) < 48) {
                    count = 0;
                    do {
                        i++;
                    } while (int(main[i]) != 32);
                }
            for (int j = (i - count); int(main[j]) != 32; j++) {
                main[j] = main[j + 1];
            }
            } while (int(main[i]) != 32);
             */
    }
    }
    for (int j = 0; j < xd; j++){
        cout << main[j] << " ";
    }
    return 0;
}
