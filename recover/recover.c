#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
int main(int argc, char *argv[])
{
    // Accept a single command line arguments: the name of memory card
    if (argc != 2)
    {
        printf("Usage: ./recover FILE\n");
        return 1;
    }
    // Open a memory card
    FILE *card = fopen(argv[1], "r");
    if (!card)
    {
        return 1;
    }

    uint8_t buffer[512];
    int i = 0;
    FILE *file = NULL;
    // While there's still data left to read from the memory card
    while (fread(buffer, 1, 512, card) == 512)
    {

        // Create JPEGs from the data
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff &&
            ((buffer[3] & 0xf0) == 0xe0))
        {
            char filename[8];
            if (file != NULL)
            {
                fclose(file);
            }
            sprintf(filename, "%03i.jpg", i);
            file = fopen(filename, "w");
            if (!file)
            {
                fclose(card);
                return 1;
            }
            // fclose(file);
            i++;
        }
        if (file != NULL)
        {
            fwrite(buffer, 1, 512, file);
        }
    }
    if (file)
    {
        fclose(file);
    }
    fclose(card);
}
