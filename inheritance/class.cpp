//
// Created by я on 26.11.2023.
//
#include "iostream"
#include "string"
#include "vector"
#include "class.h"

using namespace std;

vector<char> student::indcreate(char name, int number, int group, int year) {
    vector<char> identificator1;
    identificator1.push_back(name);
    identificator1.push_back(number);
    identificator1.push_back(year);
    identificator1.push_back(group);
}

ostream& student::operator << (ostream& os, student& ts){
    os << ts.name << '/' << ts.age << '/' << ts.year << '/' << ts.group;
    os << "Identificator: ";
}

ostream& studenta1::operator << (ostream& os, studenta1& ts){
    os << ts.name << '/' << ts.age << '/' << ts.year << '/' << ts.group;
    os << "Identificator: ";
    os << "Marks: ";
    for (int i = 0; i < 4; i++){
        os << ts.marks1[i] << " ";
    }
}

ostream& studenta2::operator << (ostream& os, studenta2& ts){
    os << ts.name << '/' << ts.age << '/' << ts.year << '/' << ts.group;
    os << "Identificator: ";
    os << "Marks: ";
    for (int i = 0; i < 5; i++){
        os << marks[i] << " ";
    }
}

double studenta1::avg(int marks[4]){
    int summ = 0;
    for (int i = 0; i < 4; i++){
        summ += marks[i];
    }
    return summ/4;
}

double studenta2::avg(int marks[5]){

}
