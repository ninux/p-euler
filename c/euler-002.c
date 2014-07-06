#include <stdio.h>

int main(int args, char* argv[])
{
	int limit = 4000000;
	
	int a = 1;
	int b = 1;
	int swp = 0;

	int i = 0;
	
	int sum = 0;

	while(swp < limit){
		swp = a+b;
		a = b;
		b = swp;
		if(swp%2 == 0){
			sum += swp;
		}
	}

	printf("Result: %i\n", sum);

	return 0;
}
