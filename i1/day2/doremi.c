#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define SAMPLE_RATE 44100
#define PI 3.14159265358979323846

int main(int argc, char *argv[]) {
    if (argc != 3) {
        fprintf(stderr, "Usage: %s <amplitude> <number of notes>\n", argv[0]);
        return 1;
    }

    int A = atoi(argv[1]);     // 振幅
    int n = atoi(argv[2]);     // 出力する音の数

    // 音階の周波数を配列に格納（ド、レ、ミ、ファ、ソ、ラ、シ、ド）
    double frequencies[] = {261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88, 523.25};

    int total_notes = sizeof(frequencies) / sizeof(frequencies[0]); // 音階の数
    int duration = SAMPLE_RATE * 0.2; // 各音の持続時間（サンプル）

    // 各音階を出力
    for (int i = 0; i < n; i++) {
        // 現在の音階の周波数を選択
        double f = frequencies[i % total_notes];

        // 指定された持続時間の間、音を生成
        for (int j = 0; j < duration; j++) {
            double t = (double)j / SAMPLE_RATE;  // 現在の時刻
            double sample = A * sin(2 * PI * f * t);  // 正弦波の計算

            // 16ビット整数に変換
            short output = (short)sample;

            // 標準出力にバイナリで書き出し
            fwrite(&output, sizeof(short), 1, stdout);
        }
    }

    return 0;
}
