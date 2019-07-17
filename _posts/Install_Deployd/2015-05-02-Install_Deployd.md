# Deployd 설치



개발환경

1. Windows10 64bit
2. NodeJS V8.9.4
3. MongoDB V3.2.22



Deployd를 사용하기 위해선 **NodeJS와 MongoDB가 설치 되어있어야합니다. **

Deployd HomePage : <http://deployd.com/>



윈도우 + r을 통해 cmd창을 엽니다. 



나는 C:\deployd 폴더 내에서 실행

```
$ npm install deployd-cli -g
$ dpd create store
$ cd store
$ dpd -d
```

이렇게 실행을 하면  오류가 발생했다면!!!

 

![installingDeployd-1](https://user-images.githubusercontent.com/24997255/56564667-884c5500-65e9-11e9-8caf-fb428bb97ff1.PNG)

**두가지 조건이 안되어 있을 때 발생한다.** 

1. 시스템 설정 Path에 mongoDB bin경로가 추가 안되어 있거나
2. DB저장폴더(data/db)를 설정하지 않았기때문입니다. 



DB 저장폴더 설정 방법

```
mongod --dbpath <Path>
```



저는 MongoDB\data\db로 DB폴더로 설정하였습니다. 

![installingDeployd-2](https://user-images.githubusercontent.com/24997255/56566556-ea0ebe00-65ed-11e9-8313-4e077b734b32.PNG)





c:\deployd\store\로 이동하여 다음 명령어를 실행합니다. 

  1.

`$ dpd -d`

localhost:2403

2. 

`$ dpd -p app.dpd dashboard`

localhost:2403/dashboard

3.  

`dpd -p 5500 app.dpd dashboard`

localhost:5500/dashboard

로 접속하면 된다. 



![installingDeployd-3](https://user-images.githubusercontent.com/24997255/56566996-e891c580-65ee-11e9-9094-8aadabeab929.PNG)

