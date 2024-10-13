#include <stdio.h>

__asm__("pop %rax\n\t"
        "pop %rdx\n\t"
        "ret\n\t"
        "movq %rdx, (%rax)\n\t"
        "ret\n\t");


int main() {

    char buf[10];

    printf(">>> ");
    gets(buf);

    return 0;
}
