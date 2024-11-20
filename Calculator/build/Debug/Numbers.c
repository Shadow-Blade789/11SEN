#include <stdio.h>
#include <cs50.h>

int prime_return = 0;

void odd_even(int x); //defining the functions in advance
void prime(int x);
void square(int x);

int main(void)
{
    int x = get_int("What Number?\n"); //establishing the number
    odd_even(x); //calling the functions
    prime(x);
    square(x);
}

void odd_even(int x)
{
    if (x % 2 == 0) //if x modulus 2 is 0
    {
        printf("Number is even\n");
    }
    else
    {
        printf("Number is odd\n");
    }
}

void prime(int x)
{
      if (x == 0 || x == 1) //if x is 0 or 1
    prime_return = 1;

  for (int i = 2; i <= x / 2; ++i) //setting the value for modulusing
  {  
    if (x % i == 0) { //if x modulus the value is 0 it is divisible
      prime_return = 1;
      break;
    }
  }

  if (prime_return == 0)
    printf("Number is a prime number.\n");
  else
    printf("Number is not a prime number.\n");
}

void square(int x)
{
    for (int i = 1; i <= x; i++) //setting the value to divide
    {
        if (x / i == i) //if x divided by i is i, it is a square
        {
            printf("The number is a square number\n");
        }
        else 
        {
            printf("The number is not a square number\n");
        }
    }
}

void timestables(int x)
{
    for (int z = 1; z < 13; z++) //setting the value multiplying by
    {
        printf("%d", x); printf(" * %d", z); printf(" = %d", x * z); //stating the x times z equals ...
    }
}