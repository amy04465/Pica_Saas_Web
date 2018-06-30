'''
Created on '2017/1/16' 
@author: 'amy liu'
'''

# coding=utf-8
from email.mime.multipart import MIMEMultipart
import os
import smtplib
from email.mime.text import MIMEText
import time
import sys


def find_result():
    # get test result path
    result_dir = "d:\\Workspace-1\\Project\\MyDemo\\report\\test_result\\"
    # get test result list
    lists = os.listdir(result_dir)
    # order by time
    lists.sort()
    # get the latest test result
    file_new = os.path.join(result_dir, lists[-1])
    # get the file name of the latest test result, and return the name
    file_name = str(lists[-1])
    return file_new, file_name


def send_result_mail():
    file_new = find_result()[0]
    file_name = find_result()[1]
    mail_from = 'liuchunyan.sh@superjia.com'
    mail_to = 'liuchunyan.sh@superjia.com'
    # open result file
    result_file = open(file_new, 'rb')
    # read result file treat as the mail body
    mail_body = result_file.read()
    result_file.close()

    msgRoot = MIMEMultipart('related')
    # define mail title
    timec = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    title = 'Test Result'
    msgRoot['Subject'] = title + '_' + timec
    # define sender card
    msgRoot['From'] = 'AmyLiu' + '<' + str(mail_from) + '>'
    # define receiver card
    msgRoot['To'] = 'AmyLiu' + '<' + str(mail_to) + '>'

    # sent text is displayed as HTML
    msgText = MIMEText(mail_body, _subtype='html', _charset='utf-8')
    # get current time
    msgRoot['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')
    msgRoot.attach(msgText)

    # add an attachment
    att = MIMEText(open(file_new, 'rb').read(), 'base64', 'utf-8')
    att["Content-Type"] = 'application/octet-stream'

    # attachment title = file name
    att["Content-Disposition"] = 'attachment; filename="%s"' % (file_name)
    msgRoot.attach(att)

    try:
        smtp = smtplib.SMTP()
        smtp.connect('smtp.exmail.qq.com')
        smtp.login('liuchunyan.sh@superjia.com', 'Seven930327')
        smtp.sendmail(mail_from, mail_to, msgRoot.as_string())
        smtp.close()
        print('email has send out successfully!')
    except Exception as e:
        print(e)
        sys.exit(1)


if __name__ == "__main__":
    send_result_mail()


