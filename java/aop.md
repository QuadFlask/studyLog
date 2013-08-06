# [AOP (Aspect Oriented Programming)](http://openframework.or.kr/framework_reference/spring/ver2.x/html/aop.html)

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

 + **JoinPoint** 의 부분 집합...? (실제로 **Advice**가 **JointPoint** 적용된 스프링 정규표현식이나 **AspectJ**의 문법을 이용하여 **Pointcut**을 정의 할 수 있다.)

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

- [Pointcut 표현식](http://blog.naver.com/PostView.nhn?blogId=chocolleto&logNo=30086024618)
- 



## Example

***applicationContext.xml***

``` xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
 xmlns:p="http://www.springframework.org/schema/p" xmlns:aop="http://www.springframework.org/schema/aop"
	xmlns:context="http://www.springframework.org/schema/context"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://www.springframework.org/schema/beans   
       http://www.springframework.org/schema/beans/spring-beans-3.0.xsd
       http://www.springframework.org/schema/aop
       http://www.springframework.org/schema/aop/spring-aop-3.0.xsd
       http://www.springframework.org/schema/context
       http://www.springframework.org/schema/context/spring-context-3.0.xsd">

	<aop:aspectj-autoproxy />

	<bean id="performanceTraceAspect" class="com.flask.springs.ProfilingAspect" />

	<bean id="writeArticleService" class="com.flask.springs.WriteArticleServiceImpl">
		<property name="articleDao" ref="articleDao"></property>
	</bean>

	<bean id="articleDao" class="com.flask.springs.MySqlArticleDao" />

</beans>
```

***ProfilingAspect.java***

``` java
@Aspect
public class ProfilingAspect {
 @Pointcut("execution(public * com.flask.springs..*(..))")
	private void profileTarget() {
	}

	@Around("profileTarget()")
	public Object trace(ProceedingJoinPoint joinPoint) throws Throwable {
		String signatureString = joinPoint.getSignature().toShortString();
		System.out.println(signatureString + "시작");
		long start = System.currentTimeMillis();

		try {
			Object result = joinPoint.proceed();
			return result;
		} finally {
			long finish = System.currentTimeMillis();
			System.out.println(signatureString + "종료, 실행시간 :" + (finish - start) + "ms");
		}
	}
}

```


#### 수식어 패턴

`execution(수식어패턴? 리턴타입패턴 패키지패턴?이름패턴(파라미터패턴)`

`execution(public * com.flask.springs..*(..))"`


접근제한자가 *public*,

리턴 타입은 *모든 타입*,

패키지는 *com.flask.spring안의 0개 이상 패키지들*,

이름은 *모든 이름*,

파라미터는 *0개 이상*
