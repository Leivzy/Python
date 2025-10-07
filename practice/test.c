#include <stdio.h>
int main() 
{
    char a = 'a';
    char b;
    b = a;
    a = 'x';

    printf("%c,%c",a,b);

}