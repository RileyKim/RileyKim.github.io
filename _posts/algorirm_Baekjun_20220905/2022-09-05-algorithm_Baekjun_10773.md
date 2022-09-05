---
ayout: post
title:  "[C언어] BaekJun Algorithm Problem 10773"
date:   2022-9-05 00:00:00
author: RileyKim
categories: Algorithm
tags: Algorithm
cover:  "/assets/instacode.png"
comments: true
---





**백준 10773  제로 c언어**

다른 문제에 비해 쉽게 풀었다..

stack을 더하는 과정에서 top만큼 더해야 하는데 입력받은 크기만큼 더하니 틀렸다..

스택의 위치를 잘 계산해서 코드를 짜야한다.



임의로 배열의 크기를 정하여 선언하지않고 동적할당 1차원 배열을 사용하여 문제를 풀었다. 

동적할당을 사용하니 메모리를 최적하하고, 배열의 크기를 수정할 필요가 없어 매우 효율적이라고 생각된다. 



<script src="https://gist.github.com/RileyKim/ba751ac4e522168402230bdd79a99a5a.js"></script>