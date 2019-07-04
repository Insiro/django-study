####mvt
model, view, templates  
모델 url 입력시 -> url에 매핑괴는 view로 이동  

####앱생성 순서
> django-admin startproject projectname  
> cd -> manage.py startapp appname  
> app 내부에 templates 폴더 필요 -> 화면 관리용
> settings.py 에 앱추가 : apps.py의 이름
> templates.htmlname.html 작성
> views.py 작성
> urls.py 작성

####설명
>
1. project
> 1. settings.py 프로젝트 설정
    >> 앱의 존재를 알려줘야함 : apps.py의 함수명 등록 필요  
    ex) 'firstapp.apps.FirstappConfig', [appname].apps.[appname]Config   
> 2. urls.py 프로젝트 url 관련 파일  
   >> path('/뒤에 붙는 내용', [appname].views.[funtion],name)  

2. apps
> 1. model  : db
view : 데이터 처리
>> view 에서 데이터 보낼때 render 안에 {'변수명':data}  
>> return render(request, html, data dic)
> 2. templates : 보여줄 화면  
>> view 의 데이터 가져올때 {{변수명}}  
>>{%url 'lotto'%} url의 lotto이름을 가진 함수를 실행