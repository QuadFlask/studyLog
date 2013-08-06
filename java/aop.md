# AOP (Aspect Oriented Programming)

> 문제를 바라보는 관점을 기준으로 프로그래밍 하는 기법?

 - 공통 관심 사항 (Cross-cutting Concern)

 - 핵심 관심 사항 (Core Cocern)
 
전처리  <----------------공통 관심 사항

매서드 (=동작행위) 

후처리  <----------------공통 관심 사항


## AOP 용어

- **Advice**

 + 언제 공통 관심 사항을 핵심 로직에 적용할지 정의

- **JoinPoint**

 + **Advice** 적용 가능 지점

- **Pointcut** 

 + 

- **Weaving**

 + **Advice**를 핵심 로직 코드에 적용하는것
 + Weaving 방식 3가지
 + 컴파일시, 클래스 로딩시, 런타임시
 
- **Aspect**

 + 공통 관심 사항

- [**POJO (Plain-Old-Java-Object)**](http://okjsp.net/seq/143884)

> POJO에서 제일 중요한 뜻이 Plain입니다.. 
> 특정한 API(Servlet, EJB 등)를 상속하거나 구현하지 않고 사용한다는 뜻이죠. 
> 이식성을 높일 수 있고(프레임워크간이거나 클라이언트간이거나), 
> 테스트 효율이 높아진다는 중요한 의미가 있습니다..


### Advice

> 언제 공통 관심 사항을 핵심 로직에 적용할지 정의

#### 태그

- `<aop:before>` : 매서드 실행 전
- `<aop:after-returning>` : 매서드 실행 후
- `<aop:throwing>` : 예외 발생시 (catch)
- `<aop:after>` : finally
- `<aop:around>` : 모든 시점
****
- `<aop:config>` : AOP configuration
- `<aop:aspect>` : Aspect 설정
- `<aop:pointcut>` : Pointcut설정


### Aspect

> 공통 관심 사항. `@Aspect` 어노테이션으로 클래스 구현. 이떄 Advice method, pointcut을 포함함?


### PointCut

> Pointcut : JoinPoint의 부분 집합
