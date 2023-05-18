//Adding two numbers using functions 07.05.2023
#include <stdio.h>


int add(int a, int b){
    return a+b;
}
int main(){
    int x,y;
    printf("Enter the numbers: ");
    scanf("%d %d",&x,&y);
    printf("The sum is %d",add(x,y));
    return 0;
}