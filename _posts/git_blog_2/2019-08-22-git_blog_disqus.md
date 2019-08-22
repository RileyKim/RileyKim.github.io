---
layout: post
title:  "Install Disqus at GitBlog"
date:   2019-08-22 00:00:00
author: RileyKim
categories: GitBlog
tags: GitBlog
cover:  "/assets/instacode.png"
comments: true
---

# Git Blog에 댓글 추가하기(Feat. Disqus)



깃블로그 포스팅에 대해 피드백을 얻을 수 있는 좋은 방법 중 하나는 댓글입니다. 

**Disqus를 통해 GitBlog에 댓글 기능을 추가하도록 하겠습니다. **



그전에 DIsqus에 대해 간략히 알아보겠습니다. 

**Disqus는 네트워크 플랫폼을 사용하는 모든 전세계 블로그의 호스팅 서비스**라고 생각하시면 됩니다. 



##### 댓글을 추가하기 위해선 다음의 3단계를 진행하면 됩니다. 

----------------------

1. DIsqus 가입하기
2. Disqus 설정하기
3. GitBlog와 Disqus 연동하기
4. post 작성



### 1. Disqus 가입하기

---------------

![Git_Blog_Disqus_1](https://user-images.githubusercontent.com/24997255/62588137-9c4d6580-b8ff-11e9-870a-3441fcc3dfe4.PNG)

**Get Started - 회원가입을 하도록 합니다!**



### 2. Disqus 설정하기

--------------------------------

![Git_Blog_Disqus_2](https://user-images.githubusercontent.com/24997255/62588167-bab36100-b8ff-11e9-8f2e-751d2dadd54d.PNG)

**I want to install Disqus on my site 클릭**



![Git_Blog_Disqus_3](https://user-images.githubusercontent.com/24997255/62599909-78524a00-b928-11e9-84d0-ad1012903842.PNG)

**Site를 생성하도록 합시다.**

Website Name은 RileyKim으로 하였습니다. 



![Git_Blog_Disqus_4](https://user-images.githubusercontent.com/24997255/62600007-b3ed1400-b928-11e9-9830-909b245fe5b5.PNG)

Website URL은 본인이 사용할 사이트 또는 블로그의 URL을 입력하시면 됩니다!

설정 끝!!!!!!!!!!!!



**Shortname은 GitBlog와 연동시 사용됩니다. 꼭 알아두세요**



### 3. GitBlog와 Disqus 연동하기

--------------------

Gitblog와 Disqus를 연동하기 위해선 2가지의 요소가 필요합니다. 

1. _config.yml 수정
2. _incluedes폴더 내 disqus.html파일 추가



#### 3-1. _config.yml 수정

----------------------

먼저 _config.yml파일을 수정하도록 합니다. 

_config.yml파일내 disqus 댓글을 적용하기 위한 소스가 있을 겁니다.

그 소스는 잘 못된 것이니 지워버리고 다음과 같이 수정합니다.  혹은 없다면 추가한다. 

![Git_Blog_Disqus_5](https://user-images.githubusercontent.com/24997255/62606474-498fa000-b937-11e9-8bc8-e470cfe8fa02.PNG)



**disqus : [Shortname]**



![Git_Blog_Disqus_4](https://user-images.githubusercontent.com/24997255/62600007-b3ed1400-b928-11e9-9830-909b245fe5b5.PNG)

**disqus site - genernal에서 확인할 수 있습니다. **



--------------

![Git_Blog_Disqus_6](https://user-images.githubusercontent.com/24997255/62606655-aa1edd00-b937-11e9-9261-06eb2211d39d.PNG)

-----------------

**나의 Shortname은 https-rileykim-github-io**



#### 3-2. _includes폴더 내 disqus.html파일 추가

----------------

![Git_Blog_Disqus_7](https://user-images.githubusercontent.com/24997255/63253159-48059680-c2ac-11e9-9aa5-8f0146f7519d.PNG)

**Jekyll 선택**



**dusqus.html **

![Git_Blog_Disqus_9](https://user-images.githubusercontent.com/24997255/63497017-efc5d300-c4fd-11e9-9b63-7b48cdfc4dda.PNG)

**dusqus.html  Code**

```html
<div id="disqus_thread"></div>
<script>

/**
*  RECOMMENDED CONFIGURATION VARIABLES: EDIT AND UNCOMMENT THE SECTION BELOW TO INSERT DYNAMIC VALUES FROM YOUR PLATFORM OR CMS.
*  LEARN WHY DEFINING THESE VARIABLES IS IMPORTANT: https://disqus.com/admin/universalcode/#configuration-variables*/
/*
var disqus_config = function () {
this.page.url = PAGE_URL;  // Replace PAGE_URL with your page's canonical URL variable
this.page.identifier = PAGE_IDENTIFIER; // Replace PAGE_IDENTIFIER with your page's unique identifier variable
};
*/
(function() { // DON'T EDIT BELOW THIS LINE
var d = document, s = d.createElement('script');
s.src = 'https://https-rileykim-github-io.disqus.com/embed.js';
s.setAttribute('data-timestamp', +new Date());
(d.head || d.body).appendChild(s);
})();
</script>
<noscript>Please enable JavaScript to view the <a href="https://disqus.com/?ref_noscript">comments powered by Disqus.</a></noscript>
```

_includes폴더에 disqus.html 파일을 생성합니다. 



#### 3-3 . _config.yml 수정

----------------------------------------

**_config.yml **

![Git_Blog_Disqus_10](https://user-images.githubusercontent.com/24997255/63497155-33b8d800-c4fe-11e9-88e0-9c396da33aad.PNG)



몇몇 블로그에 다양한 방법이 서술되어 있는데 할 필요없습니다. 안됩니다....

분명히 그런 블로그들은 본인이 안했거나 어디서 복사한 것이겠죠....? 하...

 저도 처음에 그 부분 따라하다가 안되서 한동안 헤맸습니다...

하나만 하시면 됩니다. 

 **disqus : (Shortname)** 넣어주세요

보통 주석처리가 되어있을 겁니다. 확인하시고 없으면 작성해주세요.



**Shortname**

![Git_Blog_Disqus_6](https://user-images.githubusercontent.com/24997255/63497460-bcd00f00-c4fe-11e9-933c-b9ffc9ef317e.PNG)



### 4. Post 작성

-------------

Post 작성해보신 분들은 아시겠지만, ```.md```  최상단에 title, date 등을 넣습니다. 

그 안에 **comments: true**만 넣어주시면 됩니다. 



![Git_Blog_Disqus_8](https://user-images.githubusercontent.com/24997255/63497734-5f888d80-c4ff-11e9-992b-e2fdbb9a9b16.PNG)

1번 항목과 같이 해주시면 됩니다!



**완성된 Disqus**

![Git_Blog_Disqus_11](https://user-images.githubusercontent.com/24997255/63497855-a8d8dd00-c4ff-11e9-9e9f-08ba013c914a.PNG)

