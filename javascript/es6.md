ES6
-----------------

## [Generator function](http://davidwalsh.name/es6-generators)

[MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function*)


제너레이터는 함수 실행 컨텍스트에서 나갔다가 다시 들어올 수 있는 함수. 컨텍스트는(변수 바인딩) 다시 들어왔을때에도 저장된다. -> 그래서 제너레이터(뭔가 생성하는)라고 부르는듯
> Generators are functions which can be exited and later re-entered. Their context (variable bindings) will be saved across re-entrances.

제너레이터 함수를 호출하는것은 그 바디를 바로 실행하지 않는다;그 함수의 이터레이터 오브젝트를 대신 리턴한다. 이터레이터의 `next()`  매서드가 호출되면, 값을 리턴하는 첫 `yield` 표현식을 만날때까지 제너레이터 함수의 바디가 실행된다.? 또는 `yield*` 로 다른 제너레이터에게 대리
> Calling a generator function does not execute its body immediately; an iterator object for the function is returned instead. When the iterator's next() method is called, the generator function's body is executed until the first yield expression, which specifies the value to be returned from the iterator or, with yield*, delegates to another generator function. The next() method returns an object with a value property containing the yielded value and a done property which indicates whether the generator has yielded its last value.


기본적인 문법은 그냥 정의할때 *을 붙임.

```javascript
function* foo(){
}
```

하지만 `yield` 표현식이 있어야 진정한 generator?

일단 외우기 쉽게 하기 위해서 그냥 *양보 리턴* 이라고 생각하면 쉬운듯

양보 한다는것은 `yield` 표현식이 나왔을때 현재 함수 실행을 멈추고 다른 일을 하도록, 

리턴 한다는것은 `yield` 표현식을 리턴한다는것임

ex)

```javascript
function *foo(x) {
    var y = 2 * (yield (x + 1));
    var z = yield (y / 3);
    return (x + y + z);
}

var it = foo( 5 ); // 제너레이터를 생성하고(호출이 아님, 생성임. 그런데 왜 new 키워드가 없을까?),

// note: not sending anything into `next()` here
console.log( it.next() );       // { value:6, done:false } 생성할때 5를 넣어주었으니, 
console.log( it.next( 12 ) );   // { value:8, done:false }
console.log( it.next( 13 ) );   // { value:42, done:true }
```

1. `console.log( it.next() );`: 생성할때 5를 넣어주었으니, `var y = 2 * (yield (x + 1));` 에서 x 값에 5를 받고 `(x+1)` 를 리턴

2. `console.log( it.next( 12 ) )`: x 값에 12를 받고, `var z = yield (y / 3);` 에서 `y/3` 리턴

3. `console.log( it.next( 13 ) );`: x 값에 13을 받고, 마지막으로 `return (x + y + z);` 리턴


좀더 유용한 예제

### Genterator interator

```javascript
function *foo() {
    yield 1;
    yield 2;
    yield 3;
    yield 4;
    yield 5;
}

var it = foo();

console.log( it.next() ); // { value:2, done:false }
console.log( it.next() ); // { value:3, done:false }
console.log( it.next() ); // { value:4, done:false }
console.log( it.next() ); // { value:5, done:false }

console.log( it.next() ); // { value:undefined, done:true }
```

> 마지막에 return 을 안넣는 이유? -> for .. of 문에서 마지막 리턴은 씹어버림.

```javascript
function *foo() {
    yield 1;
    yield 2;
    yield 3;
    yield 4;
    yield 5;
    return 6;
}

for (var v of foo()) {
    console.log( v );
}
// 1 2 3 4 5

console.log( v ); // still `5`, not `6` :(
```



## [ES6 Overview in 350 Bullet Points](https://ponyfoo.com/articles/es6)


> ES6, Harmony, ES2015 는 같은 스팩을 지칭하는것. 하지만 ES2015가 정식 이름이 되었고, 이제부턴 ESXXXX 식으로 년도가 붙는 네이밍을 쓴다고 함. 그리고 매년 새 스펙이 나올거라능!! 벤더로 하여금 좀 더 새로운 피쳐들을 추가하는것을 장려하기위해...?


### Assignment Destructuring

> requirejs? 에서 처음 봤던 표현법인데 알고보니 언어 기능이었던!

```javascript
var {foo} = pony;
// 는 아래와 같음
var foo = pony.foo;

// 심지어 배열에도 가능함
[a,b] = [0,1]
// a = 0, b = 1

[a,,b] = [0,1,2]
// a = 0, b = 2 이렇게 스킵!

// 게다가 추가적인 변수없이 스왑으로도 사용 할 수 있다
[a,b] = [b,a]

// 함수에도 사용 한다!! 근데 잘 이해가 안되네

```


### Spread Operator and Rest Parameters

> 나머지(rest) 파라미터는 기존 `argument` 보다 나음
> 
> 자바에서처럼 `...` 을 사용가능 하도록.

```javascript
// 배열을 함수에 파라미터로 주고 싶을때 `apply`를 사용하지 말고 rest를 사용하자!
fn(...[1,2,3]) // == fn(1,2,3)

// 배열 중간에 붙이기도 쉽다!
[1, 2, ...[3, 4, 5], 6, 7]

// 게다가 디스트럭쳐링도 쉽도!!
[a, , ...rest] = [1,2,3,4,5]
// a = 1, rest = [3,4,5]

// new 할때 대입도 쉽다!!
new Date(...[2015, 10, 24])
```

### Arrow Functions

> 화살표 연산자...인데 자바(->)랑 달라서 계속 헷갈린다..
> 
> 구문적 스코프를 따르고(즉, this는 밖(부모)의 this와 같다)
> 
> `call`, `apply`같은 리플랙션 타입의 함수로 수정 할 수 없다.


