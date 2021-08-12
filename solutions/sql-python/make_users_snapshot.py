import psycopg2
from datetime import datetime
from pipeline import Pipeline

if __name__ == '__main__':
    conn = psycopg2.connect(dbname='socialmedia', user='postgres', 
                            host='localhost', port='5435')
    today = '2014-08-14'
    date = datetime.strptime(today, '%Y-%m-%d').strftime("%Y%m%d")

    pipeline = Pipeline(conn)
    pipeline.add_step('''CREATE TEMPORARY TABLE tmp_friends AS
                         SELECT 
                             userid1 AS userid, 
                             COUNT(*) AS num_friends
                         FROM
                             (SELECT 
                                 userid1, 
                                 userid2 
                              FROM friends
                              UNION
                              SELECT 
                                  userid2, 
                                  userid1 
                              FROM friends) a
                         GROUP BY userid1;
                      ''')

    pipeline.add_step('''CREATE TEMPORARY TABLE tmp_logins AS
                         SELECT 
                             a.userid, 
                             a.cnt AS logins_7d_mobile,
                             b.cnt AS logins_7d_web
                         FROM
                            (SELECT 
                                userid,
                                COUNT(*) AS cnt
                             FROM logins
                             WHERE 
                                 logins.tmstmp > timestamp %(date)s - interval '7 days'
                             AND 
                                 type='mobile'
                             GROUP BY userid) a
                         JOIN
                            (SELECT
                                userid,
                                COUNT(*) AS cnt
                             FROM logins
                             WHERE 
                                 logins.tmstmp > timestamp %(date)s - interval '7 days' 
                             AND type='web'
                             GROUP BY userid) b
                         ON a.userid=b.userid;
                      ''', {'date': date})

    pipeline.add_step('''CREATE TABLE users_snapshot AS
                         SELECT 
                             a.userid,
                             a.reg_date, 
                             a.last_login, 
                             f.num_friends,
                             COALESCE(l.logins_7d_mobile + l.logins_7d_web, 0) AS logins_7d,
                             COALESCE(l.logins_7d_mobile, 0) AS logins_7d_mobile,
                             COALESCE(l.logins_7d_web, 0) AS logins_7d_web,
                             CASE WHEN optout.userid IS NULL THEN 0 ELSE 1 END AS optout,
                             timestamp %(date)s AS date_7d
                         FROM
                             (SELECT 
                                 r.userid, 
                                 r.tmstmp::date AS reg_date, 
                                 MAX(l.tmstmp::date) AS last_login
                              FROM 
                                  registrations r
                              LEFT OUTER JOIN 
                                  logins l
                              ON 
                                  r.userid=l.userid
                              GROUP BY r.userid, r.tmstmp) a
                         LEFT OUTER JOIN tmp_friends f
                         ON 
                             f.userid=a.userid
                         LEFT OUTER JOIN 
                             tmp_logins l
                         ON 
                             l.userid=a.userid
                         LEFT OUTER JOIN 
                             optout
                         ON 
                             a.userid=optout.userid;
                      ''', {'date': date})

    pipeline.execute()
    pipeline.close()
