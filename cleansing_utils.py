import cv2
import sys
import dlib
import os
import time 
import pandas as pd

rootDev = './dev/'
rootEval = './eval/'
dirNamesDev = os.listdir(rootDev)
dirNamesEval = os.listdir(rootEval)
# freqDev = {}
# freqEval = {}

def dataCleansing(root, names):
    detector = dlib.get_frontal_face_detector()

    delCount = 0
    prcsCount = 0

    for name in names:
        for pic in os.listdir(root + name):
            prcsCount += 1
            path = '{}{}/{}'.format(rootroot, name, pic)
            img = cv2.imread(path)
            try:
                img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            except Exception:
                os.remove(path)
                continue
            faces = detector(img_gray, 1)
            if not faces:
                os.remove(path)
                delCount += 1
                print("{} deleted out of {} processed".format(delCount, prcsCount))
            else:
                continue

def dataCount(root, names):
    for name in names:
        freq.update({name: len(os.listdir(root + name))})
    return freq

def dataSort(freq):
    freqSorted = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    final = {}
    for i in freqSorted:
        final.update({i[0]: i[1]})

def toCSV(d):
    df = pd.DataFrame.from_dict(d, orient='index')
    df.to_csv ('../output.csv', header=True)
