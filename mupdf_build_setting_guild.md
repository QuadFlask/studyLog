## MuPDF 안드로이드 빌드환경 셋팅하기 (1.6 버전)

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

5. ant 설치 (설치되있지 않았을때...)

	```
brew install ant
```

6. 자바 레퍼 빌드하기 

	```
ant debug
```

	이때 잘 안된다면 보통 설치된 안드로이드 sdk 버전이 없어서 그럴 수 있음.

	> android-16 을 설치하던가, (AndroidManifest.xml, project.properties 에서 타겟을 바꿔준다.)


7. 라이브러리를 모든 플랫폼으로 빌드하고 싶을 때 (기본적으론 `armeabi-v7a` 만 빌드된다.)
	
	`jni/Application.mk` 에서 `APP_ABI := all` 로 변경한뒤, `ndk-build` 를 하면,

`arm64-v8a`, `x86_64`, `mips64`, `armeabi-v7a`, `armeabi`, `x86`, `mips`

를 빌드한다. 꽤 오래 걸린다...(MacBook Pro (Retina, 15-inch, Mid 2014) i7 2.5GHz, 16GB 로 15분(+-5) 정도?)
	
이렇게 빌드가 끝나면 `libs` 디렉터리에 각 cpu플랫폼에 대해서 빌드된녀석들이 나오는데, 총 용량이 69M 이 된다.

이 모든것을 앱에 임베드 시키기엔 부담스러운데, 64 비트를 뺀다면 29.7M 이 된다. 또 mips 디바이스는 거의 없기때문에(뭔지 자세히 몰라서 [검색](https://www.google.co.kr/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8#newwindow=1&q=android+mips+devices+list)했는데 [스택오버플로에 답변](http://stackoverflow.com/questions/25052234/statistics-about-android-devices-with-mips-processors)으론 2개의 공식적인 디바이스를 보았다고 하니 지원하지 않아도 될듯 하다. 결국, arm, x86만 지원하면 되기에, 18.7M 이 된다. 뭐 이정도는 납득가능해 보인다.


끝!
