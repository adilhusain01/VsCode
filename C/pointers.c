#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

// SUM  OF TWO NUMBERS USING POINTERS

int summation(int *x,int *y, int *sum){
    *sum = ((*x) + (*y));
    return *sum;
}

int main(){
    int a=0,b=0,sum=0;
    int *A=&a,*B=&b,*SUM=&sum;

     printf("\n\n\t\tIts a program to do \n\t\tsum of two numbers\n\n\n");

    printf("Enter first number : ");
    scanf("%d",A);
    printf("Enter second number : ");
    scanf("%d",B);
    printf("\n\t\tThe sum of both numbers is : %d\n\n",summation(A,B,SUM));
}



//                             #POINTERS

// 1.NULL POINTER
/*
int main(){
    int *p=NULL; //p IS MADE NULL AT DECLARARTION HENCE NULL POINTER
    printf("initially(null) : %d",p); // CANT DEREFERENCE IT OTHERWISE IT'LL GIVE ERROR
    int x=20;
    p=&x;   //NOW p IS NOT NULL POINTER
    printf("\nafter : %d",*p); 
}
*/

// 2. WILD POINTER
/*
int main(){
    int *p; //ONLY DECLARATION NOT INITIALIZATION HENCE p IS A WILD POINTER CONTAINING SOME GARBAGE ADDRESS AS ITS VALUE
    printf("%d",p); //CANT DEREFERENCE IT BUT CAN GET WHAT IT CONTAINS

    int x=10;
    p=&x; //NOW p IS A NORMAL POINTER AND CAN BE DEREFERENCED 
    printf("%d",*p);
}
*/

// 3. VOID POINTER
/*
int main(){
    void *p; // p IS DECLARED AS VOID AS WE ARE NOT CONFIRMING ITS DATATYPE
    int x = 67;
    p=&x; // VALUE OF X AS INT GOES TO p
    printf("%d",*(int*)p); //USING ITS UNIQUE DEREFERENCING METHOD WE PRINT WHAT IT REFERS TO AS INTEGER
    char y='a';
    p=&y; // NOW P REFERNCES TO A y CONTAINING A CHARACTER
    printf("\n%c",*(char*)p);
}
*/

// 4. CONST POINTER
/*
int main(){
    int x=10,y=20;
    int *const p=&x;
    printf("%d",*p);
    p=&y; // AS p IS A CONSTANT DECLARED POINTER, IT IS PREVENTING p FROM GETTING ASSIGNED TO ANOTHER VARIABLE
    printf("%d",*p);
}
*/

// 5.DANGLING POINTER
/*
int *okay(){
    int x=20;
    int *p1=&x;
    return *p1;  //LOCAL VARIABLE X's SCOPE ENDS HERE AND ITS MEMORY ADDRESS GET DEALLOCATED 
}
int main()
{  
    int *p=okay();
    printf("%d",*p); //NOW THE POINTER POINTS AT DEALLOCATED ADDRESS THUS RETURNS ERROR
    return 0;
}
*/

//IN THIS *P IS A DANGLING POINTER