import odroid_wiringpi as wiringpi

wiringpi.wiringPiSetup() 
wiringpi.wiringPiSetupSys() 
wiringpi.wiringPiSetupGpio()

wiringpi.mcp23017Setup(1, "/dev/i2c-1")