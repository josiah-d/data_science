import psycopg2 as pg2
from datetime import datetime

conn = pg2.connect(dbname="socialmedia", host="localhost", password=None, user='postgres', port='5432')
cur = conn.cursor()

today = '2014-08-14'

# This is not strictly necessary but demonstrates how you can convert a date
# to another format
ts = datetime.strptime(today, '%Y-%m-%d').strftime("%Y%m%d")

cur.execute(
    '''

    /* counts the # of times a user has logged in in the last 7 days*/
    CREATE TEMPORARY TABLE logins_7d AS
    SELECT userid, COUNT(*) AS cnt
    FROM logins
    WHERE logins.tmstmp > timestamp %(ts)s - interval '7 days'
    GROUP BY userid;

    /* counts the # of times a user has logged in using a mobile in the last 7 days */
    CREATE TEMPORARY TABLE logins_7d_mobile AS
    SELECT userid, COUNT(*) AS cnt
    FROM logins
    WHERE logins.tmstmp > timestamp %(ts)s - interval '7 days' and type =  'mobile'
    GROUP BY userid;

    /* counts the # of times a user has logged in using a web in the last 7 days */
    CREATE TEMPORARY TABLE logins_7d_web AS
    SELECT userid, COUNT(*) AS cnt
    FROM logins
    WHERE logins.tmstmp > timestamp %(ts)s - interval '7 days' and type =  'web'
    GROUP BY userid;

    /* gets the last login date for each user */
    CREATE TEMPORARY TABLE last_login as 
    SELECT l.userid, max(l.tmstmp) as last_login
    FROM logins l WHERE l.tmstmp <= %(ts)s
    GROUP BY l.userid;

    /* use the above tables to create a snapshot */
    CREATE TABLE snapshot AS
    SELECT r.userid, last_login, 
    r.tmstmp as reg_date, 
    COALESCE(l7d.cnt, 0) as logins_7d, 
    COALESCE(l7d_mobile.cnt,0) as logins_7d_mobile,
    COALESCE(l7d_web.cnt,0) as logins_7d_web,
    COALESCE(optout.userid,0) as optout_userid
    FROM registrations r
    LEFT JOIN last_login as ll on r.userid = ll.userid 
    LEFT JOIN logins_7d AS l7d ON l7d.userid = ll.userid
    LEFT JOIN logins_7d_mobile as l7d_mobile ON l7d_mobile.userid = ll.userid 
    LEFT JOIN logins_7d_web as l7d_web ON l7d_web.userid = ll.userid
    LEFT JOIN optout on ll.userid = optout.userid
    ORDER BY userid;
    '''  , {'ts': ts}
)

conn.commit()
conn.close()
