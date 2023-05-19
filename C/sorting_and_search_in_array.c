#include <stdio.h>


// BUBBBLE SORTING SYSTEM
/*
int main(){

    printf("\n\n\t\t\tThis Program consists sorting the array\n\t\t\tby pushing heavy elements towards the end.\n\n");

    int arr[100],n;

    printf("Enter the amount of values : ");
    scanf("%d",&n);

    printf("\n");
    for(int i=0;i<n;i++){
        printf("Enter the %d - number : ",i+1);
        scanf("%d",&arr[i]);
    }

    for(int i=0;i<n;i++){
        for(int j=0;j<n-1;j++){
                if(arr[j]>arr[j+1]){
                    int temp=arr[j+1];
                    arr[j+1]=arr[j];
                    arr[j]=temp;
                }
        }
    }
    for(int i=0;i<n;i++){
        printf("\n%d",arr[i]);
    }
}
*/


// Linear Search of an element through array & providing it's index
/*
int main(){
    int arr[100],n,number;

    printf("\n\n\t\t\tThis Program consists searching for position of an element \n\t\t\tusing linear search concept in the array.\n\n");

    printf("Enter the amount of numbers : ");
    scanf("%d",&n);

    printf("\n");
    for(int i=0;i<n;i++){
        printf("Enter the %d - number : ",i+1);
        scanf("%d",&arr[i]);
    }

    printf("\nEnter the number whose index position you want : ");
    scanf("%d",&number);

    for(int i=0;i<n;i++){
        if  (arr[i]==number){
            printf("%d\n",i);
        }
    }
}
*/

// Binary Search of an element through array & providing it's index
/*
int main(){
    int arr[100],n,number;

    printf("\n\n\t\t\tThis Program consists searching for position of an element \n\t\t\tusing linear search concept in the array.\n\n");

    printf("Enter the amount of numbers : ");
    scanf("%d",&n);

    printf("\n");
    for(int i=0;i<n;i++){
        printf("Enter the %d - number : ",i+1);
        scanf("%d",&arr[i]);
    }

    printf("\nEnter the number whose index position you want : ");
    scanf("%d",&number);

// First sorting array using bubble sorting system


    for(int i=0;i<n;i++){
        printf("\n%d",arr[i]);
    }

    for(int i=0;i<n;i++){
        for(int j=0;j<n-1;j++){
                if(arr[j]>arr[j+1]){
                    int temp=arr[j+1];
                    arr[j+1]=arr[j];
                    arr[j]=temp;
                }
        }
    }

    for(int i=0;i<n;i++){
        printf("\n%d",arr[i]);
    }



// Now implementing the binary search
    int low=0;
    int high=n-1;

    while (low<=high){
        int mid=(high+low)/2;
        if (number==arr[mid]){
            printf("\nPoosition is : %d",mid+1);
            break;
        } else if (number>arr[mid]){
            low=mid+1;
        } else if(number<arr[mid]) {
            high=mid-1;
        }
    }
}
*/