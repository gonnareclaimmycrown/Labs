#include <iostream>

int main() {
#include <iostream>
#include <vector>
    using namespace std;

    int main() {
        int const size = 20;
        char cool[size];
        cout << "enter string" << endl;
        cin.getline(cool, size);
        vector <char> DigitWords(size);
        vector <char> DigitWordsFake(size);
        vector <char> OtherWords(size);
        int count = 0, i = 0, bear = 0;
        bool isDigitWord;
        while (true){
            cout << i << " ";
            int j = count;
            isDigitWord = true;
            if (int(cool[i]) < 48 || int(cool[i]) > 57){
                while(int(cool[i]) != 32 && i < size){
                    OtherWords.push_back(cool[i]);
                    i++;
                    isDigitWord = false;
                    bear = i;
                    cout << i << " ";
                }
            }
            else if (int(cool[i]) > 47 && int(cool[i]) < 58){
                while (int(cool[i]) != 32 && i < size){
                    DigitWordsFake.push_back(cool[i]);
                    i++;
                    if (int(cool[i]) < 48 || int(cool[i]) > 57){
                        isDigitWord = false;
                        DigitWordsFake.clear();
                        while (int(cool[i]) != 32 && i < size){
                            OtherWords.push_back (cool[bear]);
                            bear++;
                            i++;
                        }
                    }
                }
            }
            count = i;
            if (isDigitWord){
                while(j <= count){
                    j++;
                    DigitWords.push_back(cool[j]);
                }
            }
            i++;
            cout << "xd" << " ";
            if (i >= size){
                goto end1;
            }
        }
        end1:
        int k = 0;
        while (k < sizeof (cool)){
            cout << DigitWords[k];
            k++;
        }
        k = 0;
        while (k < sizeof (cool)){
            cout << OtherWords[k];
            k++;
        }
        return 0;
    }

