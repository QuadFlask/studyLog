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

### java.util.functional

- Predicate
- Consumer
- Function
- Supplier
- UnarOperator
- BineryOperator

#### Predicate

