#include <stdio.h>
#include <stdlib.h>
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


/*
{
	char str1[15],str2[15];
	int n;
	printf("\nEnter Source String:");
	gets(str1);
	printf("\nEnter Destination String:");
	gets(str2);
	printf("Enter number of characters to copy in destination string:");
	scanf("%d",&n);
	strncpy(str2,str1,n);
	printf("Source string is:%s",str1);
	printf("\nDestination String is:%s",str2);
	return 0;
}
*/

/*
{
int a=123;
char str[100];
itoa(a,str,2);
printf("\n Binary value:%s",str);
itoa(a,str,10);
printf("\n Decimal value:%s",str);
itoa(a,str,16);
printf("\n Hexadecimal value:%s",str);
itoa(a,str,8);
printf("\n Octal value:%s",str);
return 0;
}
*/

/*
struct site {
    char name[20];
    int pages;
};

{
    struct site s;  // Declare a structure variable

    // Assign values to the structure members
    strcpy(s.name, "GeeksQuiz");
    s.pages = 200;

    struct site *ptr;  // Declare a pointer to the structure
    ptr = &s;  // Assign the address of the structure variable to the pointer

    printf("%d\n", ptr->pages);  // Access structure member using the pointer
    printf("%s\n", ptr->name);

    getchar();
    return 0;
}
*/


struct {
		short s[5];
		union{
			float y;
			long z;
		}u;
}t;

Assume that the objects of type short,float and long occupy 2,4,8 bytes respectively, so the memory requirement for variable t, ignoring alignment considerations is :
