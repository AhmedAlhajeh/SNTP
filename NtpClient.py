import socket
import struct
import sys
import time

NTP_SERVER = '0.pool.ntp.org' #The NTP server we are connecting to
TIME1970 = 2208988800 #seconds between 1 Jan 1900 to 1 Jan 1970


def sntp_client():

    client= socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #Creating NTP UDP Socket
    data = '\x1b' + 47 * '\0' #represents the data field of 48 bytes followed by 47 times
    client.sendto(data.encode(), (NTP_SERVER, 123)) #Client is sending data to NTP UDP server port number is 123
    data, address = client.recvfrom(4096) #data variable contains the received Data and the address the NTP replied from






    if data:
        print('Response received from:', address)
        t = struct.unpack('!12I', data)[10] - TIME1970 #calculate the current time from the server (1900 - 1970)



        print('\tTime=%s' % time.ctime(t)) #printing the current time
if __name__ == '__main__': #It runs the function when the python interpreter reads the source file as the main program
    sntp_client()


