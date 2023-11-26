//
// Created by я on 26.11.2023.
//

#ifndef INHERITANCE_CLASS_H
#define INHERITANCE_CLASS_H

#endif //INHERITANCE_CLASS_H

#include "iostream"
#include "string"
#include "vector"
using namespace std;

class student{
protected:
    char name;
    int age;
    int year;
    int group;
    const int number;
    vector<char> indcreate(char name, int number, int group, int year);
    vector <char> identificator = indcreate(name, number, group, year);

public:
    char GetName(){
        return name;
    };
    int GetAge(){
        return age;
    };
    int GetYear(){
        return year;
    };
    int GetGroup(){
        return group;
    };
    const int GetNumber(){
        return number;
    };
    vector<char> GetIdentificator(){
        return identificator;
    };
    char SetName(char value){
        name = value;
    }
    int SetYear(int value){
        year = value;
    }
    int SetAge(int value){
        age = value;
    }
    int SetGroup(int value){
        group = value;
    }

    friend ostream operator << (ostream& os, student& testsubj);

};

class studenta1: protected student{
private:
    int marks1[4];
public:
    int GetMarks() {
        for (int i = 0; i < 4; i++) {
        cout << marks1[i];
        }
    }
    int SetMarks(int a, int b, int c, int d){
        marks1[1] = a;
        marks1[2] = b;
        marks1[3] = c;
        marks1[4] = d;
    }

    virtual double avg(int marks[]);

};
class studenta2: private studenta1{
private:
    int marks[5];
public:

    double avg(int marks[]) override;

    int GetMarks() {
        for (int i = 0; i < 5; i++) {
            cout << marks[i];
        }
    }
    int SetMarks(int a, int b, int c, int d, int e){
        marks[1] = a;
        marks[2] = b;
        marks[3] = c;
        marks[4] = d;
        marks[5] = e;
    }

};