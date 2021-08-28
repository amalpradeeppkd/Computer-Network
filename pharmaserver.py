import socket
import pandas as pd
df=pd.read_csv(r"C:\Users\pradeep\Downloads\pharmacy.csv")
a=df.to_string(index=False)
s=socket.socket()
print("socket created")
s.bind(('localhost',5001))
s.listen(3)
print("waiting for Connection")
while True:
    c,addr=s.accept()
    print("Connected with",addr)
    c.send(bytes(a,'utf8'))
