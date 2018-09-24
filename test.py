import sys
import os
import glob
import time
 
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
 
base_dir = '/sys/bus/w1/devices/'
path = "/sys/bus/w1/devices/"
dirs=os.listdir(path)
sensorList = []








def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines
 
def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c, temp_f

for file in dirs:
	if file.startswith("28"):
		sensorList.append(file)
		
print(len(sensorList))

while True:
	for sen in sensorList:
		global device_file
		device_file=base_dir+sen+ '/w1_slave'
		print(read_temp())	
	time.sleep(5)
