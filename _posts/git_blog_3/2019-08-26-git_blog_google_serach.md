---
layout: post
title:  "GitBlog is searched at google"
date:   2019-08-26 00:00:00
author: RileyKim
categories: GitBlog
tags: GitBlog
cover:  "/assets/instacode.png"
comments: true
---

# git Blog 구글 검색 노출방법



GithubBlog하시는 분들은 다들 포스팅을 하실텐데요. 

포스팅한 글을 구글, 네이버, 다음에서 검색 노출이 되는 방법에 대해 알아보도록 하겠습니다. 



## 요약

1. 구글 웹마스터 도구 접속
2. 깃블로그 등록 및 인증
3. sitemap.xml파일 생성 및 제출
4. robot.txt파일 생성
5. 구글 검색 확인
6. 주의사항



#### 1. [구글 웹마스터 도구](<https://search.google.com/search-console/about?hl=ko>) 접속

![git_blog_serach_1](https://user-images.githubusercontent.com/24997255/64095388-a1d08b00-cd99-11e9-95b9-9d6bf1321f14.PNG)



#### 2. 깃블로그 등록

![git_blog_serach_1](https://user-images.githubusercontent.com/24997255/64092896-6af67700-cd91-11e9-99c8-8f33bd8b2c35.PNG)



#### 3. 깃블로그 인증

구글 웹마스터에서 제공하는 html파일을 다운받아, 깃블로그 최상단 디렉토리에 저장합니다.  
git push를 진행하여 소유권 확인을 인증합니다. 예시로 www.naver.com으로 되어있습니다. 

![git_blog_serach_2](https://user-images.githubusercontent.com/24997255/64093453-5fa44b00-cd93-11e9-8c09-27dc414004be.PNG)



​![git_blog_serach_3](https://user-images.githubusercontent.com/24997255/64093772-94fd6880-cd94-11e9-91ee-ac7131cd02b3.PNG)



#### 4. sitemap.xml파일 생성

---------------------
**Sitemap 이란?**

1. 웹 크롤링 로봇이 이용할 수 있는 웹사이트의 접근 가능한 페이지의 목록
2. 웹사이트의 웹페이지를 계층별로 구분지어 웹사이트의 전체 구조를 보여주며, 검색엔진의 크롤링 로봇들이 크롤링 작업에 유용하게 사용할 수 있다.
3. sitemap.xml 파일을 사용하면 사이트 및 콘텐츠 구조를 Google 및 기타 검색엔진에 손쉽게 제출할 수 있다.
4. 검색엔진에 크롤링해야하는 URL을 알려줌으로써 색인을 생성하는 방법과 색인을 생성하는 방법을 제어한다.

   

sitemap.xml파일을 작성하여 깃블로그 최상단 디렉토리에 저장합니다.  

git push를 진행합니다. 


<script src="https://gist.github.com/RileyKim/05be5d258903781b83f42dd4e144ae68.js"></script>



**깃블로그주소/sitemap.xml**에 접속하여 다음과 같은 화면이 나오면 정상적으로 push가 완료된 것입니다.

![git_blog_serach_4](https://user-images.githubusercontent.com/24997255/64094281-291bff80-cd96-11e9-94c7-8bce95b52da2.PNG)



#### 5. 구글 웹마스터 sitemap.xml 제출

![git_blog_serach_6](https://user-images.githubusercontent.com/24997255/64095096-ced06e00-cd98-11e9-8b45-f75a4399d487.PNG)



#### 6. robot.txt파일 생성

-------------------------
**robots.txt 이란?**

1. 검색엔진의 웹 크롤러가 방문할 때 참고하는 정책을 명시
2. robots.txt 파일에 sitemap.xml 위치를 등록해두면 검색엔진의 크롤러들이 홈페이지를 크롤링하는데 도움을 준다.

   

robot.txt파일을 작성하여 깃블로그 최상단 디렉토리에 저장합니다. 
git push를 진행합니다. 


<script src="https://gist.github.com/RileyKim/aa649d8b3802c6f2b78767153fdb2455.js"></script>



#### 7. 구글 검색 확인

모든 과정이 완료된 후 깃블로그가 구글 검색엔진에 적용되기 위해서 몇일간의 시간이 필요합니다. 
바로 검색되지 않을테니 몇일 간의 기간을 준 후 검색해보시는 걸 추천드립니다. 

![git_blog_serach_7](https://user-images.githubusercontent.com/24997255/64095935-3e475d00-cd9b-11e9-8d16-b1933b86f413.PNG)



#### 8. 주의사항

title명으로 검색됩니다. 
한글로 검색되길 원하시는 분은 title명을 한글로 작성해주시면 됩니다!

![git_blog_serach_8](https://user-images.githubusercontent.com/24997255/64095992-620aa300-cd9b-11e9-9ea9-ce6896fbf30a.PNG)

