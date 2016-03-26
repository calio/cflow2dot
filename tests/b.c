#include <stdio.h>

void bar()
{
    printf("bar");
}

void foo()
{
    printf("foo");
    bar();
}

int main(int argc, char **argv)
{
    printf("main");
    foo();
    return 0;
} /* }}} */


/* Modeline for ViM {{{
 * vim:set ts=4:
 * vim600:fdm=marker fdl=0 fdc=3:
 * }}} */


