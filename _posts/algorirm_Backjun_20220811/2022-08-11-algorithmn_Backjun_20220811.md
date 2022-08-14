---
layout: post
title:  "[C언어] BackJun Algorithm Problem 1331"
date:   2022-8-11 00:00:00
author: RileyKim
categories: Algorithm
tags: Algorithm
cover:  "/assets/instacode.png"
comments: true
---

## Codeup 4040 펜션 (C언어_그리디 알고리즘 )







## (C언어) 백준 알고리즘 문제 1331번 나이트투어 





아직 푸는 중....


**2022.08.15
왜 두번쨰 문자 입력부터 쓰레기 값(?)이 포함되어 들어오는지 모르겠음...
이유 아시는 분은 댓글로 좀 알려주세요..ㅠㅠ
아무래도 다른 방법을 찾아봐야할 것 같음...


```c
#include <stdio.h>
#include <string.h>
#include <stdbool.h>
int main()
{
    bool flag = true;
    bool panel[6][6];                
    memset(panel, false, sizeof(panel));
    
    char start[2];
    char now[2];
    char prev[2];
    
    printf("start\n");
    scanf("%c%c" ,&start[0],&start[1]);
    
    
    start[0] = start[0] -'@';
    start[1] = start[1] -'0';
    
    prev[0] = start[0];
    prev[1] = start[1];
    
    printf("%d\n",start[0]);
    printf("%d\n",start[1]);
    
    while(true){
        scanf("%c%c", &now[0], &now[1]);
        now[0] -= '@';
        now[1] -= '0';
        if( panel[now[0]][now[1]] == false &&(abs(prev[0]-now[0]) == 2 && abs(prev[1]-now[1] == 1)) || (abs(prev[0]-now[0]) == 1 && abs(prev[1]-now[1] == 2))){
            panel[now[0]][now[1]] = true;
            prev[0] = now[0];
            prev[1] = now[1];
            
        }else{
            flag = false;
            
        }
    }
    
    if(flag){
        printf("Valid");
    }else{
        printf("Invalid");
    }
    
    
    
}
```

