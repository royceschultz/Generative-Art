# Image Processing Toolkit

## Abstract

This repo is a collection of image processing scripts.

## Pixel Sorting

### Method 1: Randomized Bubble Sort

Randomly select and adjacent pair. If they are not in sorted order, swap them.

![Pixel Sorting Gif](/Present/BubbleSort.gif?)

### Method 2: Group Selection by Pixel Similarity

Randomly select a 'seed' pixel on each row. Increase the sorting range to the left and right so long as the left and right pixels are within a prescribed tolerance of the seed pixel, then sort the selection.

![Pixel Sorting Gif](/Present/SelectSort.gif?)

## Pixel Clustering

This method is inspired by Sherrie Levine's piece titled [Meltdown](https://www.moma.org/collection/works/65711).

Randomly select 12 'palette' pixels from an image. Select another larger set of 'training' pixels. Match each pixel in the training set with a pixel in the palette by Hamming distance. Nudge the palette pixel a small step towards each paired pixel.

![Pixel Clustering Image](/Present/PixelClustering.png)

The maximum pair distance does converge when this process is repeated over many iterations.

![Cluster Convergence](/Present/ClusterConvergence.png)
