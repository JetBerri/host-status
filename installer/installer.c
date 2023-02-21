#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include "err.h"

int main() {
    if (geteuid() != 0) {
        fatal("This program must be executed as root!\n");
    }

    int status = system("curl -o /opt/host-status/req https://github.com/JetBerri/host-status.git");
    if (status == -1) {
        fatal("Error: Couldn't load the installation file 'req'\n");
    }

    status = system("chmod +x /etc/host-status/req");
    if (status == -1) {
        fatal("Error: Couldn't set file permissions 'req'\n");
    }

    status = system("sudo /etc/host-status/req");
    if (status == -1) {
        fatal("Error: Couldn't execute file 'req'\n");
    }

    printf("The installation has been completed successfully\n");
    return 0;
}