---
layout: post
title:  "connect RaspberryPI LTE"
date:   2019-07-10 00:00:00
author: RileyKim
categories: RaspberryPI
tags: RaspberryPI
cover:  "/assets/instacode.png"
---

# Raspberry-LTE(sixfab) 설치 및 사용



OS : Rasbian (raspberry3 B+)

LTE Module : sixfab raspberry LTE shield



sixfab 구입사이트 : <https://sixfab.com/product/raspberry-pi-4g-lte-shield-kit/>



### preparation

---------------------------------------

**라즈베리파이의 LTE통신을 사용하기 위해 Sixfab LTE모듈을 구매하였습니다.** 

통신사 대리점에서 Sixfab 모듈 등록이 가능하지만, 대리점 직원들은 처리할 줄 모르니 근처 고객센터로 방문하여 등록하는 것이 정신 건강에 이롭습니다.



**LTE모듈 등록에는 2가지 방법이 있는데 번호를 부여받거나, 그냥 번호 부여없이 등록할 수 있습니다. **

모듈의 고유 데이터 사용은 번호를 부여받아야지만 신청할 수 있습니다. 저는 함께쓰기(1대까지 무료)를 사용하였기 때문에 번호 부여가 필요없지만, 함께쓰기여도 모듈의 데이터 사용량이 정해져있기 때문에 혹시 몰라 번호를 부여받았습니다. 가격 차이는 없으니 그냥 번호 부여받는 걸 추천드립니다. 



참고 자료 : <https://sixfab.com/updated-tutorial-3-make-a-ppp-internet-connection-with-3g-4glte-shields-on-raspberry-pi/>

이 자료 그대로 하시면 안됩니다. 조금의 수정사항이 있습니다. 



#### SSH Enable

------------------

터미널을 열고 라즈베리파이 설정창에 접속합니다. 

```sudo rasp-config```



![raspberry-lte-18](https://user-images.githubusercontent.com/24997255/60785630-97758480-a18e-11e9-8617-26d14ba79c5a.PNG)

`Interfaceing Options`에서 `SSH enable` 합니다. 



패키지 설치 전, `sudo apt-get update && sudo apt-get upgrade`를 해주는 습관을 기릅시다. 



#### Install ppp Package

----------------------------------

`sudo apt-get install -y --no-install-recommends ppp`

PPP 패키지 설치 명령어입니다.



![raspberry-lte-7](https://user-images.githubusercontent.com/24997255/60786458-a9a4f200-a191-11e9-88d5-c05f44749df1.PNG)



`sudo reboot`

재시동!



#### acting PPP

---------------------------------------------

ppp는 ppp0이라는 네트워크 인터페이스를 통해서 동작된다. 

그렇게 때문에 `pppd-creator.sh`파일을 통해서 ppp를 동작시켜야한다. 



pppd-creator.sh파일 

```bash
#!/bin/bash


echo "creating directories"
mkdir -p /etc/chatscripts
mkdir -p /etc/ppp/peers

echo "creating script file : /etc/chatscripts/quectel-chat-connect"
echo "
ABORT \"BUSY\"
ABORT \"NO CARRIER\"
ABORT \"NO DIALTONE\"
ABORT \"ERROR\"
ABORT \"NO ANSWER\"
TIMEOUT 30
\"\" AT
OK ATE0
OK ATI;+CSUB;+CSQ;+COPS?;+CGREG?;&D2
# Insert the APN provided by your network operator, default apn is $1
OK AT+CGDCONT=1,\"IP\",\"\\T\",,0,0
OK ATD*99#
CONNECT" > /etc/chatscripts/quectel-chat-connect


echo "creating script file : /etc/chatscripts/quectel-chat-disconnect"
echo "
ABORT \"ERROR\"
ABORT \"NO DIALTONE\"
SAY \"\nSending break to the modem\n\"
""  +++
""  +++
""  +++
SAY \"\nGoodbay\n\"" > /etc/chatscripts/quectel-chat-disconnect


echo "creating script file : /etc/ppp/peers/gprs"
echo "
/dev/$2 115200
# The chat script, customize your APN in this file
connect 'chat -s -v -f /etc/chatscripts/quectel-chat-connect -T $1'
# The close script
disconnect 'chat -s -v -f /etc/chatscripts/quectel-chat-disconnect'
# Hide password in debug messages
hide-password
# The phone is not required to authenticate
noauth
# Debug info from pppd
debug
# If you want to use the HSDPA link as your gateway
defaultroute
# pppd must not propose any IP address to the peer
noipdefault
# No ppp compression
novj
novjccomp
noccp
ipcp-accept-local
ipcp-accept-remote
local
# For sanity, keep a lock on the serial line
lock
modem
dump
nodetach
# Hardware flow control
nocrtscts
remotename 3gppp
ipparam 3gppp
ipcp-max-failure 30
# Ask the peer for up to 2 DNS server addresses
```



`pppd-creator.sh`을 실행시킬 때 2가지 요소가 필요하다. 

1. 통신사에서 제공받는 `APN`을 명령어에 기입해야한다. 
2. 인터넷에 접속하기 위한 USB포트는 `ttyUSB3`이다



`pppd-creator.sh` 을 실행시키기 위한 명령어는 다음과 같다. 

`sudo bash ppp-creator.sh (APN) ttyUSB3`



---------------------------

**통신사별 APN**

sk :  lte-internet.sktelecom.com

kt APN : lte.ktfwing.com

LG U+ :  internet.lguplus.co.kr

본인이 해당하는 통신사 APN를 기입하여 실행시킵니다. 

------------------------------



저는 SK텔레콤을 사용하였기 때문에 명령어는 다음과 같습니다.

![raspberry-lte-13](https://user-images.githubusercontent.com/24997255/60787574-369d7a80-a195-11e9-9eba-d4c28a6e2d15.PNG)





LTE모듈을 실행합니다. 

`sudo pppd call gprs&`



실행 후 `ifconfig ppp0`으로 정상 작동하는지 확인합니다. 

![raspberry-lte-15](https://user-images.githubusercontent.com/24997255/60787747-c3483880-a195-11e9-89ef-ef7db0c29d32.PNG)



ip가 잡히더라도 정상적으로 실행이 되지않는다면, ppp0을 default route에 추가합니다. 

`sudo route add default ppp0`





#### Making it work on each boot

-----------------------------------

`reboot` 할때마다 `sudo ppp call gprs&` , `sudo route add default ppp0`을 해줘야하는 불편함이 있습니다. 

그래서 저는 리눅스 부팅시마다 실행되는 파일 (rc.local)에 ppp0 실행 명령어를 기입하였습니다. 



`sudo vi /etc/rc.local`를 통해 소스를 편집합니다. 



```bash
if [ "$_IP" ]; then
  printf "My IP address is %s\n" "$_IP"
fi

(
sleep 10
sudo pppd call gprs&
sleep 5
sudo route add default ppp0
) > /tmp/rc.log 2>&1


exit 0
```



