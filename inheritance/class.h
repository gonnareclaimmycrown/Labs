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
public:
    static int count;
protected:
    char* name;
    int age;
    int year;
    int group;
    int number;
    int id;
    int NameSize;
    student(int age, int year, int group, const int number, int id, string name);
    student(const student &ts);

public:
    char *GetName() {
        return name;
    }
    int GetAge(){
        return age;
    };
    int GetYear(){
        return year;
    };
    int GetGroup(){
        return group;
    };
    int GetNameSize() const {
        return NameSize;
    }
    const int GetNumber(){
        return number;
    };
    int GetId(){
        return id;
    };
    void SetYear(int value){
        year = value;
    }
    void SetAge(int value){
        age = value;
    }
    void SetGroup(int value){
        group = value;
    }
    void SetName(string _name){
        this->name =new char[NameSize];
        for (int i = 0; i < NameSize; i++){
            this->name[i] = _name[i];
        }
    }

    friend ostream &operator << (ostream& os, student& testsubj);
    virtual double AvgMarkAft1session(){
        return 0;
    };
    virtual double AvgMarkAft2session(){
        return 0;
    };
};

class studenta1: protected student{
protected:
    int marks1[4];
    double avg;
public:
    friend ostream &operator << (ostream& os, studenta1& testsubj);
    studenta1(int age, int year, int group, const int number, int id, std::string name, int a, int b, int c, int d);
    studenta1(studenta1 &ts);
    using student::GetAge;
    using student::GetGroup;
    using student::GetYear;
    using student::GetName;
    using student::GetId;
    using student::GetNumber;
    int GetMarks() {
        for (int i = 0; i < 4; i++) {
        cout << marks1[i];
        }
    }

    double GetAvg(){
        return avg;
    }

    virtual int SetMark1(int a) {
        marks1[0] = a;
    }

    virtual int SetMark2(int b) {
        marks1[1] = b;
    }

    virtual int SetMark3(int c) {
        marks1[2] = c;
    }

    virtual int SetMark4(int d) {
        marks1[3] = d;
    }
    double AvgMarkAft1session() override;
};
class studenta2: studenta1{
private:
    int marks[5];
    double avg1;
    double avgayear;
public:
    double AvgMarkAft1session() override;
    double AvgMarkAft2session() override;

    int GetMarks() {
        for (int i = 0; i < 5; i++) {
            cout << marks[i];
        }
    }
    int SetMark1(int a) {
        marks[0] = a;
    }
    int SetMark2(int b) {
        marks[1] = b;
    }
    int SetMark3(int c) {
        marks[2] = c;
    }
    int SetMark4(int d) {
        marks[3] = d;
    }
    int SetMark5(int e){
        marks[4] = e;
    }
    studenta2(studenta1 &ts, int a, int b, int c, int d, int e);
    studenta2(studenta2 &ts);
    friend ostream &operator << (ostream& os, studenta2& testsubj);
};