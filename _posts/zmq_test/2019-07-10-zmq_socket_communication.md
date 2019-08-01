---
layout: post
title:  "Socket Communication"
date:   2019-07-10 00:00:00
author: RileyKim
categories: Socket Python
tags: Python
cover:  "/assets/instacode.png"
comments: true
---

# zmq socket communication



개발언어 : python



zmq는 `분산 메세징 라이브러리`이다.  소켓 프로그래밍과 연관이 많은 것 같은데 자세히 알기 위해선 공부가 많이 필요할 것 같다. 

간단히 zmq는 `소켓 통신 라이브러리`라고 생각이 된다. 



------------------------

예를 들자면,  휴대폰과 연관지을 수 있을 것 같다. 

휴대폰을 구매한다 ==> 소켓을 연다.

휴대폰을 개통한다 ==> IP와 PORT를 할당한다. 

전화를 건다 ==> 데이터를 송신한다.

전화를 받는다 ==> 데이터를 받는다.

--------------------------



**zmq_server.py**

```python
import sys
import zmq

ctx = zmq.Context()

def run_server(port, name):
    print("STARTING SERVER")
    sock = ctx.socket(zmq.REP)
    sock.bind(f'tcp://*:{port}')
    print("READY")
    while True:
        message = sock.recv_string()
        print(f'RECEIVED: {message}')
        print(f'SENDING:  {name},{message}')
        sock.send_string(','.join((name, message)))

if __name__ == '__main__':
    run_server(5000, 'kim')
```

`zmq.Context()`를 만든다.  Client에서 `Requset` 가 왔을 때 `Respond`를 하기 위한 소켓`sock=ctx.socket(zmq.REP)` 을 만들었다. `Server`에는 `bind`가 있어야 된다. 이는 Client의 메세지를 받기 위해 열어둔 `ip`, `port`를 의미한다. 

`sock.recv_String()`은 받은 메세지, `sock.send_string()`은 보내는 메세지를 의미한다. 



**zmq_client.py**

```python
import sys
import zmq

ctx = zmq.Context()

def run_client(*ports):
    sock = ctx.socket(zmq.REQ)
    for port in ports:
        sock.connect(f'tcp://localhost:{port}')
    while True:
        line = input('>> ')
        print(f'SENDING: {line}')
        sock.send_string(line)
        rep = sock.recv_string()
        name, message = rep.split(',', 1)
        print(f'RECEIVED: {message} FROM {name}')
        if line == 'bye':
            break
    sock.close()

if __name__ == '__main__':
    run_client(*sys.argv[1:])

```

`zmq.Context()`를 만든다. `sock.connect()`를 통해 접속할 `ip`와 `port`에 연결한다. 

입력한 내용을 `send_string()`을 통해 전달하고, `sock.recv_string`을 통해 응답을 받는다. 응답한 내용에서 `,`를 구분자로 사용하여 응답 내용을 나눈다. 

