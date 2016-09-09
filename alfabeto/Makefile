run:a.out
	./a.out
a.out:main.o alfabeto.o
	gcc main.o alfabeto.o
main.o:main.c
	gcc -c -Wall main.c
alfabeto.o:main.c
	gcc -c -Wall alfabeto.c
