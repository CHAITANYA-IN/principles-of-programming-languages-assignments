#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>

void check(int rc, pthread_t thread_id) {
    if(rc) {
        printf("\n ERROR: return code from pthread_create is %d \n", rc);
        exit(1);
    }
    printf("\nCreated new thread (%u) ... \n", (unsigned int)thread_id);
}

void *putstring(char *string) {
    puts(string);
    return NULL;
}

int main() {
    int rc;
    pthread_t thread_id;
    char hello[] = "Hello World\n";
    char bye[] = "Goodbye World\n";
    rc = pthread_create(&thread_id, NULL, (void *)putstring, hello);
    check(rc, thread_id);
    pthread_join(thread_id, NULL);
    rc = pthread_create(&thread_id, NULL, (void *)putstring, bye);
    check(rc, thread_id);
    pthread_join(thread_id, NULL);
    pthread_exit(NULL);
}
