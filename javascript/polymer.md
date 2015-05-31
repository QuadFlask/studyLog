Quick tour of Polymer
--------------

폴리머는 선언적으로 웹 컴포넌트를 만들기 쉽게 한다.

커스텀 엘리먼트는 폴리머의 특수한 기능으로 보일러플레이트를 줄이고 복잡하고 인터넥티브한 엘리먼트들을 더 쉽게 만들 수 있도록 도와준다.

- 엘리먼트 등록하기 
- 라이프 사이클 콜백들
- 프로퍼티 관찰
- 로컬 돔 템플릿
- 데이터 바인딩

이 섹션에선 아무것도 설치하지 않고 폴리머 라이브러리의 퀵 투어를 볼 수 있다. Edit on Plunker 버튼을 눌러 어떤 샘플이든 인터렉티브 샌드박스에서 열어볼 수 있다.

각각의 피쳐에 대한 더 자세한 내용에 대해선 [Developer guide](https://www.polymer-project.org/1.0/docs/devguide/feature-overview.html)를 확인하라.

## 엘리먼트 등록하기 

브라우저에 새로운 앨리먼트를 등록하기 위해선 `Polymer` 함수를 호출한다. 앨리먼트를 등록하는것은 프로토타입과 함께 태그네임과 연관되어 커스텀 엘리먼트에 프로퍼티와 매서드를 추가할 수 있다.

`Polymer`함수는 앨리먼트의 프로토타입으로 정의된 하나의 오브젝트 인자를 받는다.

sample


이 샘플은 초기화 됬을 때 contents를 `<proto-element>`에 추가하기 위해 라이프사이클 콜백을 사용한다. 커스텀 엘리먼트의 초기화가 끝나면 `ready` 라이프사이클 콜백이 호출된다. `ready` 콜백은 생성자처럼 초기화 작업을 하기 좋은 곳이다.

[Learn more: Element registration]()

[Learn more: Lifecycle callbacks]()

## 로컬 돔 추가하기

많은 앨리먼트들은 앨리먼트의 UI와 동작을 구현하기 위해 몇가지 내부 돔 노드(internal DOM nodes)를 포함한다. 폴리머는 이것을 로컬 돔(local DOM)이라고 부르고 쉽게 구성할 수 있는 방법을 제공한다.

sample

로컬 돔은 앨리먼트의 내부를 캡슐화 한다.

[Learn more: Local DOM]()

## 로컬돔으로 조합하기(Composition with local DOM)

로컬돔은 조합을 조작할 수 있게 해준다. 앨리먼트의 자식들은 로컬 돔 트리에 추가된대로 분배되어 렌더링 된다.

이 예제는 스타일된 `<div>`태그로 이미지를 감싸는 간단한 태그를 만든다.

sample

> Note: `<dom-module>`안에 정의된 CSS 스타일은 앰리먼트의 로컬 돔에 한정된다. 따라서 `div`룰은 오직 `<picture-frame>` 태그 안의 `<div>` 에만 적용된다.

[Learn more: Composition & Distribution]()

## 데이터 바인딩

당연하게도 정적 로컬돔으로는 충분하지 않다. 로컬돔의 앨리먼트들을 동적으로 업데이트하고 싶을것이다.

데이터 바인딩은 앨리먼트에 변화를 빠르게 전개(propagate)하는 좋은 방법이며 보일러 플레이트 코드를 줄인다. 더블 머스태치(`{{}}`)문법을 사용해 컴포넌트의 프로퍼티에 바인딩을 할 수 있다. `{{}}`는 프러퍼티의 값으로 대체한다.

sample

[Learn more: Data binding]()

## 정의된 프로퍼티

프로퍼티들은 앨리먼트의 public API의 중요한 부분이다. 폴리머틑 *정의된 프러퍼티들*은 자주 사용하는 패턴(common patterns)의 프로퍼티들을 많이 제공한다 - 기본값을 셋팅하거나, 마크업으로 부터 프로퍼티를 설정하거나, 프로퍼티의 변화를 관찰(observing)하거나 등등.

아래의 예제에선 `owner` 프로퍼티를 기본값과 함께 정의했고, 이 값을 `index.html`에서 설정했다.

sample

[Learn more: Declared properties]()

### 프로퍼티에 바인딩 하기

추가로, 텍스트 컨텐츠에 엘리먼트의 프로퍼티를 바인드 할 수 있다.(`property-name="{{binding}}`을 이용해서) 폴리머 프로퍼티들은 옵셔널하게 2-way 바인딩을 지원한다.

이 예제는  2-way 바인딩을 이용한다: 커스텀 인풋 엘리먼트(`iron-input`)의 값을 엘리먼트의 `owner`프로퍼티에 바인딩하여 유저의 입력에 따라 업데이트 된다. 

> Note: `iron-input` 애트리뷰트는 확장 타입 커스텀 엘리먼트(type-extension custom element) 인풋을 나타낸다; 네이티브 인풋을 확장한다.

## 다음 단계

이제 자신만의 앨리먼트를 만드는 방법을 알게 되었으니, 첫번째 폴리머 프로젝트를 만들기 위해 코드를 받거나, 디벨로터 가이드를 더 깊이 파라.

계속: 
[Get the Code]() 

[Developer Guide]()


-------------------------------

# Feature Overview
기능 둘러보기

폴리머 라이브러리는 커스텀 엘리먼트를 만들기 위한 여러가지 기능(feature)를 제공한다. 이러한 기능은 스탠다드 돔 엘리먼트처럼 더 쉽고 빠르게 커스텀 엘리먼트를 만들고 동작하게 만들어 준다. 

스탠다드 돔에 대해서 이렇게 예상할것이다.

- 생성자 또는 `document.createElement`를 통해서 생성한다.
- 애트리뷰트 또는 프로퍼티를 통해 설정한다
- 각각의 인스턴스에 대해 만들어진 몇가지 내부 돔을 가질 수 있다?(It may have some internal DOM that’s created for each instance.)
- 프로퍼티와 애트리뷰트 변경에 대해 반응한다.(예를들어 데이터를 돔으로, 또는 이벤트 발생)
- 기본 스타일을 가지고 외부에서 스타일 될 수 있다. 
- 내부 상태를 조작할 수 있는 방법을 제공한다. 

기본적인 폴리머 엘리먼트는 아래와 같다. 

```html
<dom-module id="element-name">
  <style>
    /* CSS rules for your element */
  </style>
  <template>
    <!-- local DOM for your element -->

    <div>{{greeting}}</div> <!-- data bindings in local DOM -->
  </template>
</dom-module>

<script>
  // element registration
  Polymer({
    is: "element-name",

    // add properties and methods on the element's prototype

    properties: {
      // declare properties for the element's public API
      greeting: {
        type: String,
        value: "Hello!"
      }
    }
  });
</script>
```

이 가이드는 기능들을 아래와 같이 그룹으로 나눈다:

- [등록과 라이프 싸이클]() 엘리먼트 이름과 클래스가 연관된 커스텀 엘리먼트를 등록한다. 앨리먼트는 자신의 라이프 사이클을 관리하기 위한 콜백을 제공한다. 코드를 공유하기 위해 행동을 사용한다.(Use behaviors to share code.)

- [정의된 프로퍼티들]() 정의된 프로퍼티들은 마크업의 애트리뷰트를 통해 설정될 수 있다. 정의된 프로퍼티들은 옵셔널하게 변경 옵저버(optionally support change observers), 2-way 데이터 바인딩, 애트리뷰트 리플렉션을 제공한다. 또한 계산된 프로퍼티들 그리고 읽기전용 프로퍼티를 정의할 수 있다.

- [로컬 돔; Local DOM](). 로컬 돔은 엘리먼트에 의해 생성되고 관리되는 돔이다.(Local DOM is the DOM created and managed by the element.)

- [이벤트](). 호스트 오브젝트 그리고 로컬 돔 자식에 이벤트 리스너를 붙이는 것이다. Event retargeting.?

- [데이터 바인딩](). 프로퍼티 바인딩. 애트리뷰트에 바인딩 하는것.

- [동작? 행동?; Behaviors](). Behavior는 폴리머 앨리먼트와 혼합되는? 재사용 가능한 코드의 모듈이다. (Behaviors are reusable modules of code that can be mixed into Polymer elements.)

- [유틸리티 함수들](). 공통된 태스트에 대한 핼퍼 매소드들

- [실험용 피쳐와 앨리먼트](). 실험용 템플릿과 스타일링 피쳐들. 


-------------------------------

# Registration and lifecycle

## 커스텀 엘리먼트 등록하기

커스텀 엘리먼트를 등록하기 위해선, `Polymer` 함수를 사용하고 새로운 엘리먼트에 대해 프로토타입을 넘겨주면 된다. 프로토타입은 반드시 HTML 태그 이름을 명시하는 `is` 프로퍼티를 가지고 있어야 한다.

example

```javascript
// register an element
MyElement = Polymer({

  is: 'my-element',

  // See below for lifecycle callbacks
  created: function() {
    this.innerHTML = 'My element!';
  }

});

// create an instance with createElement:
var el1 = document.createElement('my-element');

// ... or with the constructor:
var el2 = new MyElement();
```

`Polymer` 함수는 브라우져에 엘리먼트를 등록하고, 코드로 앨리먼트의 인스턴스를 만들 수 있는 생성자를 리턴한다.

`Polymer` 함수는 커스텀 엘리먼트의 프로토타입 체인을 만들고(set up) 폴리머 `Base` 프로토타입에 체이닝한다.(폴리머의 값 추가 피쳐(?value-added features)를 제공하는) 따라서, 자신만의 프로토타입 체인을 설치(set up)할 수 없다. 하지만 엘리먼트간 코드 공유를 위해 [프로토타입 믹스인(prototype mixins)]()를 사용할 수 있다.

> Note: 메인 HTML 도큐먼트에 엘리먼트를 정의하는것은 아직 지원하지 않음.

## 커스텀 생성자 정의하기 

`Polymer` 함수는 커스텀 엘리먼트를 초기화하는데 사용될 수 있는 기본 생성자를 리턴한다. 생성자에 인자를 넣어 새 엘리먼트를 설정 위해선  프로토타입에  커스텀  `factoryImpl` 함수를 기술할 수 있다.

`Polymer` 함수로 부터 리턴된 생성자는 `document.createElement` 를 통해 새 인스턴스를 만들 수 있고, 유저가 제공한 `factoryImpl` 함수를  엘리먼트 인스턴스에 바인딩된 this와 함께 호출한다. 실제 생성자에 넘겨지는 모든 인자들은 `factoryImpl`함수에 넘겨진다.(Any arguments passed to the actual constructor are passed on to factoryImpl function.)

example:
```javascript
MyElement = Polymer({

  is: 'my-element',

  factoryImpl: function(foo, bar) {
    this.foo = foo;
    this.configureWithBar(bar);
  },

  configureWithBar: function(bar) {
    ...
  }

});

var el = new MyElement(42, 'octopus');
```

https://www.polymer-project.org/1.0/docs/devguide/registering-elements.html

# Developer Guide

















