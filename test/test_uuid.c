#include <stdlib.h>
#include <stdio.h>
#include <uuid/uuid.h>

int main(int argc, char* argv[]) {

	uuid_t uu;
	char s[42];

	uuid_generate(uu);
	uuid_unparse(uu, s);
	uuid_clear(uu);
	
	printf("uuid=%s\n", s);
	
	return EXIT_SUCCESS;
}
