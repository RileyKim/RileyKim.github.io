---
layout: post
title:  "make AngularJS App easily"
date:   2019-04-09 00:00:00
author: RileyKim
categories: AngularJS
tags: AngularJS
cover:  "/assets/instacode.png"
comments: true
---

# 간단한 AngularJS 앱 만들기(todo.HTML)



OS환경 : Window10

코드 편집기 : WebStorm



**#진행함에 따라 소스가 추가되는데 CTRL+F에서 "추가"를 검색하여 추가된 소스를 쉽게 찾을 수 있다!**



**C://angularjs폴더 내에 todo.html이라는 간단한 HTML파일을 추가한다.**



```html
<!DOCTYPE html>
<html data-ng-app>
<head>
    <title>To Do List</title>
    <link href="bootstrap.css" rel="stylesheet">
    <link href="bootstrap-theme.css" rel="stylesheet">
</head>
<body  ng-app="todoApp">
    <div class="page-header">
        <h1>
            TO do list
        </h1>
    </div>

    <div class="panel">
        <div class="input-group">
            <input class="form-control"/>
            <span class="input-group-btn">
                <button class="btn btn-default">Add</button>
            </span>
        </div>

        <table class="table table-striped">
            <thead>
                <tr>
                    <th>Description</th>
                    <th>Done</th>
                </tr>
            </thead>
            <tbody>
                <tr><td>Buy Flowers</td><td>No</td></tr>
                <tr><td>Get Shoes</td><td>No</td></tr>
                <tr><td>Collect Ticket</td><td>Yes</td></tr>
                <tr><td>Call Joe</td><td>No</td></tr>
            </tbody>
        </table>
    </div>
</body>
</html>
```



**결과**

