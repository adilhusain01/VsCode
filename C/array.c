#include <stdio.h>

// Passing full arrray to the function
/*
void printarray(int [],int);
int main(){
    int arr[100],size;
    printf("Enter the size of the array : ");
    scanf("%d",&size);
    printf("\n");
    for (int i=0;i<size;i++){
        printf("Enter the number => %d value : ",i+1);
        scanf("%d",&arr[i]);
    }
    printarray(arr,size);
}

void printarray(int Arr[],int Size){
    printf("\n");
    Arr[0]=100;
    for (int i=0;i<Size;i++){
        printf("number => %d value is : %d\n",i+1,Arr[i]);
    }
}
*/

// Passing Individual values of array to the function
/*
void printarray(int x, int i){
    printf("\n");
    printf("number => %d value is : %d",i+1,x);
}

int main(){
    int arr[100],size;
    printf("Enter the size of the array : ");
    scanf("%d",&size);
    printf("\n");
    for (int i=0;i<size;i++){
        printf("Enter the number => %d value : ",i+1);
        scanf("%d",&arr[i]);
    }
    for (int i=0;i<size;i++){
        printarray(arr[i],i);
    }
}
*/
