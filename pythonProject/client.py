import socket
ob=socket.socket()
ob.connect(('localhost',2301))

''''msg='hello this is first client'
ob.send(msg.encode('utf-8'))

ob.close()
'''
conn=True
while conn:
    msg=input("enter you message")
    ob.send(msg.encode('utf-8'))
    if msg=='no':
        conn=False
        ob.close()
