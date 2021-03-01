#include <stdio.h>
#include <stdlib.h>

int main(){
    setvbuf(stdout, NULL, _IONBF, 0);
    printf("ctfCTF{Test_test!}");
	system("/bin/bash");
}
