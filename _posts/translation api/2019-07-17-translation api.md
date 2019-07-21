---
layout: post
title:  "Use google translationAPI"
date:   2019-07-10 00:00:00
author: RileyKim
categories: JAVA
tags: JAVA
cover:  "/assets/instacode.png"
---


# 구글 번역 api 사용하기 feat. java, eclipse



구글 번역 인증키 받는 법은 모두 아실꺼라 생각합니다. 

하지만 구글 번역 api 인증키를 받아서 사용하는 법을 알려주는 포스트는 없더군요...



개발환경 : Windows 10 eclipse

사용언어 : java



**해당 소스는 특정한 DB에 접속하여 저장되어 있는 한국어를 영어로 변환하여 보여주는 소스입니다.**

그렇기 때문에 소스를 이해하기 위해선 몇가지 알고 넘어가야하는 내용이 있습니다. 



### 알고 있어야하는 내용.

--------------------------------------

1. 이클립스 자바에서 DB에 접속하는 방법
2. DB Table create, insert, select 
3. 구글 인증키 받는 방법

위의 내용을 모른다면 소스를 이해하기 어려울 수 있습니다..



```java
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

import com.google.cloud.translate.Translate;
import com.google.cloud.translate.Translate.TranslateOption;
import com.google.cloud.translate.TranslateOptions;
import com.google.cloud.translate.Translation;



public class GoogleTranslator {
	public static void main(String[] args) throws Exception {
        //DB 접속
		Connection conn = DriverManager.getConnection("DB_IP", "DB_ID", "DB_Password");
		//실행할 Query
        //테이블 내에 "KO"라는 컬럼이 있습니다. ("KO" : Korean column)
		PreparedStatement pstmt = conn.prepareStatement("select * from DB_Table_name");
		//실행된 결과값을 rs에 저장		
		ResultSet rs = pstmt.executeQuery();
		
        //구글 번역 api 인증키를 사용하여 service 사용하기
		Translate translate = TranslateOptions.newBuilder().setApiKey("Google_translation_api_key").build().getService();
		
        //Query 결과값 한 줄씩 영어로 변환
        //Target : english, Source : Korean
		while (rs.next()) {
			String text = rs.getString("KO"); //"KO" : Korean column name
				Translation translation = 
					translate.translate(text, 
							TranslateOption.sourceLanguage("ko"),
							TranslateOption.targetLanguage("en"));
			String en_text = translation.getTranslatedText();
            
            //print translated english
			System.out.println(en_text);
		}
	
	}
}
```



------------------------------------

Input Source

1. DB_IP
2. DB_ID
3. DB_Password
4. DB_Table_name
5. Google_translation_api_key

---------------------------------------



실행시키면 끝~~



인증키 사용방법 참고

<https://stackoverflow.com/questions/33424349/how-do-you-make-a-request-for-a-translation-with-the-google-translate-v2-api-cli>