![결과](https://user-images.githubusercontent.com/24997255/55522040-443af400-56be-11e9-92fd-649f19f60da1.PNG)



### HTML 파일에 AngularJS적용

---------------------------------------------------------------



**AngularJS 요소 중 가장 중요한 요소는 ng-app 어트리뷰트이다. 
이는 html 엘리먼트 중 AngularJS가 컴파일하고 처리해야 할 모듈이 들어있음을 알려주는 역할**



```html
<!DOCTYPE html>


<!---추가--->
<html data-ng-app = "todoApp">
<!--------->
    
<head>
    <title>To Do List</title>
    <link href="bootstrap.css" rel="stylesheet">
    <link href="bootstrap-theme.css" rel="stylesheet">
    
    <!-------------------추가-------------------------->
    <script src="angular.js"></script>
    <script>
        var todoApp = angular.module("todoApp",[]);
    </script>
    <!------------------------------------------------>
    
</head>
<body  ng-app="todoApp">
<div class="page-header">
    <h1>
        TO do list
    </h1>
</div>

<div class="panel">
    <div class="input-group">
        <input class="form-control"/>
        <span class="input-group-btn">
                <button class="btn btn-default">Add</button>
            </span>
    </div>

    <table class="table table-striped">
        <thead>
        <tr>
            <th>Description</th>
            <th>Done</th>
        </tr>
        </thead>
        <tbody>
        <tr><td>Buy Flowers</td><td>No</td></tr>
        <tr><td>Get Shoes</td><td>No</td></tr>
        <tr><td>Collect Ticket</td><td>Yes</td></tr>
        <tr><td>Call Joe</td><td>No</td></tr>
        </tbody>
    </table>
</div>
</body>
</html>
```



### 데이터 모델 생성

------------------------------------



```html
<!DOCTYPE html>
<html data-ng-app = "todoApp">
<head>
    <title>To Do List</title>
    <link href="bootstrap.css" rel="stylesheet">
    <link href="bootstrap-theme.css" rel="stylesheet">
    <script src="angular.js"></script>
    <script>
   	/******************* 추가 *******************************/
        var model = {
            user : "Adam",
            items: [{action : "Buy Flowers", done : false},
                {action: "Get shoes", done: false},
                {action : "Collect Tickets", done:true},
                {action : "Call Hoe", done: false}]
        };
	/*****************************************************/
        var todoApp = angular.module("todoApp",[]);
    </script>
</head>
<body  ng-app="todoApp">
<div class="page-header">
    <h1>
        To do list
    </h1>
</div>

<div class="panel">
    <div class="input-group">
        <input class="form-control"/>
        <span class="input-group-btn">
                <button class="btn btn-default">Add</button>
            </span>
    </div>

    <table class="table table-striped">
        <thead>
        <tr>
            <th>Description</th>
            <th>Done</th>
        </tr>
        </thead>
        <tbody>
        <tr><td>Buy Flowers</td><td>No</td></tr>
        <tr><td>Get Shoes</td><td>No</td></tr>
        <tr><td>Collect Ticket</td><td>Yes</td></tr>
        <tr><td>Call Joe</td><td>No</td></tr>
        </tbody>
    </table>
</div>
</body>
</html>
```



**결과**

----------------------------------

![](https://user-images.githubusercontent.com/24997255/55522059-51f07980-56be-11e9-9e8b-e00dbf7bd9c5.PNG)



### 컨트롤러 생성

-------------------------------------



컨트롤러를 사용해 뷰가 접근할 수 있는 데이터 영역을 선택하는데, 이를 **스코프**라고 부른다.

이 컨트롤러 함수의 인자는 $scope로서, AngularJS 앱에서 $로 시작하는 변수명은, AngularJS에서 제공하는 내장 기능을 나타낸다.



```html
<!DOCTYPE html>
<html data-ng-app = "todoApp">
<head>
    <title>To Do List</title>
    <link href="bootstrap.css" rel="stylesheet">
    <link href="bootstrap-theme.css" rel="stylesheet">
    <script src="angular.js"></script>
    <script>

        var model = {
            user : "Adam",
            items: [{action : "Buy Flowers", done : false},
                {action: "Get shoes", done: false},
                {action : "Collect Tickets", done:true},
                {action : "Call Hoe", done: false}]
        };

        var todoApp = angular.module("todoApp",[]);
        
		/****************************추가**************************/
        todoApp.controller("ToDoCtrl", function ($scope) {
            $scope.todo= model;
        });
		/********************************************************/
        
    </script>
</head>
    
    <!-------추가--------->
<body  ng-app="todoApp", ng-controller='ToDoCtrl'>
    <!------------------->
    
<div class="page-header">
    <h1>
        To do list
    </h1>
</div>

<div class="panel">
    <div class="input-group">
        <input class="form-control"/>
        <span class="input-group-btn">
                <button class="btn btn-default">Add</button>
            </span>
    </div>

    <table class="table table-striped">
        <thead>
        <tr>
            <th>Description</th>
            <th>Done</th>
        </tr>
        </thead>
        <tbody>
        <tr><td>Buy Flowers</td><td>No</td></tr>
        <tr><td>Get Shoes</td><td>No</td></tr>
        <tr><td>Collect Ticket</td><td>Yes</td></tr>
        <tr><td>Call Joe</td><td>No</td></tr>
        </tbody>
    </table>
</div>
</body>
</html>
```





### 뷰 생성

-------------------------------------

<script src="https://gist.github.com/RileyKim/24826a21c71d1e3e6821f5f2b3118dbd.js"></script>

![](https://user-images.githubusercontent.com/24997255/55522069-5f0d6880-56be-11e9-8652-f9f00750b93e.PNG)



### 컨트롤러 동작 구현 및 활용

-------------------------------------

**false의 갯수 반환하는 함수 추가. **

$scope 객체에 함수를 첨부하는 데 사용한 속성명은 동작명으로 사용된다. 필자가 정의한 동작명은 incompleteCount이며, 이 동작은 뷰를 형성하는 HTML 엘리먼트에 컨트롤러를 적용하는 ng-controller 어트리뷰트 스코프 내에서 호출할 수 있다.

ng-hide 디렉티브는 어트리뷰트로 지정된 표현식이 true일 경우 이 디렉티브가 적용된 엘리먼트를 숨겨준다. 여기서 incompleteCount 동작을 호출하고 끝내지 못한 할일 개수가 0인지 검사한다. 



```html
<!DOCTYPE html>
<html data-ng-app>
<head>
    <title>To Do List</title>
    <link href="bootstrap.css" rel="stylesheet">
    <link href="bootstrap-theme.css" rel="stylesheet">
    <script src="angular.js"></script>
    <script>
        var model = {
            user : "Adam",
            items: [{action : "Buy Flowers", done : false},
                        {action: "Get shoes", done: false},
                        {action : "Collect Tickets", done:true},
                        {action : "Call Hoe", done: false}]
        };

        var todoApp = angular.module("todoApp",[]);
        todoApp.controller("ToDoCtrl", function ($scope) {
            $scope.todo= model;

            $scope.incompleteCount = function () {
                var count = 0;
                angular.forEach($scope.todo.items, function (item) {
                    if(!item.done){count++}
                });
                return count;
            }
        });
    </script>
</head>
<body  ng-app="todoApp", ng-controller='ToDoCtrl'>
    <div class="page-header">
        <h1>
            {{todo.user}}'s To Do List
            <span class="label label-default" ng-hide="incompleteCount() == 0">{{incompleteCount()}}</span>
        </h1>
    </div>

    <div class="panel">
        <div class="input-group">
            <input class="form-control"/>
            <span class="input-group-btn">
                <button class="btn btn-default">Add</button>
            </span>
        </div>

        <table class="table table-striped">
            <thead>
                <tr>
                    <th>Description</th>
                    <th>Done</th>
                </tr>
            </thead>
            <tbody>
                <tr ng-repeat="item in todo.items">
                    <td>{{item.action}}</td>
                    <td><input type="checkbox" ng-model="item.done"/></td>
                    <td>{{item.done}}</td>
                </tr>
            </tbody>
        </table>
    </div>
</body>
</html>
```



![](https://user-images.githubusercontent.com/24997255/55522090-7187a200-56be-11e9-8b6c-7b689972110c.PNG)



![](https://user-images.githubusercontent.com/24997255/55522106-7d736400-56be-11e9-9690-272710da1462.PNG)



### 다른 동작에 의존하는 동작의 활용

----------------------------------

**false 항목 갯수를 기반으로 CSS 클래스를 선택하는 동작 구현 **



WarningLevel 동작을 정의, false 항목의 갯수를 토대로 부트스트랩 CSS 클래스명을 반환.

warningLevel 동작은 ng-class 디렉티브를 사용해 적용.



```html
<!DOCTYPE html>
<html data-ng-app>
<head>
    <title>To Do List</title>
    <link href="bootstrap.css" rel="stylesheet">
    <link href="bootstrap-theme.css" rel="stylesheet">
    <script src="angular.js"></script>
    <script>
        var model = {
            user : "Adam",
            items: [{action : "Buy Flowers", done : false},
                        {action: "Get shoes", done: false},
                        {action : "Collect Tickets", done:true},
                        {action : "Call Hoe", done: false}]
        };

        var todoApp = angular.module("todoApp",[]);
        todoApp.controller("ToDoCtrl", function ($scope) {
            $scope.todo= model;

            $scope.incompleteCount = function () {
                var count = 0;
                angular.forEach($scope.todo.items, function (item) {
                    if(!item.done){count++}
                });
                return count;
            }

            $scope.warningLevel = function () {
                return $scope.incompleteCount() < 3 ? "lavel-success" : "label-warning";
            }
        });
    </script>
</head>
<body  ng-app="todoApp", ng-controller='ToDoCtrl'>
    <div class="page-header">
        <h1>
            {{todo.user}}'s To Do List
            <span class="label label-default" ng-hide="incompleteCount() == 0">{{incompleteCount()}}</span>
        </h1>
    </div>

    <div class="panel">
        <div class="input-group">
            <input class="form-control"/>
            <span class="input-group-btn">
                <button class="btn btn-default">Add</button>
            </span>
        </div>

        <table class="table table-striped">
            <thead>
                <tr>
                    <th>Description</th>
                    <th>Done</th>
                </tr>
            </thead>
            <tbody>
                <tr ng-repeat="item in todo.items">
                    <td>{{item.action}}</td>
                    <td><input type="checkbox" ng-model="item.done"/></td>
                    <td>{{item.done}}</td>
                </tr>
            </tbody>
        </table>
    </div>
</body>
</html>
```



**(1,2)개는 회색 라벨, (3,4)개는 노란색 라벨로 보여진다.**

![](https://user-images.githubusercontent.com/24997255/55522117-91b76100-56be-11e9-8e41-0e539b988019.PNG)

![](https://user-images.githubusercontent.com/24997255/55522127-9f6ce680-56be-11e9-90b3-da96c9764ee4.PNG)

### 사용자 상호작용 반응

-------------------------------

**Add버튼을 통해 항목 추가 구현.**



```html
<!DOCTYPE html>
<html data-ng-app>
<head>
    <title>To Do List</title>
    <link href="bootstrap.css" rel="stylesheet">
    <link href="bootstrap-theme.css" rel="stylesheet">
    <script src="angular.js"></script>
    <script>
        var model = {
            user : "Adam",
            items: [{action : "Buy Flowers", done : false},
                        {action: "Get shoes", done: false},
                        {action : "Collect Tickets", done:true},
                        {action : "Call Hoe", done: false}]
        };

        var todoApp = angular.module("todoApp",[]);
        todoApp.controller("ToDoCtrl", function ($scope) {
            $scope.todo= model;

            $scope.incompleteCount = function () {
                var count = 0;
                angular.forEach($scope.todo.items, function (item) {
                    if(!item.done){count++}
                });
                return count;
            }

            $scope.warningLevel = function () {
                return $scope.incompleteCount() < 3 ? "lavel-success" : "label-warning";
            }

            $scope.addNewItem = function (actionText) {
                $scope.todo.items.push(
                    {action : actionText,
                    done : false}
                );
            }
        });
    </script>
</head>
<body  ng-app="todoApp", ng-controller='ToDoCtrl'>
    <div class="page-header">
        <h1>
            {{todo.user}}'s To Do List
            <span class="label label-default" ng-class = "warningLevel()" ng-hide="incompleteCount() == 0">{{incompleteCount()}}</span>
        </h1>
    </div>

    <div class="panel">
        <div class="input-group">
            <input class="form-control" ng-model="actionText"/>
            <span class="input-group-btn">
                <button class="btn btn-default" ng-click="addNewItem(actionText)">Add</button>
            </span>
        </div>

        <table class="table table-striped">
            <thead>
                <tr>
                    <th>Description</th>
                    <th>Done</th>
                </tr>
            </thead>
            <tbody>
                <tr ng-repeat="item in todo.items">
                    <td>{{item.action}}</td>
                    <td><input type="checkbox" ng-model="item.done"/></td>
                    <td>{{item.done}}</td>
                </tr>
            </tbody>
        </table>
    </div>
</body>
</html>
```



![](https://user-images.githubusercontent.com/24997255/55522141-ad226c00-56be-11e9-8b2f-724e768922aa.PNG)



### AngularJS 필터, 모델 데이터의 필터링과 정렬

--------------------------------------------------

**todo.html에 필터 기능 추가**

해당 소스에서는 2개의 필터 사용, (filter 필터, orderBy 필터)

filter 필터의 경우, 설정된 기준에 따라 객체를 선택한다. 여기선 false인 항목만 선택하게끔 필터를 적용하였다.

orderBy 필터의 경우, 데이터 정렬을 위해 action 속성 값으로 정렬하게끔 지정하였다. 

필터링은 데이터 모델의 어느 부분에나 적용할 수 있다. 



**체크 박스 선택시 목록에서 사라지며 to do list 갯수가 줄어듬**

![](https://user-images.githubusercontent.com/24997255/55522165-bd3a4b80-56be-11e9-8c8c-98ea0f016abf.PNG)



### 필터 개선 (커스텀 필터 생성)

--------------------------------------------------

**이전 필터링은 체크한 항목이 사용자가 완전히 볼 수 없으므로 쓸모가 없다.**

 커스텀 필터를 생성해보자. 



Show Complete 체크박스 클릭 시 완료된 항목을 볼 수 있다. 

```html
<!DOCTYPE html>
<html data-ng-app>
<head>
    <title>To Do List</title>
    <link href="bootstrap.css" rel="stylesheet">
    <link href="bootstrap-theme.css" rel="stylesheet">
    <script src="angular.js"></script>
    <script>
        var model = {
            user : "Adam",
            items: [{action : "Buy Flowers", done : false},
                        {action: "Get shoes", done: false},
                        {action : "Collect Tickets", done:true},
                        {action : "Call Hoe", done: false}]
        };

        var todoApp = angular.module("todoApp",[]);

        todoApp.filter("checkedItems",function () {
            return function(items, showComplete){
                var resultArr = [];
                angular.forEach(items, function(item) {
                    if(item.done == false || showComplete == true){
                        resultArr.push(item);
                    }
                });
                return resultArr;
            }
        });
        todoApp.controller("ToDoCtrl", function ($scope) {
            $scope.todo= model;

            $scope.incompleteCount = function () {
                var count = 0;
                angular.forEach($scope.todo.items, function (item) {
                    if(!item.done){count++}
                });
                return count;
            }

            $scope.warningLevel = function () {
                return $scope.incompleteCount() < 3 ? "lavel-success" : "label-warning";
            }

            $scope.addNewItem = function (actionText) {
                $scope.todo.items.push(
                    {action : actionText,
                    done : false}
                );
            }
        });
    </script>
</head>
<body  ng-app="todoApp", ng-controller='ToDoCtrl'>
    <div class="page-header">
        <h1>
            {{todo.user}}'s To Do List
            <span class="label label-default" ng-class = "warningLevel()" ng-hide="incompleteCount() == 0">{{incompleteCount()}}</span>
        </h1>
    </div>

    <div class="panel">
        <div class="input-group">
            <input class="form-control" ng-model="actionText"/>
            <span class="input-group-btn">
                <button class="btn btn-default" ng-click="addNewItem(actionText)">Add</button>
            </span>
        </div>

        <table class="table table-striped">
            <thead>
                <tr>
                    <th>Description</th>
                    <th>Done</th>
                </tr>
            </thead>
            <tbody>
                <tr ng-repeat = "item in todo.items | checkedItems:showComplete | orderBy:'action'">
                    <td>{{item.action}}</td>
                    <td><input type="checkbox" ng-model="item.done"/></td>
                    <td>{{item.done}}</td>
                </tr>
            </tbody>
        </table>
        <div class="checkbox-inline">
            <label><input type="checkbox" ng-model = "showComplete">Show Complete</label>
        </div>
    </div>
</body>
</html>
```



![](https://user-images.githubusercontent.com/24997255/55522176-ccb99480-56be-11e9-97eb-31fbfed13b3f.PNG)

![SimpleAngularjsApp-11](https://user-images.githubusercontent.com/24997255/55522191-dcd17400-56be-11e9-8912-d4cf1e62e601.PNG)



### Ajax를 통한 데이터 통신

------------------------------------

Ajax 요청을 통해 데이터를 JSON  데이터로 받을 것이다.



angularjs폴더 내에 **todo.json**파일을 생성한다. 



**todo.json 내용**

```
[{"action":  "Buy Flower", "done": false},
 {"action":  "GetShoes", "done": false},
 {"action": "Collect Tickets", "done": true },
  {"action": "Call Joe", "done": false}]
```



**todo.html 내용**

```html
<!DOCTYPE html>
<html data-ng-app>
<head>
    <title>To Do List</title>
    <link href="bootstrap.css" rel="stylesheet">
    <link href="bootstrap-theme.css" rel="stylesheet">
    <script src="angular.js"></script>
    <script>
        var model = {
            user: "Adam"
        };

        var todoApp = angular.module("todoApp",[]);

        todoApp.run(function ($http){
            $http.get("todo.json").success(function(data){
                model.items = data;
            });
        });

        todoApp.filter("checkedItems",function () {
            return function(items, showComplete){
                var resultArr = [];
                angular.forEach(items, function(item) {
                    if(item.done == false || showComplete == true){
                        resultArr.push(item);
                    }
                });
                return resultArr;
            }
        });
        todoApp.controller("ToDoCtrl", function ($scope) {
            $scope.todo= model;

            $scope.incompleteCount = function () {
                var count = 0;
                angular.forEach($scope.todo.items, function (item) {
                    if(!item.done){count++}
                });
                return count;
            }

            $scope.warningLevel = function () {
                return $scope.incompleteCount() < 3 ? "lavel-success" : "label-warning";
            }

            $scope.addNewItem = function (actionText) {
                $scope.todo.items.push(
                    {action : actionText,
                    done : false}
                );
            }
        });
    </script>
</head>
<body  ng-app="todoApp", ng-controller='ToDoCtrl'>
    <div class="page-header">
        <h1>
            {{todo.user}}'s To Do List
            <span class="label label-default" ng-class = "warningLevel()" ng-hide="incompleteCount() == 0">{{incompleteCount()}}</span>
        </h1>
    </div>

    <div class="panel">
        <div class="input-group">
            <input class="form-control" ng-model="actionText"/>
            <span class="input-group-btn">
                <button class="btn btn-default" ng-click="addNewItem(actionText)">Add</button>
            </span>
        </div>

        <table class="table table-striped">
            <thead>
                <tr>
                    <th>Description</th>
                    <th>Done</th>
                </tr>
            </thead>
            <tbody>
                <tr ng-repeat = "item in todo.items | checkedItems:showComplete | orderBy:'action'">
                    <td>{{item.action}}</td>
                    <td><input type="checkbox" ng-model="item.done"/></td>
                    <td>{{item.done}}</td>
                </tr>
            </tbody>
        </table>
        <div class="checkbox-inline">
            <label><input type="checkbox" ng-model = "showComplete">Show Complete</label>
        </div>
    </div>
</body>
</html>
```



localhost:5000/todo.html에 접속하면 동일하게 작동하는 것을 알 수 있다. 

다만 이 경우는 todo.json을 통해 목록 데이터를 ajax요청을 통해 json 데이터로 받는  것이다!



