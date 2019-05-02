# YOLO 설치 및 Real-Time Object detection from cam



설치 환경 : Window 64bit, CUDA 10.0.130, cuDNN 10.0(v7.5.56), OpenCV3.1, Visual Studio 2015	

가급적 저와 개발환경을 동일하게 진행하는 것을 추천드립니다. 



기본적으로 YOLO를 하기 위해선 GPU가 있어야 됩니다. 

그리고 저는 노트북 내장형 카메라를 사용하였고, 필히 캠이 있으셔야 Real-Time Detection이 가능합니다.





진행 순서를 정리해드리면, 

1. CUDA 설치
2. cuDNN 설치
3. Visual Studio 2015 설치
4. OpenCV 설치
5. Visual Studio 2015 환경 설정(OpenCV 개발환경)
6. YOLO 다운(깃허브)
7. YOLO 개발 환경
8. YOLO 실행



1,2,3 번은 사이트에 접속하여 설치 파일을 다운로드하여 진행하시면 아주 간단합니다!

cuDNN은 회원가입이 필요합니다. 

##### 아, 그리고 참고로 cuDNN 다운받은 후 CUDA 설치 폴더 위치에 추가하여 넣어줘야합니다!!(중요!)



CUDA 다운로드 페이지 : <https://developer.nvidia.com/cuda-toolkit-archive>

cuDNN 다운로드 페이지 : <https://developer.nvidia.com/rdp/form/cudnn-download-survey>

OpenCV 다운로드 페이지 : <https://opencv.org/releases.html>

Visual Studio 다운로드 페이지 : <https://visualstudio.microsoft.com/ko/vs/older-downloads/>

YOLO 깃허브 다운로드 페이지 : <https://github.com/AlexeyAB/darknet>



1,2 번은 쉽게 설치할 수 있을 거라 생각되어 Visual Studio 설치부터 설명드리도록 하겠습니다.



### VIsual Studio 2015 설치

------

Visual Studio 다운로드 페이지 : <https://visualstudio.microsoft.com/ko/vs/older-downloads/>



