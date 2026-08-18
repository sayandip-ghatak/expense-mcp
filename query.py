from db_connection import connect_db
from psycopg2.extras import RealDictCursor


def check_id():
    query =  "select count(user_id) cnt from public.user_details"
    conn = connect_db()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return str((result[0]['cnt']+1)).zfill(4)

def create_user(name):
    fname,lname = name.split(" ")
    id_fname = fname[0].upper()
    id_lname = lname[0].upper()
    id = id_fname+id_lname+check_id()
    insert_query = "insert into public.user_details (user_id,user_name) values (%(id)s, %(name)s)"
    conn = connect_db()
    cur = conn.cursor()
    cur.execute(insert_query,{"id":id,"name":name})
    conn.commit()
    conn.close()
    return id

def get_user_by_name(name):
    lower_name = str(name).lower()
    fetch_query = "select user_id from public.user_details where lower(user_name) = %(name)s"
    conn = connect_db()
    cur = conn.cursor()
    cur.execute(fetch_query,{"name":lower_name})
    result = cur.fetchone()
    return str(result[0])