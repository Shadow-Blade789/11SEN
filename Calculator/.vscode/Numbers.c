#include <stdio.h>
#include <cs50.h>

int prime_return = 0;

void odd_even(int x);
void prime(int x);
void square(int x);

int main(void)
{
    int x = get_int("What Number, between 1 and 100\n");
    odd_even(x);
}

void odd_even(int x)
{
    if (x % 2 == 0)
    {
        printf("Number is even\n");
    }
    else
    {
        printf("Number is not even\n");
    }
}

void prime(int x)
{
      if (x == 0 || x == 1)
    prime_return = 1;

  for (int i = 2; i <= x / 2; ++i) 
  {  
    if (x % i == 0) {
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
    for (int i = 1; i <= x; i++)
    {
        if (x / i == i)
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
    for (int z = 1; z < 13; z++)
    {
        printf("%d", x); printf(" * %d", z); printf(" = %d", x * z);
    }
}