---
layout: post
title:  "Atemga128 UART"
date:   2020-09-15 00:00:00
author: RileyKim
categories: Atmel
tags: Atmel
cover:  "/assets/instacode.png"
comments: true
---


# Atmega128 UART 



항상 데이터시트의 중요성을 강조하고싶다. 

데이터시트는 기본 중에 기본이다. 

단지, 많은 요약어와 설명이 있기 때문에 보기 불편할 뿐이다. 모든 것은 데이터시트 안에 답이 있다. 





uart를 사용하기 위해선 mcu의 uart핀을 파악하고 register 설정을 할 줄 알아야한다. 



### 먼저 atmega128의 PinMap를 살펴보자.

![atmega128_uart_1](https://user-images.githubusercontent.com/24997255/93166448-724cb080-f759-11ea-9c86-62eb1a3d2269.PNG)



PORTE의 bit 0,1과, PORTD의 bit 2,3이 rx,tx 지원 가능한 것을 알 수 있다. 



### uart register를 살펴보자. 

시스템 클록과 원하는 baud rate를 이용하여 USART Baud Rate Register(UBRR)을 계산한다.

UBRR0은 12비트 레지스터이기 때문에 나누어서 넣어야 한다.

1. UDRn : 데이터 버퍼 기능을 수행하는 8bit 레지스터
2. UCSRnA :  송수신 데이터가 남아있는 지 확인하는 레지스터
3. UCSRnB : rx, tx 송수신 허용 레지스터
4. UCSRnC  : Async, parity, stop 등을 설정하는 레지스터
5. UBRRn  : baudrate 설정 레지스터

 5가지 레지스터를 다뤄서 uart를 사용한다. 



n은 번호이다. 

예를 들어 n에 1이 들어간 UART 레지스터는 RXD1, TXD1과 관련있다.  



##### UDRn

![atmega128_uart_3_UDRn](https://user-images.githubusercontent.com/24997255/93170135-8eece680-f761-11ea-83c5-0b95a15a3c3c.PNG)

##### UCSRnA

![atmega128_uart_4_UCSRnA](https://user-images.githubusercontent.com/24997255/93170396-23efdf80-f762-11ea-96c0-df7ef1b8c17f.PNG)

bit7- RXCn 

RXCn = 1 : UDRn의 수신 버퍼에 아직 안 읽은 데이터가 존재하는 상태

RXCn = 0 : UDRn의 수신 버퍼를 읽어서 비워져 있는 상태 



bit5 - UDREn

UDREn = 1 : 송신 버퍼가 비어있어서 새로운 송신 데이터를 받을 준비가 된 상태

##### UCSRnB

![atmega128_uart_5_UCSRnB](https://user-images.githubusercontent.com/24997255/93170448-3833dc80-f762-11ea-912f-345dc2e2a50d.PNG)

##### UCSRnC

![atmega128_uart_6_UCSRnC](https://user-images.githubusercontent.com/24997255/93171060-5bab5700-f763-11ea-905a-824d84d8de8f.PNG)

##### UBRRnL and UBRRnH 

![atmega128_uart_6_UBRRnL_UBRRnH](https://user-images.githubusercontent.com/24997255/93170498-513c8d80-f762-11ea-83aa-56c4889c71d3.PNG)



### 소스 작성시 설정 순서

1. ##### UBRR을 통하여 baudrate설정 

   Baudrate가 9600일 경우, (14745600/(16*9600)) -1 = 95
   95 = 0x5f이다.

   ````
   #define CPUCLK 14745600UL
   
   ///baudrate 9600은 하위 8비트 안에 들어가므로 상위 비트는 비워준다. 
   //UBRR0L = (uint8_t) ((F_CPU / (16*baudrate))-1);
   UBRR1L = 0x5f;	// baudrate 9600
   UBRR1H = (uint8_t) (UBRR1L >> 8); 
   ````

2. ##### UCSRA

    default 설정

3. ##### UCSRB

   ````
   // tx 
   UCSR0B = (1<<TXEN0);
   ````

4. ##### UCSRC

   default 설정

5. ##### UDR0에서 데이터 설정(tx)

````
//The UDREn flag indicates if the transmit buffer (UDRn) is ready to receive new data. If UDREn is
//one, the buffer is empty, and therefore ready to be written.

// 송신 버퍼가 비어있을 떄 새로운 송신 데이터를 받을 준비. udre0 = 0일 때 데이터를 받는다.
#if 1
void TX_ch_rs232(uint8_t data){
	 while(!(UCSR0A&(1<<UDRE0))); 
	 {
		 UDR0 = data;
	 }
}
#endif
````





##### 참고 코드



<script src="https://gist.github.com/RileyKim/6343854b114e25aac5f3526587a8c337.js"></script>

<script src="https://gist.github.com/RileyKim/c302269966c3da102a8e1fae795c3660.js"></script>