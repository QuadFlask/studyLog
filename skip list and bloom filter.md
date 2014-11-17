## Skip list
[http://en.wikipedia.org/wiki/Skip_list](http://en.wikipedia.org/wiki/Skip_list)

일반적인 정렬된 링크드 리스트와 같은데, 
 레이어화되있어 검색/삽입/삭제시 o(log n)으로 처리할 수 있게 해줌.

![](http://upload.wikimedia.org/wikipedia/commons/thumb/8/86/Skip_list.svg/470px-Skip_list.svg.png)


b 트리랑 비슷해 보이는데, b 트리와 성능 비교에선 밀림.

1. 비록 b 트리가 밸런스를 유지해야 하지만, red-black 트리의 경우 항상 밸런스되어있어 오버헤드가 적다
2. 메모리 로컬리티가 안됨 ( 캐시 미스 확률이 높음)
3. 실제로는 퍼포먼스, 공간을 많이 잡아 먹음...
4. 하지만 각각의 레이어 유지에 있어서 패러럴로 동작 할 수 있게 해줌 ( pros )

상황에 따라 데이터 바운드가 정해져 있을 경우 b-tree나 red-black tree 가 좋지만,
계속해서 데이터가 들어가는 경우엔 red-black tree나 skip list 를 생각해 보면 좋을듯.


## Bloom filter
[http://en.wikipedia.org/wiki/Bloom_filter](http://en.wikipedia.org/wiki/Bloom_filter)

공간 효율적인 가능성(확률) 데이터 스트럭쳐..?
앨리먼트들을 세트로 생각하고 False positive, False negative

> False positive, False negative: 그 안에 존재할 수 있다 <-> 절대 없다

0으로 셋 된 비트 어레이를 준비하고 완벽한 해시 알고리즘을 이용해서 해당되는 비트를 1로 셋. 다른 데이터가 존재하는지를 확인할땐 해시하고, 비트 어레이에서 0을 가리키면 존재하지 않음.
하지만 모두 1이라고 해서 반드시 존재하는것은 아니고 존재할 가능성이 있다.

![](http://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/Bloom_filter.svg/360px-Bloom_filter.svg.png)

> {x, y, z}가 셋에 존재하는것. w는 존재하는지 확인할 앨리먼트.
> w는 0을 가리키기 때문에 존재하지 않음. 
> m = 18, k =3

bloom filter의 공간 효율성을 이해하기 위해 k=1일때의 특수한 경우를 보면, false positive rate를 굉장히 줄이기 위해 적은수의 비트들이 세트되어야 한다. 즉, 배열이 굉장히 커야하고 0가 굉장히 길게 있다는것이다.
일반적인 bloom filter(k>1)은 flase positive rate를 낮추면서 다른 많은 비트들이 세트될 수있도록 한다.
k, m이 잘 설정됬다면 반 정도의 비트가 세트될것이고 분명히 랜덤하고, 중복을 최소화하면서 정보량을 최대화 할것이다.

### Type I error (also called false positive)
null 가설==true
실제로 존재하지 않는다.

### Type II error (also called false negative)
null 가설==false
존재 할 수도, 없을 수도 있다.
