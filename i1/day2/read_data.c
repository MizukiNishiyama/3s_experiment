#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/stat.h>

int main(int argc, char **argv) {
    if (argc < 2) {
        fprintf(stderr, "Usage: %s <filename>\n", argv[0]);
        return 1;
    }
    int fd = open(argv[1], O_RDONLY);
    if (fd == -1) {
        perror("open");
        return 1;
    }
    struct stat statbuf;
    if (fstat(fd, &statbuf) == -1) {
        perror("fstat");
        close(fd);
        return 1;
    }
    off_t filesize = statbuf.st_size;
    unsigned char *data = malloc(filesize);
    if (data == NULL) {
        fprintf(stderr, "Failed to allocate memory\n");
        close(fd);
        return 1;
    }
    ssize_t total_read = 0;
    while (total_read < filesize) {
        ssize_t n = read(fd, data + total_read, filesize - total_read);
        if (n == -1) {
            perror("read");
            free(data);
            close(fd);
            return 1;
        }
        if (n == 0) {
            break;
        }
        total_read += n;
    }
    close(fd);
    for (ssize_t i = 0; i < total_read; i++) {
        printf("%zd %d\n", i, data[i]);
    }
    free(data);
    return 0;
}
