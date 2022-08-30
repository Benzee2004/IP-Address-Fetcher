"""We are going to use socket module to get our IP address"""
import socket

hostname =socket.gethostname()

IP = socket.gethostbyname(hostname)

print(f"Computer name: {hostname}")
print(f" Ip address : {IP}")

