---
layout: post
title:  "Installing a Raspbian in RaspberryPI"
date:   2019-03-04 00:00:00
author: RileyKim
categories: RaspberryPI
tags: RaspberryPI
cover:  "/assets/instacode.png"
comments: true
---

# 라즈베리파이3 B+ 라즈비안 설치



Raspberry3 B+ 에 라즈비안을 설치하는 방법을 알아보겠습니다.

저의 개발 환경은 Mac입니다. 



준비물 : 라즈베리파이, Micro sd카드, 어댑터(2.5A이상)



1. 라즈비안 다운로드

   [RaspberryPi HomePage]: https://www.raspberrypi.org/downloads/	"RaspberryPi HomePage"

   ![스크린샷 2019-03-04 오후 8 38 29](https://user-images.githubusercontent.com/24997255/54749115-f1216580-4c16-11e9-8b95-d3f07696095f.png)



2. sd카드를 맥북에 연결하여 다운받은 Raspbian 이미지 파일을 sd카드에 설치합니다.

   터미널을 실행한 후 **diskutil list**를 실행하면 아래와 같은 목록을 확인하게됩니다.

   <img width="569" alt="스크린샷 2019-03-04 오후 9 00 02" src="https://user-images.githubusercontent.com/24997255/54749147-0ac2ad00-4c17-11e9-85e2-66c74789fe09.png">

   ​	

   	/dev/disk2가 sd카드인 것을 확인할 수 있습니다.



3. sd카드의 마운트를 해제합니다.

   **diskutil unmountDisk /dev/disk2**



4. sd카드에 다운받은 이미지 파일을 설치합니다. 

   **sudo dd bs=1M if=이미지 파일명 of=/dev/disk2 conv=sync**



5. dd 실행이 끝난 후 sd카드를 분리합니다. 

   **sudo diskutil eject /dev/disk2**



6. 분리한 sd카드를 라즈베리파이와 결합한 후 전원을 연결하면 자동적으로 라즈비안이 설치되어 실행됩니다. 

   실행이 완료되면 라즈비안에서 지원해주는 소프트웨어를 꼭 업데이트하세요.