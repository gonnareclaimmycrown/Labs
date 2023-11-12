//
// Created by я on 12.11.2023.
//

#ifndef PRIMITIVECLASS_CLASS_H
#define PRIMITIVECLASS_CLASS_H

#endif //PRIMITIVECLASS_CLASS_H
#include "string"
class fraction{
private:
    int _numerator;
    int _denominator;

void simplify();
    fraction(int numerator, int denominator);
    fraction(const string &string);;
    int getNumerator();
    int getDenominator();
    string tostring();

    fraction& operator + (const fraction &fraction);
    fraction& operator - (const fraction &fraction);
    fraction& operator * (fraction fraction);
    fraction& operator / (const fraction &fraction);
};

