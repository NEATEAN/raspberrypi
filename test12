import sys
import time
import Adafruit_DHT
import spidev

sensor = Adafruit_DHT.DHT11
pin=2

spi=spidev.SpiDev()
spi.open(0,0)

def read_spi(adcchannel):
    if adcchannel >7 or adcchannel<0:
      return -1
    buff=spi.xfer2([1,(8+adcchannel)<<4,0])
    adcValue=((buff[1]&3)<<8)+buff[2]
    return adcValue

adcchannel=0

conn=pymysql.connect(host="220.149.235.54", user="dku18", passwd="1234", db="test")

try : 
  with conn.cursor() as cur : 
    sql="insert into gain (date_pre, date_suf, date, CO, Temperature, Humidity, Place) values( %d, %d, %s, %d, %d, %d)"
    while True:
      humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
      adcvalue=read_spi(adcchannel)
      if humidity is not None and temperature is not None:      
          print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity)) 
          print('CO = %0.1f'%(adcvalue))
          cur.execute(sql, (time.strftime("%Y%m%d", time.localtime()),time.strftime("%H%M%S", time.localtime(), time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),adcvalue,temperature, humidity, 1)
      conn.commit()
      else : 
          print("Failed to get reading.")
      time.sleep(10)
except KeyboardInterrupt:
  exit()
finally:
conn.close()
