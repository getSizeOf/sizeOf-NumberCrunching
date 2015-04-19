#!/usr/bin/env python

import numpy
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plot

class crunch(object):

    def __init__(self):
        pass

    def focalLengthComp(self, dist):
        return ((2.004 * (dist ** 4.0)) - (21.875 * (dist ** 3.0)) +
            (78.249 * (dist ** 2.0)) - (115.936 * dist) + 111.396)

    def objectHeight(self, dist, pxHeight, sensorHeight, fLenEff, subHeight):
        return (subHeight * dist * sensorHeight) / (fLenEff * pxHeight)

    def objHeight(self, dist, pxHeight, sensH, fL, sH):
        focus = 2.0 * math.atan(sensH / (2.0 * fL))
        halfH = 2.0 * math.tan(focus/2.0)
        pH = (halfH * dist) / pxHeight
        return pH * sH

    def strip_keys(self, xmlDict, x=None, y=None):
        if x is None:
            x = []
        if y is None:
            y = []
        for key in xmlDict:#key is dataset id
            values = xmlDict[key]
            x.append(values[1])#focal length value [0,1]
            y.append(values[0])#cm to object [0, inf)
        return x, y

    def crunch_data(self, x, y, deg):
        x = numpy.array(x)
        x.sort()
        y = numpy.array(y)
        y.sort()
        fit = numpy.polyfit(x, y, deg)
        p = numpy.poly1d(fit)
        xp1 = numpy.linspace(min(x), max(x))
        plot.plot(x, y)#, xp1, p(xp1),alpha=0.4)
        plot.plot(xp1, p(xp1), color='r')
        print "fit: " + str(p)
        plot.show()

    def parse_xml_data(self, filename):
        tree = ET.parse(filename)
        root = tree.getroot()
        result = dict()
        currKey = None#current key
        for child in root:
            if child.tag == "key":
                currKey = child.text
            elif child.tag == "array":
                arry = []
                for inner in child:
                    arry.append(float(inner.text))
                    if len(arry) is 2:
                        result[currKey] = arry
        return result

    def parse_csv_data(self, filename):
        x = []
        y = []
        i = 10
        for line in open(filename):
            line = line.strip()
            optims = line.split(',')#ideal focus length
            optimAvg = 0.0
            for optim in optims:
                optimAvg += float(optim)
            i += 3
            y.append(float(i))#CM to focus
            x.append(float(optimAvg)/3.0)#
        return x,y

if __name__=="__main__":
    cruncher = crunch()
    #xml = cruncher.parse_xml_data('data/iPhone6_1.xml')
    #x,y = cruncher.strip_keys(xml)
    #xml = cruncher.parse_xml_data('data/iPhone6_2.xml')
    #x,y = cruncher.strip_keys(xml, x, y)
    x,y = cruncher.parse_csv_data('data/DROID_MAXX_alt.csv')
    cruncher.crunch_data(x, y, 5)
    #dist = .447
    #fL = cruncher.focalLengthComp(dist)
    #print (cruncher.objHeight(dist, 4000, 15.6, fL, 905.44))

