---
dark-graylayout: post
title:  "How to deploy git"
date:   2019-11-25 00:00:00
author: RileyKim
categories: GitBlog
tags: GitBlog
cover:  "/assets/instacode.png"
comments: true
---

# 깃 브런치 생성 및 배포



프로젝트를 진행하며,  협업을 하신다면 깃 브런치 생성과 배포는 필수적으로 알아야합니다. 

나의 작업물과 협업자의 작업물을 분리하여 작업할 수 있기때문에 소스 관리에 굉장히 효율적입니다. 



하나의 프로젝트가 있다고 칩시다. 

그 프로젝트의 뿌리는 master라고 칭하고, branch를 생성하여 여러갈래의 작업자로 나눕니다. 

각 작업자들이 완료한 작업들을 push하고 master에서 병합합니다. :)



### 브런치 생성 명령어

-------------------

**Make Branch**

<script src="https://gist.github.com/RileyKim/e2d8d6226a933608e8e4f6c2cc76e2bf.js"></script>

만약 'taeksu'라는 branch를 만들고 싶다면 ```git branch taeksu```를 입력하면 됩니다 ㅎ



### 브런치 목록 확인

-------------------

**check branch list**

<script src="https://gist.github.com/RileyKim/353df954ed70c4ad65924dd89cbe5cd3.js"></script>

.git이 있는 경로로 가서 실행해야합니다. 



지금 저의 branch는 ba인 것을 확인할 수 있습니다. 

![git_branch_8](https://user-images.githubusercontent.com/24997255/66546370-d34a2c80-eb77-11e9-8fe2-7b1817f15a09.PNG)



### 브런치 변경

--------------

**change branch**

<script src="https://gist.github.com/RileyKim/cdf74e2144533de5dd57ef54628acdbe.js"></script>

master Branch를 사용하고 싶다면, 

![git_branch_9](https://user-images.githubusercontent.com/24997255/66547049-55872080-eb79-11e9-869c-44ae16c72c2e.PNG)



master Branch로 변경된 것을 확인할 수 있습니다. 

![git_branch_10](https://user-images.githubusercontent.com/24997255/66547069-62a40f80-eb79-11e9-9834-4f624702fe64.PNG)



### 브런치 커밋 & 푸쉬

------------

ba라는 작업자(Branch)가 작업을 완료한 후 커밋 & 푸쉬를 진행해보도록 하겠습니다. 

<script src="https://gist.github.com/RileyKim/5120ee18190fdad33f7c796ebea4fb89.js"></script>

만약 master branch가 아니라면 , git repository에 접속해서 master 계정으로 merge를 진행하면 됩니다!

또 하나의 팁은 push하기 전 pull를 통해 수정사항을 업데이트하는 습관을 기릅시다!



