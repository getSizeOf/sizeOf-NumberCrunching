#!/usr/bin/env python

import math

class crunch(object):

    def __init__(self):
        pass

    def focalLengthComp(self, dist):
        return ((2.004 * math.pow(dist, 4.0)) - (21.875 * (math.pow(dist, 3.0))) + 
            (78.249 * math.pow(dist, 2.0)) - (115.936 * dist) + 111.396)

    def objectHeight(self, dist, pxHeight, sensorHeight, fLenEff, subHeight):
        return ((pxHeight * dist * sensorHeight) / (fLenEff * subHeight))


if __name__=="__main__":
    cruncher = crunch()
    dist = .447
    fL = cruncher.focalLengthComp(dist)
    print(cruncher.objectHeight(dist, 4000, 15.6, fL, 905.44))
