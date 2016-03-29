# Javascript OOP
[참고-aji님](https://github.com/niceaji/javascript-study/blob/gh-pages/doc/oop.md)

# ECMA 2015 style

`class` 키워드가 추가되었다. 그래서 프로토타입이 어쩌고 이럴필요 없음ㅋㅋ

```javascript
class Laptop {
  constructor(owner) {
    this.owner = owner;
  }
}

class MacBook extends Laptop {
  constructor(owner, spec) {
    super(owner);
    this.spec = spec;
  }
}
```

심지어 `static`, `get`, `set` 도 추가되었다....

[참고: https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Classes](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Classes)


---------------

# ECMA 5 style

## 객체

JS에서는 함수도 객체. 그래서 객체 만들때 함수를 가지고 만드는건가?

```javascript
function MyObject(){
  this.age = 23;
  this.name = "Flask";
  this.someTag.click(this.getAge());
}
```
이게 생성자가 되는듯.
내부에는 맴버 변수를 선언할 수 있음.

### 맴버 함수 선언

여러가지 방법이 있는데 그중 추천할만한 방법 -> `prototype`!

```javascript
MyObject.prototype = function{
  getAge: function(){
    return this.age;
  },
  getName: function(){
    return this.name;
  },
  

}
```

여기서 중요한것! `this`!!

함수를 실행하는 곳의 스코프를 사용(?) 하게 되서, 저기 ** `this`가 `MyObject`의 인스턴스가 아니게됨**.


#### 해결하는 방법

1. 인자로 넘겨주기

```javascript
var that = this;
```
이런식으로 `that`(=`this`)을 전달해줌.
> 하지만 코드가 더러워 질 수 있음....ㅠㅠ


2. `bind()` 하기

```javascript
...
{
  myObject.getAge().bind(this);
}
...
```


## 즉시 실행 함수

이번 MICE IT 기말 과제를 하다가 중간과제때 가르쳐 주신것을 사용해봄.ㅋ

```javascript
(function($){
  ...
})(jQuery);
```

이런식으로 괄호로 싸서 선언과 동시에 실행이 되는?

이렇게 하면 나중에 js 합치기(minimize?)할때 함수 꼬이는 일 없이 됨.?ㅋ

과제에서는 파일 구조가

app.js
mynote.js
util.js
config.js

이렇게 되있음.

#### util.js
```javascript
var myNoteApp = {};

(function($, app){
  app.IS_DEBUG           = true;
	app.LOCAL_STORAGE_NAME = "note";
	app.SAVE_FILE_NAME     = app.LOCAL_STORAGE_NAME + ".html";
})(jQuery, myNoteApp);
```

> 여기서 빈 객체를 리러터럴로 생성한뒤, 즉시실행함수에 인자로 전달해줌.

#### app.js
```javascript
(function($, ap){
  function App(){
		this.init();
	}
	
	App.prototype = {
		init:function(){
			$('#mynote').mynote();
		}
	}
	window.app = new App();
})(jQuery, myNoteApp);
```

> 여기도 똑같이 인자로 전달해주게 됨.

* [jQuery custom function](https://www.google.co.kr/search?q=jquery+custom+function&oq=jquery+custom+function&aqs=chrome.0.57j0l3j62l2.246j0&sourceid=chrome&ie=UTF-8) 만들기

[redactor](http://imperavi.com/redactor/) 사용하다가, 이상하게 jQuery의 함수처럼 쓰는것을 보고 찾아봄.
```javascript 
$.fn.myFunc = function(){
  ...  
}
```

이렇게 하면 jQuery의 맴버함수 처럼 사용할 수 있음! (저기 app.js의 `mynote()` 함수 호출하는것처럼ㅋ)

