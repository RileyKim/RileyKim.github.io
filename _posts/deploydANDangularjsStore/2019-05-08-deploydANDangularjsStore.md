---
layout: post
title:  "make webStore by AngularJS, Deployd"
date:   2019-05-08 00:00:00
author: RileyKim
categories: AngularJS
tags: AngularJS
cover:  "/assets/instacode.png"
---
# Deployd와 AngularJS를 통한 상점 만들기



1. 개발환경
   1. Windows10 64bit
   2. NodeJS V8.9.4
   3. MongoDB V3.2.22



[AngularJS 설치방법]()

[Deployd 설치방법]()



사이트에 접속하여 Dashboard를 확인하자.

![deploydANDangularjsStore-1](https://user-images.githubusercontent.com/24997255/57285742-d041a080-70ee-11e9-8084-a87ddcee98e9.PNG)



new collection을 생성하자. 나는 /products 로 생성하였다. 

![deploydANDangularjsStore-2](https://user-images.githubusercontent.com/24997255/57285655-a25c5c00-70ee-11e9-8582-e3f1a11235c0.PNG)



해당 collection에 필요한 속성들을 추가하자.

![deploydANDangularjsStore-3](https://user-images.githubusercontent.com/24997255/57286206-c10f2280-70ef-11e9-97a9-0ad24d16f0eb.PNG)



데이터를 추가해보자.

![deploydANDangularjsStore-4](https://user-images.githubusercontent.com/24997255/57286263-e00db480-70ef-11e9-84ea-ab8ae6cf6e57.PNG)



http://localhost:5500/products에 접속해보면 JSON문자열 형태의 데이터를 볼 수 있다. 

![deploydANDangularjsStore-5](https://user-images.githubusercontent.com/24997255/57286369-15b29d80-70f0-11e9-980e-1504ec9dad92.PNG)



### 디렉토리 구조 생성

사진과 같이 폴더를 생성하고 파일을 채워넣자. (부트스트랩, 컨트롤러 폴더, angular.js, app.html)

![deploydANDangularjsStore-6](https://user-images.githubusercontent.com/24997255/57286997-80b0a400-70f1-11e9-823b-243ce287a40a.PNG)



c:\angularjsStore\app.html 파일의 내용을 채워준다.

~~~html
<!DOCTYPE html>
<html ng-app="Store">
<head>
	<title>Store</title>
	<script src="angular.js"></script>
	<link rel="stylesheet" type="text/css" href="bootstrap-theme.css">
	<link rel="stylesheet" type="text/css" href="bootstrap.css">
	<script>
		angular.module('Store',[]); 		
	</script>
</head>
<body>
	<div class="navbar navbar-inverse">
		<a class="navbar-brand" href="#">STORE</a>
	</div>
	<div class="panel-default row">
	<div class="col-xs-3">
		Categories go here
	</div>
	<div class="col-xs-8">
		product go here
	</div>
	</div>
</body>
</html>
~~~



### 컨트롤러 구현

최상위 컨트롤러로 사용할 Store.js를 생성한다.

![deploydANDangularjsStore-8](https://user-images.githubusercontent.com/24997255/57342213-c2d0f880-7178-11e9-9e35-d8a73d4f07f7.PNG)

Store.js 내용은 다음과 같다.

~~~
angular.module("Store").controller("StoreCtrl", function($scope){
	$scope.data = {
		product: [
			{name : "Product #1" , description : "A product", category : "Category #1", price : 100},
			{name : "Product #2" , description : "A product", category : "Category #1", price : 110},
			{name : "Product #3" , description : "A product", category : "Category #2", price : 210},
			{name : "Product #4" , description : "A product", category : "Category #3", price : 202}

		]
	};
}); 
~~~

Store.js 내용을 보면 angular.module을 호출한다는 것을 알 수 있다.



### 콘텐츠 엘리먼트 생성

app.html에 내용을 추가하자.

~~~html
<!DOCTYPE html>
<html ng-app="Store">
<head>
	<title>Store</title>
	<script src="angular.js"></script>
	<link rel="stylesheet" type="text/css" href="bootstrap-theme.css">
	<link rel="stylesheet" type="text/css" href="bootstrap.css">
	<script>
		angular.module('Store',[]); 		
	</script>
	<script src="controllers/Store.js"></script>
</head>
<body ng-controller="StoreCtrl">
	<div class="navbar navbar-inverse">
		<a class="navbar-brand" href="#">STORE</a>
	</div>
	<div class="panel-default row">
	<div class="col-xs-3">
		Categories go here
	</div>
	<div class="col-xs-8">
		<div class="well" ng-repeat="item in data.product">
			<h3>
				<strong>{{item.name}}</strong>
				<span class="pull-right label label-primary">
					{{item.price | currency}}
				</span>
			</h3>
			<span class="lead">{{item.description}}</span>
		</div>
		product go here
	</div>
	</div>
</body>
</html>
~~~



serverStore.js를 실행하여 localhost:5400/app.html에 접속하면 다음과 같은 화면을 볼 수 있다.

![deploydANDangularjsStore-9](https://user-images.githubusercontent.com/24997255/57350203-1999fa80-7198-11e9-8907-48f5efb2f83b.PNG)



### 카테고리 목록 표시

c:\angularjsStore\filters\customFilters.js를 생성합니다.

![deploydANDangularjsStore-10](https://user-images.githubusercontent.com/24997255/57353690-448a4b80-71a4-11e9-8d12-b574cbcdb2c4.PNG)





customFilters.js 에 소스를 채워줍니다.

~~~js
angular.module("customFilters",[]).filter("unique",function(){
	return function(data, propertyName){
		if (angular.isArray(data) && angular.isString(propertyName)) {
			var results=[];
			var keys = {};
			for (var i = 0; i<data.lenth; i++){
				var val = data[i][propertyName];
				
				if(angular.isUndefined(keys[val])){
				key[val] = true;
				results.push(val);
				}
			}
			return results;
		}else{
			return data;
		}
	}
});
~~~



### 카테고리 내비게이션 링크 생성

app.html 파일 내 내비게이션 링크 생성 내용을 채워줍니다.

~~~html
<!DOCTYPE html>
<html ng-app="Store">
<head>
	<title>Store</title>
	<script src="angular.js"></script>
	<link rel="stylesheet" type="text/css" href="bootstrap-theme.css">
	<link rel="stylesheet" type="text/css" href="bootstrap.css">
	<script>
		angular.module('Store',["customFilters"]); 		
	</script>
	<script src="controllers/Store.js"></script>
	<script src="filters/customFilters.js"></script>
</head>
<body ng-controller="StoreCtrl">
	<div class="navbar navbar-inverse">
		<a class="navbar-brand" href="#">STORE</a>
	</div>
	<div class="panel-default row">
	<div class="col-xs-3">
		<a ng-click="selectCategory()" class="btn btn-block btn-default btn-lg">Home</a>
		<a ng-repeat="item in data.products | orderBy:'category' | unique:'category'" ng-click="selectCategory(item)" class="btn btn-block btn-default btn-lg" >{{item}}</a>
	</div>
	<div class="col-xs-8">
		<div class="well" ng-repeat="item in data.products">
			<h3>
				<strong>{{item.name}}</strong>
				<span class="pull-right label label-primary">
					{{item.price | currency}}
				</span>
			</h3>
			<span class="lead">{{item.description}}</span>
		</div>
		product go here
	</div>
	</div>
</body>
</html>
~~~

