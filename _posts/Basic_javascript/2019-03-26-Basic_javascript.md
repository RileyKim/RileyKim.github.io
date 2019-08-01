---
layout: post
title:  "Basic JavaScript"
date:   2019-03-26 00:00:00
author: RileyKim
categories: JavaScript
tags: JavaScript
cover:  "/assets/instacode.png"
comments: true
---
# 자바스크립트 기초



기본적인 자바스크립트 기법을 사용하는 예와 더불어 자바스크립트 언어를 보완하기 위해 AngularJS에서 제공하는 범용 유틸리티 메서드를 살펴볼 것이다.



```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Example</title>
    <script src="angular.js"></script>
    <script type="text/javascript">
        console.log("hello");
    </script>
</head>
<body>
    this is a simple example
</body>
</html>
```



![](C:\Users\Kim\Documents\javasctrip이해-1.PNG)



### 함수의 정의 및 사용

---------------------------------

**myFunc()**라는 함수를 정의하고 **myFunc()**를 통해 함수를 사용하였다.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Example</title>
    <script src="angular.js"></script>
    <script type="text/javascript">
        function myFunc(name,weather){
            console.log("hello " + name + "!");
            console.log("today's weather is " + weather);
        };
        myFunc("Taek","sunny");
    </script>
</head>
<body>
    this is a simple example
</body>
</html>
```



![](C:\Users\Kim\Documents\javasctrip이해-2.PNG)



파라미터보다 많은 인자를 사용해 함수를 호출하면 추가 인자는 그냥 무시된다. 자바스크립트에서는 같은 이름과 서로 다른 파라미터를 사용해 두개의 함수를 정의하고, 함수를 호출할 때 제공한 인자를 기반으로 자바스크립트에서 함수를 구분해주는 기능을 사용할 수 없다. 



### 결과를 반환하는 함수의 정의

-------------------------

