
CFLAGS=-fno-stack-protector -fcf-protection=none -no-pie

$1:
	gcc -o $1 $1.c $(CFLAGS)
