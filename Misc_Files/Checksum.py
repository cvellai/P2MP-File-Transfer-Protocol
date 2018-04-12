import sys



def carry_around_add(a, b):
    c = a + b
    return (c & 0xffff) + (c >> 16)

def checksum(msg):
    s = 0
    for i in range(0, len(msg), 2):
        print i
        if msg[i] == msg[len(msg)-1]:
            w = ord(msg[i])<<8
        else:
            w = (ord(msg[i])<<8) + (ord(msg[i+1]))
            print "\nmsg[%d]: %s" %(i,bin(ord(msg[i]))[2:])
            print "\nmsg[%d]: %s" %(i+1,bin(ord(msg[i+1]))[2:])
        print "\nw: "+bin(w)[2:]
        s = carry_around_add(s, w)
    print "\nsum: %s" %(bin(s)[2:])
    print "\nchecksum: %s" %(bin(~s & 0xffff)[2:])
    return ~s & 0xffff

def validate(msg,chcksum):
    print "\nValidating Checksum....."
    s = 0
    for i in range(0, len(msg), 2):
        print i
        if msg[i] == msg[len(msg)-1]:
            w = ord(msg[i])<<8
        else:
            w = (ord(msg[i])<<8) + (ord(msg[i+1]))
            print "\nmsg[%d]: %s" %(i,bin(ord(msg[i]))[2:])
            print "\nmsg[%d]: %s" %(i+1,bin(ord(msg[i+1]))[2:])
        print "\nw: "+bin(w)[2:]
        s = carry_around_add(s, w)
    print "\nSum: %s" %(s)
    print "\nCHcksum in int: %s" %(int(chcksum))
    print "\nChcksum,2: %s" %(int(chcksum,2))
    #print "\npseudo result: %d" %(s^int(chcksum))
    print "\nResult: %s" %(bin(s^int(chcksum,2))) 



def main():

    while True:
        string = raw_input("\nEnter a string: ")
        for i in string:
            print "%s: %d(%s)\n" %(i,ord(i),bin(ord(i))[2:])
        
        chcksum = checksum(string)
        chcksum = '{0:016b}'.format(chcksum)
        validate(string,chcksum)
        prompt = raw_input("another round? ;)")
        if prompt == "n":
            break
    sys.exit(0)


if __name__ == '__main__':
    main()
