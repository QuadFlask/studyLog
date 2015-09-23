Promise with Generator
-----------------

기존의 callback hell 을 해결하기 위해서 프로미스를 사용하지만 에러 처리가 난감함. 그에 대한 해결책으로 es6의 `generator`, `yield` 로 해결을 하는 방법(es7의 `await`도 관련이 있는듯?)

참고 : [Deview2015: large scale backend service develpment](http://www.slideshare.net/deview/212-large-scale-backend-service-develpment)

[A Study on Solving Callbacks with JavaScript Generators](http://jlongster.com/A-Study-on-Solving-Callbacks-with-JavaScript-Generators)


### Callback hell
![](http://image.slidesharecdn.com/221largescalebackendservicedevelpment-150915001346-lva1-app6892/95/212-large-scale-backend-service-develpment-16-1024.jpg?cb=1442277886)

> 에러 처리를 계속 내부 콜백에서 받아다가 처리 하는 방법....

### to this!!
![](http://image.slidesharecdn.com/221largescalebackendservicedevelpment-150915001346-lva1-app6892/95/212-large-scale-backend-service-develpment-17-1024.jpg?cb=1442277886)

```javascript

function* (req, res) {
	try {
		yield process1();
		yield process2();
		yield process3();
		yield process4();
	} catch(e) {
		print(e);
	}
}

```

> 걍 싹다 한번에 처리



```javascript

var db = {
    get: Q.nbind(client.get, client),
    set: Q.nbind(client.set, client),
    hmset: Q.nbind(client.hmset, client),
    hgetall: Q.nbind(client.hgetall, client)
};

db.hmset('blog::post', {
    date: '20130605',
    title: 'g3n3rat0rs r0ck',
    tags: 'js,node'
}).then(function() {
    return db.hgetall('blog::post');
}).then(function(post) {
    var tags = post.tags.split(',');

    return Q.all(tags.map(function(tag) {
        return db.hgetall('blog::tag::' + tag);
    })).then(function(taggedPosts) {
        // do something with post and taggedPosts

        client.quit();
    });
}).done();

```

> `then` 이 붙은걸로 보아 `db.hmset` 호출시 프로미스가 리턴되는것을 알 수 있고,


```javascript

Q.async(function*() {
    yield db.hmset('blog::post', {
        date: '20130605',
        title: 'g3n3rat0rs r0ck',
        tags: 'js,node'
    });

    var post = yield db.hgetall('blog::post');
    var tags = post.tags.split(',');

    var taggedPosts = yield Q.all(tags.map(function(tag) {
        return db.hgetall('blog::tag::' + tag);
    }));

    // do something with post and taggedPosts

    client.quit();
})().done();

```

> `Q.async` 는 제너레이터 함수를 받아 실행시켜 받은 함수를 실행한다?

> Q.async takes a generator and returns a function that runs it, much like the suspend library. However, there's a key difference, which is that the generator yields promises. **Q takes each promise and ties the generator to it, making it resume when the promise is fulfilled, and sending back the result.**


```javascript

Q.async(function*() {
    try {
        var post = yield db.hgetall('blog::post');
        var tags = post.tags.split(',');

        var taggedPosts = yield Q.all(tags.map(function(tag) {
            return db.hgetall('blog::tag::' + tag);
        }));

        // do something with post and taggedPosts
    }
    catch(e) {
        console.log(e);
    }

    client.quit();
})();

```


### 만약 ES7 이 가능하다면?

[https://jakearchibald.com/2014/es7-async-functions/](https://jakearchibald.com/2014/es7-async-functions/)

ES7의 `async`, `await` 키워드를 사용하면 좋음

`async` == `Q.async`

`awiat` == `yield`


#### ES6

```javascript

function loadStory() {
  return spawn(function *() {
    try {
      let story = yield getJSON('story.json');
      addHtmlToPage(story.heading);
      for (let chapter of story.chapterURLs.map(getJSON)) {
        addHtmlToPage((yield chapter).html));
      }
      addTextToPage("All done");
    } catch (err) {
      addTextToPage("Argh, broken: " + err.message);
    }
    document.querySelector('.spinner').style.display = 'none';
  });
}

```


#### ES7

```javascript

async function loadStory() {
  try {
    let story = await getJSON('story.json');
    addHtmlToPage(story.heading);
    for (let chapter of story.chapterURLs.map(getJSON)) {
      addHtmlToPage((await chapter).html);
    }
    addTextToPage("All done");
  } catch (err) {
    addTextToPage("Argh, broken: " + err.message);
  }
  document.querySelector('.spinner').style.display = 'none';
}

```

