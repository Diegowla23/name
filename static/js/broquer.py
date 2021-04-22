
import paho.mqtt.client as mqtt 
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN)
GPIO.setup(5,GPIO.IN)
GPIO.setup(6,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)


def nueva(a):
	global con
	con=a
	
	
def datos():
	print("contrasena correcta")
	
def on_message(client, obj, msg):    
	print(msg.payload.decode("utf-8"))
	accion=(msg.payload.decode("utf-8")).split(" ")[0]
	clave=(msg.payload.decode("utf-8")).split(" ")[1]
	print(accion)
	print(clave)
	if clave==con:
		datos()
	elif clave=="nueva":
		H=clave
		nueva(H)
	elif clave=="misma":
		datos()
	
mqttc = mqtt.Client() 
mqttc.on_message = on_message 
mqttc.username_pw_set("cinthyaanabel14@gmail.com","embebidos") 
mqttc.connect("maqiatto.com", 1883) 
mqttc.subscribe("cinthyaanabel14@gmail.com/raspberry", 0)
rc=0
print("inicio...")
i = 0
while rc == 0:
	time.sleep(2)
	rc = mqttc.loop()
	if GPIO.input(4):
		GPIO.output(6,True)
		mqttc.publish("cinthyaanabel14@gmail.com/servidor", "S1 activo")
	else:
		GPIO.output(6,False)
		mqttc.publish("cinthyaanabel14@gmail.com/servidor", "S1 desactivado")
	if GPIO.input(5):
		GPIO.output(7,True)
		mqttc.publish("cinthyaanabel14@gmail.com/servidor", "S2 activo")
	else:
		GPIO.output(7,False)
		mqttc.publish("cinthyaanabel14@gmail.com/servidor", "S2 desactivado")