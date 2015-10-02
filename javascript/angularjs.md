### `controller` 에서 `directive` 함수 호출하기 방법 1 

노출시킬 api 객체를 팩토리를 통해서 만들고, 
디렉티브 안에서 api 객체의 프롭을 와치함....

```javascript

angular.module("canvas.drawing", []).factory('canvasDrawingToolApi', function() {
	return {
		clearFlag : true,
		penColor : '#000000',
		smooth: true,
		clear : function() {
			this.clearFlag = this.clearFlag ? false : true;
		}
	};
}).directive('canvasDrawingTool', function() {
	var isDrawing, points = [];
	var canvas, context;
	var smooth = false;

	function start(event) {
		isDrawing = true;
		var xy = getXY(event);
		if (smooth) {
			points.push({
				x : xy[0],
				y : xy[1]
			});
		} else {
			context.beginPath();
			context.moveTo(xy[0], xy[1]);
		}
		event.preventDefault();
	}

	function draw(event) {
		if (isDrawing) {
			var xy = getXY(event);
			if (smooth) {
				points.push({
					x : xy[0],
					y : xy[1]
				});

				var p1 = points[0];
				var p2 = points[1];

				context.beginPath();
				context.moveTo(p1.x, p1.y);

				for (var i = 1, len = points.length; i < len; i++) {
					var midPoint = midPointBtw(p1, p2);
					context.quadraticCurveTo(p1.x, p1.y, midPoint.x, midPoint.y);
					p1 = points[i];
					p2 = points[i + 1];
				}
				context.stroke();
			} else {
				context.lineTo(xy[0], xy[1]);
				context.stroke();
			}
		}
		event.preventDefault();
	}

	function stop(event) {
		if (isDrawing) {
			if (smooth) {
				points.length = 0;
			} else {
				context.stroke();
				context.closePath();
			}
			isDrawing = false;
		}
		event.preventDefault();
	}

	var arr = [0,0];
	function getXY(event) {
		if (event.type.indexOf("touch") > -1) {
			arr[0] = event.targetTouches[0].pageX;
			arr[1] = event.targetTouches[0].pageY;
		} else {
			arr[0] = event.pageX;
			arr[1] = event.pageY;
		}
		return arr;
	}

	function midPointBtw(p1, p2) {
		return {
			x : p1.x + (p2.x - p1.x) / 2,
			y : p1.y + (p2.y - p1.y) / 2
		};
	}

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

	function clear() {
		context.clearRect(0, 0, canvas.width, canvas.height);
	}

	var link = function(scope, elem, attr) {
		canvas = elem[0];
		context = getRetinaCanvas(canvas, window.innerWidth, window.innerHeight);
		isDrawing = false;

		context.lineWidth = 1.5;
		context.strokeStyle = "#000000";
		context.lineJoin = context.lineCap = 'round';

		canvas.addEventListener("touchstart", start, false);
		canvas.addEventListener("touchmove", draw, false);
		canvas.addEventListener("touchend", stop, false);
		canvas.addEventListener("mousedown", start, false);
		canvas.addEventListener("mousemove", draw, false);
		canvas.addEventListener("mouseup", stop, false);
		canvas.addEventListener("mouseout", stop, false);
	}

	return {
		controller : function($scope, canvasDrawingToolApi) {
			$scope.api = canvasDrawingToolApi;
			$scope.$watch('api.clearFlag', clear);
			$scope.$watch('api.penColor', function(newVal, oldVal) {
				context.strokeStyle = newVal;
			});
			$scope.$watch('api.smooth', function(newVal){
				smooth = newVal;
			});
		},
		link : link
	};
})

```
