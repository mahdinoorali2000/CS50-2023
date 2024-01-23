#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE\n");
        return 1;
    }

    FILE *input_file = fopen(argv[1], "r");

    if (input_file == NULL)
    {
        printf("Could not open %s.\n", argv[1]);
        return 1;
    }

    unsigned char *buffer = malloc(512 * sizeof(unsigned char));

    if (buffer == NULL)
    {
        printf("Failed to allocate memory.\n");
        return 1;
    }

    char *image_name = malloc(8 * sizeof(char));

    if (image_name == NULL)
    {
        printf("Failed to allocate memory.\n");
        return 1;
    }

    int im = 0;
    FILE *output_file = NULL;
    // burn images
    while (fread(buffer, 1, 512, input_file))
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            if (output_file != NULL)
            {
                fclose(output_file);
            }
            sprintf(image_name, "%03d.jpg", im);
            output_file = fopen(image_name, "a");

            if (output_file == NULL)
            {
                printf("Could not open %s.\n", image_name);
                return 1;
            }

            fwrite(buffer, 1, 512, output_file);
            im++;
        }
        else if (im > 0)
        {
            fwrite(buffer, 1, 512, output_file);
        }
    }
    if (output_file != NULL)
    {
        fclose(output_file);
    }
    fclose(input_file);
    free(buffer);
    free(image_name);
    return 0;
}