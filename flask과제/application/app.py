from flask import Flask, render_template        # flask 내장 모듈 불러오기

app = Flask(__name__)                   

# 루트 URL ("/")
@app.route("/")
def index():                # 함수안에 사용자 목록 데이터 users 정의 
    users = [
        {"username" : "traveler", "name" : "Alex"},
        {"username" : "photographer", "name" : "Sam"},
        {"username" : "gourmet", "name" : "Chris"},
        {"username" : "BE_09_HSW", "name" : "HSW"}
        ]
    
    # rendering할 html 파일명(index.html) 입력
    # html로 넘겨줄 데이터 입력
    return render_template('index.html', users=users)

if __name__ == "__main__":
    app.run(debug=True)
