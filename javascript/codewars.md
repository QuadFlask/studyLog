## Codewars


### `(0.1234).toFixed(2)`

소숫점 잘라내기 

### `Number.isInteger`, `typeof x !== "number"`

숫자 체크 

### `arr.some(fn)`

하나라도 만족할경우 true

### `arr.every`

모두 만족할경우 true

### `var [ a, b ] = numbers.sort((a, b) => a - b)`

ES 2015 Destructuring?


### rottenFruit

```
Our fruit guy has a bag of fruits (array of strings) where some fruits are rotten, he wants to replace all the rotten fruits by good ones. For example, given this array ["apple","rottenBanana","apple"] the replaced array should be ["apple","banana","apple"]. Your task is to implement a method that will take as an argument an array of strings containing fruits and should return an array of strings where all the rotten fruits are replaced by good ones.

Note: If the array is null or empty you should return empty array ([]). The rotten fruit name will be in this format rottenFruitname where is the 1st letter of the fruit name is uppercase. NB: The returned array should be in LOWER case.
```

```javascript
function removeRotten(bagOfFruits){
  if(!bagOfFruits || !bagOfFruits.length) {return [];} 
  else {return bagOfFruits.map(e => e.replace(/^rotten/g, '').toLowerCase())};
}
```

regex 를 쓰면 쉽다!!! `/^rotten/g` rotten 으로 시작하는 패턴


### Range

range 가 없을땐 이런식으로 사용하면 range 처럼 만들 수 있음

(하지만 그냥 lodash 쓰는게 맘편할듯?)

```javascript
Array.from(new Array(20), (_,i) => x=x*y);
```