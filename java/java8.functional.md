## JAVA8 에 새로 추가된 람다식 등등

### 간단한 람다식 예제

```java

// 익명 클래스로 정렬하기 
Collections.sort(personList, new Comparator<Person>(){
  @Override
  public int compare(Person p1, Person p2){
    return p1.getName().compaerTo(p2.getName());
  }
}

// 람다식으로 정렬하기
Collections.sort(personList, (Person p1, Pserson p2) -> p1.getName().compaerTo(p2.getName()));

// 람다식으로 정렬하기 - 타입 명시 없이 - 타입 추측
Collections.sort(personList, (p1, p2) -> p1.getName().compaerTo(p2.getName()));

```

### `java.util.functional`

> 람다식을 대입 할 수 있음.

- `Predicate`
- `Consumer`
- `Function`
- `Supplier`
- `UnarOperator`
- `BineryOperator`


### `Predicate`

 조건 판단용?

- `test(T t)`
  : 비교 
- `and(Predicate<? super T> p), or(Predicate<? super T> p), negate()`
  : 다른 `Predicate`와 Short circuit logical 연산 


### `Consumer`

 매소드 실행용? 수행 후, 아무것도 리턴하지 않음. 

- `accept(T t)`
  : 주어진 파라미터에 대해 기능 수행 

- `andThen(Consumer<? super T> after)`
  : 일련의 작업들을 시퀀스로 실행 할 수 있도록


### `Functional`

 ? 한개의 인풋, 하나의 아웃풋을 가진, 일반적인 메소드를 대표함??
 
- `R apply(T t)`
  : 주어진 파라미터에 대해 기능 수행 후 R 리턴
- `andThen(Function<? super R,? extends V> after)`
- `compose(Function<? super V,? extends T> before)`
- `identity()`
  : 인풋만 리턴


### `Supplier`


----


## Closure

### 개념

?????????


## `stream`, `filter`, `map`, `forEach`

java8 버전 부터 Collection 인터페이스에 `stream()`, `parallelStream()` 메소드가 생겻음.

그리고 list에 대해 `forEach(Consumer<? super T> arg)` 를 수행 할 수 있게됨.

- `removeIf(Predicate<? super T> arg)` : (Collection) 내부적으로 Iterator 로 동작하는듯? 모든 객체 참조해서 조건에 부합하면 Iterator.remove 수행
 
- `replaceAll(UnaryOperator<T> arg)` : (List) 내부적으로 ListIterator 로 동작함 "the operator to apply to each element"
 
- `sort(Comparator<? super T> arg)` : `Collections.sort` 와 같음.
 
- `ListIterator` : An iterator for lists that allows the programmer to traverse the list in either direction, *modify the list **during iteration**, and obtain the iterator's current position in the list*. A ListIterator has no current element; its cursor position always lies between the element that would be returned by a call to previous() and the element that would be returned by a call to next()

- `Spliterator` : [?????????????](http://docs.oracle.com/javase/8/docs/api/java/util/Spliterator.html)


### Stream ?
 
Iterator 랑 비슷해 보임

`psersonList`에서 10살 이상인 사람들의 모든 나이의 합
```java 
int sum = personList.stream() // personList 에서 시퀀스 스트림 가져오기..
                    .filter(p->p.getAge()>=10) // 조건 - 필터링  return stream
                    .mapToInt(p->p.getAge()) // 매핑 return IntStream
                    .sum(); // 동작 
```






