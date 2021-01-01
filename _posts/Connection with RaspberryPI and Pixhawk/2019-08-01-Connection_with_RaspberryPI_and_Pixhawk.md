---
layout: post
title:  "Connection with Raspberry via MavLink"
date:   2019-08-01 00:00:00
author: RileyKim
categories: Drone
tags: Drone
cover:  "/assets/instacode.png"
comments: true
---
# Connection with RaspberryPI and Pixhawk via MavLink



**MaVLink는 라즈베리파이에서 명령어를 통해 Pixhawk의 설정 값을 변경하거나 명령하기 위한 프로그램입니다. 라즈베리파이에 LTE모듈을 결합하여 원격으로 Pixhawk에 명령할 수 있습니다.**

[connection with Raspberry-LTE](<https://rileykim.github.io/raspberrypi/2019/07/10/raspberry_lte_sixfab.html>)



### 개발 환경 및 설정

---------------------------------------

개발 환경 : RaspberryPI3 B+(Ubuntu) , Pixhawk

준비 : RaspberryPI, Pixhawk, Monitor, Keyboard, Mouse, Internet....





![Connecting the Pixhawk and RPi-1](https://user-images.githubusercontent.com/24997255/62024398-c3c17580-b20f-11e9-97ad-21cc598f30ec.png)



그림과 같이 pixhawk terminal에 대칭하는 RaspberryPI pin에 연결합니다. 

**(Rx는 Tx, Tx는 Rx에 연결하여야 합니다.)**



![Connecting the Pixhawk and RPi-2](https://user-images.githubusercontent.com/24997255/62025050-efddf600-b211-11e9-9198-2920fea70980.png)

라즈베리파이 터미널을 열고 항상 설치 전 `sudo apt-get update`를 해주는 습관을 기릅시다. 



### MAVLink 설치

----------------------------



![Connecting the Pixhawk and RPi-3](https://user-images.githubusercontent.com/24997255/62025374-f1f48480-b212-11e9-9eae-4734d145549f.png)

`sudo apt-get install screen python-wxgtk2.8 python-matplotlib python-opencv python-pip python-numpy python-dev libxml2-dev libxslt-dev python-lxml` 



![Connecting the Pixhawk and RPi-4](https://user-images.githubusercontent.com/24997255/62025747-09803d00-b214-11e9-94db-ef63e7834359.png)

설치중....



![Connecting the Pixhawk and RPi-5](https://user-images.githubusercontent.com/24997255/62025780-1d2ba380-b214-11e9-9b9f-2107d5bc36c0.png)

`sudo pip install future`



![Connecting the Pixhawk and RPi-6](https://user-images.githubusercontent.com/24997255/62025970-9fb46300-b214-11e9-8af4-c150c9e5a9da.png)

설치중....



![Connecting the Pixhawk and RPi-7](https://user-images.githubusercontent.com/24997255/62026005-b65aba00-b214-11e9-8400-89c9874ce34c.png)

`sudo pip install pymavlink`



![Connecting the Pixhawk and RPi-8](https://user-images.githubusercontent.com/24997255/62026229-65979100-b215-11e9-9fdd-85cafe57362a.png)

설치 설치!



![Connecting the Pixhawk and RPi-9](https://user-images.githubusercontent.com/24997255/62026336-ad1e1d00-b215-11e9-9758-8d28523f7861.png)

`sudo pip install mavproxy`



![Connecting the Pixhawk and RPi-10](https://user-images.githubusercontent.com/24997255/62026360-c3c47400-b215-11e9-805d-a320649039c9.png)

설치 끝ㅎ



### 실행

------------------------

```
sudo -s
mavproxy.py --master=/dev/ttyS0 --baudrate 921600 --aircraft MyCopter
```



**확인 사항**

baudrate를 연결된 pixhawk terminal의 baudrate 설정 값과 동일한 값을 입력해주어야 합니다. 

MissionPlanner에서 설정 값을 확인 또는 변경이 가능합니다.



### 오류 시 해결 방안

-------------------------

![Connecting the Pixhawk and RPi-11](https://user-images.githubusercontent.com/24997255/62026382-d50d8080-b215-11e9-811a-fac810b56592.png)

`sudo nano /boot/config.txt`파일을 수정합니다.



![Connecting the Pixhawk and RPi-12](https://user-images.githubusercontent.com/24997255/62030058-266e3d80-b21f-11e9-8c55-0b9080853002.png)

다음과 같이 내용을 수정한 후 실행합니다. (RaspberryPI3 B+)

**`RaspberryPI3`와 `RaspberryPI3 B+`와 설정 값이 다르니 확인하시고 수정해주세요!**



Note

On newer versions of Raspberry Pi 3 the uart serial connection may be disable by default. In order to enable serial connection on the Raspberry Pi edit **/boot/config.txt** and `set enable_uart=1`. the build-in serial port is `/dev/ttyS0`.

For Raspberry Pi 3B+, the bluetooth module occupied uart serial port. To disable the bluetooth, add `dtoverlay=pi3-disable-bt` and `enable_uart=1` at the end of **/boot/config.txt**.



### 참고자료

------------------

 [ArduPilot_raspberry-pi-via-mavlink](http://ardupilot.org/dev/docs/raspberry-pi-via-mavlink.html)



