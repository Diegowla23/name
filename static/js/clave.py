import paho.mqtt.client as mqtt 
import time
import RPi.GPIO as GPIO
import datetime

GPIO.setmode(GPIO.BCM)
GPIO.setup (20, GPIO.IN)
GPIO.setup (19, GPIO.IN)
GPIO.setup (18, GPIO.OUT)
GPIO.setup (17, GPIO.OUT)
f=open("sensor.txt","w")

def listToString(s): 
	str1 = "" 
	for ele in s: 
		str1 += ele   
	return str1 

def on_message(client, obj, msg):    
	mensaje=(msg.payload.decode("utf-8"))
	print(mensaje)
	if mensaje=="historial":
		print("Enviando Historial")
		f=open("sensor.txt","r")
		#lines = f.readlines()
		#for line in lines:
		#	mqttc.publish("wlady_hp66@hotmail.com/tema1", line)
		#	print(line)
		#f.close()
		lineash1 = []
		lineash2 = []
		lines = f.readlines()
		for line in lines:
			palabras = line.split(' ')
			for p in palabras:
				if p=="H1":
					 lineash1.append(line)
				elif p=="H2":
					lineash2.append(line)
		print(lineash1)
		print(lineash2)
		mqttc.publish("wlady_hp66@hotmail.com/tema1", listToString(lineash1))
		mqttc.publish("wlady_hp66@hotmail.com/tema1", listToString(lineash2))





mqttc = mqtt.Client() 
mqttc.on_message = on_message 
mqttc.username_pw_set("wlady_hp66@hotmail.com","DiegoWladimir")
mqttc.connect("maqiatto.com", 1883)
mqttc.subscribe("wlady_hp66@hotmail.com/tema2", 0)

rc=0
print("Inicio de conexion")
i = 0
while rc == 0:
	time.sleep(1)
	rc = mqttc.loop()
	Fechahora=datetime.datetime.now().strftime('%d-%m-%Y     %H:%M:%S    ')
	if GPIO.input(20):
		GPIO.output(18, True)
		men=("Sensor1 Activado")
		mqttc.publish("wlady_hp66@hotmail.com/tema1", "S1 activo")
		f=open("sensor.txt","a")
		f.write("H1 "+Fechahora  +men +"\n")
		f.close()
	else:
		GPIO.output(18, False)
		mqttc.publish("wlady_hp66@hotmail.com/tema1", "S1 desactivado")

	if GPIO.input(19):
		GPIO.output(17, True)
		men=("Sensor2 Activado")
		mqttc.publish("wlady_hp66@hotmail.com/tema1", "S2 activo")
		f=open("sensor.txt","a")
		f.write("H2 "+Fechahora  +men +"\n")
		f.close()
	else:
		GPIO.output(17, False)
		mqttc.publish("wlady_hp66@hotmail.com/tema1", "S2 desactivado")

