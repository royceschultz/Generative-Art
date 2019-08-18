# Image Processing Toolkit

## Abstract

This repo is a collection of image processing scripts.

## Pixel Sorting

### Method 1: Randomized Bubble Sort

Randomly select and adjacent pair. If they are not in sorted order, swap them.

![Pixel Sorting Gif](/Present/BubbleSort.gif)

### Method 2: Group Selection by Pixel Similarity

Randomly select a 'seed' pixel on each row. Increase the sorting range to the left and right so long as the left and right pixels are within a prescribed tolerance of the seed pixel.

![Pixel Sorting Gif](/Present/SelectSort.gif)
