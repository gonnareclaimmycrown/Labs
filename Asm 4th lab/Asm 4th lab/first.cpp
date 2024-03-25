.686P
.MODEL FLAT, C

.CODE 

first        PROC x:dword
mov eax, x
mov edx, 4
imul edx
sub eax, 1
mov ecx, eax

mov eax, 0
mov eax, x
mov ebx, 4
imul ebx
add eax, 1
mov ebx, eax

imul ecx
shr eax, 2
ret
             
first        ENDP

second       PROC a:dword
mov eax, a
mov ecx, 11
cycle1 :
imul a
dec ecx
cmp ecx, 0
jne cycle1

mov ebx, eax
mov eax, a
mov ecx, 7
cycle2 :
imul a
dec ecx
cmp ecx, 0
jne cycle2

add eax, ebx
add eax, a
ret
second       ENDP

END