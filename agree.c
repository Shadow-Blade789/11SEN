#include <stdio.h>
#include <cs50.h>

int main(void)
{
    char c = get_char("Do you agree? y/n");

    if (c == 'y' || c == 'Y')
    {
        printf("We have agreement.\n");
    }
    else if (c == 'n' || c == 'N')
    {
        printf("We have not reached agreement.\n");
    }
}