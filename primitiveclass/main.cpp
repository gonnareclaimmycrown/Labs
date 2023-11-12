#include <iostream>
#include "string"
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

#include "class.h"

fraction::fraction(int numerator, int denominator) {
    _numerator = numerator;
    _denominator = denominator;
    if (_denominator == 0){
        cout << ") denominator -> 1";
        _denominator = 1;
    }
}

fraction::fraction(const string &string){
        int pos = string.find("/");
        if (pos == string::npos){
            _numerator = stoi(string);
            _denominator = 1;
        } else{
            _numerator = stoi(string.substr(0, pos));
            _denominator = stoi(string.substr(pos, string.length()));
        }
    }

void fraction::simplify() {
        int gcd1 = gcd(abs(_numerator), _denominator);
        if (gcd1 != 1){
            _numerator /= gcd1;
            _denominator /= gcd1;
        }
}

string fraction::tostring() {
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

fraction& fraction::operator*(fraction fraction){
        _numerator = _numerator * fraction.getNumerator();
        _denominator = _denominator * fraction.getDenominator();
    }

    int main() {

}