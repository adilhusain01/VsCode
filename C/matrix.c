#include <stdio.h>

int main(){
    int matrix[3][3],row,col,i,j;

    printf("\n\n\t\tIts a program to output the\n\t\tmatrix using 3D array\n\n\n");

    for (row=0;row<3;row++){
        for(col=0;col<3;col++){
            printf("\nEnter value of matrix for [%d][%d] : ",row,col);
            scanf("%d",&matrix[row][col]);
        }
    }
    printf("\n\n\t\tThe given matrix is : \n\n");
    for (i=0;i<3;i++){
        printf("\t\t\t");
        for(j=0;j<3;j++){
            printf("%d ",matrix[i][j]);
        }
        printf("\n");
    }
    printf("\n\n");
   
}