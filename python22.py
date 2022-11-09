import sys

print(sys.argv)

import pickle

f=open("test.txt","wb")
data={1:"python",2:"you need"}
pickle.dump(data,f) # data 딕셔너리 객체를 그대로 파일에 저장하는 기능
f.close()

f=open("test.txt","rb")
data=pickle.load(f)
print(data)