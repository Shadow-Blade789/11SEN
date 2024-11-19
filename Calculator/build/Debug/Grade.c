#include <stdio.h>


int main() {
    int mark = 65;
    //adjust to ask for number later

    switch(mark)
    {
        case 85 ... 100:
        printf("High Distinction\n");
        break;

        case 75 ... 84:
        printf("Distinction\n");
        break;

        case 65 ... 74:
        printf("Credit");
        break;

        case 50 ... 64:
        printf("Pass\n");
        break;

        default:
        printf("Fail\n");
    }
}