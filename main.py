import datetime
import re

def main(): 
    dt_now = datetime.datetime.now()

    f = open('README.md', 'w', encoding='UTF-8')
    contents = f.read()
    date = re.search(r'\<update-at>.+?\</update-at>', contents)
    fix_contents = contents.replace(date, dt_now.strftime('WEBサイトの最終更新 : ' + '%Y年%m月%d日 %H:%M:%S'))
    f.write(fix_contents)
    f.close()

if __name__=="__main__":
    main()