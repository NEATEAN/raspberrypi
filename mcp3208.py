#git clone http://github.com/doceme/py-spidev
import spidev
import time

spi=spidev.SpiDev()
spi.open(0,0)

def read_spi(adcchannel):
    if adcchannel >7 or adcchannel<0:
      return -1
    buff=spi.xfer2([1,(8+adcchannel)<<4,0])
    adcValue=((buff[1]&3)<<8)+buff[2]
    return adcValue
#def spi_close(self):
#    self.spi.close()

adcchannel=0

while True:
  adcvalue=read_spi(adcchannel)
  print("CO : {}".format(adcvalue))

  time.sleep(1)

