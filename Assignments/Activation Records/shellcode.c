#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void virus(){
    char *shell[2];
    shell[0] = "/bin/sh";
    shell[1] = NULL;
    execve(shell[0], shell, NULL);
}

int main(){
    int a[2] = {7, 1};
    a[2] = 1;
    a[3] = 0x00010464;
    return 0;
}
