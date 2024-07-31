#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    // loop over all pixels
    for (int i = 0, n = height; i < n; i++)
    {
        for (int j = 0, num = width; j < num; j++)
        {
            int t = image[i][j].rgbtBlue;
            int u = image[i][j].rgbtGreen;
            int v = image[i][j].rgbtRed;
            int average = round((t+u+v)/3.0);
            image[i][j].rgbtBlue = average;
            image[i][j].rgbtGreen = average;
            image[i][j].rgbtRed = average;

        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
        for (int i = 0, n = height; i < n ; i++)
    {
        for (int j = 0, num = width; j < num ; j++)
        {
            int t = image[i][j].rgbtBlue;
            int u = image[i][j].rgbtGreen;
            int v = image[i][j].rgbtRed;
            int newBlue = round(0.272 * v + 0.534 * u+0.131 * t );
            int newGreen =round (0.349 * v + 0.686 * u+0.168 * t );
            int newRed = round(0.393 * v + 0.769 * u+0.189 * t );
            if (newBlue > 255)
            {
                newBlue = 255;
            }
            if (newGreen > 255)
            {
                newGreen = 255;
            }
            if (newRed > 255)
            {
                newRed = 255;
            }
            image[i][j].rgbtBlue = newBlue;
            image[i][j].rgbtGreen = newGreen;
            image[i][j].rgbtRed = newRed;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
     for (int i = 0, n = height; i < n ; i++)
    {
        for (int j = 0, num = width; j < num/2 ; j++)
        {
            // holding value temporarily to swap later
            int t = image[i][j].rgbtBlue;
            int u = image[i][j].rgbtGreen;
            int v = image[i][j].rgbtRed;

            // reflecting the images value
            image[i][j].rgbtBlue = image[i][num-1 - j].rgbtBlue;
            image[i][j].rgbtGreen= image[i][num-1 -j].rgbtGreen;
            image[i][j].rgbtRed =  image[i][num-1 - j].rgbtRed;

            image[i][num-1 - j].rgbtBlue = t ;
            image[i][num-1 -j].rgbtGreen = u ;
            image[i][num-1 - j].rgbtRed  = v ;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE copy[height][width];
    for (int i = 0, n = height; i < n ; i++)
    {

        for (int j = 0, num = width; j < num ; j++)
        {
            copy[i][j] = image[i][j];
        }
    }
     for (int i = 0, n = height; i < n ; i++)
    {

        for (int j = 0, num = width; j < num ; j++)
        {
            int total_red = 0;
            int total_green = 0;
            int total_blue = 0;
            int count = 0;

            for (int k = i-1; k <= i+1; k++)
            {
                for (int l = j-1; l <= j+1; l++)
                {
                    if (l >= 0 && l < width && k >= 0 && k < height )
                     {

                        total_red +=   copy[k][l].rgbtRed;
                        total_green += copy[k][l].rgbtGreen;
                        total_blue  += copy[k][l].rgbtBlue;
                        count ++;
                    }
                }
            }

            if (count != 0)
            {
            image[i][j].rgbtBlue = round(((float)total_blue/count ));
            image[i][j].rgbtGreen =round(((float)total_green/count));
            image[i][j].rgbtRed =  round(((float)total_red/count  ));
            }

        }
    }
    return;
}
