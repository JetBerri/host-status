#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[])
{
    int status = system("/usr/bin/python /etc/host-status/main.py");
    if (status == -1) {
        printf("Error: No se pudo ejecutar el programa main.py\n");
    }
    return 0;
}
