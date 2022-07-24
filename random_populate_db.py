# ----------------------------------------------------------------
# Adds random apporiate data to the database for testing the Graph and DB api
# ----------------------------------------------------------------


import pymysql
import random
import time
DBconn = pymysql.connect(
    host='121.98.68.25',
    port=1706,
    user='appuser',
    passwd='o6Rf@K*#5%sLDt',
    db='MagsHealthApp')
sqlCur = DBconn.cursor()

emailsUsed = ['a', 'krish@gmail.com']
numberOfGeneratedRecords = 50
for crntemail in emailsUsed:
    crntday = 1
    crntMonth = 3
    crntweight = 55
    for i in range(numberOfGeneratedRecords):
        # Random vars ------------------------------------------------
        crntweight += round(random.uniform(-4.5, 4.65), 2)
        crntday = crntday + random.randint(1, 3)
        if(crntday >= 30):
            crntday = 1
            crntMonth += 1
        todayStrtemp = "2022-0" + str(crntMonth) + "-" + str(crntday)
        sqlcmd = """
            INSERT INTO dataTable (email, weight, time) 
            SELECT '{0}',{1},'{2}' FROM DUAL 
            WHERE NOT EXISTS (SELECT * FROM dataTable WHERE email='{0}' and time='{2}');
        """.format(crntemail, str(crntweight)[0:5], todayStrtemp)
        sqlCur.execute(sqlcmd)
        print(i, "--", crntemail, str(crntweight)[0:5], todayStrtemp)
        time.sleep(0.2)
    DBconn.commit()
