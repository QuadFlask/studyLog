Gradle Signing Setting
---------


#### gradle.properties

프로젝트의 gradle.properties 세팅

keystore 파일 위치, 비번, alias 이름, 비번 정보를 적어준다. 

**반드시 `.gitignore` 에 등록시켜야 함!!**

```
RELEASE_STORE_FILE=...
RELEASE_STORE_PASSWORD=...
RELEASE_KEY_ALIAS=...
RELEASE_KEY_PASSWORD=...
```


#### build.gradle

앱(모듈)의 build.gradle 세팅

```groovy

signingConfigs {
	release {
		storeFile file(RELEASE_STORE_FILE)
		storePassword RELEASE_STORE_PASSWORD
		keyAlias RELEASE_KEY_ALIAS
		keyPassword RELEASE_KEY_PASSWORD
	}
}

buildTypes {
	release {
		minifyEnabled false
		proguardFiles getDefaultProguardFile('proguard-android.txt'), 'proguard-rules.pro'
			signingConfig signingConfigs.release
	}
}

```

