---
layout: post
title:  "Basic bootstrap"
date:   2019-04-09 00:00:00
author: RileyKim
categories: Bootstrap
tags: Bootstrap
cover:  "/assets/instacode.png"
comments: true
---

# 부트스트랩의 이해

angularjs 폴더 내에 bootstrap.html 파일을 생성한다.



**bootstrap.html  내용**

```html
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <title>Bootstrap Examples</title>
    <link href="bootstrap.css" rel="stylesheet"/>
    <link href="bootstrap-theme.css" rel="stylesheet"/>
</head>
<body>
    <div class="panel">
        <h3 class="panel-heading">Button Styles</h3>
        <button class="btn">Basic Button</button>
        <button class="btn btn-primary">Primary</button>
        <button class="btn btn-success">Success</button>
        <button class="btn btn-warning">Warning</button>
        <button class="btn btn-info">Info</button>
        <button class="btn btn-danger">Danger</button>
    </div>
    <div class="well">
        <h3 class="panel-heading">Button Sizes</h3>
        <button class="btn btn-large btn-success">Lage Success</button>
        <button class="btn btn-warning">Standard Warning</button>
        <button class="btn btn-small btn-danger">Small Danger</button>
    </div>
    <div class="well">
        <h3 class="panel-heading">Black Button</h3>
        <button class="btn btn-block btn-large btn-success">Large Block Success</button>
        <button class="btn btn-block btn-warning">Standard Block Warning</button>
        <button class="btn btn-block btn-small btn-info">Small Block Info</button>
    </div>
</body>
</html>
```



