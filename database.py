import pymysql.cursors

con = pymysql.connect(host='88.99.218.137',
                      port=3306,
                      user='webmazei_project',
                      password='Project@2021',
                      db='webmazei_project',
                      charset='utf8mb4',
                      cursorclass=pymysql.cursors.DictCursor)
