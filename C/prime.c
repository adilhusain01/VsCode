//Finding Prime numbers in a range without using functions 07.05.2023
#include <stdio.h>
int main(){
    int x=0,flag=0;
    printf("\n\n\t\tIts a program to check,\n\t\twhether the number is prime or not\n\n\n");
    printf("Enter a number: ");
    scanf("%d",&x);
    if(x<=1){
        printf("Its is not a prime number");
    }else{  
        for(int i=2;i<x;i++){
            for(int j=2;j<i;j++){
                if(i%j==0){
                    flag=1;
                    break;
                }
            }
        }
        if(flag==0){
            printf("\n\t\tIt is a prime number\n\n");
        } else if (flag==1){
            printf("\n\t\tIt is not a prime number\n\n");
        }
    }
    return 0;
}