### Template Literals

> 오!! 있었구나
> 
> ` 로 감싸면 되고, 리플레이스먼트부분은 jstl처럼 ${} 를 쓰면됨
> 
> ${} 안에 들어갈 식은 올바른 자바스크립트 표현식이면 됨. 변수나, 함수 호출 등


### Object Literals

> ES2015 오면서 신택스 슈가가 많이 추가된듯
> 
> 패스


### Classes

> 전통적인 클래스가 아니라 프로토타입기반의 상속의 신택스 슈가
> 
> `class`, `extends`, `static` 등의 키워드가 추가되었다

### Let and Const

> 변수 선언방법
> 
> `let`은 구문적 스토프, 블록 맨 위로 호이스팅되고(var 는 함수의 맨 위로 호이스팅되는 반면)
> 
> “Temporal Dead Zone” – TDZ for short

- Starts at the beginning of the block where let foo was declared
- Ends where the let foo statement was placed in user code (hoisiting is irrelevant here)
- Attempts to access or assign to foo within the TDZ (before the let foo statement is reached) result in an error
- Helps prevent mysterious bugs when a variable is manipulated before its declaration is reached

> 
> const는 상수 선언시 사용할 수 있고, 또한 블록 스코핑 호이스팅, TDZ
> 
> 중요! 할당은 반드시 해야 하고, 할당 실패시 조용히 실패함(즉, 스트릭트 모드를 써라! 그럼 익셉션이 발생할지니!)
> 
> ES6에선 함수는 블록 스코프임


### Symbols

> 새로운 프리미티브 타입!
> 
> `var symbol = Symbol()`로 새 심볼을 만들 수 있다.
> 
> `Symbol('foo')`로 디스크립션을 추가할 수도 있다 -> 디버깅하기 위한 용도로
> 
> 심볼은 이뮤터블, 유니크 하다. 타입은  `'symbol'`이므로 `typeof Symbol() === 'symbol'` 
> 
> `Symbol.for(key)` 글로벌 심볼을 만들 수 있다.
> 
> 역함수(ㅋㅋ?)로 `Symbol.keyFor(symbol)`로 키를 가져올 수 있음
> 
> 어따가 쓰는거지??? 


### Iterators

> 잘 알려진 `Symbol`이 이터레이터에 다른 오브젝트들을 할당하는데에 사용된다?
> 
> `var foo = { [Symbol.iterator]: iterable }` or `foo[Symbol.iterator] = iterable`
> 
> `iterable`은 `next`매서드를 가진 `iterator`를 리턴하는 매서드
> `next`매서드는 `value`,`done` 두 프롭을 가진 옵젝을 리턴
> 
> `value`는 현재 이터레이트 되는 시퀀스의  현재 값
> 
> `done`는 더이상 할 아이템이 이터레이터에 남아 있지 않다는 플래그 프롭

- Objects that have a [Symbol.iterator] value are iterable, because they subscribe to the iterable protocol
- Some built-ins like Array, String, or arguments – and NodeList in browsers – are iterable by default in ES6
- Iterable objects can be looped over with for..of, such as for (let el of document.querySelectorAll('a'))
- Iterable objects can be synthesized using the spread operator, like [...document.querySelectorAll('a')]
- You can also use Array.from(document.querySelectorAll('a')) to synthesize an iterable sequence into an array
- Iterators are lazy, and those that produce an infinite sequence still can lead to valid programs
- Be careful not to attempt to synthesize an infinite sequence with ... or Array.from as that will cause an infinite loop


### Generators

> 이건 위에서도 설명을 했으니,,,, 중요, 몰랐던 부분만
> 
> 위에서 봤던 `Symbol`이 여기에 쓰임!!
> 
> `g = generator(); g[Symbol.iterator]`는 이터레이터 프로토콜을 따른다(?adhere; 고수하다, 지지하다?)
> 
> 이렇게 이터레이터 프로토콜을 따르면 `Array.from(g)`, `[..g]`, `for (let item of g)` 이런데서 사용 가능하다!!
> 
> `yield`는 시퀀스의 다음 값을 리턴하는 표현식
> 
> `return`문은 시퀀스의 마지막 값을 리턴
> 
> `throw`문은 전체 제너레이터의 실행을 종료
> 
> 제너레이터의 맨 마지막에 도달하면 `{done: true}`, 맨 마지막에 도달한뒤로 `g.next()`호출해도 효과가 없다

- Generator functions are a special kind of iterator that can be declared using the function* generator () {} syntax
- Generator functions use yield to emit an element sequence
- Generator functions can also use yield* to delegate to another generator function – or any iterable object
- Generator functions return a generator object that’s adheres to both the iterable and iterator protocols
	- Given g = generator(), g adheres to the iterable protocol because g[Symbol.iterator] is a method
	- Given g = generator(), g adheres to the iterator protocol because g.next is a method
	- The iterator for a generator object g is the generator itself: g[Symbol.iterator]() === g
- Pull values using Array.from(g), [...g], for (let item of g), or just calling g.next()
- Generator function execution is suspended, remembering the last position, in four different cases
	- A yield expression returning the next value in the sequence
	- A return statement returning the last value in the sequence
	- A throw statement halts execution in the generator entirely
	- Reaching the end of the generator function signals { done: true }
- Once the g sequence has ended, g.next() simply returns { done: true } and has no effect

#### 여기 중요!

- **It’s easy to make asynchronous flows feel synchronous**
	- Take user-provided generator function
	- User code is suspended while asynchronous operations take place
	- Call g.next(), unsuspending execution in user code


### Promises


### Maps


### WeakMaps


### Sets


### WeakSets


### Proxies


### Replection


### `Number`


### `Math`


### `Array`


### `Object`


### Strings and Unicode


### Modules












