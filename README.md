# 90b_entropy
Compute the min entropy input requirements for SP800-90B Vetted Conditioning Components

SP800-90B specifies some entropy extraction algorithms.
The algorithms input a number of bits and outputs a fixed size number of bits (like 128 or 256).

The specification also provides equations to compute the min-entropy of the data out of the conditioner, given the min entropy of the input data and some parameters of the algorithm used.

The equations only asymptotically approach 100% at the output, so you cannot find a amount and quality of input data to get full entropy output. You have to decide how close you want to get to full entropy.

This code uses the mpf library to enable it to compute the entropy quality needed to get the output min entropy to within 10^-2048 of 100%. It does this over a number of input sizes and finds the lowest input min-entropy rate for each input size that will yield output entropy close enough to 100%.

The output is a set of tables, one for each algorithm.

```
$ python3 90b_entropy.py
AES-CBC-MAC Extraction, n_out = 128
BITS=    256.0 Bytes=    32  efficiency= 0.7293   Required Min_input_entropy_rate= 0.6856
BITS=    384.0 Bytes=    48  efficiency= 0.7292   Required Min_input_entropy_rate= 0.4571
BITS=    512.0 Bytes=    64  efficiency= 0.7293   Required Min_input_entropy_rate= 0.3428
BITS=    640.0 Bytes=    80  efficiency= 0.7291   Required Min_input_entropy_rate= 0.2743
BITS=    768.0 Bytes=    96  efficiency= 0.7291   Required Min_input_entropy_rate= 0.2286
BITS=    896.0 Bytes=   112  efficiency= 0.7292   Required Min_input_entropy_rate= 0.1959
BITS=   1024.0 Bytes=   128  efficiency= 0.7293   Required Min_input_entropy_rate= 0.1714
BITS=   1152.0 Bytes=   144  efficiency= 0.7291   Required Min_input_entropy_rate= 0.1524
BITS=   1280.0 Bytes=   160  efficiency= 0.7289   Required Min_input_entropy_rate= 0.1372
BITS=   1408.0 Bytes=   176  efficiency= 0.7290   Required Min_input_entropy_rate= 0.1247
BITS=   1536.0 Bytes=   192  efficiency= 0.7291   Required Min_input_entropy_rate= 0.1143
BITS=   1664.0 Bytes=   208  efficiency= 0.7291   Required Min_input_entropy_rate= 0.1055
BITS=   1792.0 Bytes=   224  efficiency= 0.7289   Required Min_input_entropy_rate= 0.0980
BITS=   1920.0 Bytes=   240  efficiency= 0.7286   Required Min_input_entropy_rate= 0.0915
BITS=   2048.0 Bytes=   256  efficiency= 0.7293   Required Min_input_entropy_rate= 0.0857
BITS=   2176.0 Bytes=   272  efficiency= 0.7289   Required Min_input_entropy_rate= 0.0807
BITS=   2304.0 Bytes=   288  efficiency= 0.7291   Required Min_input_entropy_rate= 0.0762
BITS=   2432.0 Bytes=   304  efficiency= 0.7290   Required Min_input_entropy_rate= 0.0722
BITS=   2560.0 Bytes=   320  efficiency= 0.7289   Required Min_input_entropy_rate= 0.0686
BITS=   2688.0 Bytes=   336  efficiency= 0.7292   Required Min_input_entropy_rate= 0.0653
BITS=   2816.0 Bytes=   352  efficiency= 0.7284   Required Min_input_entropy_rate= 0.0624
BITS=   2944.0 Bytes=   368  efficiency= 0.7283   Required Min_input_entropy_rate= 0.0597
BITS=   3072.0 Bytes=   384  efficiency= 0.7284   Required Min_input_entropy_rate= 0.0572
BITS=   3200.0 Bytes=   400  efficiency= 0.7286   Required Min_input_entropy_rate= 0.0549
BITS=   3328.0 Bytes=   416  efficiency= 0.7284   Required Min_input_entropy_rate= 0.0528
BITS=   3456.0 Bytes=   432  efficiency= 0.7291   Required Min_input_entropy_rate= 0.0508
BITS=   3584.0 Bytes=   448  efficiency= 0.7289   Required Min_input_entropy_rate= 0.0490
BITS=   3712.0 Bytes=   464  efficiency= 0.7290   Required Min_input_entropy_rate= 0.0473
BITS=   3840.0 Bytes=   480  efficiency= 0.7278   Required Min_input_entropy_rate= 0.0458
BITS=   3968.0 Bytes=   496  efficiency= 0.7282   Required Min_input_entropy_rate= 0.0443
BITS=   4096.0 Bytes=   512  efficiency= 0.7284   Required Min_input_entropy_rate= 0.0429
BITS=   4224.0 Bytes=   528  efficiency= 0.7284   Required Min_input_entropy_rate= 0.0416
BITS=   4352.0 Bytes=   544  efficiency= 0.7280   Required Min_input_entropy_rate= 0.0404
BITS=   4480.0 Bytes=   560  efficiency= 0.7289   Required Min_input_entropy_rate= 0.0392
BITS=   4608.0 Bytes=   576  efficiency= 0.7291   Required Min_input_entropy_rate= 0.0381
BITS=   4736.0 Bytes=   592  efficiency= 0.7285   Required Min_input_entropy_rate= 0.0371
BITS=   4864.0 Bytes=   608  efficiency= 0.7290   Required Min_input_entropy_rate= 0.0361
BITS=   4992.0 Bytes=   624  efficiency= 0.7284   Required Min_input_entropy_rate= 0.0352
BITS=   5120.0 Bytes=   640  efficiency= 0.7289   Required Min_input_entropy_rate= 0.0343
BITS=   5248.0 Bytes=   656  efficiency= 0.7281   Required Min_input_entropy_rate= 0.0335
BITS=   5376.0 Bytes=   672  efficiency= 0.7281   Required Min_input_entropy_rate= 0.0327
BITS=   5504.0 Bytes=   688  efficiency= 0.7290   Required Min_input_entropy_rate= 0.0319
BITS=   5632.0 Bytes=   704  efficiency= 0.7284   Required Min_input_entropy_rate= 0.0312
BITS=   5760.0 Bytes=   720  efficiency= 0.7286   Required Min_input_entropy_rate= 0.0305
BITS=   5888.0 Bytes=   736  efficiency= 0.7271   Required Min_input_entropy_rate= 0.0299
BITS=   6016.0 Bytes=   752  efficiency= 0.7287   Required Min_input_entropy_rate= 0.0292
BITS=   6144.0 Bytes=   768  efficiency= 0.7284   Required Min_input_entropy_rate= 0.0286
HMAC/SHA-256 Extraction, n_out = 128
BITS=    384.0 Bytes=    48  efficiency= 0.8461   Required Min_input_entropy_rate= 0.7879
BITS=    512.0 Bytes=    64  efficiency= 0.8462   Required Min_input_entropy_rate= 0.5909
BITS=    640.0 Bytes=    80  efficiency= 0.8462   Required Min_input_entropy_rate= 0.4727
BITS=    768.0 Bytes=    96  efficiency= 0.8460   Required Min_input_entropy_rate= 0.3940
BITS=    896.0 Bytes=   112  efficiency= 0.8461   Required Min_input_entropy_rate= 0.3377
BITS=   1024.0 Bytes=   128  efficiency= 0.8460   Required Min_input_entropy_rate= 0.2955
BITS=   1152.0 Bytes=   144  efficiency= 0.8459   Required Min_input_entropy_rate= 0.2627
BITS=   1280.0 Bytes=   160  efficiency= 0.8460   Required Min_input_entropy_rate= 0.2364
BITS=   1408.0 Bytes=   176  efficiency= 0.8461   Required Min_input_entropy_rate= 0.2149
BITS=   1536.0 Bytes=   192  efficiency= 0.8460   Required Min_input_entropy_rate= 0.1970
BITS=   1664.0 Bytes=   208  efficiency= 0.8458   Required Min_input_entropy_rate= 0.1819
BITS=   1792.0 Bytes=   224  efficiency= 0.8458   Required Min_input_entropy_rate= 0.1689
BITS=   1920.0 Bytes=   240  efficiency= 0.8460   Required Min_input_entropy_rate= 0.1576
BITS=   2048.0 Bytes=   256  efficiency= 0.8457   Required Min_input_entropy_rate= 0.1478
BITS=   2176.0 Bytes=   272  efficiency= 0.8458   Required Min_input_entropy_rate= 0.1391
BITS=   2304.0 Bytes=   288  efficiency= 0.8456   Required Min_input_entropy_rate= 0.1314
BITS=   2432.0 Bytes=   304  efficiency= 0.8462   Required Min_input_entropy_rate= 0.1244
BITS=   2560.0 Bytes=   320  efficiency= 0.8460   Required Min_input_entropy_rate= 0.1182
BITS=   2688.0 Bytes=   336  efficiency= 0.8458   Required Min_input_entropy_rate= 0.1126
BITS=   2816.0 Bytes=   352  efficiency= 0.8457   Required Min_input_entropy_rate= 0.1075
BITS=   2944.0 Bytes=   368  efficiency= 0.8459   Required Min_input_entropy_rate= 0.1028
BITS=   3072.0 Bytes=   384  efficiency= 0.8460   Required Min_input_entropy_rate= 0.0985
BITS=   3200.0 Bytes=   400  efficiency= 0.8457   Required Min_input_entropy_rate= 0.0946
BITS=   3328.0 Bytes=   416  efficiency= 0.8453   Required Min_input_entropy_rate= 0.0910
BITS=   3456.0 Bytes=   432  efficiency= 0.8456   Required Min_input_entropy_rate= 0.0876
BITS=   3584.0 Bytes=   448  efficiency= 0.8453   Required Min_input_entropy_rate= 0.0845
BITS=   3712.0 Bytes=   464  efficiency= 0.8462   Required Min_input_entropy_rate= 0.0815
BITS=   3840.0 Bytes=   480  efficiency= 0.8460   Required Min_input_entropy_rate= 0.0788
BITS=   3968.0 Bytes=   496  efficiency= 0.8456   Required Min_input_entropy_rate= 0.0763
BITS=   4096.0 Bytes=   512  efficiency= 0.8457   Required Min_input_entropy_rate= 0.0739
BITS=   4224.0 Bytes=   528  efficiency= 0.8453   Required Min_input_entropy_rate= 0.0717
BITS=   4352.0 Bytes=   544  efficiency= 0.8452   Required Min_input_entropy_rate= 0.0696
BITS=   4480.0 Bytes=   560  efficiency= 0.8453   Required Min_input_entropy_rate= 0.0676
BITS=   4608.0 Bytes=   576  efficiency= 0.8456   Required Min_input_entropy_rate= 0.0657
BITS=   4736.0 Bytes=   592  efficiency= 0.8459   Required Min_input_entropy_rate= 0.0639
BITS=   4864.0 Bytes=   608  efficiency= 0.8462   Required Min_input_entropy_rate= 0.0622
BITS=   4992.0 Bytes=   624  efficiency= 0.8448   Required Min_input_entropy_rate= 0.0607
BITS=   5120.0 Bytes=   640  efficiency= 0.8460   Required Min_input_entropy_rate= 0.0591
BITS=   5248.0 Bytes=   656  efficiency= 0.8454   Required Min_input_entropy_rate= 0.0577
BITS=   5376.0 Bytes=   672  efficiency= 0.8458   Required Min_input_entropy_rate= 0.0563
BITS=   5504.0 Bytes=   688  efficiency= 0.8457   Required Min_input_entropy_rate= 0.0550
BITS=   5632.0 Bytes=   704  efficiency= 0.8449   Required Min_input_entropy_rate= 0.0538
BITS=   5760.0 Bytes=   720  efficiency= 0.8450   Required Min_input_entropy_rate= 0.0526
BITS=   5888.0 Bytes=   736  efficiency= 0.8459   Required Min_input_entropy_rate= 0.0514
BITS=   6016.0 Bytes=   752  efficiency= 0.8460   Required Min_input_entropy_rate= 0.0503
BITS=   6144.0 Bytes=   768  efficiency= 0.8452   Required Min_input_entropy_rate= 0.0493
HMAC/SHA-384 Extraction, n_out = 256
BITS=    512.0 Bytes=    64  efficiency= 0.8939   Required Min_input_entropy_rate= 0.8390
BITS=    640.0 Bytes=    80  efficiency= 0.8939   Required Min_input_entropy_rate= 0.6712
BITS=    768.0 Bytes=    96  efficiency= 0.8940   Required Min_input_entropy_rate= 0.5593
BITS=    896.0 Bytes=   112  efficiency= 0.8940   Required Min_input_entropy_rate= 0.4794
BITS=   1024.0 Bytes=   128  efficiency= 0.8939   Required Min_input_entropy_rate= 0.4195
BITS=   1152.0 Bytes=   144  efficiency= 0.8939   Required Min_input_entropy_rate= 0.3729
BITS=   1280.0 Bytes=   160  efficiency= 0.8939   Required Min_input_entropy_rate= 0.3356
BITS=   1408.0 Bytes=   176  efficiency= 0.8939   Required Min_input_entropy_rate= 0.3051
BITS=   1536.0 Bytes=   192  efficiency= 0.8938   Required Min_input_entropy_rate= 0.2797
BITS=   1664.0 Bytes=   208  efficiency= 0.8938   Required Min_input_entropy_rate= 0.2582
BITS=   1792.0 Bytes=   224  efficiency= 0.8940   Required Min_input_entropy_rate= 0.2397
BITS=   1920.0 Bytes=   240  efficiency= 0.8937   Required Min_input_entropy_rate= 0.2238
BITS=   2048.0 Bytes=   256  efficiency= 0.8937   Required Min_input_entropy_rate= 0.2098
BITS=   2176.0 Bytes=   272  efficiency= 0.8940   Required Min_input_entropy_rate= 0.1974
BITS=   2304.0 Bytes=   288  efficiency= 0.8937   Required Min_input_entropy_rate= 0.1865
BITS=   2432.0 Bytes=   304  efficiency= 0.8936   Required Min_input_entropy_rate= 0.1767
BITS=   2560.0 Bytes=   320  efficiency= 0.8939   Required Min_input_entropy_rate= 0.1678
BITS=   2688.0 Bytes=   336  efficiency= 0.8940   Required Min_input_entropy_rate= 0.1598
BITS=   2816.0 Bytes=   352  efficiency= 0.8936   Required Min_input_entropy_rate= 0.1526
BITS=   2944.0 Bytes=   368  efficiency= 0.8934   Required Min_input_entropy_rate= 0.1460
BITS=   3072.0 Bytes=   384  efficiency= 0.8935   Required Min_input_entropy_rate= 0.1399
BITS=   3200.0 Bytes=   400  efficiency= 0.8935   Required Min_input_entropy_rate= 0.1343
BITS=   3328.0 Bytes=   416  efficiency= 0.8938   Required Min_input_entropy_rate= 0.1291
BITS=   3456.0 Bytes=   432  efficiency= 0.8939   Required Min_input_entropy_rate= 0.1243
BITS=   3584.0 Bytes=   448  efficiency= 0.8936   Required Min_input_entropy_rate= 0.1199
BITS=   3712.0 Bytes=   464  efficiency= 0.8933   Required Min_input_entropy_rate= 0.1158
BITS=   3840.0 Bytes=   480  efficiency= 0.8937   Required Min_input_entropy_rate= 0.1119
BITS=   3968.0 Bytes=   496  efficiency= 0.8936   Required Min_input_entropy_rate= 0.1083
BITS=   4096.0 Bytes=   512  efficiency= 0.8937   Required Min_input_entropy_rate= 0.1049
BITS=   4224.0 Bytes=   528  efficiency= 0.8939   Required Min_input_entropy_rate= 0.1017
BITS=   4352.0 Bytes=   544  efficiency= 0.8940   Required Min_input_entropy_rate= 0.0987
BITS=   4480.0 Bytes=   560  efficiency= 0.8938   Required Min_input_entropy_rate= 0.0959
BITS=   4608.0 Bytes=   576  efficiency= 0.8932   Required Min_input_entropy_rate= 0.0933
BITS=   4736.0 Bytes=   592  efficiency= 0.8939   Required Min_input_entropy_rate= 0.0907
BITS=   4864.0 Bytes=   608  efficiency= 0.8931   Required Min_input_entropy_rate= 0.0884
BITS=   4992.0 Bytes=   624  efficiency= 0.8934   Required Min_input_entropy_rate= 0.0861
BITS=   5120.0 Bytes=   640  efficiency= 0.8939   Required Min_input_entropy_rate= 0.0839
BITS=   5248.0 Bytes=   656  efficiency= 0.8934   Required Min_input_entropy_rate= 0.0819
BITS=   5376.0 Bytes=   672  efficiency= 0.8940   Required Min_input_entropy_rate= 0.0799
BITS=   5504.0 Bytes=   688  efficiency= 0.8933   Required Min_input_entropy_rate= 0.0781
BITS=   5632.0 Bytes=   704  efficiency= 0.8936   Required Min_input_entropy_rate= 0.0763
BITS=   5760.0 Bytes=   720  efficiency= 0.8937   Required Min_input_entropy_rate= 0.0746
BITS=   5888.0 Bytes=   736  efficiency= 0.8934   Required Min_input_entropy_rate= 0.0730
BITS=   6016.0 Bytes=   752  efficiency= 0.8940   Required Min_input_entropy_rate= 0.0714
BITS=   6144.0 Bytes=   768  efficiency= 0.8929   Required Min_input_entropy_rate= 0.0700
HMAC/SHA-512 Extraction, n_out = 384
BITS=    640.0 Bytes=    80  efficiency= 0.9183   Required Min_input_entropy_rate= 0.8712
BITS=    768.0 Bytes=    96  efficiency= 0.9183   Required Min_input_entropy_rate= 0.7260
BITS=    896.0 Bytes=   112  efficiency= 0.9183   Required Min_input_entropy_rate= 0.6223
BITS=   1024.0 Bytes=   128  efficiency= 0.9183   Required Min_input_entropy_rate= 0.5445
BITS=   1152.0 Bytes=   144  efficiency= 0.9183   Required Min_input_entropy_rate= 0.4840
BITS=   1280.0 Bytes=   160  efficiency= 0.9183   Required Min_input_entropy_rate= 0.4356
BITS=   1408.0 Bytes=   176  efficiency= 0.9183   Required Min_input_entropy_rate= 0.3960
BITS=   1536.0 Bytes=   192  efficiency= 0.9183   Required Min_input_entropy_rate= 0.3630
BITS=   1664.0 Bytes=   208  efficiency= 0.9182   Required Min_input_entropy_rate= 0.3351
BITS=   1792.0 Bytes=   224  efficiency= 0.9181   Required Min_input_entropy_rate= 0.3112
BITS=   1920.0 Bytes=   240  efficiency= 0.9183   Required Min_input_entropy_rate= 0.2904
BITS=   2048.0 Bytes=   256  efficiency= 0.9181   Required Min_input_entropy_rate= 0.2723
BITS=   2176.0 Bytes=   272  efficiency= 0.9180   Required Min_input_entropy_rate= 0.2563
BITS=   2304.0 Bytes=   288  efficiency= 0.9183   Required Min_input_entropy_rate= 0.2420
BITS=   2432.0 Bytes=   304  efficiency= 0.9181   Required Min_input_entropy_rate= 0.2293
BITS=   2560.0 Bytes=   320  efficiency= 0.9183   Required Min_input_entropy_rate= 0.2178
BITS=   2688.0 Bytes=   336  efficiency= 0.9180   Required Min_input_entropy_rate= 0.2075
BITS=   2816.0 Bytes=   352  efficiency= 0.9183   Required Min_input_entropy_rate= 0.1980
BITS=   2944.0 Bytes=   368  efficiency= 0.9182   Required Min_input_entropy_rate= 0.1894
BITS=   3072.0 Bytes=   384  efficiency= 0.9183   Required Min_input_entropy_rate= 0.1815
BITS=   3200.0 Bytes=   400  efficiency= 0.9180   Required Min_input_entropy_rate= 0.1743
BITS=   3328.0 Bytes=   416  efficiency= 0.9179   Required Min_input_entropy_rate= 0.1676
BITS=   3456.0 Bytes=   432  efficiency= 0.9179   Required Min_input_entropy_rate= 0.1614
BITS=   3584.0 Bytes=   448  efficiency= 0.9181   Required Min_input_entropy_rate= 0.1556
BITS=   3712.0 Bytes=   464  efficiency= 0.9183   Required Min_input_entropy_rate= 0.1502
BITS=   3840.0 Bytes=   480  efficiency= 0.9183   Required Min_input_entropy_rate= 0.1452
BITS=   3968.0 Bytes=   496  efficiency= 0.9177   Required Min_input_entropy_rate= 0.1406
BITS=   4096.0 Bytes=   512  efficiency= 0.9178   Required Min_input_entropy_rate= 0.1362
BITS=   4224.0 Bytes=   528  efficiency= 0.9183   Required Min_input_entropy_rate= 0.1320
BITS=   4352.0 Bytes=   544  efficiency= 0.9177   Required Min_input_entropy_rate= 0.1282
BITS=   4480.0 Bytes=   560  efficiency= 0.9180   Required Min_input_entropy_rate= 0.1245
BITS=   4608.0 Bytes=   576  efficiency= 0.9183   Required Min_input_entropy_rate= 0.1210
BITS=   4736.0 Bytes=   592  efficiency= 0.9177   Required Min_input_entropy_rate= 0.1178
BITS=   4864.0 Bytes=   608  efficiency= 0.9177   Required Min_input_entropy_rate= 0.1147
BITS=   4992.0 Bytes=   624  efficiency= 0.9182   Required Min_input_entropy_rate= 0.1117
BITS=   5120.0 Bytes=   640  efficiency= 0.9183   Required Min_input_entropy_rate= 0.1089
BITS=   5248.0 Bytes=   656  efficiency= 0.9178   Required Min_input_entropy_rate= 0.1063
BITS=   5376.0 Bytes=   672  efficiency= 0.9175   Required Min_input_entropy_rate= 0.1038
BITS=   5504.0 Bytes=   688  efficiency= 0.9183   Required Min_input_entropy_rate= 0.1013
BITS=   5632.0 Bytes=   704  efficiency= 0.9183   Required Min_input_entropy_rate= 0.0990
BITS=   5760.0 Bytes=   720  efficiency= 0.9183   Required Min_input_entropy_rate= 0.0968
BITS=   5888.0 Bytes=   736  efficiency= 0.9182   Required Min_input_entropy_rate= 0.0947
BITS=   6016.0 Bytes=   752  efficiency= 0.9181   Required Min_input_entropy_rate= 0.0927
BITS=   6144.0 Bytes=   768  efficiency= 0.9178   Required Min_input_entropy_rate= 0.0908
```
