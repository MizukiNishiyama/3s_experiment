#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdlib.h>

int main(int argc, char **argv) {
    int fd = open(argv[1], O_RDONLY);
    unsigned char data[200000];
    while (1) {
        int n = read(fd, data, 157680);
        if (n == -1) {
            perror("read");
            exit(1);
        }
        if (n == 0) break;
    }
    close(fd);
    for (int i = 0; i < 157680; i++) {
        printf("%d %d\n", i, data[i]);
    }
    return 0;
}
