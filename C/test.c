#include <stdio.h>
int main()
{
    char *str1 = "Hello";
    char str2[] = "Hello";
    printf("sizeof(str1) = %d, sizeof(str2) = %d",sizeof(str1), sizeof(str2));
    return 0;
}