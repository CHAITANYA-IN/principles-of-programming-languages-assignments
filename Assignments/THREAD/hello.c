#include <stdio.h>
#include <pthread.h>
#include <stdlib.h>
#include <unistd.h>

void* PrintHello(void *id) {
    sleep(1);
    printf("Hello\n");
    pthread_exit(NULL);
}

int main(int argc, char* argv[]) {
    int rc;
    pthread_t thread_id;
    while(1) {
        rc = pthread_create(&thread_id, NULL, (void *)PrintHello, (void *)thread_id);
        if(rc) {
            printf("\nERROR: return code from pthread_create is %d \n", rc);
            exit(1);
        }
        printf("\nCreated new thread (%u) ... \n", (unsigned int)thread_id);
        pthread_join(thread_id, NULL);
    }
    pthread_exit(NULL);
}
