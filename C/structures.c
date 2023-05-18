#include <stdio.h>
#include <string.h>

/*
struct car{
    char company[50];
    char model[50];
    int yearMf;
    int seats;
    char fuel[10];
};

struct car car1={"AUDI","R8 e-tron",2018,2,"Petrol"};

int main()
{
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
*/


/*
int main()
)
{
    struct car{
    int okay;
    }*p;

    (*p).okay=10;
    p->okay=20;
    printf("%d",p->okay);
}*/


/*
int main()
{
    struct books{
        int pages;
        char str[4];
    }*ptr;
    printf("%d",sizeof(ptr));  //Depends on compiler => 4bits on  VS Code, 8bits on online compiler
    return 0;
}
*/


//                                                          Nested Structures

// #1
/*
int main(){
    struct d{
        int date;
        int month;
        int year;
    };

    struct info{
        char name[20];
        char gender;
        struct d dob;
    }i1;

    i1.dob.date=20;
    i1.dob.month=10;
    i1.dob.year=2005;

    strcpy(i1.name,"adil");
    i1.gender='m';

    printf("%s %c", i1.name, i1.gender);
    printf(" %d %d %d",i1.dob.date,i1.dob.month,i1.dob.year);
}
*/


// #2
/*
int main(){
    struct info{
    char name[20];
    char gender;
    struct d{
        int date;
        int month;
        int year;
    }dob;
    }i1;

    i1.dob.date=20;
    i1.dob.month=10;
    i1.dob.year=2005;

    strcpy(i1.name,"adil");
    i1.gender='m';

    printf("%s %c", i1.name, i1.gender);
    printf(" %d %d %d",i1.dob.date,i1.dob.month,i1.dob.year);
}
*/