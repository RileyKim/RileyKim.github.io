---
ayout: post
title:  "[C언어] BackJun Algorithm Problem 1331"
date:   2022-8-22 00:00:00
author: RileyKim
categories: Algorithm
tags: Algorithm
cover:  "/assets/instacode.png"
comments: true
---



## (C언어) 백준 알고리즘 문제 1340번 연도진행바



**2022.08.22**

백준 1340번 문제 연도진행바 푸는중...



문자열 비교 함수 strcmp

```c
int ret = strcmp(cal_mon[i], month); // 정상 출력
if(cal_mon[i] == month) // 동일하다고 판단못함...이유는 Null값의 위치, 그리고 선언된 배열의 크기로 인해 발생된다고 판단됨..

```



<script src="https://gist.github.com/RileyKim/b7f3dbe57ae71c4b14a5e3afe731b432.js"></script>