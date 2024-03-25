

#include <iostream>

extern "C" int first(int);
extern "C" int second(int);

int main()
{
    std::cout << first(2) << '\n' << second(2);
}

