#include <stdio.h>

int main() {
	char name[100];

	while(1) {
		scanf("%s", name);
		printf("%s", name);

		if (name == '') {
			break;
		}
	}

	return 0;
}