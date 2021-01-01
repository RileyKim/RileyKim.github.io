---
layout: post
title:  "Start GitBlog"
date:   2019-08-06 00:00:00
author: RileyKim
categories: GitBlog
tags: GitBlog
cover:  "/assets/instacode.png"
comments: true
---

# Git Blog 시작하기



개발환경 : MacBook 2015, HomeBrew

OS :  High Sierra



처음 깃 블로그를 시작하면서 부분적으로만 설명하는 곳이 많아, 긴 내용이지만 처음부터 끝까지 하나의 포스팅으로 정리하려고 합니다. 

처음하는 사람도 그대로 따라하면 Git Blog를 생성할 수 있게 최대한 세세하게 작성하려고 합니다. 

혹시나 모르는 부분이 생기거나 궁금한 점있으시면 댓글로 남겨주세요!



**Mac OS 기준으로 포스팅되어있습니다.**



## Git Blog 생성과정

1. HomeBrew 설치하기
2. Git 설치하기
3. Ruby 설치하기
4. Jekyll 설치
5. Git Repository 생성하기
6. Jekyll 테마 다운받기
7. Git Repository와 Jekyll 연동하기(Jekyll테마 적용)



### 1. HomeBrew 설치하기
------

**HomeBrew는 쉽게 패키지 매니저라고 생각하면 됩니다. **

여러가지 프로그램들을 패키지로 관리할 수 있기 때문에 설치, 삭제, 업데이트 등 관리가 굉장히 쉬워집니다. 



HomeBrew 설치 : <https://brew.sh/index_ko.html>

터미널을 실행한 후 페이지에 보이는 명령어를 복사하여, 실행하면 설치가 완료됩니다. 



**설치 명령어**

```
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

![git_blog_init_1](https://user-images.githubusercontent.com/24997255/62440609-de559a80-b78b-11e9-8740-b4ad7a873bb8.PNG)



#### 1-1 HomeBrew 사용법
-----------------

```
$ brew install [패키지 명]   # 필요한 패키지 설치
$ brew uninstall [패키지 명] # 설치한 패키지 삭제
$ brew search [패키지 명]    # 설치하고자 하는 패키지명 검색
$ brew info [패키지 명]      # 패키지 정보 확인
$ brew upgrade [패키지 이름]  # 패키지 업데이트
$ brew list                 # Homebrew로 설치된 리스트 확인
$ brew update               # Homebrew 업데이트
```



### 2. Git 설치하기
-----------------------------------------

터미널을 열어 `git --version`을 실행해보자. 

만약 설치되어 있다면, 넘어가도 된다. 

설치 되어 있지 않다면 2가지 방법으로 설치를 진행하면 됩니다. 



#### 2-1 HomeBrew
---------------

HomeBrew를 설치가 되어있다면, 

`brew install git`명령어를 통해 설치하면 된다. 



#### 2-2 git HomePage
---------------------

HomeBrew 설치를 안했다면, 

다운로드 홈페이지에 접속하여 설치 파일은 다운받아 설치한다. 



 Git 다운로드 : <https://git-scm.com/downloads>

![git_blog_init_1](https://user-images.githubusercontent.com/24997255/62435439-228a7000-b777-11e9-817f-ff5b8ef4047a.PNG)

설치 파일을 다운받아 설치하면 됩니다!



### 3. Ruby 설치하기
-----------------------

**맥북은 기본적으로 설치가 되어 있는 걸로 알고 있습니다. **

먼저 터미널을 실행한 후 `ruby -v`을 통해 Ruby가 설치되어 있는지 또는 버전을 확인하도록 합니다. 



---------------------

**주의사항**!

**Jekyll 설치에 필요한 Ruby버전은 2.25이상이므로 버전이 낮다면 업데이트를 하도록 합니다.**

```
$ brew upgrade [패키지 이름]  # 패키지 업데이트
```

----------------------------



**rbenv는 루비 버전별 실행환경을 관리하는 툴**

```
#rbenv 설치
$ brew install rbenv ruby-build

