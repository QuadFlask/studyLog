# [AndroidAnnotations 사용법](https://github.com/excilys/androidannotations/wiki)

[위키](https://github.com/excilys/androidannotations/wiki)

[다운로드](https://github.com/excilys/androidannotations/wiki/Download)

[이클립스 설정방법](https://github.com/excilys/androidannotations/wiki/Eclipse-Project-Configuration)


간단하게 말하자면, 
`XXX-api.jar` 은 실제로 `apk`에 포함되는것이고, `XXX.jar`은 컴파일타임에 필요한것!

`XXX-api.jar`  ->  `libs` 폴더에
`XXX.jar`  ->  절대 `libs` 폴더가 아닌 다른 폴더에 넣어야! `compile-libs` 폴더로.

마지막으론 프로젝트 속성에서 자바 컴파일러에서 어노테이션 프로세싱에 체크!, 팩토리 패스엔 XXX.jar 을 추가.



## [FirstActivity](https://github.com/excilys/androidannotations/wiki/FirstActivity)


엑티비티에 `@EActivity` 어노테이션을 반드시 추가해준다. 이렇게 해주면 자바 어노터에션 처리 툴(APT)가 처리를 하는데, 
이때 이 엑티비티를 상속한 엑티비티가 만들어진다. 네이밍은 뒤에 언더스코어`_` 가 붙은것으로.

따라서, `AndroidManifest.xml` 파일에서 액티비티를 바꿔줘야 한다.


테스트 해보니, `onCreate()`에서는 안먹히는건가? (아무래도 `super.onCreate()`가 먼저 선행되기 때문에 뷰를 못가져온 산태에서 호출하니 그런듯.)


그럼 초기화는 어떻게 하지?
이것또한 어노테이션으로 제공된다. 두가지 정도 있는거 같은데,,,

[`@AfterViews`](https://github.com/excilys/androidannotations/wiki/Enhance-custom-classes#executing-code-after-dependency-injection)

view 바인딩이 끝나면 호출됨


[`@AfterInjection`](https://github.com/excilys/androidannotations/wiki/Enhance-custom-classes#executing-code-after-dependency-injection)

이것은 뷰바인딩보다는 다른 속성?들의 Injection이 끝난뒤 호출되는것인듯.


Roboguice는 RoboActivity를 상속해야되던데 그러면 좀 제한적인듯....흐음..;; AndroidAnnotations 가 나은거 같기도...


## 팁



