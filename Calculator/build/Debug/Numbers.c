#include <stdio.h>
#include <cs50.h>

int prime_return = 0;
int square_num = -1;

void odd_even(int x); //defining the functions in advance
void prime(int x);
void square(int x);
void timestables(int x);
void numbers_to_words(int x);

int main(void)
{
    int x = get_int("What Number?\n"); //establishing the number
    odd_even(x); //calling the functions
    prime(x);
    square(x);
    timestables(x);
    numbers_to_words(x);
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
        if ((x / i) == i) //if x divided by i is i, it is a square
        {
            square_num = 1;
            break;
        }
        else 
        {
            square_num = 0;
        }
    }
    if(square_num == 1)
    {
        printf("The number is a square number\n");
    }
    else if(square_num == 0)
    {
        printf("The number is not a square number\n");
    }
    else
    {
        printf("vghjdbkaklhfuibkgcefyak\n");
    }
}

void timestables(int x)
{
    for (int z = 1; z < 13; z++) //setting the value multiplying by
    {
        printf("%d", x); printf(" * %d", z); printf(" = %d", x * z); printf("\n"); //stating the x times z equals ...
    }
}

void numbers_to_words(int x)
{
    const char* TEXTUAL[101] = 
    {
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", 
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", 
        "eighteen", "nineteen", 
        "twenty", "twenty-one", "twenty-two", "twenty-three", "twenty-four", "twenty-five", 
        "twenty-six", "twenty-seven", "twenty-eight", "twenty-nine", 
        "thirty", "thirty-one", "thirty-two", "thirty-three", "thirty-four", "thirty-five", 
        "thirty-six", "thirty-seven", "thirty-eight", "thirty-nine", 
        "forty", "forty-one", "forty-two", "forty-three", "forty-four", "forty-five", 
        "forty-six", "forty-seven", "forty-eight", "forty-nine", 
        "fifty", "fifty-one", "fifty-two", "fifty-three", "fifty-four", "fifty-five", 
        "fifty-six", "fifty-seven", "fifty-eight", "fifty-nine", "sixty", "sixty-one", "sixty-two", "sixty-three", "sixty-four", "sixty-five", 
        "sixty-six", "sixty-seven", "sixty-eight", "sixty-nine", 
        "seventy", "seventy-one", "seventy-two", "seventy-three", "seventy-four", 
        "seventy-five", "seventy-six", "seventy-seven", "seventy-eight", "seventy-nine", 
        "eighty", "eighty-one", "eighty-two", "eighty-three", "eighty-four", "eighty-five", 
        "eighty-six", "eighty-seven", "eighty-eight", "eighty-nine", 
        "ninety", "ninety-one", "ninety-two", "ninety-three", "ninety-four", "ninety-five", 
        "ninety-six", "ninety-seven", "ninety-eight", "ninety-nine", 
        "one hundred"
    };

    printf("%s", TEXTUAL[x]);

}