#SENSOR HC-SR40

#Author : Schrodinger's Kat
import RPi.GPIO as GPIO #import RPi.GPIO file for interaction
import time		#import time file

GPIO.setmode(GPIO.BCM)	#set GPIO pin mode to BCM

GPIO_TRIGGER1 = 2	#Assign Trigger pin of HC-SR04 Sensor 1 to GPIO Pin 2 of Raspberry
GPIO_ECHO1 = 3		#Assign Echo Pin of HC-SR04 Sensor 1 to GPIO Pin 3 of Rasberry
GPIO_TRIGGER2 = 23
GPIO_ECHO2 = 24
GPIO_TRIGGER3 = 17
GPIO_ECHO3 = 27
GPIO_TRIGGER4 = 5
GPIO_ECHO4 = 6
GPIO_TRIGGER5 = 18
GPIO_ECHO5 = 25
GPIO_TRIGGER6 = 4
GPIO_ECHO6 = 22

GPIO.setup(GPIO_TRIGGER1, GPIO.OUT)	#Setup Pin  to type of Signal !! OUT for Write Signal
GPIO.setup(GPIO_ECHO1, GPIO.IN)		#Setup Pin  to type of Signal !! IN for Read Signal
GPIO.setup(GPIO_TRIGGER2, GPIO.OUT)
GPIO.setup(GPIO_ECHO2, GPIO.IN)
GPIO.setup(GPIO_TRIGGER3,GPIO.OUT)
GPIO.setup(GPIO_ECHO3,GPIO.IN)
GPIO.setup(GPIO_TRIGGER4,GPIO.OUT)
GPIO.setup(GPIO_ECHO4,GPIO.IN)
GPIO.setup(GPIO_TRIGGER5,GPIO.OUT)
GPIO.setup(GPIO_ECHO5,GPIO.IN)
GPIO.setup(GPIO_TRIGGER6,GPIO.OUT)
GPIO.setup(GPIO_ECHO6,GPIO.IN)


def sens1():				#define function sens1() for Ultrasonic Sensor 1 Readings

    GPIO.output(GPIO_TRIGGER1, True)


    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER1, False)

    initial1 = time.time()	#variable initial1 stores the time @ which signal is transmitted from trigger pin
    final1 = time.time()	#variable final1 stores the time @ which signal is received @ the echo pin


    while GPIO.input(GPIO_ECHO1) == 0:
        initial1 = time.time()


    while GPIO.input(GPIO_ECHO1) == 1:
        final1 = time.time()


    timetaken1 = final1 - initial1


    distance = (timetaken1 * 34300) / 2		#distance is calculated as timetaken * speed of sound(343m/s) divided by 2. Since total time is taken for distance of sensor to object and from object to sensor

    return distance


def sens2(): #define function sens2() for Ultrasonic Sensor 2 Readings

        GPIO.output(GPIO_TRIGGER2, True)


        time.sleep(0.00001)
        GPIO.output(GPIO_TRIGGER2, False)

        initial2 = time.time()
        final2 = time.time()


    	while GPIO.input(GPIO_ECHO2) == 0:
                        initial2 = time.time()
    	while GPIO.input(GPIO_ECHO2) == 1:
                        final2 = time.time()

	timetaken = final2 - initial2

	distance = (timetaken * 34300) / 2

	return distance


def sens3(): #define function sens3() for Ultrasonic Sensor 3 Readings

    GPIO.output(GPIO_TRIGGER3, True)


    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER3, False)

    initial3 = time.time()
    final3 = time.time()


    while GPIO.input(GPIO_ECHO3) == 0:
        initial3 = time.time()


    while GPIO.input(GPIO_ECHO3) == 1:
        final3 = time.time()


    timetaken3 = final3 - initial3


    distance = (timetaken3 * 34300) / 2

    return distance

def sens4():	#define function sens4() for Ultrasonic Sensor 4 Readings

    GPIO.output(GPIO_TRIGGER4, True)


    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER4, False)

    initial4 = time.time()
    final4 = time.time()


    while GPIO.input(GPIO_ECHO4) == 0:
        initial4 = time.time()


    while GPIO.input(GPIO_ECHO4) == 1:
        final4 = time.time()


    timetaken4 = final4 - initial4


    distance = (timetaken4 * 34300) / 2

    return distance

def sens5():#define function sens5() for Ultrasonic Sensor 5 Readings

    GPIO.output(GPIO_TRIGGER5, True)


    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER5, False)

    initial5 = time.time()
    final5 = time.time()


    while GPIO.input(GPIO_ECHO5) == 0:
        initial5 = time.time()


    while GPIO.input(GPIO_ECHO5) == 1:
        final5 = time.time()


    timetaken5 = final5 - initial5


    distance = (timetaken5 * 34300) / 2

    return distance

def sens6(): #define function sens6() for Ultrasonic Sensor 6 Readings

    GPIO.output(GPIO_TRIGGER6, True)


    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER6, False)

    initial6 = time.time()
    final6 = time.time()


    while GPIO.input(GPIO_ECHO6) == 0:
        initial6 = time.time()


    while GPIO.input(GPIO_ECHO6) == 1:
        final6 = time.time()


    timetaken6 = final6 - initial6


    distance = (timetaken6 * 34300) / 2

    return distance


def chk(dist,no): #define function chk to check weather the slot is currently free or busy 

	if(dist>20):	#if distance between the sensor & obstacle(car) is more than 20cm implies Slot is Free
		print("SLOT %i  is Available for Parking") %no
	else:		#if distance between the sensor & obstacle(car) is less than 20cm implies Slot is Busy
		print("SLOT %i  is Unavilable for Parking...SORRY") %no

if __name__ == '__main__':
  try:
    while True:		#loop till False
        dist1 = sens1()	#dist1 stores Sensor 1's Realtime Reading
        dist2 = sens2()
        dist3 = sens3()
        dist4 = sens4()
        dist5 = sens5()
        dist6 = sens6()

	    chk(dist1,1)#chk function to check slot availability
	    chk(dist2,2)
	    chk(dist3,3)
	    chk(dist4,4)
	    chk(dist5,5)
	    chk(dist6,6)

        time.sleep(10)


    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
