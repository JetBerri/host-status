#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include "err.h"

int main() {
    if (geteuid() != 0) {
        fatal("Este programa debe ser ejecutado como root\n");
    }

    int status = system("curl -o /etc/host-status/req https://ruta/del/archivo/req");
    if (status == -1) {
        fatal("Error: No se pudo descargar el archivo 'req'\n");
    }

    status = system("chmod +x /etc/host-status/req");
    if (status == -1) {
        fatal("Error: No se pudo establecer los permisos del archivo 'req'\n");
    }

    status = system("sudo /etc/host-status/req");
    if (status == -1) {
        fatal("Error: No se pudo ejecutar el archivo 'req'\n");
    }

    printf("La instalación ha sido completada con éxito\n");
    return 0;
}