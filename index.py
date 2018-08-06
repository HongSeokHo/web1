#!C:\Users\tjrgh\AppData\Local\Programs\Python\Python36-32\python.exe
print("Content-Type: text/html")
print()
print('''<!doctype html>
<html>
<head>
  <title>HongSeokHo's first website</title>
  <meta charset="utf-8">
  <style>
    h1{
      text-align: center;
      border:1px solid gray;
      padding-bottom:10px;
      margin-bottom:20px;
    }
    a{
      color:black;
    }
    ul{
      border:1px solid gray;
      width:200px;
      margin:0;
      padding-right:10px;
      padding-top:35px;
    }
    .saw{
      color:gray;
    }
    .active{
      color:red;
    }
    @media(max-width:700px){
      #grid{
        display: grid;
        grid-template-columns: 100px 1fr;
      }
      #article{
        padding-left:150px;
        margin:10px;
      }
    }
    #category{
      display: block;
      border:1px solid gray;
      background-color: white;
      width:200px;
      margin:20px;
      padding:10px;
    }
    #article{
      display: block;
      border:1px solid gray;
      margin-left: 250px;
      margin-right: 20px;
    }
    #grid{
      display:grid;grid-template-columns: 10px 1fr
    }
  }
  </style>
</head>
<body>
  <h1>Welcome to my first website</h1>
  <div id="grid";>
    <div id="category";>
        Category
        <br><br>
        <li><a href="1.python.html" class="saw active">1. 학점 계산기 구현하기</a></l\i>
        <li><a href="2.feeling.html"  class="saw active">2. 느낀점</a></li>
        <li><a href="3.Linux.html"  class="saw active">3. 리눅스 환경 구축</a></li>
        <li><a href="4.웹과 클라이언트 관계.html"  class="saw active">4. 서버와 클라이언트</a></li>
    </div>
    <div id="article";>
      <h2>안녕하세요!!</h2>
      <p>
        안녕하세요 저의 첫 웹 사이트이자 공부방에 오신것을 환영합니다~!!\
        <br><br>
        이곳에는 제가 공부하는 대부분의 자료들을 올리고 있구요, 아직 웹을 공부한지 얼마 안되어서 사이트를 꾸미고 관리하는데에는 시간이 걸릴 것 같습니다.
      </p>
    </div>
  </div>
</body>
</html>
''')
