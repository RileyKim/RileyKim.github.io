---
layout: post
title:  "Install OpenCV easily"
date:   2019-06-18 00:00:00
author: RileyKim
categories: DeepLearning
tags: DeepLearning
cover:  "/assets/instacode.png"
---

# OpenCV 간단하게 설치하는 방법



OS 환경

1. linux (라즈비안)
2. Python3.X 버전 설치(Python 3.5 추천)



본 환경은 우분투나 다른 리눅스 기반의 환경에서도 적용되니, 똑같이 진행하시면 됩니다!



![linux-pip3-1](https://user-images.githubusercontent.com/24997255/58858895-9959ad00-86e3-11e9-8725-010eb0cc55fd.PNG)

날짜를 확인하도록 합니다. 

설정이 제대로 되어 있지 않으면 apt-get update, apt-get upgrade 등이 동작하지 않습니다. 

```sudo date -s  'yyyy-mm-dd hh:mm:ss'``` 로 변경해주시면 됩니다.



![linux-pip3-2](https://user-images.githubusercontent.com/24997255/58859228-3f0d1c00-86e4-11e9-9bc1-9026c601e1b5.PNG)

뭐든지 시작 전 `sudo apt-get update`, `sudo apt-get upgrade`를 해주는 습관을 가지도록 합시다. ㅎ



![linux-pip3-3](https://user-images.githubusercontent.com/24997255/58859326-74196e80-86e4-11e9-9833-55172cbde83b.PNG)

`Opencv`는 `Python3` 기반으로 되어있기 때문에 `PIP3`를 사용해야 합니다. 

필히, `PIP3`를 설치하도록 합니다.



![linux-pip3-4](https://user-images.githubusercontent.com/24997255/58859391-a32fe000-86e4-11e9-9bae-ae184a8674cb.PNG)

설치 완료!



![linux-pip3-5](https://user-images.githubusercontent.com/24997255/58859417-b478ec80-86e4-11e9-867f-f52d0ada9c5d.PNG)

`Opencv`를 설치합니다. 

`Python3.x`, `PIP3`가 설치가 되어 있기 때문에 `opencv-python` 설치가 가능한 것입니다. 



![linux-pip3-8](https://user-images.githubusercontent.com/24997255/58859550-f73ac480-86e4-11e9-826f-c7fe8a417e61.PNG)

설치 완료.



![linux-pip3-9](https://user-images.githubusercontent.com/24997255/58859573-06ba0d80-86e5-11e9-9807-5c9f0bd0618d.PNG)

`Python3`를 실행하여 `import cv2`를 `import`해보았습니다. 

로그를 보시면  `libhdf5_serial.so.100`이 없기 때문에 오류가 발생한 것을 알 수 있습니다. 

해당 내용을 설치하여 해결해주시면 됩니다. 



![linux-pip3-10](https://user-images.githubusercontent.com/24997255/58859673-54cf1100-86e5-11e9-90a5-17b38c0d2678.PNG)

설치.



![linux-pip3-12](https://user-images.githubusercontent.com/24997255/58859729-729c7600-86e5-11e9-83b5-88b503a7d287.PNG)

`libcblas.so.3`이 없어서...오류 발생. 

설치하도록 합시다!



![linux-pip3-14](https://user-images.githubusercontent.com/24997255/58859783-965fbc00-86e5-11e9-98c0-9e8793359fa8.PNG)



설치 완료.



![linux-pip3-15](https://user-images.githubusercontent.com/24997255/58859811-abd4e600-86e5-11e9-9d3c-4faa31342608.PNG)

`libjasper.so.1` 파일이 없습니다. 

이것도 설치하도록 합시다. 



![linux-pip3-16](https://user-images.githubusercontent.com/24997255/58859856-c018e300-86e5-11e9-94b1-37fe6d81241d.PNG)

설치.



![linux-pip3-18](https://user-images.githubusercontent.com/24997255/58859881-cad37800-86e5-11e9-9c2f-a3e1adab1202.PNG)

`libQtTest.so.4` 파일이 없습니다. 

설치합시다. 



![linux-pip3-19](https://user-images.githubusercontent.com/24997255/58859927-e179cf00-86e5-11e9-836f-6638bcaa779b.PNG)

설치.



![linux-pip3-21](https://user-images.githubusercontent.com/24997255/58859950-ef2f5480-86e5-11e9-91e3-8e152b93ff62.PNG)

`Python3`를 실행합니다. `import cv2`를 실행한 후 `cv2.__version__`을 통해 Opencv 버전을 확인합니다. 



이상입니다-