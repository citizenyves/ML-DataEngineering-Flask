# 동행복권 API로 역대 로또 회차별 당첨번호 데이터를 가져온 

# API로 데이터 저장하기
import os, sys
import sqlite3
import requests
import json

DB_NAME = 'lotto.db'
#DB_FILEPATH = os.path.join(os.getcwd(), DB_NAME)

# 파이썬에 sqlite3 연결 객체 생성
conn = sqlite3.connect(DB_NAME)
cur = conn.cursor()

# 테이블 생성
cur.execute("DROP TABLE IF EXISTS lotto;")
cur.execute("""CREATE TABLE lotto(
                    drwNo INTEGER NOT NULL PRIMARY KEY,
                    drwNoDate TEXT,
                    drwtNo1 INTEGER,
                    drwtNo2 INTEGER,
                    drwtNo3 INTEGER,
                    drwtNo4 INTEGER,
                    drwtNo5 INTEGER,
                    drwtNo6 INTEGER,
                    bnusNo INTEGER,
                    totSellamnt INTEGER,
                    firstWin INTEGER,
                    firstWinNo INTEGER,
                    firstAccumamnt INTEGER
                    )""")
    

# 데이터베이스에 저장할 변수 및 데이터 삽입 함수
def intodb(lotto_json):
    drwNo = lotto_json['drwNo'] #회차
    drwNoDate = lotto_json['drwNoDate'] #진행날짜
    drwtNo1 = lotto_json['drwtNo1'] #당첨번호1
    drwtNo2 = lotto_json['drwtNo2'] #당첨번호2
    drwtNo3 = lotto_json['drwtNo3'] #당첨번호3
    drwtNo4 = lotto_json['drwtNo4'] #당첨번호4
    drwtNo5 = lotto_json['drwtNo5'] #당첨번호5
    drwtNo6 = lotto_json['drwtNo6'] #당첨번호6
    bnusNo = lotto_json['bnusNo'] #보너스번호 #Target
    totSellamnt = lotto_json['totSellamnt'] #누적당첨금
    firstWin = lotto_json['firstWinamnt'] #1등당첨금
    firstWinNo = lotto_json['firstPrzwnerCo'] #1등당첨인원
    firstAccumamnt = lotto_json['firstAccumamnt'] #1등당첨금총액
    returnValue = lotto_json['returnValue'] #실행결과

    # 데이터 삽입
    cur.execute("""INSERT INTO lotto (drwNo, drwNoDate, drwtNo1, drwtNo2, drwtNo3,
                   drwtNo4, drwtNo5, drwtNo6, bnusNo, totSellamnt, firstWin, 
                   firstWinNo, firstAccumamnt) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);""",
                   (drwNo, drwNoDate, drwtNo1, drwtNo2, drwtNo3, drwtNo4, drwtNo5, drwtNo6,
                    bnusNo, totSellamnt, firstWin, firstWinNo, firstAccumamnt)                  
                )

    conn.commit()


# lotto api url
API_URL = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo="

# 2021-10-7 기준 총 983회까지 진행된 로또.. (난 한번도 안 사본 것인가..)
for i in range(1, 984):
    resp = requests.get(API_URL + str(i))
    lotto_json = resp.json()
    intodb(lotto_json)


