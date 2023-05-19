#include <stdio.h>
int main()


// 1.Size of pointer and string array (\0) 
/*
{
    char *str1 = "Hello";
    char str2[] = "Hello";
    printf("sizeof(str1) = %d, sizeof(str2) = %d",sizeof(str1), sizeof(str2));
    return 0;
}
*/

// 2. Garbage value gets in pointer if its made free
/*
{
    int *j = (int*)malloc(4 * sizeof(int));
    *j = 15;
    free(j);
    printf("%d\n", &j);
    printf("%d\n", j);
    printf("%d", *j);
    return 0;
}
*/
