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
