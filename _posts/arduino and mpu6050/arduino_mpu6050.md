## mpu6050 dmp (feat. arduino iot 33)



먼저 arduino iot 33 스펙을 살펴보자.

<https://store.arduino.cc/usa/nano-33-iot>

clock speed가 48MHz라 arduino nano보다 훨씬 빠르다.

해당 주소로 들어가면, DataSheet, TechSpecs 등 정보를 확인할 수 있다. 



**Arduino 33 iot Tutorial**

arduino 33 iot의 main controller는 SAMD21 Cortex라 arduino IDE에서 프로그래밍을 하기 위해선

해당 칩에 대한 드라이버를 설치해야한다. 

참고: <https://www.arduino.cc/en/Guide/NANO33IoT>



**mpu6050**을 사용해보자



먼저 arduino와 mpu6050은 I2C통신을 합니다. 

I2C통신은 SCL, SDA 을 사용합니다. 



**참고사이트**

<https://github.com/jrowberg/i2cdevlib>

<https://github.com/jrowberg/i2cdevlib>

 