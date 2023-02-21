#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[]) {
    if (argc == 2 && strcmp(argv[1], "-v") == 0) {
        printf("Version 1.0\n");
    } else if (argc == 2 && strcmp(argv[1], "-h") == 0) {
        printf("This program will allow you to check if there is any vulnerability into the port's service that is currently running, you can change the IPs in the file /opt/host-status/scripts/config/ips.yaml\n");
    } else {
        system("python3 /opt/host-status/main.py");
    }
    return 0;
}