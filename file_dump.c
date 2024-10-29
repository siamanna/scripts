#include <stdio.h>
#include <stdlib.h>

#define BYTES_PER_LINE 16

void print_hexdump(FILE *file) {
    unsigned char buffer[BYTES_PER_LINE];
    size_t bytesRead;
    unsigned int offset = 0;

    printf("Hexadecimal and Octal Dump:\n\n");

    // Read the file in chunks
    while ((bytesRead = fread(buffer, 1, BYTES_PER_LINE, file)) > 0) {
        // Print the offset
        printf("%08x  ", offset);

        // Print each byte in hexadecimal format
        for (size_t i = 0; i < bytesRead; i++) {
            printf("%02x ", buffer[i]);
        }

        // Fill remaining space if line is incomplete
        for (size_t i = bytesRead; i < BYTES_PER_LINE; i++) {
            printf("   ");
        }

        // Print each byte in octal format
        printf(" | ");
        for (size_t i = 0; i < bytesRead; i++) {
            printf("%03o ", buffer[i]);
        }

        // Print ASCII representation for readability
        printf(" | ");
        for (size_t i = 0; i < bytesRead; i++) {
            if (buffer[i] >= 32 && buffer[i] <= 126) {
                printf("%c", buffer[i]);
            } else {
                printf(".");
            }
        }

        printf("\n");

        offset += bytesRead;
    }
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <file>\n", argv[0]);
        return EXIT_FAILURE;
    }

    FILE *file = fopen(argv[1], "rb");
    if (!file) {
        perror("Failed to open file");
        return EXIT_FAILURE;
    }

    print_hexdump(file);

    fclose(file);
    return EXIT_SUCCESS;
}
