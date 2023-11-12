

#include "class.h"

int main() {
        fraction first(2, 3);
        fraction second(3, 5);
        fraction third("5/7");
        fraction result = (first * second) + third;
        result.tostring();
}