![](https://user-images.githubusercontent.com/24997255/55521816-481a4680-56bd-11e9-8774-11e665468f5d.PNG)





**기본 부트스트랩 스타일 클래스**

--------------------------------

panel : 둥근 모서리를 적용한 패널을 표시

panel-heading : 패널의 제목을 생성한다. 

btn : 버튼을 생성한다. 

well : 들여쓰기 효과와 함께 엘리먼트를 그룹으로 지정한다.





### 스타일 적용 테이블

------------------------------

bootstrap.html 파일의 내용을 수정한다. 



**수정된 bootstrap.html**

```html
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <title>Bootstrap Examples</title>
    <link href="bootstrap.css" rel="stylesheet"/>
    <link href="bootstrap-theme.css" rel="stylesheet"/>
</head>
<body>
    <div class="panel">
        <h3 class="panel-heading">Standard Table with Context</h3>
        <table class="table">
            <thead>
                <tr><th>Country</th><th>Capital City</th></tr>
            </thead>
            <tr class="success"><td>United Kingdom</td><td>London</td></tr>
            <tr class="danger"><td>France</td><td>Paris</td></tr>
            <tr><td>Spain</td><td class="warning">Madrid</td></tr>
        </table>
    </div>
    <div class="panel">
        <h3 class="panel-heading">Striped Bordered and highlighted Table</h3>
        <table class="table table-striped table-bordered table-hover">
            <thead>
                <tr><th>Country</th><th>Capital</th></tr>
            </thead>
                <tr><td>United Kingdom</td><td>London</td></tr>
                <tr><td>France</td><td>Paris</td></tr>
                <tr><td>Spain</td><td>Madrid</td></tr>
        </table>
    </div>
</body>
</html>
```



![](https://user-images.githubusercontent.com/24997255/55521831-5c5e4380-56bd-11e9-8fa2-cea5a9f088a5.PNG)



### 부트스트랩을 활용한 폼 생성

-------------------------

기본적인 폼 스타일은 다음과 같이 label 과 input 엘리먼트가 들어있는 div엘리먼트에 form-group클래스를 적용해 지정하면 된다.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Bootstrap Examples</title>
    <link href="bootstrap-theme.css" rel="stylesheet">
    <link href="bootstrap.css" rel="stylesheet">
</head>
<body>
    <div class="panel">
        <h3 class="panel-heading">
            Form Elements
        </h3>

        <div class="form-group">
            <label>Name:</label>
            <input name="name" class="form-control" />
        </div>

        <div class="form-group">
            <label>Email:</label>
            <input name="email" class="form-control" />
        </div>

        <div class="radio">
            <label>
                <input type="radio" name="junkmail" value="yes" checked>
                yes, send me endless junk mail
            </label>
        </div>
        <div class="radio">
            <label>
                <input type="radio" name="junkmail" value="no"/>
                no, i never want to hear from you again
            </label>
        </div>

        <div class="checkbox">
            <label>
                <input type="checkbox"/>
                i agree to the terms and conditions.
            </label>
        </div>
        <input type="button" class="btn btn-primary" value="Subscribe"/>
    </div>
</body>
</html>
```



![](https://user-images.githubusercontent.com/24997255/55521836-6a13c900-56bd-11e9-9bb2-3eb28507471d.PNG)



### 부트스트랩을 활용한 그리드 생성

------------------------------------------------------

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Bootstrap examples</title>
    <link href="bootstrap-theme.css" rel="stylesheet">
    <link href="bootstrap.css" rel="stylesheet">
    <style>
        #gridContainer {padding:20px;}
        .grid-row > div {
            border: 1px solid lightgrey;
            padding: 10px;
            background: aliceblue;
            margin: 5px 0;}
    </style>
</head>
<body>
    <div class="panel">
        <h3 class="panel-header">
            Grid Layout
        </h3>

        <div id="gridContainer">
            <div class="row grid-row">
                <div class="col-xs-1">1</div>
                <div class="col-xs-1">1</div>
                <div class="col-xs-2">2</div>
                <div class="col-xs-2">2</div>
                <div class="col-xs-6">6</div>
            </div>


            <div class="row grid-row">
                <div class="col-xs-3">3</div>
                <div class="col-xs-4">4</div>
                <div class="col-xs-5">5</div>
            </div>

            <div class="row grid-row">
                <div class="col-xs-11">11</div>
                <div class="col-xs-1">1</div>
            </div>


            <div class="row grid-row">
                <div class="col-xs-6">6</div>
                <div class="col-xs-6">6</div>
            </div>

            <div class="row grid-row">
                <div class="col-xs-12">12</div>
            </div>

        </div>
    </div>
</body>
</html>
```



![](https://user-images.githubusercontent.com/24997255/55521852-7b5cd580-56bd-11e9-81ac-57b07afd5e39.PNG)



### 반응형 그리드 생성해보자

-----------------------------------

반응형 그리드는 브라우저 창의 크기에 따라 레이아웃이 조절한다. 반응형 그리드의 주요 목적은 사용할 수 있는 화면 크기에 따라 같은 콘텐츠를 모바일 기이에 데스크톱 등에서 다르게 보여주는 데에 있다. 



**반응형 그리드를 위한 부트스트랩 CSS클래스**

| col-sm-*     | 화면 크기가 768픽셀보다 크면 그리드 셀이 가로로 표시된다.    |
| ------------ | :----------------------------------------------------------- |
| **col-md-*** | **화면 크기가 940픽셀보다 크면 그리드 셀이 가로로 표시된다.** |
| **col-lg-*** | **화면 크기가 1170픽셀보다 크면 그리드 셀이 가로로 표시된다.** |



```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Bootstrap examples</title>
    <meta name="viewport" content="width=device-width" initial-scale="1">
    <link href="bootstrap-theme.css" rel="stylesheet">
    <link href="bootstrap.css" rel="stylesheet">
    <style>
        #gridContainer {padding:20px;}
        .grid-row > div {
            border: 1px solid lightgrey;
            padding: 10px;
            background: aliceblue;
            margin: 5px 0;}
    </style>
</head>
<body>
    <div class="panel">
        <h3 class="panel-header">
            Grid Layout
        </h3>

        <div id="gridContainer">
            <div class="row grid-row">
                <div class="col-sm-1">1</div>
                <div class="col-sm-1">1</div>
                <div class="col-sm-2">2</div>
                <div class="col-sm-2">2</div>
                <div class="col-sm-6">6</div>
            </div>


            <div class="row grid-row">
                <div class="col-sm-3">3</div>
                <div class="col-sm-4">4</div>
                <div class="col-sm-5">5</div>
            </div>

            <div class="row grid-row">
                <div class="col-sm-11">11</div>
                <div class="col-sm-1">1</div>
            </div>


            <div class="row grid-row">
                <div class="col-sm-6">6</div>
                <div class="col-sm-6">6</div>
            </div>

            <div class="row grid-row">
                <div class="col-sm-12">12</div>
            </div>

        </div>
    </div>
</body>
</html>
```