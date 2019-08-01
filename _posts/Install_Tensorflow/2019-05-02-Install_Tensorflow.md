---
layout: post
title:  "Install Tensorflow"
date:   2019-05-02 00:00:00
author: RileyKim
categories: DeepLearning
tags: DeepLearning
cover:  "/assets/instacode.png"
comments: true
---

# Tensorflow 설치 및 Object detection from Picture



설치 환경 : Window 64bit

기본적으로 Tensorflow를 하기 위해선 GPU가 있어야 됩니다. 



Tensorflow를 하기 위한 2가지 방법이 있습니다. 

**첫번째**는 아나콘다를 사용하는 것,

**두번째**는 아나콘다 없이 Python, Tensorflow 등을 통해 진행하는 것입니다. 



**개인적으로 아나콘다 없이 진행하는 것을 추천드립니다**



## 아나콘다를 사용하여 Tensorflow 설치하기

먼저 아나콘다를 사용하여 설치하는 법을 설명드리겠습니다. 

(아나콘다를 설치할 시 CUDA, cuDNN이 자동적으로 설치됩니다)

아나콘다를 설치하면 자동적으로 파이썬이 설치되기 때문에 기존의 파이썬을 삭제 후 진행해야합니다. 

[현재까지 배포된 아나콘다 설치파일](<https://repo.continuum.io/archive/>)을 확인하여 원하시는 설치 파일을 다운받아 설치를 진행하면 됩니다. 



저는 최신버전인 [Anaconda3-2019.03-Windows-x86_64.exe](https://repo.continuum.io/archive/Anaconda3-2019.03-Windows-x86_64.exe)을 다운받아 진행하였습니다. (클릭시 다운로드 진행)



다운받은 후 실행하시면, 



![tensorflow설치방법-1](https://user-images.githubusercontent.com/24997255/55710227-1f7baf00-5a25-11e9-995b-a713b0736431.PNG)

next



![tensorflow설치방법-2](https://user-images.githubusercontent.com/24997255/55710257-34584280-5a25-11e9-8a5b-5dca7d1d58af.PNG)

All Users



쭉쭉 진행하시면 됩니다!



설치를 완료하시면 Anaconda Navigator를 실행합니다. 

root는 관리자이므로 기본적으로 몇가지 라이브러리가 설치되어있습니다. 



아나콘다의 장점은 다양한 가상환경을 생성하고 여러가지의 가상 환경 중 임의의 가상환경을 선택하여 진행할 수 있다는 것이 가장 큰 장점입니다. 



root 밑에 create를 선택하여 하나의 가상환경을 생성합시다. 

저는 tensorflow라는 가상 환경을 생성하였습니다. 



![tensorflow설치방법-7](https://user-images.githubusercontent.com/24997255/55710755-42f32980-5a26-11e9-9dcd-a4af3c3843a6.PNG)

오른쪽 상단을 보시면 installed, uninstall 등을 선택할 수 있고 검색창이 있습니다. 



![tensorflow설치방법-8](https://user-images.githubusercontent.com/24997255/55710929-a0877600-5a26-11e9-90ad-987d4f18cf13.PNG)

not installed를 선택하시고, tensorflow를 검색하시면 tensorflow 라이브러리를 찾을 수 있습니다. 



![tensorflow설치방법-9](https://user-images.githubusercontent.com/24997255/55711018-d88eb900-5a26-11e9-8932-f401dee3e3f8.PNG)



####  **Tensorflow는 ipython 기반이기 때문에 spyder 또는 jupyter notebook를 통해서만 실행이 가능합니다.** 이클립스에 파이썬을 설치하여 진행해보았더니 get_ipython().run_line_magic('matplotlib', 'inline')에서 에러가 발생하더군요

(tensorflow detection부분에서 다시 설명하도록 하겠습니다.)



#### 제가 아나콘다를 설치하지 않고 Tensorflow를 진행하라고 추천하는 이유

------------------------------------------------------

![tensorflow설치방법-3](https://user-images.githubusercontent.com/24997255/55711387-8306dc00-5a27-11e9-9aad-9855d3d545de.PNG)



제가 아나콘다를 사용하지 않는 큰 이유는 설치되어 있지 않은 라이브러리도 실행 가능(?)하기 때문입니다. 

사진을 보시면 root에는 jupyter book이 설치되어 있고, tensorflow에는 jupyter notebook가 설치되어 있지않습니다. 또한 root에는 tensorflow가 설치되어 있지 않고, tensorflow가상 환경에는  tensorflow 라이브러리가 설치되어 있습니다.

tensorflow 가상환경이 activate되어 있는 상황에서 jupyter notebook이 실행되는 것을 확인할 수 있고, tensorflow가 설치되어 있지 않았다고 나옵니다. (사실상 root 가상환경이랑 동일)

원인을 알 수 없으나 , 이러한 것이 저에게 상당히 불편하다고 느껴졌습니다. (아마, 제가 아나콘다가 미숙하기 떄문이라고 생각됩니다.)

두번째 이유는 굳이 아나콘다를 설치하지 않아도 아나콘다에서 제공하는 라이브러리를 설치할 수 있기 때문입니다. pip 등을 통해서 쉽게 다양한 라이브러리를 설치할 수 있습니다. 





## 개별적으로 다운받아 Tensorflow 설치하기

앞서 언급했듯이 Tensorflow를 하기 위해선 GPU가 있어야 합니다. 

또한 GPU가 있어야 CUDA, cuDNN을 사용할 수 있습니다. 



저는 CUDA 10.0.130 버전/ cuDNN 10.0 (v7.5.56)을 사용하였습니다. 

제가 이렇게 버전을 자세하게 기입한 이유는 Tensorflow를 진행하면서 지원되지 않는 것이 있기 때문입니다. 

(그래서 여러번 재설치를 했었습니다 ㅠㅠ...)

저 버전으로 설치하시면 한번에 성공하실 수 있으실 겁니다 ^^



설치 순서를 정리해드리면, 

1. CUDA 설치
2. cuDNN 설치
3. Python3.x 버전으로 설치(저는 참고로 3.6.8)
4. Tensorflow데이터 깃에서 다운받아 개발 환경 설치(중요)
5. spyder 다운 및 진행(다운 받은 소스 중 오류 몇개 잡아줘야함)



1,2,3 번은 사이트에 접속하여 설치 파일을 다운로드하여 진행하시면 아주 간단합니다!

cuDNN은 회원가입이 필요합니다. 

##### 아, 그리고 참고로 cuDNN 다운받은 후 CUDA 설치 폴더 위치에 추가하여 넣어줘야합니다!!(중요!)

Python을 설치하여야 pip를 사용할 수 있습니다. 



CUDA 다운로드 페이지 : <https://developer.nvidia.com/cuda-toolkit-archive>

cuDNN 다운로드 페이지 : <https://developer.nvidia.com/rdp/form/cudnn-download-survey>

Python 다운로드 페이지 : <https://www.python.org/downloads/>



### Tensorflow 설치 및 Object detection with Tensorflow



Tensorflow는 [Tensorflow github](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/installation.md)에 자세한 설명이 나와있습니다. 여기에 나와있는 글을 천천히 읽어보시면 Tensorflow 설치는 하실 수 있을꺼라 생각합니다. 



밑 내용은 간략하게 요약하여 설명드리겠습니다.



##### tensorflow 설치 (저는 GPU 버전으로 설치하였습니다. CPU 버전은 작업 속도가 느리더라구요...)

```
# For CPU
pip install tensorflow
# For GPU
pip install tensorflow-gpu
```



##### 패키지 설치

```
$ pip install jupyter
$ pip install matplotlib
$ pip install Pillow
```



[Tensorflow github](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/installation.md)에 coco API에 대한 내용이 나오는데 건너뛰셔도 됩니다. (Option)



##### Protobuf Compliation

##### 이 부분이 중요한데, proto 버전이 3.3으로 해야합니다. 저는 처음에 3.7버전으로 했는데 안되서 3.3 버전으로 하니 잘 되더라구요...64bit여도 protoc 3.3 32bit 사용해도 됩니다.

예시

```
# From tensorflow/models/research/
C:\Users\Kim\Desktop\tensorflow\protoc-3.3.0-win32\bin\protoc object_detection/protos/*.proto --python_out=.
```

protoc 앞에 protoc.exe 경로를 다 적어주세요(중요!). 컴터가 멍충해서 경로를 못찾음....



object_detection폴더가 Object detection 관련 폴더인데 tensorflow/models/research/ 안에 있을 겁니다. 

그리고 protobuf를 진행하고 나면 object_detection 폴더 내에 py파일이 많이 생겼을 겁니다. ^^

한번 확인해주세요. 

 

##### object detection을 확인할 수 있는 첫번째 방법 - jupyter notebook

다시 cmd 창을 엽니다. 

jupyter-notebook 엔터를 하시면 jupyter notebook이 실행됩니다. 명령어가 어디는 jupyter-notebook, jupyter notebook 이라고 쳐야 됩니다. 환경마다 다른듯..



저는 jupyter-notebook이라고 쳐야했어요

![tensorflow설치방법-10](https://user-images.githubusercontent.com/24997255/55783446-6337ec80-5ae9-11e9-8165-e801cce736f5.PNG)



Jupyter notebook 화면

![tensorflow설치방법-11](https://user-images.githubusercontent.com/24997255/55783661-e35e5200-5ae9-11e9-8607-ce7440ad8aa1.PNG)



폴더 경로는 protobuf comfile 후 생성된 파일과 함께 복사하여 Tensorflow 하위 폴더로 옮겼습니다. 

사진 제일 하단 보시면 object_detection_tutorial.ipynb파일을 클릭합니다. 



![tensorflow설치방법-12](https://user-images.githubusercontent.com/24997255/55783895-64b5e480-5aea-11e9-8e26-5a5ebeb845f7.PNG)



제일 하단에 이 사진이 보이시면 완성!

그렇지만 아마 안될 겁니다. 그 이유는 실행하시면 import object_detection에서 오류가 날 것입니다. 

util폴더 인가 거기서 오류가 났던 걸로 기억...하여튼 object_detection 오류 나는 문구 모두 삭제하고 다시 진행하시면 됩니다 ^^



##### object detection을 확인할 수 있는 두번째 방법 - spyder

다시 cmd 창을 엽니다. 



spyder를 설치합니다. 

`$ pip install spyder`



spyder 버전을 확인합니다. 아마 spyder3로 설치되었을 겁니다. 

`$ spyder --version`



만약 spyder3이면  cmd창에 `spyder3` 입력합니다. (spyder3 실행)



여기서 중요한 것은 jupyter-notebook 실행한 후 object_detection 폴더 내 object_detection_tutorial.ipynb를 실행합니다. 



file-download클릭 - py파일로 다운합니다. 



spyder 실행 후 상단에 project-new poject-Existing directory 하여 object_detection을 프로젝트 생성합니다. 

![tensorflow설치방법-13](https://user-images.githubusercontent.com/24997255/55784790-3cc78080-5aec-11e9-9179-b8bacafe22ca.PNG)



 object_detection_tutorial.py 파일를 실행합니다. 아마 jupyter와 동일하게 object_detection 오류가 생길텐데 모두 object_detection 문구를 삭제하여 오류를 수정합니다. 



그리고 다시 실행하시면, ipython colsole 창에서 결과물을 확인할 수 있습니다.

![tensorflow설치방법-14](https://user-images.githubusercontent.com/24997255/55786569-72ba3400-5aef-11e9-8021-52eabd04d547.PNG)

완료!



참고로 eclipse python 개발환경에서는 실행이 안됩니다. 

ipython IDE에서만 결과물 확인이 가능합니다. 



여기까지 진행한 후 Realtime Object Detection을 테스트할 수 있습니다. 

약간의 소스 수정을 거치면 웹캠 또는 내장 카메라를 통해서 Object detection이 가능합니다. 



Youtube 영상에 잘 나와있는 것 같아 첨부합니다. 

[Realtime Object Detection with tensorflow](https://www.youtube.com/watch?v=MoMjIwGSFVQ) 관련 영상입니다. 



다음 포스팅에 Realtime Object Detection에 대해서 다뤄보도록 하겠습니다. 