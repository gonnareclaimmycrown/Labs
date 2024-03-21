// 3rd asm lab task 4.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//

#include <iostream>

int main()
{
    int num, den, gcd, count(0);
    std::cout << "enter numerator";
    std::cin >> num;
    '\n';
    std::cout << "enter denominator";
    std::cin >> den;
    '\n';
    _asm {
        mov eax, num
        cmp eax, -1
        jle minus
        jg end1

        minus:
        mov ebx, -1
        imul ebx
        mov num, eax
        inc count 
        xor eax, eax
        xor ebx, ebx 

            end1:
        xor eax, eax
        xor ebx, ebx
}
    _asm {
        mov eax, num
        mov ebx, den

        gcd_loop :
        cmp eax, ebx
        je end

        jg greater    

        sub ebx, eax
        jmp gcd_loop 

        greater :
        sub eax, ebx 
        jmp gcd_loop

       
    end:
        mov gcd, eax
    }

    _asm {
        mov eax, num 
        cdq
        div gcd
        mov num, eax
        mov eax, den
        cdq
        div gcd
        mov den, eax
    }
    std::cout << gcd << '\n';
    if (count == 1) {
        std::cout << "-";
    }
    std::cout << num << "/" << den;
}

// Запуск программы: CTRL+F5 или меню "Отладка" > "Запуск без отладки"
// Отладка программы: F5 или меню "Отладка" > "Запустить отладку"

// Советы по началу работы 
//   1. В окне обозревателя решений можно добавлять файлы и управлять ими.
//   2. В окне Team Explorer можно подключиться к системе управления версиями.
//   3. В окне "Выходные данные" можно просматривать выходные данные сборки и другие сообщения.
//   4. В окне "Список ошибок" можно просматривать ошибки.
//   5. Последовательно выберите пункты меню "Проект" > "Добавить новый элемент", чтобы создать файлы кода, или "Проект" > "Добавить существующий элемент", чтобы добавить в проект существующие файлы кода.
//   6. Чтобы снова открыть этот проект позже, выберите пункты меню "Файл" > "Открыть" > "Проект" и выберите SLN-файл.
