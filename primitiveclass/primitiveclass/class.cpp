//
// Created by я on 12.11.2023.
//
#include <iostream>
#include "string"
#include "class.h"
using namespace std;

int gcd(int a, int b){
    while (b > 0){
        int c = a % b;
        a = b;
        b = c;
    }
    return a;
}

int lcm(int a, int b){
    return (a*b)/ gcd(a, b);
}


fraction::fraction(int numerator, int denominator) {
    _numerator = numerator;
    _denominator = denominator;
    if (_denominator == 0){
        cout << ") denominator -> 1";
        _denominator = 1;
    }
}

/* fraction::fraction(const string &string){
    int pos1 = string.find("/");
    if (string == ""){
        cout << "empty input";
        _numerator = 1;
        _denominator = 1;
    }
    if (pos1 == string::npos){
        _numerator = stoi(string);
        _denominator = 1;
    } else{
        _numerator = stoi(string.substr(0, pos1));
        _denominator = stoi(string.substr(pos1, string.length()));
    }
    if (_denominator == 0){
        cout << ") denominator -> 1";
        _denominator = 1;
    }
}
*/

void fraction::simplify(fraction) {
    int gcd1 = gcd(abs(_numerator), _denominator);
    if (gcd1 != 1){
        _numerator /= gcd1;
        _denominator /= gcd1;
    }
}

string fraction::tostring() const {
    string fraction = "";
    if (_numerator == 0){
        fraction.append("0");
        return fraction;
    }
    fraction.append(reinterpret_cast<const char *>(_numerator));
    if (_denominator != 1){
        fraction.append("/");
        fraction.append(reinterpret_cast<const char *>(_denominator));
    }
    return fraction;
}

fraction& fraction::operator*(fraction second) {
    int result_num;
    int result_den;
    result_num = _numerator * second._numerator;
    result_den = _denominator * second._denominator;
    fraction result(result_num, result_den);
    simplify(result);
    return result;
}

fraction& fraction::operator/(fraction second){
    int result_num;
    int result_den;
    result_num = _numerator * second._denominator;
    result_den = _denominator * second._numerator;
    fraction result(result_num, result_den);
    simplify(result);
    return result;
}

fraction& fraction::operator+(fraction second) {
    int result_num;
    int result_den;
    result_num = _numerator * second._denominator + second._numerator * _denominator;
    result_den = _denominator * second._denominator;
    fraction result(result_num, result_den);
    simplify(result);
    return result;
}

fraction& fraction::operator-(fraction second) {
    int result_num;
    int result_den;
    result_num = _numerator * second._denominator - second._numerator * _denominator;
    result_den = _denominator * second._denominator;
    fraction result(result_num, result_den);
    simplify(result);
    return result;
}