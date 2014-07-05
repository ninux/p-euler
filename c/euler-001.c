#include <stdio.h>

int main(int argc, char* argv[])
{
	int range = 1000;
	int result = 0;
	int i = 0;

	for(i = 0; i < range; i++) {
		if (i%3 == 0) {
			result += i;
		}
		else {
			if (i%5 == 0) {
				result += i;
			}
		}
	}

	printf("%i\n", result);

	return 0;
}
