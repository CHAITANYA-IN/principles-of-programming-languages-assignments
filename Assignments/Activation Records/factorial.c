#include <stdlib.h>

int factorial(int number) {
	if(number == 1) {
		return 1;
	}
	return number * factorial(number - 1);
}

int main(int argc, char **argv) {
	return factorial(atoi(argv[1]));
}
