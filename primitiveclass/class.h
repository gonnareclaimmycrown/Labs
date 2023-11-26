//
// Created by я on 12.11.2023.
//

#ifndef PRIMITIVECLASS_CLASS_H
#define PRIMITIVECLASS_CLASS_H

#endif //PRIMITIVECLASS_CLASS_H
#include "string"
using namespace std;
class fraction{
private:
    int _numerator;
    int _denominator;

void simplify(fraction);
public:
    fraction(int numerator, int denominator);
    fraction(const string &string);
    int GetDenominator(){
        return _denominator;
    };
    int GetNumerator(){
        return _numerator;
    }
    string tostring() const;

    fraction& operator + (fraction fraction);
    fraction& operator - (fraction fraction);
    fraction& operator * (fraction fraction);
    fraction& operator / (fraction fraction);
};

