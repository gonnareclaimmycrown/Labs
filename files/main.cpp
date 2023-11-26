#include <iostream>
#include <fstream>
#include <string>
using namespace std;
int main() {
    ifstream input_file("..\\input.txt");
    if (!input_file.is_open()) {
        cout << "File no found." << endl;
        return 0;
    }

    ofstream output_file1("..\\output1.txt");
    ofstream output_file2("..\\output2.txt");

    if (!output_file1.is_open() || !output_file2.is_open()) {
        cout << "Couldn't open the files" << endl;
        return 0;
    }

    string line;
    while (getline(input_file, line)) {
        int word_count = 0;
        for (int i = 0; i < line.length(); i++) {
            if (line[i] == ' ' && line[i-1] != ' ') {
                word_count++;
            }
        }
        word_count++;

        if (word_count <= 2) {
            output_file1 << line << endl;
        } else if (word_count >= 3 && word_count <= 6) {
            output_file2 << line << endl;
        }
    }

    output_file1.close();
    output_file2.close();
    input_file.close();

    return 0;
}