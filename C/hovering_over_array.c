

#include <stdio.h>

// In this program using fucntions property I'm inserting any constant value
//inside a particular position in the array
/*
int main(){
    printf("\n\n\t\t\tThis Program consists inserting a number\n\t\t\tat any position in the array.\n\n");

    int arr[100],n,number,position;

    printf("\nEnter the amount of numbers to insert : ");
    scanf("%d",&n);

    for (int i=0;i<n;i++){
        printf("Entter the %d - number : ",i+1);
        scanf("%d",&arr[i]);
    }

    printf("\nEnter the number to insert : ");
    scanf("%d",&number);

    printf("\nEnter the position at which to insert : ");
    scanf("%d",&position);
    
    for (int i=n-1;i>=position-1;i--){
        arr[i+1]=arr[i];
    }
    arr[position-1]=number;

    for (int i=0;i<n+1;i++){
        printf("%d\n",arr[i]);
    }
}
*/


// In this program using fucntions property I'm deleting any constant value
//inside a particular position in the array
/*
int main(){
    int arr[100],n,position;

    printf("\n\n\t\t\tThis Program consists inserting a number\n\t\t\tat any position in the array.\n\n");

    printf("Enter the amount of numbers : ");
    scanf("%d",&n);

    printf("\n");
    for(int i=0;i<n;i++){
        printf("Enter the %d - number : ",i+1);
        scanf("%d",&arr[i]);
    }

    printf("\nEnter the postion of number in the array to remove : ");
    scanf("%d",&position);

    for(int i=position;i<n;i++){
        arr[i-1]=arr[i];
    }
    printf("\n");
    for(int i=0;i<n-1;i++){
        printf("%d\n",arr[i]);
    }
}
*/