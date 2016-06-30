import pyupm_grove as g
from time import sleep

if __name__ == '__main__':
    bttn = g.GroveButton(4)

    while True:
        if bttn.value():
            print 'Button is pressed'
        else:
            print 'Button is not pressed'
        sleep(1.0)

