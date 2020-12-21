# 90b_entropy
Compute the min entropy input requirements for SP800-90B Vetted Conditioning Components

SP800-90B specifices some entropy extraction algorithms.
The algorithms input a number of bits and outputs a fixed size number of bits (like 128 or 256).

The specification also provides equations to compute the min-entropy of the data out of the conditioner, given the min entropy of the input data and some parameters of the algorithm used.

The equations only asymptotically approach 100% at the output, so you cannot find a amount and quality of input data to get full entropy output. You have to decide how close you want to get to full entropy.

This code uses the mpf library to enable it to compute the entropy quality needed to get the output min entropy to within 10^-2048 of 100%. It does this over a number of input sizes and finds the lowest input min-entropy rate for each input size that will yield output entropy close enough to 100%.

The output is a set of tables, one for each algorithm.

