#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>

int main(int argc, char **argv) {
    int fd = open(argv[1], O_WRONLY | O_CREAT | O_TRUNC, 0644);
    unsigned char data[256];
    for (int i = 0; i < 256; i++) {
        data[i] = i;
    }
    write(fd, data, 256);
    close(fd);
}

