//Finding Prime numbers in a range without using functions 07.05.2023
#include <stdio.h>
int main(){
    int x=0,flag=0;
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
            printf("It is a prime number");
        } else if (flag==1){
            printf("It is not a prime number");
        }
    }
    return 0;
}