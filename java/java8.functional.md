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


#### `Predicate`

 조건 판단용?

- `test(T t)`
  : 비교 
- `and(Predicate<? super T> p), or(Predicate<? super T> p), negate()`
  : 다른 `Predicate`와 Short circuit logical 연산 


### Consumer

 매소드 실행용?

- `accept(T t)`
  : 주어진 파라미터에 대해 기능 수행 

- `andThen(Consumer<? super T> after)`
  : 일련의 작업들을 시퀀스로 실행 할 수 있도록



