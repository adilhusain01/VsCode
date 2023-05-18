#include <stdio.h>

int cube(int *num1){
	return (*num1 * *num1 * *num1);
}
int main()
{	
int num,output;
printf("Enter the number: ");
scanf("%d",&num);
output=cube(&num);
printf("%d",output);
}
