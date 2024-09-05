#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

/**
 * display_error_and_exit - Display "Error" and exit with status 98
 *
 * Return: void
 */
void display_error_and_exit(void)
{
	printf("Error\n");
	exit(98);
}

/**
 * is_number - Check if a character is a number
 * @c: The character to check
 *
 * Return: 1 if c is a number, 0 otherwise
 */
int is_number(char c)
{
	return (c >= '0' && c <= '9');
}

/**
 * check_arguments - Validate the arguments
 * @argc: The number of arguments
 * @argv: The arguments
 *
 * Return: void
 */
void check_arguments(int argc, char *argv[])
{
	int i, j;

	if (argc != 3)
	{
		display_error_and_exit();
	}
	for (i = 1; i < 3; i++)
	{
		for (j = 0; argv[i][j] != '\0'; j++)
		{
			if (!is_number(argv[i][j]))
			{
				display_error_and_exit();
			}
		}
	}
}

/**
 * calculate_product - Multiply two numbers
 * @num1: The first number
 * @num2: The second number
 *
 * Return: void
 */
void calculate_product(char *num1, char *num2)
{
	int len1, len2, i, j, prod, sum;
	int *result;

	len1 = strlen(num1);
	len2 = strlen(num2);
	result = (int *)calloc(len1 + len2, sizeof(int));
	if (result == NULL)
	{
		display_error_and_exit();
	}

	for (i = len1 - 1; i >= 0; i--)
	{
		for (j = len2 - 1; j >= 0; j--)
		{
			prod = (num1[i] - '0') * (num2[j] - '0');
			sum = prod + result[i + j + 1];
			result[i + j + 1] = sum % 10;
			result[i + j] += sum / 10;
		}
	}

	i = 0;
	while (i < len1 + len2 && result[i] == 0)
	{
		i++;
	}
	if (i == len1 + len2)
	{
		printf("0\n");
	}
	else
	{
		for (; i < len1 + len2; i++)
		{
			printf("%d", result[i]);
		}
		printf("\n");
	}
	free(result);
}

/**
 * main - Entry point
 * @argc: The number of arguments
 * @argv: The arguments
 *
 * Return: 0 on success, 98 on failure
 */
int main(int argc, char *argv[])
{
	check_arguments(argc, argv);
	calculate_product(argv[1], argv[2]);
	return (0);
}
