---
layout: post
title:  "[C++언어] Programmers Algorithm(HASH) Level2"
date:   2024-02-07 00:00:00
author: RileyKim
categories: Algorithm
tags: Algorithm
cover:  "/assets/instacode.png"
comments: true
---



## 전화번호 목록

**문제설명**

전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.

구조대 : 119
박준영 : 97 674 223
지영석 : 11 9552 4421
전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때, 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.

제한 사항
phone_book의 길이는 1 이상 1,000,000 이하입니다.
각 전화번호의 길이는 1 이상 20 이하입니다.
같은 전화번호가 중복해서 들어있지 않습니다.



**1) Sorting함수를 이용한 방법**

<script src="https://gist.github.com/RileyKim/351eb3803caa00e87bae99333c012e0f.js"></script>



**2) Hash 알고리즘을 이용한 방법**

<script src="https://gist.github.com/RileyKim/b4f21e42a1a85a6ebcd54ec5efd43f02.js"></script>