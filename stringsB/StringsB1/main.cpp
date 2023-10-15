#include <iostream>
#include <vector>
using namespace std;

int main() {
    int const size = 300;
    char cool[size];
    int WordSize = 0;
    cout << "enter string" << endl;
    cin.getline(cool, size);
    vector <char> DigitWords;
    vector <char> DigitWordsFake;
    vector <char> OtherWords;
    vector <char> Word;
    int i = 0;
    bool isDigitWord;
    while (i < size) {
        isDigitWord = true;
        while (int(cool[i]) != 32 && i < size) {
            Word.push_back(cool[i]);
            if (int(Word[i]) < 48 || int(Word[i]) > 57){
                isDigitWord = false;
            }
            i++;
            WordSize++;
        }
        char space = 32;
        Word.push_back(space);
        if (isDigitWord) {
            for (int j = 0; Word[j] != '\0'; j++) {
                DigitWords.push_back(Word[j]);
            }
        } else {
            for (int j = 0; Word[j] != '\0'; j++) {
                OtherWords.push_back(Word[j]);
            }
        }
        Word.clear();
        i++;
    }
    cout << endl;
    for (int k = 0; DigitWords[k] != '\0'; k++){
        DigitWords.push_back(OtherWords[k]);
        cout << DigitWords[k];
    }
    return 0;
}
