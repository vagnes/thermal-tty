import board
import digitalio
import busio

# Test digital input
pin = digitalio.DigitalInOut(board.D4)
print("Digital IO is working.")

# Test I2C device
i2c = busio.I2C(board.SCL, board.SDA)
print("I2C is working.")

# Test SPI device
spi = busio.SPI(board.SCLK, board.MOSI, board.MISO)
print("SPI is working.")

print("--completed--")
