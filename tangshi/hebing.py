# -*- coding:utf-8 -*-
import os
import sys
import glob
def dirTxtToLargeTxt():
  '''从dir目录下读入所有的TXT文件,将它们写到outputFileName里去'''
  #如果dir不是目录返回错误
  outputFileName = 'res.txt'
  dir='tang'
  outputFile = open(outputFileName,"a")
  for txtFile in glob.glob(os.path.join(dir,"*.txt")):
    print((txtFile))
    inputFile = open(txtFile,"rb")
    for line in inputFile:
      print(line.decode('gbk'))
      outputFile.write(line.decode('gbk'))
  return True

  dirTxtToLargeTxt()