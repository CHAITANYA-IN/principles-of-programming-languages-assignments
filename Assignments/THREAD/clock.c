#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>
#include <time.h>

int days = 0;
int hours = 0;
int minutes = 0;
int seconds = 0;

void check(int rc, pthread_t thread_id) {
    if(rc) {
        printf("\n ERROR: return code from pthread_create is %d \n", rc);
        exit(1);
    }
}

void *f_seconds() {
    seconds++;
    pthread_exit(NULL);
}

void *f_minutes() {
    seconds = 0;
    minutes++;
    pthread_exit(NULL);
}

void *f_hours() {
    minutes = 0;
    hours++;
    pthread_exit(NULL);
}

void *f_days() {
    hours = 0;
    days++;
    pthread_exit(NULL);
}

void *print() {
    system("clear");
    puts("Time:");
    printf("%02d:%02d:%02d:%02d\n", days, hours, minutes, seconds);
    sleep(1);
    pthread_exit(NULL);
}

int main(int argc, char *argv[]) {
    time_t s;
    struct tm *t;
    pthread_t t_id;
    int err = 0;
    
    s = time(NULL);
    t = localtime(&s);
    
    days = 0;
    hours = (int)t->tm_hour;
    minutes = (int)t->tm_min;
    seconds = (int)t->tm_sec;
    
    while(1) {
        err = pthread_create(&t_id, NULL, (void *)f_seconds, NULL);
        check(err, t_id);
        pthread_join(t_id, NULL);
        if(seconds == 60) {
            err = pthread_create(&t_id, NULL, (void *)f_minutes, NULL);
            check(err, t_id);
            pthread_join(t_id, NULL);
        }
        if(minutes == 60) {
            err = pthread_create(&t_id, NULL, (void *)f_hours, NULL);
            check(err, t_id);
            pthread_join(t_id, NULL);
        }
        if(hours == 24) {
            err = pthread_create(&t_id, NULL, (void *)f_days, NULL);
            check(err, t_id);
            pthread_join(t_id, NULL);
        }
        err = pthread_create(&t_id, NULL, (void *)print, NULL);
        check(err, t_id);
        pthread_join(t_id, NULL);
    }
    return 0;
}
/*
while(1) {
       system("clear");
       puts("Time:");
       printf("%02d:%02d:%02d:%02d\n", days, hours, minutes, seconds);
       seconds++;
       if(seconds == 60) {
           seconds = 0;
           minutes++;
       }
       if(minutes == 60) {
           minutes = 0;
           hours++;
       }
       if(hours == 24) {
           days++;
       }
       sleep(1);
   }
*/
