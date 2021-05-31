#include <stdio.h>

int my_int = 0; // %i o %d
float my_float = 0; // %f
char my_char = "c";
char my_str[10] = "hola";

// pointer //
int* my_ptr_int = &my_float; // %p


int main( int argc, char** argv){
    printf("my_int: %i, my_float: %f, my_char: %c, my_str: %s, my_ptr_int: %p.\n", my_int, my_float, my_char, my_str, my_ptr_int);
    printf("argc :%i, element 1: %d, elemn 2 : %s char: %c \n", argc, base*altura, argv[2], "L");

}