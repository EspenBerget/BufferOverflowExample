#include <stdio.h>

int add(int a, int b) {
    return a + b;
}

void puts_str(char *s) {
    puts(s);
}


int main() {
    char *s = "hello word";
    puts_str(s);

    char buf[10];

    printf(">>> ");
    gets(buf);

    return 0;
}
