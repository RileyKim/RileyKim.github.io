---
layout: post
title:  "Declare Atmega port"
date:   2020-05-12 00:00:00
author: RileyKim
categories: Atmega
tags: Atmega
cover:  "/assets/instacode.png"
comments: true
---

# Define Atmega128 PORT Register



구글을 검색해보면 포트 레지스터를 선언하는 당연한 방법이 있다. 

하지만 대부분 일일히 타이핑해야하거나, 허접한 선언들이 많이 있다. 



개인적으로 함수는 심플하고, 효용성이 높고, 다른 사람이 봤을 때 쉽게 이해할 수 있어야한다고 생각한다. 

환변학 코딩은 없으니 최대한 이와 같도록 노력한다. 



port 선언에는 다양한 방법이 있다. 

<img width="963" alt="스크린샷 2020-05-12 오후 11 01 21" src="https://user-images.githubusercontent.com/24997255/81706880-3bb11180-94ab-11ea-828c-b2b6fd52691e.png">

가장 기본적인 방법은

<script src="https://gist.github.com/RileyKim/57707a5b278b5969f61fd0c0005db980.js"></script>



**이렇게 한 비트씩 밀어내서 세팅하는 이유는 코드가 복잡해지면 값에 영향을 줄 수 있기 때문이다.** 



두번째 방법

<script src="https://gist.github.com/RileyKim/2a5d1066e2e87367fd6b67fad724cfeb.js"></script>



세번째 방법

<script src="https://gist.github.com/RileyKim/bfa8f3d9ab772cfe4460626d2af2fd68.js"></script>



참고해서 PORT a,b,c 등등 잘 확인해서 사용하길 바랍니다. :)



