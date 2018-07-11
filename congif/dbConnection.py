'''
__data__ = 2018/7/11
__author__ = amy liu
'''
from congif.constant import *

# encoding=utf-8
import pymysql
import re

# 打开数据库连接- BETA 环境
conn = pymysql.connect(
    host=HOST,
    user=USER,
    passwd=PASSWORD,
    port=PORT,
    charset='utf8',
    cursorclass=pymysql.cursors.DictCursor
)

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = conn.cursor()


def do_mysql(sql, db):
    try:
        conn.select_db(db)
        cursor.execute(sql)
        print(sql)
        result = cursor.fetchall()
        print(str(result))

        # 截取验证码
        # mobileContent = re.findall(r"\d{6}", str(result))
        # mobileCode = mobileContent[0]
        # if (len(mobileContent) == 0):
        #     print('')
        # else:
        #     print('验证码：'+ mobileCode)

        print('--------------执行完毕-----------------')

    except Exception as e:
        print(repr(e))

    conn.commit()
    cursor.close()
    conn.close()

def get_mobileCode():
        # 截取验证码

        mobileContent = re.findall(r"\d{6}", do_mysql(re))
        mobileCode = mobileContent[0]
        if (len(mobileContent) == 0):
            print('')
        else:
            print('验证码：'+ mobileCode)

if __name__ == "__main__":
    # 调用 do_mysql() 方法
    do_mysql("SELECT content FROM `p_mobile_send_log` where mobile = '18016311461' ORDER BY id DESC LIMIT 1 ",
             'pica')
