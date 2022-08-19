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



## (C언어) 백준 알고리즘 문제 1331번 나이트투어 





아직 푸는 중....



**2022.08.15**
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





**업데이트 2022.08.18**

일단 문제는 풀었다..

이해 안가는 부분이 있어서 몇 일동안 계속 헤맸다...

결론은 아직도 이해가 안간다는 것이다...



밑에 2코드를 보자..



```c
#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <stdlib.h>
int main(void)
{
    bool flag = true;
    

    char xpos[36] = {};
    int ypos[36] = {};
    


    for(int i =0; i < 36; i++){
        
        //문제의 코드, 왜 스페이스가 있고 없고에 정답, 오답이 되는지 이해가 아직도 되지않는다
        scanf("%c%1d", &xpos[i], &ypos[i]);

        if(i!=0){
            //i=35가 되기전 정상적으로 이동하는지 확인한다.
            if((xpos[i-1]+2) == xpos[i] || (xpos[i-1]-2) == xpos[i]){
                if((ypos[i-1]+1) == ypos[i] || (ypos[i-1]-1) == ypos[i]){
                    flag = true;
                }
                else{
                    flag = false;
                    break;
                }
            }else if((xpos[i-1]+1) == xpos[i] || (xpos[i-1]-1) == xpos[i]){
                if((ypos[i-1]+2) == ypos[i] || (ypos[i-1]-2) == ypos[i]){
                    flag = true;
                }
                else{
                    flag = false;
                    break;
                }
            }else{
                flag = false;
                break;
            }
        }
         //마지막 횟차(i ==35) 에 초기값으로 갈 수 있는지 없는지 확인한다.
        if(i == 35){
            if((xpos[i]+2) == xpos[0] || (xpos[i]-2) == xpos[0]){
                if((ypos[i]+1) == ypos[0] || (ypos[i]-1) == ypos[0]){
                    flag = true;
                }
                else{
                    flag = false;
                    break;
                }
            }else if((xpos[i]+1) == xpos[0] || (xpos[i]-1) == xpos[0]){
                if((ypos[i]+2) == ypos[0] || (ypos[i]-2) == ypos[0]){
                    flag = true;
                }
                else{
                    flag = false;
                    break;
                }
            }else{
                flag = false;
                
            }
        }
        //이전에 입력된 값이 들어오는 지 for문을 통해 확인한다
        for(int j=0; j<i; j++){
    	if(xpos[j]==xpos[i] && ypos[j]==ypos[i]){
    		flag = false;
    		break;
		}
	  }
	  if(!flag)
	  	break;
    }
    
    if(flag){
        printf("Valid");
    }else{
        printf("Invalid");
    }
    
    
    
}
```



```c
#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <stdlib.h>
int main(void)
{
    bool flag = true;
    

    char xpos[36] = {};
    int ypos[36] = {};
    


    for(int i =0; i < 36; i++){
        
        //문제의 코드, 왜 스페이스가 있고 없고에 정답, 오답이 되는지 이해가 아직도 되지않는다
        scanf(" %c%1d", &xpos[i], &ypos[i]);

        if(i!=0){
            //i=35가 되기전 정상적으로 이동하는지 확인한다.
            if((xpos[i-1]+2) == xpos[i] || (xpos[i-1]-2) == xpos[i]){
                if((ypos[i-1]+1) == ypos[i] || (ypos[i-1]-1) == ypos[i]){
                    flag = true;
                }
                else{
                    flag = false;
                    break;
                }
            }else if((xpos[i-1]+1) == xpos[i] || (xpos[i-1]-1) == xpos[i]){
                if((ypos[i-1]+2) == ypos[i] || (ypos[i-1]-2) == ypos[i]){
                    flag = true;
                }
                else{
                    flag = false;
                    break;
                }
            }else{
                flag = false;
                break;
            }
        }
        //마지막 횟차(i ==35)에 초기값으로 갈 수 있는지 없는지 확인한다.
        if(i == 35){
            if((xpos[i]+2) == xpos[0] || (xpos[i]-2) == xpos[0]){
                if((ypos[i]+1) == ypos[0] || (ypos[i]-1) == ypos[0]){
                    flag = true;
                }
                else{
                    flag = false;
                    break;
                }
            }else if((xpos[i]+1) == xpos[0] || (xpos[i]-1) == xpos[0]){
                if((ypos[i]+2) == ypos[0] || (ypos[i]-2) == ypos[0]){
                    flag = true;
                }
                else{
                    flag = false;
                    break;
                }
            }else{
                flag = false;
                
            }
        }
        //이전에 입력된 값이 들어오는 지 for문을 통해 확인한다
        for(int j=0; j<i; j++){
    	if(xpos[j]==xpos[i] && ypos[j]==ypos[i]){
    		flag = false;
    		break;
		}
	  }
	  if(!flag)
	  	break;
    }
    
    if(flag){
        printf("Valid");
    }else{
        printf("Invalid");
    }
    
    
    
}
```





뭐가 정답일까...

답은 두번째이다...

단지 

```c
scanf(" %c%1d", &xpos[i], &ypos[i]);
```



scanf에서 " 후에 스페이스를 안넣어서...

과연 그게 결과값에 차이를 줄까...

아무리 이해할려고 해도 저 스페이스 하나 차이로 정답, 오답이 구분되는 게 이해가 가질 않는다...

누군가 아신다면 댓글로 알려주시면 감사하겠습니다...



만약 실제 결과에 차이가 없는 코드이고 스페이스때문에 오답을 처리한다면...정말 짜증날 것 같다...





**2022.08.19**

ypos의 타입을 char로 변경하고, scanf에서 %c로 입력받게 수정하여도 정답입니다!



<script src="https://gist.github.com/RileyKim/4d78a26a284af011b8edfbe6e9430a8b.js"></script>

