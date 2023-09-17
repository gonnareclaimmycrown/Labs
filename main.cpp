#include <iostream>
#include "cmath"
#include <iomanip>
using namespace std;
int main() {
    double x, slug (1.0), summ (1.0), realfun;
    int k, xd(1), limit (1);
    cout << "Please enter the variable of x";
    cin >> x;
    cout << "Please enter the variable of k";
    cin >> k;
    realfun = (exp(-x));
    cout << fixed;
    cout << setprecision (k);
    cout << realfun << endl;
    while (abs(slug) >= pow(10, -k)){
        slug = -1 * slug*x/xd;
        limit++;
        if (limit > 1){
            xd++;
        }
        summ = summ + slug;
    }
    cout << fixed;
    cout << setprecision (k);
    cout << summ;
    return 0;
}
