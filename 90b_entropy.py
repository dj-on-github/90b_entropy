#!/usr/bin/env python3

from __future__ import print_function

import math
#import matplotlib.pyplot as plt
from mpmath import *

PRECISION = 2048

out_format = "text"
#out_format = "csv"

def output_entropy(n_in,n_out,nw, h_in):
    n = min(n_out,nw)
    ttninmn = mpf(2.0)**(n_in-n)
    p_high = mpf(2.0)**(-h_in)
    p_low = (mpf(1.0)-p_high)/((mpf(2.0)**n_in)-mpf(1.0))
    phi = ttninmn*p_low + p_high
    U = ttninmn + sqrt(mpf(2.0) * n * ttninmn * log(mpf(2.0)))
    w = U * p_low
    return -log(max(phi,w),2)

if __name__=="__main__":

    if out_format=="csv":
        print("algorithm, output_bits, input_bits, efficiency, min_entropy_input_rate")
    for type in ["cbc-mac","sha-256", "sha-384", "sha-512"]:
        if type=="cbc-mac":
            nw = mpf(128)
            n_out = mpf(128)
            if out_format == "text":
                print("AES-CBC-MAC Extraction, n_out = %d" % n_out)
        elif type=="sha-256":
            nw = mpf(256)
            if out_format == "text":
                print("HMAC/SHA-256 Extraction, n_out = %d" % n_out)
            n_out = mpf(256)
        elif type=="sha-384":
            if out_format == "text":
                print("HMAC/SHA-384 Extraction, n_out = %d " % n_out)
            nw = mpf(512)
            n_out = mpf(384)
        elif type=="sha-512":
            if out_format == "text":
                print("HMAC/SHA-512 Extraction, n_out = %d" % n_out)
            nw = mpf(512)
            n_out = mpf(512)
        else:
            print("Need a working type")
            exit(1)


        for L in range(2,49):
            n_in = mpf(128*L)
            xs = [x*0.0001 for x in range(10001)]
            ys = list()
            found = False
            for x in xs:
                h_in = x * n_in
                entropy = output_entropy(n_in, n_out, nw, h_in)
                ys.append(entropy)
                if (found == False) and (entropy >= n_out):
                    found = True
                    if out_format == "text":
                        print("BITS=",str(n_in).rjust(8),"Bytes=",str(int(n_in/8)).rjust(5), (" efficiency= %3.4f" %(n_out/h_in)).rjust(8),"  Required Min_input_entropy_rate= %3.4f" % x)
                    elif out_format == "csv":
                        print(type," , ",int(n_out)," , ",int(n_in)," , ","%3.4f"%(n_out/h_in)," , ","%3.4f"%x) 

        #plt.plot(xs,ys,label="L="+str(L))

    #plt.legend()
    #plt.show()


    

