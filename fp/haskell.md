## 하스켈로 배우는 함수형 프로그래밍

### REPL

```
$ ghci
```
> 인터프리터 키기

```
$ Prelude> :q
```
> 끄기

// 타입 추론, 패턴 매칭


### 하스켈의 경우 - 타입의 정의/사용의 용이성

```haskell
-- 1 + (2 + 3)^2
-- 26

--식
data Expr a = Plus (Expr a) (Expr a) -- 덧셈 식
            | Square (Expr a)        -- 제곱 식
            | Number a               -- 숫자 식

-- 식의 평가를 실시하는 함수
evalExpr :: Expr Int -> Int
evalExpr (Plus e1 e2) = evalExpr e1 + evalExpr e2
evalExpr (Square e) = evalExpr e ^ (2 :: Int)
evalExpr (Number n) = n

-- 식을 문자열로 하는 함수
showExpr :: Expr Int -> String
showExpr (Plus e1 e2) = showExpr e1 ++ " + " ++ showExpr e2
showExpr (Square e)   = "(" ++ showExpr e ++ ")^2"
showExpr (Number n)   show n

main :: IO ()
main = do
	-- 실제로는 구문분석등에 의해 좀 더 크고 복잡한 것을 가정
	let e = Plus (Number 1) Square (Plus (Number 2) (Number 3)))
	pusStrLn (showExpr e)
	print (evalExpr e)

```

#### 코드양의 차이가 발생하는 이유

* 타입을 간단하게 정의
* 패턴 매치

##### 타입을 간단하게 정의

```haskell
data Expr a = Plus (Expr a) (Expr a) -- 덧셈 식
            | Square (Expr a)        -- 제곱 식
            | Number a               -- 숫자 식
```

표현식이 어떤 타입인지를 BNF 처럼 정의 하고 있음 

자바였다면... 최소 4개 이상의 인터페이스나 클래스를 정의해야하지


##### 패턴 매치

> 식의 타입은 정의 시점에 막혀있고, 정의 이외에서 식의 타입에 값을 추가할 수 없다. 따라서 식의 타입을 갖는 값은 **이것들중 어떤것**을 판별할 수 있다. -> **생성자의 역계산: 어떤 타입에 값이 있을대 값이 실제로 어떤 타입에서 만들어졌는지 판별하고, 만들어졌을 때에 주어진 각 요소를 꺼낼 수 있는 기능** 

> 일단은... 매소드 오버로딩 같은 개념이라고 생각해보자...

```haskell
-- 식의 평가를 실시하는 함수
evalExpr :: Expr Int -> Int
evalExpr (Plus e1 e2) = evalExpr e1 + evalExpr e2
evalExpr (Square e) = evalExpr e ^ (2 :: Int)
evalExpr (Number n) = n

-- 식을 문자열로 하는 함수
showExpr :: Expr Int -> String
showExpr (Plus e1 e2) = showExpr e1 ++ " + " ++ showExpr e2
showExpr (Square e)   = "(" ++ showExpr e ++ ")^2"
showExpr (Number n)   show n
```


#### 하스켈의 경우 - 성질의 보증은 제공자의 의무

> p113


### 2. 타입

...

#### 람다식 - 함수 리터럴

```
Prelude> \x -> 2 * x

Error -- 함수 리터럴은 따로 출력할 수 있지 않음(인쇄할 수 없는 타입임). 그래서 아래처럼 값을 **적용**하여 실행하면 됨

Prelude> (\x -> 2 * x) 3
6
```

> 하스켈에선 스페이스가 함수 적용에 해당(호출?) 
> 

#### 값 생성자 - 부울값, True/False는 값 생성자

> 리터럴처럼 보이지만, 값 생성자임


### 변수 

변수, 상수, 바인딩

#### 바인딩

```haskell
let a = 10 -- 하스켈에선 모든 변수는 상수임

let double = \x -> 2 * x -- 함수도 값이므로 변수에 바인딩 가능
```

### 타입

```haskell
Prelude> :t True -- :t 로 타입을 확인 할 수 있음
True :: Bool
```

#### 함수의 타입

```haskell
Prelude> not True -- 논리 부정 함수
False
Prelude> not False
True

Prelude> : not
not :: Bool -> Bool -- 함수 not은 Bool타입의 값을 받아들여 Bool타입의 값이 된다
```

```haskell
Prelude> :t (&&) -- 논리곱 연산자를 ()괄호로 감싸 함수로 맹근다
(&&) :: Bool -> Bool -> Bool -- (&&)는 부울타입 값을 받아들이고 또 부울값을 받아들여 부울값이 된다.(커링)
```

#### 커링화

```haskell
Prelude> let andT = (&&) True -- (&&)에 부울 값 하나만 적용할 수 있고,

Prelude> :t andT
andT :: Bool -> Bool -- 적용 결과는 함수이다
```

*n인자 함수*를 *1인자 함수*만으로 구성되는 형태로 하는것을 **커링(currying)**이라고 함

하스켈의 함수는 커링되어 있다




* first class citizen : 일반적인 모든 오퍼레이션이 가능한 타입(?) int, float 같은 녀석들

* first class function : 함수가 first class citizen

* high order function : 결과가 함수가 되거나 인수로 함수를 요구하는 함수

* Currying : 함수의 인자의 일부를 적용 하는??

* Currying function : 함수의 인자가 일부 적용되어 있는? 적용 가능한? 함수?

```haskell
inc :: Int -> Int
inc = (+1) 1
```
> inc 함수는 이항연산자인 + 에 1이 적용되어 있는 함수

