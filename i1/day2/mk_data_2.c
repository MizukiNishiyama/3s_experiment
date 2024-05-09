#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>

int main(int argc, char **argv) {
    int fd = open(argv[1], O_WRONLY | O_CREAT | O_TRUNC, 0644);
    if (fd == -1) {
        perror("open");
        return 1;
    }
    unsigned char data[256];
    for (int i = 0; i < 256; i++) {
        data[i] = i;
    }
    int a = write(fd, data, 256);
    if (a == -1) {
        perror("write");
        return 1;
    }
    close(fd);
}

