하스켈로 배우는 함수형 프로그래밍

first class citizen : 일반적인 모든 오퍼레이션이 가능한 타입(?) int, float 같은 녀석들

first class function : 함수가 first class citizen

high order function : 결과가 함수가 되거나 인수로 함수를 요구하는 함수

Currying : 함수의 인자의 일부를 적용 하는??

Currying function : 함수의 인자가 일부 적용되어 있는? 적용 가능한? 함수?

```haskell
inc :: Int -> Int
inc = (+1) 1
```
> inc 함수는 이항연산자인 + 에 1이 적용되어 있는 함수

