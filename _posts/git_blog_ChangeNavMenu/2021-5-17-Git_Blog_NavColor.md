---
layout: post
title:  "Change Git Blog Navigation Color"
date:   2021-05-17 00:00:00
author: RileyKim
categories: GitBlog
tags: GitBlog
cover:  "/assets/instacode.png"
comments: true
---



### Change Git Blog Navigation Color



기존의 블로그 네비 메뉴 색상이 마음에 들지 않아 회색(?)으로 변경하였습니다. 

<img width="601" alt="스크린샷 2021-07-02 오후 8 52 29" src="https://user-images.githubusercontent.com/24997255/124353353-eef54080-dc40-11eb-928b-c4b1b3243cb1.png">

아마 깃 블로그에 적용된 테블릿 소스코드 구조는 비슷할 꺼라 생각됩니다. 

네비 메뉴 수정 소스코드 위치는 __sass/base/_variables.scss 에서 

`dark-gray:#333을 추가.`

`$action-color:$dark-gray로 변경히여 색상 적용.`



<img width="452" alt="스크린샷 2021-07-03 오후 8 58 31" src="https://user-images.githubusercontent.com/24997255/124353430-7642b400-dc41-11eb-8751-2b115ddc0d37.png">



