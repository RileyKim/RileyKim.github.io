---
layout: post
title:  "Install AngularJS Enviroment"
date:   2019-04-09 00:00:00
author: RileyKim
categories: AngularJS
tags: AngularJS, Deployd
cover:  "/assets/instacode.png"
---

# Angularjs 개발환경 설정



OS환경 : Window10

코드 편집기 : WebStorm



## 개발 환경 설정



1. Node.js 설치

2. 웹서버 설치

3. AngularJS 라이브러리 다운로드

4. 부트스트랩 다운로드

5. 웹서버 실행

6. 테스트 파일 로드



AngularJS를 시작하기 전 개발환경 설정을 해보도록 하겠습니다. 



#### Node.js 설치

---------------------------------------------------

[Node.js다운로드](http://nodejs.org) 로 이동하여 자신의 플랫폼(원도우, 리눅스, 맥OS)에 맞는 Node.js패키지를 내려받자.

(나는 6.17.0 버전을 다운받아 설치하였다. 동일한 버전을 다운받는 것을 추천한다. 안정성 측면이나 버전별 차이점이 존재할 수 있기 때문이다.)



설치 파일을 실행하여 C://안에 nodejs폴더를 생성하여 설치 디렉토리로 지정하자!



설치 후 프롬프트를 열고 **Node --version**을 입력하여 설치가 잘되었는지 확인합니다.



![](https://user-images.githubusercontent.com/24997255/55447104-5e60cd80-55fd-11e9-9f78-3ccb2cbe13c6.PNG)



#### 웹 서버 설치

-----------------------------------------

Node.js 설치 디렉토리로 이동한 후 다음 명령을 실행합시다.



**npm install connect@2.0.0**

(connect@2.0.0 버전을 사용해야만 다음 예제에 사용하는  require('connect')를 사용할 수 있다. 버전 별로 차이점이 많으니 꼭! 2.0.0을 설치하도록 하자!!!)



다음으로 , nodejs 폴더 내에 **server.js 파일**을 생성하여 다음 내용을 넣는다.



```javascript
var connect = require('connect');
var path = require('path');
var app = connect().use(connect.static(path.resolve(__dirname, '..', 'angularjs')));
app.listen(5000);
```

이 파일에서는 5000포트에 대한 요청에 응답하는 간단한 서버를 생성하고, angularjs라는 폴더에 들어있는 파일을 제공한다. (angularjs 폴더는 나중에 생성할 것이다.) 



#### AngularJS 라이브러리 다운로드

----------------------------------

Angular 라이브러리를 [AngularJS 다운로드](http://angularjs.org)에서 다운받도록 하자!



![](https://user-images.githubusercontent.com/24997255/55447130-7e908c80-55fd-11e9-8c79-08a946f38137.PNG)

Previous Versions 클릭하면 모든 버전을 볼 수 있으며 나는 1.2.5 버전 라이브러리를 다운받아 진행하였다. 

(uncompressed를 선택하여 라이브러리만 다운받는다!)

**angularjs 1.2.5 버전을 다운받아 진행하는 걸 추천한다. angularjs는 버전 차이가 심하다.**



**c://에 angularjs폴더를 생성하여 angularjs 라이브러리 파일을 넣는다!**



#### 부트스트랩 다운로드

------------------------------------

[부트스트랩 다운로드](http://getbootstrap.com)으로 이동하여 bootstrap-3.0.3 압축파일을 다운받도록하자. 

압축은 푼 후 angularjs폴더 내에 bootstrap.css, bootstrap-theme.css 파일을 복사한다.

(어떤 책 내에서는 설명이 헷갈리게 되어있다. 저 파일들만 복사하여 angularjs폴더 내에 넣는다. 경로 어쩌구 저쩌구 하는데 무시하고 angularjs폴더 내에 복사한다.)



#### 간단한 테스트

------------------------------------------------------------



test.html을 angularjs폴더 내에 생성하여 다음 내용을 넣어준다.

```html
<!DOCTYPE html>
<html ng-app>
<head>
   <title>    First Test</title>
   <script src="angular.js"></script>
   <link href="bootstrap.css" rel="stylesheet"/>
   <link href="bootstrap-theme.css" rel="stylesheet">
</head>

<body>
   <div class="btn btn-default">{{"AngularJS"}}</div>
   <div class="btn btn-success">Bootstrap</div>
</body>
</html>
```



#### 웹 서버 실행

------------------------------

프롬프트를 실행하여 Nodejs 폴더로 이동한 후 **node server.js**를 실행한다. 

(사실 WebStorm을 설치한 후 하는 것이 편하긴 하다...)

![](https://user-images.githubusercontent.com/24997255/55447146-910ac600-55fd-11e9-8f12-018e98b7aeba.PNG)

server.js 파일을 로드하고 5000포트에서 HTTP요청의 리스닝을 시작한다. 



#### 테스트 파일 로드 

-----------------------------------

[http://localhost:5000/test.html](http://localhost:5000/test.html)로 이동한다. 그럼 다음과 같은 결과를 확인할 수 있다. ^^&



![](https://user-images.githubusercontent.com/24997255/55447166-a1bb3c00-55fd-11e9-8474-f19c6db276e0.PNG)

이상으로 개발 환경 설정을 마치도록 하겠습니다. 

다음에는 todo.html파일을 통해 AngularJS 페이지를 만들어 보도록 하겠습니다~