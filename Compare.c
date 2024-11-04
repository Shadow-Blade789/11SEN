#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int x = get_int("What's the first number? ");
    int y = get_int("What is the second number? ");

    if (x < y)
    {
        printf("The number is smaller than the second one.");
    }
    else if (x > y)
    {
        printf("The number is larger than the second.");
    }
    else;
    {
        printf("The numbers are the same");
    }
}
