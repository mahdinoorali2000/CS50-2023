#include "helpers.h"
#include <math.h>
// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    int R, G, B;
    int Grayscale;

    for (int h = 0; h < height; h++)
    {
        for (int w = 0; w < width; w++)
        {
            R = image[h][w].rgbtRed;
            G = image[h][w].rgbtGreen;
            B = image[h][w].rgbtBlue;

            Grayscale = round((R + G + B) / 3.0);

            image[h][w].rgbtRed = Grayscale;
            image[h][w].rgbtGreen = Grayscale;
            image[h][w].rgbtBlue = Grayscale;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int h = 0; h < height; h++)
    {
        for (int w = 0; w < width / 2; w++)
        {
            RGBTRIPLE temp = image[h][width - (w + 1)];
            image[h][width - (w + 1)] = image[h][w];
            image[h][w] = temp;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE image1[height][width];

    for (int h = 0; h < height; h++)
    {
        for (int w = 0; w < width; w++)
        {
            image1[h][w] = image[h][w];
        }
    }

    for (int h = 0; h < height; h++)
    {
        for (int w = 0; w < width; w++)
        {
            int counter = 0;
            float R = 0;
            float G = 0;
            float B = 0;

            for (int i = -1; i < 2; i++)
            {
                for (int j = -1; j < 2; j++)
                {
                    if (h + i < 0 || h + i >= height || w + j < 0 || w + j >= width)
                    {
                        continue;
                    }
                    else
                    {
                        R += image1[h + i][w + j].rgbtRed;
                        G += image1[h + i][w + j].rgbtGreen;
                        B += image1[h + i][w + j].rgbtBlue;
                        counter++;
                    }
                }
            }
            image[h][w].rgbtRed = round(R / counter);
            image[h][w].rgbtGreen = round(G / counter);
            image[h][w].rgbtBlue = round(B / counter);
        }
    }
    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE image1[height][width];

    for (int h = 0; h < height; h++)
    {
        for (int w = 0; w < width; w++)
        {
            image1[h][w] = image[h][w];
        }
    }
    int Gx[3][3] = {{-1, 0, 1},
     {-2, 0, 2},
      {-1, 0, 1}};
    int Gy[3][3] = {{-1, -2, -1}, {0, 0, 0}, {1, 2, 1}};
    for (int h = 0; h < height; h++)
    {
        for (int w = 0; w < width; w++)
        {
            float xR = 0, yR = 0;
            float xG = 0, yG = 0;
            float xB = 0, yB = 0;

            for (int i = -1; i < 2; i++)
            {
                for (int j = -1; j < 2; j++)
                {
                    if (h + i < 0 || h + i >= height || w + j < 0 || w + j >= width)
                    {
                        continue;
                    }
                    else
                    {
                        xR += image1[h + i][w + j].rgbtRed * Gx[i + 1][j + 1];
                        yR += image1[h + i][w + j].rgbtRed * Gy[i + 1][j + 1];

                        xG += image1[h + i][w + j].rgbtGreen * Gx[i + 1][j + 1];
                        yG += image1[h + i][w + j].rgbtGreen * Gy[i + 1][j + 1];

                        xB += image1[h + i][w + j].rgbtBlue * Gx[i + 1][j + 1];
                        yB += image1[h + i][w + j].rgbtBlue * Gy[i + 1][j + 1];
                    }
                }
            }
            int R = round(sqrt(xR * xR + yR * yR));
            if (R > 255)
            {
                R = 255;
            }
            image[h][w].rgbtRed = R;

            int G = round(sqrt(xG * xG + yG * yG));
            if (G > 255)
            {
                G = 255;
            }
            image[h][w].rgbtGreen = G;

            int B = round(sqrt(xB * xB + yB * yB));
            if (B > 255)
            {
                B = 255;
            }
            image[h][w].rgbtBlue = B;
        }
    }
    return;
}
