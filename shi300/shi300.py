
def dirTxtToLargeTxt():
  '''从dir目录下读入所有的TXT文件,将它们写到outputFileName里去'''
  #如果dir不是目录返回错误
  outputFileName = 'shi300res.txt'
  inputFileName = 'shi300.txt'
  outputFile = open(outputFileName,"a")
  inputFile = open(inputFileName,"rb")
  cnt=0
  for line in inputFile:
      cnt+=1
      print(line.decode('gbk'))
      m=line.decode('gbk')
      flag=True
      for i in m:
        if i in "0123456789ABCDEFGqwertyuiopasdfghjklzxcvbnm_=（） *().+":
          print(i)
          flag=False
          break
      if len(line) < 20: continue
      print(flag)
      if flag==True:
        try:
          outputFile.write(m)
        except:
          pass

  return True

dirTxtToLargeTxt()