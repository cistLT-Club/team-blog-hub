import datetime
import re

def main(): 
    dt_now = datetime.datetime.now()

    fr = open('README.md', 'r', encoding='UTF-8')
    contents = fr.read()
    date = re.search(r'\<update-at>.+?\</update-at>', contents)
    fix_contents = contents.replace(date, dt_now.strftime('WEBサイトの最終更新 : ' + '%Y年%m月%d日 %H:%M:%S'))
    fw = open('README.md', 'w', encoding='UTF-8')
    fw.write(fix_contents)
    fw.close()

if __name__=="__main__":
    main()