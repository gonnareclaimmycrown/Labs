//
// Created by я on 26.11.2023.
//
#include "iostream"
#include "string"
#include "vector"
#include "class.h"

using namespace std;

student::student(int age, int year, int group, const int number, int id, string name) {
    this->group = group;
    this->year = year;
    this->age = age;
    this->id = id;
    this->number = number;
    this->name = new char[name.size()];
    for (int i = 0; i < name.size(); i++){
        this->name[i] = name[i];
    }
    count++;
    id = count;
    this->NameSize = name.size();
}

student::student(const student &ts) {
    this->group = ts.group;
    this->NameSize = ts.NameSize;
    this->year = ts.year;
    this->age = ts.age;
    this->id = ts.id;
    this->number = ts.number;
    this->name = new char[ts.NameSize];
    for (int i = 0; i < ts.NameSize; i++){
        this->name[i] = ts.name[i];
    }
}

ostream& operator << (ostream& os, student& ts){
    os << "age: " << ts.age << '/' << "year: " << ts.year << '/' << "group: " << ts.group;
    os << "Identificator: " << ts.id;
    os << "name: ";
    for (int i = 0; i < ts.NameSize; i++){
        os << ts.name[i];
    }
}

studenta1::studenta1(int age, int year, int group, const int number, int id, string name, int a, int b, int c, int d) : student(age, year, group, number, id, name) {
    this->group = group;
    this->year = year;
    this->age = age;
    this->id = id;
    this->number = number;
    this->name = new char[name.size()];
    for (int i = 0; i < name.size(); i++){
        this->name[i] = name[i];
    }
    this->NameSize = name.size();
    this->marks1[0]=a;
    this->marks1[1]=b;
    this->marks1[2]=c;
    this->marks1[3]=d;
    double avg = ((a+b+c+d) / 4);
}

studenta1::studenta1(studenta1 &ts) : student(age, year, group, number, id, name) {
    this->year = ts.GetYear();
    this->group = ts.GetGroup();
    this->name = ts.GetName();
    this->number = ts.number;
    this->NameSize = ts.GetNameSize();
    this->marks1[0] = ts.marks1[0];
    this->marks1[1] = ts.marks1[1];
    this->marks1[2] = ts.marks1[2];
    this->marks1[3] = ts.marks1[3];
    double avg = (marks1[0]+marks1[1]+marks1[2]+marks1[3])/4;
}

ostream& operator << (ostream& os, studenta1& ts){
    os << "age: " << ts.age << '/' << "year: " << ts.year << '/' << "group: " << ts.group;
    os << "Identificator: " << ts.id;
    os << "name: ";
    for (int i = 0; i < ts.NameSize; i++){
        os << ts.name[i];
    }
    os << "Marks: ";
    for (int i = 0; i < ts.NameSize; i++){
        os << ts.marks1[i] << " ";
    }
}

studenta2::studenta2(studenta2 &ts) : studenta1(age, year, group, number, id, name, marks1[0], marks1[1], marks1[2], marks1[3]){
    this->group = ts.GetGroup();
    this->name = ts.GetName();
    this->number = ts.number;
    this->NameSize = ts.GetNameSize();
    this->marks[0] = ts.marks[0];
    this->marks[1] = ts.marks[1];
    this->marks[2] = ts.marks[2];
    this->marks[3] = ts.marks[3];
    this->marks[4] = ts.marks[4];
    this->marks1[0] = ts.marks1[0];
    this->marks1[1] = ts.marks1[1];
    this->marks1[2] = ts.marks1[2];
    this->marks1[3] = ts.marks1[3];
    double avg1 = (marks[0] + marks[1] + marks[2] + marks[3] + marks[4]) / 5;
    double avgayear = (marks[0] + marks[1] + marks[2] + marks[3] + marks[4] + marks1[0] + marks1[1] + marks1[2] + marks1[3]) / 9;
}

ostream& operator << (ostream& os, studenta2& ts){
    os << "age: " << ts.age << '/' << "year: " << ts.year << '/' << "group: " << ts.group << endl;
    os << "Identificator: " << ts.id << endl;
    os << "name: ";
    for (int i = 0; i < ts.NameSize; i++){
        os << ts.name[i];
    }
    os << endl << "Marks: ";
    for (int i = 0; i < ts.NameSize; i++){
        os << ts.marks[i] << " ";
    }
    os << endl << "avg after 2 session" << ts.avg1 << endl;
    os << "avg after a year" << ts.avgayear;
}


