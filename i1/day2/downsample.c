#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <downsampling factor>\n", argv[0]);
        return 1;
    }

    int downsampleFactor = atoi(argv[1]);  // ダウンサンプリングの間引き率
    if (downsampleFactor <= 0) {
        fprintf(stderr, "Downsampling factor must be a positive integer.\n");
        return 1;
    }

    short buffer;  // 16ビットのサンプルデータを格納するバッファ
    int count = 0;  // サンプルカウンタ

    // 標準入力から16ビット単位でデータを読み込む
    while (fread(&buffer, sizeof(short), 1, stdin) == 1) {
        if (count % downsampleFactor == 0) {
            // ダウンサンプリングされたデータを標準出力に書き出す
            if (fwrite(&buffer, sizeof(short), 1, stdout) != 1) {
                fprintf(stderr, "Error writing to stdout.\n");
                return 1;
            }
        }
        count++;
    }

    return 0;
}
