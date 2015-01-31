## MuPDF 안드로이드 빌드환경 셋팅하기

1. http://www.mupdf.com/ 에 보면 최신 소스코드를 받을 수 있는 git repo 주소가 있다. 원하는 디렉터리에 클론

	```
git clone --recursive git://git.ghostscript.com/mupdf.git
```


2. 클론한 디렉터리에 README 파일을 읽어보면 기본적인 MuPDF를 위한 스태틱 라이브러리들을 로컬에 설치하는 명령어가 있다.

	```
make prefix=/usr/local install
```

3. ndk 설치

	[https://developer.android.com/tools/sdk/ndk/index.html]()

4. mupdf 디렉터리에서 `platform/android` 에 가서 

	```
ndk-build
```

5. ant 설치 

	```
brew install ant
```

6. 자바 레퍼 빌드하기 

	```
ant debug
```

	이때 잘 안된다면 보통 설치된 안드로이드 sdk 버전이 없어서 그럴 수 있음.

	> android-16 을 설치하던가, (AndroidManifest.xml, project.properties 에서 타겟을 바꿔준다.)


끝!