import cx_Oracle

def db_conn() : 
    try :
        conn = cx_Oracle.connect("hr", "12345", "localhost:1521/xe") #자: connect 객체 생성
        cur = conn.cursor() #자: 커서객체 생성
        print("DB 연결 성공")
        return conn, cur
    except cx_Oracle.DatabaseError as e:
        print(e)

# 자: 연결 해제
def db_disconn(conn, cur) : 
    cur.close() # 자:cursor객체는 connect 연결 객체에 있으니까 먼저 해제
    conn.close() # 자:cursor 객체 연결해제 후 connect 객체 연결 해제
    print("DB 연결 종료")

#자 : select 문
def db_search(cur, id_val, pw_val):
    sql = f"select code, name, age from member_tbl where id_val='{id_val}' and pw_val='{pw_val}'"
    
    print(sql) #자: 확인

    try : 
        cur.execute(sql)
        print("데이터 검색 완료")
        return cur.fetchone() # 자: 1개 행 검색
    except cx_Oracle.DatabaseError as e:
        print(e)