![InstallingYOLO-3](https://user-images.githubusercontent.com/24997255/56186498-7ce1b280-605a-11e9-9a37-24500c39f22e.PNG)

다운받기 위해선 회원가입이 필요합니다..



실행하시고 기본 설정 그대로 다음, 다음, 다음하시면 끝납니다...





### OpenCV 3.1 설치

---------------------

OpenCV 다운로드 페이지(<https://opencv.org/releases.html>)에 들어가시면, OpenCV 3.1.0 버전을 다운받을 수 있습니다. 



![InstallingYOLO-1](https://user-images.githubusercontent.com/24997255/56184165-25404880-6054-11e9-88da-99166ecab435.PNG)



저는 환경에 맞게 Win pack을 다운로드 합니다. 

저는 기본적으로 지정되어 있는 폴더 위치를 지우고 c:\ 내에 opencv 설치 폴더를 생성하여 진행하였습니다. 

![InstallingYOLO-2](https://user-images.githubusercontent.com/24997255/56185094-7d2c7e80-6057-11e9-828a-e67f140a0b8f.PNG)



설치를 하였으면 **환경변수**에 OpenCV 경로를 추가합니다. 

**[시작]-[제어판]-[시스템]-[고급시스템 설정]-[환경변수]**

**시스템 변수 항목 중 path에 c:\opencv\build\x64\vc14\bin; 를 추가합니다.**



----------------------------------------

##### Visual Studio Version에 따른 경로 정보(OpenCV 3.1.0 64bit)

Visual Studio 2013 이하 :  c:\opencv\build\x64\vc12\bin;

Visual Studio 2015  :  c:\opencv\build\x64\vc14\bin;

---------------------------------------





### Visual Studio 2015 환경 설정(OpenCV 개발환경)

-------------------------------



![InstallingYOLO-4](https://user-images.githubusercontent.com/24997255/56188905-a225ef00-6061-11e9-9fec-7974ce57969e.PNG)

[파일]-[새로만들기]-[프로젝트]

이름, 솔루션 명을 YOLO로 생성하였습니다.  

workplace 위치는 c:\OpencvSample로 하였습니다.



![InstallingYOLO-5](https://user-images.githubusercontent.com/24997255/56189000-da2d3200-6061-11e9-92a9-df666e04ce38.PNG)

[빈 프로젝트] 확인



![InstallingYOLO-6](https://user-images.githubusercontent.com/24997255/56189863-ef0ac500-6063-11e9-95f7-4981eab11033.PNG)



생성 완료



**OpenCV를 사용할 환경을 만들기 위해선 [프로젝트]-[속성]-[VC++ 디렉터리]에서 포함 라이브러리와 라이브러리 디렉터리를 편집해야 합니다. ** 

![InstallingYOLO-7](https://user-images.githubusercontent.com/24997255/56190530-58d79e80-6065-11e9-850b-1f039791fca0.PNG)

**해당 경로 추가**

포함 디렉터리 : c:\opencv\build\include

라이브러리 디렉터리 : c:\opencv\build\x64\vc14\lib



**[프로젝트]-[속성]-[링커]-[입력]-[추가종속성]**에 C:\opencv\build\x64\vc14\lib 폴더내 *.lib파일들을 추가한다. 

![InstallingYOLO-8](https://user-images.githubusercontent.com/24997255/56190640-963c2c00-6065-11e9-8b75-82bbbcc90630.PNG)



**플랫폼도 변경합니다**

![InstallingYOLO-9](https://user-images.githubusercontent.com/24997255/56191660-b7058100-6067-11e9-8f21-5feb57a3f45a.PNG)

Release/x64로 변경



---------------------------------------------------

**완성된 속성 시트를 저장하면 새 프로젝트 생성시 속성 시트만 적용시켜주면 OpenCV 개발 환경을 만들 수 있다**

[보기]-[다른 창]-[속성 관리자]-[새프로젝트 속성 시트 추가]에서 속성 시트  파일의 이름과 위치를 지정하여 저장한다.  새 프로젝트 생성 시 기존 속성 시트 추가를 선택하여 적용시키면된다!

------------------------------------------------------





## YOLO 다운(깃허브)

YOLO 깃허브 다운로드 페이지 : <https://github.com/AlexeyAB/darknet에서 압축파일 형식으로 다운받을 수 있습니다. 

![InstallingYOLO-10](https://user-images.githubusercontent.com/24997255/56194446-fa62ee00-606d-11e9-9b43-f534dd167571.PNG)





### YOLO 개발 환경

------------------------------------

다운받은 압축 파일을 엽니다. 



압축을 풀면 darknet-master 폴더가 생성될 것입니다.  

**build/darknet**에 **opencv\build\x64\vc14\bin** 내에 (opencv_world320.dll,opencv_ffmpeg320_64.dll) or (opencv_world340.dll,opencv_ffmpeg340_64.dll)파일을 복사하여 넣어줍니다. 

그리고 **\build\darknet\x64** 에 cuDNN 설치폴더 내 cudnn64_7.dll파일을 복사하여 넣어줍니다. 



**build\darknet**에서 darknet.sln파일을 실행시킵니다. 

컴파일을 시킵니다. 



### YOLO 실행

----------------------------------

cmd를 열고  **\build\darknet\x64** (darknet.exe파일 경로)로 가서 

**darknet.exe detector demo cfg/coco.data cfg/yolov3.cfg yolov3.weights** 을 실행하시면 됩니다. 

여기서 저 문구가 이야기하는 것은 coco.data와 yolov3.cfg파일을 바탕으로 머신러닝 학습된 파일( yolov3.weights)를 통해 물체를 인식하는 darknet프로그램을 실행하겠다는 것입니다. 



![InstallingYOLO-11](https://user-images.githubusercontent.com/24997255/56412501-5f615280-62bf-11e9-962b-f8c3c8ab68eb.PNG)





