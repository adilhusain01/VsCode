#include <stdio.h>
#include <stdlib.h>


int main(){


    //MALLOC 

    int n;
    printf("Enter the amount : ");
    scanf("%d",&n);

    int *p = (int*)malloc(n*sizeof(int));
    for(int i=0; i<n;i++){
        printf("Enter the %d - number : ",i+1);
        scanf("%d",&*(p+i));
    }
    for(int i=0; i<n;i++){
        printf("%d",*(p+i));
    }

    //CALLOC

    int *q = (int*)calloc(n,sizeof(int));
    for(int i=0; i<n;i++){
        printf("Enter the %d - number : ",i+1);
        scanf("%d",&*(q+i));
    }
    for(int i=0; i<n;i++){
        printf("%d",*(q+i));
    }

    //REALLOC

    q=(int*)realloc(q,(n+2)*sizeof(int));

    for(int i=0; i<n+2;i++){
        printf("Enter the %d - number : ",i+1);
        scanf("%d",&*(q+i));
    }
    for(int i=0; i<n+2;i++){
        printf("%d",*(q+i));
    }

    printf("%d\n", *p);
    printf("%d\n", *q);
    free(p);
    free(q);
    printf("%d\n", *p);
    printf("%d\n", *q);
}