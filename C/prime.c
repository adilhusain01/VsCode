//Finding Prime numbers in a range without using functions

#include <stdio.h>

int main(){
    int x=0;
    printf("Enter a number: ");
    scanf("%d",&x);
    for(int i=2;i<x;i++){
        int flag=0;
        for(int j=2;j<i;j++){
            if(i%j==0){
                flag=1;
                break;
            }
        }
        if(flag==0){
            printf("%d ",i);
        }
    }
    printf("\nEnd of program");
}