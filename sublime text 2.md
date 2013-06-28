[Sublime Text 2](http://www.sublimetext.com/2)
-------------------

### package control 설치하기

```
import urllib2,os; pf='Package Control.sublime-package'; ipp=sublime.installed_packages_path(); os.makedirs(ipp) if not os.path.exists(ipp) else None; urllib2.install_opener(urllib2.build_opener(urllib2.ProxyHandler())); open(os.path.join(ipp,pf),'wb').write(urllib2.urlopen('http://sublime.wbond.net/'+pf.replace(' ','%20')).read()); print 'Please restart Sublime Text to finish installation'
```

### 유용한 플러긴

#### [SublimeHighlight](https://github.com/n1k0/SublimeHighlight)

다른곳에 복붙할때 색상도 같이 옮겨주는녀석


#### [Sublime-JavaScript-API-Completions](https://github.com/Pleasurazy/Sublime-JavaScript-API-Completions)

API 코드 힌트 도와주는 녀석


#### [Alignment](http://bnufactory.com/2013/05/sublime-text-%ED%94%8C%EB%9F%AC%EA%B7%B8%EC%9D%B8-alignment/)

= 을 기준으로 앞에 공백을채워줘서 이쁘게 보이게 해주는 녀석


#### [SFTP](http://blog.naver.com/PostView.nhn?blogId=hanchiro&logNo=30136872728)

서버에 업로드 편리하게. [1](http://2thet0p.tistory.com/3)
