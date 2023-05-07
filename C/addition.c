//Adding two numbers using functions 07.05.2023
#include <stdio.h>
int add(int a, int b){
    return a+b;
}
int main(){
    int x,y;
    printf("Enter first number: ");
    scanf("%d",&x);
    printf("Enter second number: ");
    scanf("%d",&y);
    printf("The sum is %d",add(x,y));
    return 0;
}