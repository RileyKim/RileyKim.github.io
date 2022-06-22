---
layout: post
title:  "RESONANT Circuits 공진회로"
date:   2022-6-22 00:00:00
author: RileyKim
categories: RF Design
tags: RF Design
cover:  "/assets/instacode.png"
comments: true
---





# 2장 공진회로



병렬 공진 회로와 그 특성을 알아보고 부하-Q의 개념과 부하-Q가 소스 임피던스가 부하 임피던스와 어떤 관계를 갖고 있나를 다룬다.



##### 2-1 정의

공진회로는 선택된 주파수나 주파수 대역은 그대로 통과시키는 반면 선택되지 않은 즉, 선택된 주파수나 주파수 대역의 위와 아래 주파수는 감쇠시켜 통과지 않도록 한다. 



![RF](https://user-images.githubusercontent.com/24997255/174927938-f347c011-3d95-40a5-9955-a2d3d08c5ebc.JPG)

​                                                                                                    **이상적인 공진 회로에 의한 통과대역**



![RF](https://user-images.githubusercontent.com/24997255/174928156-161f88f1-0aa4-4783-85fd-e7e3e8f3284f.JPG)

​                                                                                                              **실제 필터 응답**



1. 대역폭(bandwidth) : 대역폭은 보통 진폭 특성이 통과 대역 특성의 3db 아래인 곳에서 고주파f2, 저주파f1의 차이, f2-f1으로 정의되며 반전력 대역폭이라고 한다. 

2. Q : 대역폭에 대한 공진 회로의 중심 주파수의 비로 정의된다. 

   ```Q=fc/(f1-f2)```

   여기서 사용되는 Q는 소자의 관한 Q와 다르다. 

3. 세이프 팩터(shape factor) : 감쇠의 정도는 나타내는 수치
4. 리플 : 공진회로에서 통과 대역의 평평한 정도를 dB단위로 나타내는 수치



##### 2-2 공진(무손실 소자)



![RF](https://user-images.githubusercontent.com/24997255/174930073-514726b3-38bd-42af-8bc8-bf303e60b8b7.JPG)



전압분배법칙에 의해서 
$$
Vout = \frac{Zp}{(Rs+Zp)}(Vin)
$$
임피던스 Zp는 주파수에 따라서 값이 변한다.



![RF](https://user-images.githubusercontent.com/24997255/174940332-887b75cf-d270-44a0-b77f-7297095c5d7b.JPG)

간단한  low-pass filter에 적용시켜보면, 


$$
\frac{Vout}{Vin}=20log\frac{Xc}{Rs+Xc}\\
Xc = \frac{1}{jwC}
$$


--------------------------------------------------



![RF](https://user-images.githubusercontent.com/24997255/174941315-82fe79e1-153a-4d98-aaea-ef023bf3bda8.JPG)

간단한 High-pass filter에 적용시켜보면
$$
\frac{Vout}{Vin}=20log\frac{XL}{Rs+XL}\\
XL = {jwL}
$$




---------------------



![RF](https://user-images.githubusercontent.com/24997255/174941725-1c590615-d9d2-4013-9418-10ef29cdc7a0.JPG)

2개의 능동소자가 있는 공진 회로에 적용하면, 

![RF](https://user-images.githubusercontent.com/24997255/174941828-bfdcc643-d918-4cd4-a2a3-b6fb564bfb33.JPG)

이 풀이를 정리하면, 

![RF](https://user-images.githubusercontent.com/24997255/174941911-54d57958-41d0-467e-8c0e-e1790cdedd75.JPG)

값이 도출된다. 



##### 2-3 선택도 Q (Loaded Q)

공진 회로에서의 Q는 중심주파수에서 3dB이내의 주파수의 비율을 나타낸다. 

공진회로에서 선택도 Q를 결정하는 주요 요소가 3가지 있다. 

1. 소스 저항 (Rs)

2. 부하 저항 (RL)

3. 1장에서 배운 품질계수 Q

![RF](https://user-images.githubusercontent.com/24997255/174942455-c0173ee5-02d7-4a86-a799-85a63e938e45.JPG)

선택도 Q가 높으면 낮은 선택도를 가지는 그래프에 비해 중심 주파수에 집중할 수 있고 감쇠 기울기가 크다. 



##### 2-4 선택도 Q에 대한 Rs, RL

선택도 Q는 다음의 공식으로 정의될 수 있다. 

![RF](https://user-images.githubusercontent.com/24997255/174943249-c948be21-6201-498f-abbd-129df739a7ff.JPG)



