# Image Processing Toolkit

## Abstract

This repo is a collection of image processing scripts.

## Pixel Sorting

### Method 1: Randomized Bubble Sort

Randomly select and adjacent pair. If they are not in sorted order, swap them.

![Pixel Sorting Gif](/PixelSorting/Show/BubbleSort.gif?)

### Method 2: Group Selection by Pixel Similarity

Randomly select a 'seed' pixel on each row. Increase the sorting range to the left and right so long as the left and right pixels are within a prescribed tolerance of the seed pixel, then sort the selection.

![Pixel Sorting Gif](/PixelSorting/Show/SelectSort.gif?)

## Pixel Clustering

This method is inspired by Sherrie Levine's piece titled [Meltdown](https://www.moma.org/collection/works/65711).

Randomly select 12 'palette' pixels from an image. Select another larger set of 'training' pixels. Match each pixel in the training set with a pixel in the palette by closest Hamming distance. Nudge the palette pixel a small step towards each paired pixel.

![Pixel Clustering Image](/PixelClustering/Show/PixelClustering.png)

The maximum pair distance converges when this process is repeated over many iterations.

![Cluster Convergence](/PixelClustering/Show/ClusterConvergence.png)
