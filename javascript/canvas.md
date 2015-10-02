
### Retina 대층 캔버스 컨택스트 만들기

```javascript
function getRetinaCanvas(canvas, targetWidth, targetHeight) {
	var c = canvas.getContext("2d");
	var ratio = Math.min(2, window.devicePixelRatio);
	canvas.width = targetWidth * ratio;
	canvas.height = targetHeight * ratio;
	canvas.style.width = targetWidth + 'px';
	canvas.style.height = targetHeight + 'px';
	c.scale(ratio, ratio);
	return c;
}
```

> ratio 를 2를 최대로 잡았는데, 넥5(2014)에서는 3임. 그런데 3으로 하면 개버벅임.....ㅠ


### 렌더링 최적화

```css
will-change: transform;
```

[참고](https://developers.google.com/web/fundamentals/performance/rendering/simplify-paint-complexity-and-reduce-paint-areas?hl=ko)

120~150ms 걸리던 `stroke`가 30ms 수준으로 줄어듬!!
