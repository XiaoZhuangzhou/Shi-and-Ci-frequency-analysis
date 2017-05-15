
def dirTxtToLargeTxt():
  '''从dir目录下读入所有的TXT文件,将它们写到outputFileName里去'''
  #如果dir不是目录返回错误
  outputFileName = 'Cires.txt'
  inputFileName = 'Ci.txt'
  outputFile = open(outputFileName,"a")
  inputFile = open(inputFileName,"rb")
  cnt=0
  for line in inputFile:
      if (len(line) < 20): continue
      print(line.decode('utf8'))

      cnt+=1
      try:
        outputFile.write(line.decode('utf8'))
      except:
        pass

  return True

dirTxtToLargeTxt()