#include <iostream>
#include <fstream>
#include <string>
using namespace std;
int main() {
    string input_file_name("..\\input.txt");

    ifstream input_file(input_file_name);
    if (!input_file) {
        cout << "File no found." << endl;
        return 0;
    }

    string output_file1_name("..\\output1.txt");

    string output_file2_name("..\\output2.txt");

    ofstream output_file1(output_file1_name);
    ofstream output_file2(output_file2_name);

    if (!output_file1 || !output_file2) {
        cout << "Couldn't open the files" << endl;
        return 0;
    }

    string line;
    while (getline(input_file, line)) {
        int word_count = 0;
        for (char c : line) {
            if (c == ' ') {
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