#rbenv를 bash에 추가
$ echo 'if which rbenv > /dev/null; then eval "$(rbenv init -)"; fi' >> ~/.bash_profile source ~/.bash_profile

#ruby version
$ ruby -v
```



**Install Ruby**

```
# Install Ruby 2.4.4
$ rbenv install 2.4.4 
$ rbenv global 2.4.4 
$ rbenv rehash
```



Ruby 버전을 확인해 올바른 버전이 나오는지 확인해 봅니다.

`ruby -v`

ruby version  2.4.4가 나오면 정상적으로 설치가 된 것입니다.



**Install Bundler**

```  
#install bundler
$ gem install bundler
$ rbenv rehash
```

Ruby에서 사용하는 패키지는 **Gem**이라고 불리고 gem의 의존성관리를 위해 **Bundler** 라는 의존성관리 도구가 사용됩니다. 



### 4. Jekyll 설치
-----------

```
#Jekyll 설치
gem install bundler jekyll
```



### 5. Git repository 생성
------------

![git_blog_init_3](https://user-images.githubusercontent.com/24997255/62448587-2a600980-b7a3-11e9-8250-0a79cd8ed267.PNG)

Git repository를 생성합니다. 

**Repository name을 설정할 때, (###.github.io) 의 ###은 계정 이름이어야합니다.  **

**###.github.io는 본인의 Git Blog의 URL주소이니 신중하게(?) 정해주세요**



![git_blog_init_4](https://user-images.githubusercontent.com/24997255/62448708-62ffe300-b7a3-11e9-8585-5a88a8316288.PNG)

저는 RileyKim.github.io로 정했습니다.



![git_blog_init_5](https://user-images.githubusercontent.com/24997255/62448759-74e18600-b7a3-11e9-8ed3-8b214e0d456c.PNG)

저의 Git Blog주소는 https://rileykim.github.io/ 입니다.



### 6. Jekyll 테마 다운받기
--------------

Jekyll 테마 : <http://jekyllthemes.org/>

여기에 다양한 Jekyll theme가 있으면 원하는 테마를 다운받을 수 있다. 



나는 심플하고 깔끔한 테마인 **centrarium**를 선택하였다. 

centrarium theme(Git repository) : <https://github.com/bencentra/centrarium>



![git_blog_init_6](https://user-images.githubusercontent.com/24997255/62449821-fb976280-b7a5-11e9-89d8-2cd55ba69476.PNG)

centrarium theme를 다운받는다. 



# 7. Git Repository와 Jekyll 연동하기
------------------------

다운받은 테마를 나의 repository에 연동하여 Git Blog를 생성할 것이다. 



블로그를 만들고자 하는 위치(폴더 위치)에 다음 명령어를 실행한다. 

```
$ jekyll new ###.github.io
```

**###는 github계정이름이다. (5. gitrepository 참조)**



다운받은 centrarium theme파일을 블로그를 만들고자 하는 위치에 복사한다. 

해당 폴더 위치를 Git Repository remote해준다. 

```
#git init
$ git init

#git remote
$ git remote add origin [Repository URL]

#git add
$ git add --all

#git commit
$ git commit -m "MyGitblog"

#git push
$ git push origin master
```

생성된 블로그는 `https://###.github.io`로 접속하면 블로그를 볼 수 있다. 

처음 생성하는 경우 몇분의 시간이 걸릴 수 있습니다. 



![git_blog_init_7](https://user-images.githubusercontent.com/24997255/62451105-9133f180-b7a8-11e9-9f0d-fd496bab93a8.PNG)

다음과 같이 테마가 적용된 블로그를 확인할 수 있다.



**만약 블로그가 제대로 접속이 안된다면**

1. _config.yml 파일의 URL을 수정해본다. 
2. 블로그를 만들고자 하는 위치에서 jekyll build를 실행해본다. 