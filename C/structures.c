#include <stdio.h>

struct car{
    char company[50];
    char model[50];
    int yearMf;
    int seats;
    char fuel[10];
};

struct car car1={"AUDI","R8 e-tron",2018,2,"Petrol"};

int main(){
    printf("\n\n\t\t\tPriting details normally\n\n");

    printf("Company : %s\n",car1.company);
    printf("Model : %s\n",car1.model);
    printf("yearMf : %d\n",car1.yearMf);
    printf("Seats : %d\n",car1.seats);
    printf("Fuel : %s\n",car1.fuel);


    printf("\n\n\t\t\tPriting details using pointer\n\n");
    struct car *pCar1=&car1;

    printf("\nCompany : %s\n",pCar1->company);
    printf("Model : %s\n",(*pCar1).model);
    printf("yearMf : %d\n",pCar1->yearMf);
    printf("Seats : %d\n",pCar1->seats);
    printf("Fuel : %s\n",pCar1->fuel);
}