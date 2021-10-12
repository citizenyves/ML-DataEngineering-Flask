# CSV파일 데이터를 DB에 저장하기
import os, sys
import csv, sqlite3
import pandas as pd

DB_NAME = 'lotto.db'
#DB_FILEPATH = os.path.join(os.getcwd(), DB_NAME)

# 파이썬에 sqlite3 연결 객체 생성
conn = sqlite3.connect(DB_NAME)
cur = conn.cursor()

# 테이블 생성
cur.execute("DROP TABLE IF EXISTS firsttofifth;")
cur.execute("""CREATE TABLE firsttofifth(
                    drwNo INTEGER NOT NULL PRIMARY KEY,
                    firstWinNo INTEGER,
                    firstWin INTEGER,
                    secondWinNo INTEGER,
                    secondWin INTEGER,
                    thridWinNo INTEGER,
                    thirdWin INTEGER,
                    fourhWinNo INTEGER,
                    fourthWin INTEGER,
                    fifthWinNo INTEGER,
                    fifthWin INTEGER
                    )""")

# CSV 파일 데이터 삽입
### fourh --> fourthWinNo 수정 필요
df = pd.read_csv("firsttofifth.csv")
df = df[['drwNo','firstWinNo','firstWin','secondWinNo','secondWin',
         'thridWinNo','thirdWin','fourhWinNo','fourthWin','fifthWinNo',
         'fifthWin']]

df.to_sql('firsttofifth', conn, if_exists='append', index=False)
