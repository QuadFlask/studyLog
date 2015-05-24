1. mkdir hello-git
2. cd hello-git
3. vim readme.txt
4. this is first line.
5. git init
 (master 빨간원) -> 마스터 브랜치에 있고, 변경 사항이 존재함.
6. git status 
 변경 내역 보기
7. git add . 
 모두 인덱스에 넣기 (master 초록불 or 없음) 
8. git status
9. git commit -a
10. git status 
 변경사항 없졍
11. git log
 커밋 로그 보기.
12. sourcetree
add working copy
Add
Double click
master

13. git diff 
  변경사항 확인하기 

14. git reset 

app-13@app-13 ~/temp/hello-git (master)$ git log

Fri Sep 13 16:13:18 2013 +0900 74916a6 (HEAD, master) second commit  [QuadFlask]

Fri Sep 13 15:42:11 2013 +0900 7aaca1d this is first commit  [app-13]

app-13@app-13 ~/temp/hello-git (master)$ git reset --hard HEAD~1 // 현재 헤드에서 하나 전으로

HEAD is now at 7aaca1d this is first commit

app-13@app-13 ~/temp/hello-git (master)$ git log

Fri Sep 13 15:42:11 2013 +0900 7aaca1d (HEAD, master) this is first commit  [app-13]

15. fork repo 에서 원래 repo 머지하기
 1. git remote add upstream `repo url`
 2. git fetch upstream
 3. git merge upstream/master
