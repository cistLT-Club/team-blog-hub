import datetime
import re

def main(): 
    dt_now = datetime.datetime.now()

    fr = open('README.md')
    contents = fr.read()
    print(contents)
    date = re.search(r'\<update-at>.+?\</update-at>', contents).group()
    print(date)
    fix_date = dt_now.strftime('<update-at>WEBサイトの最終更新 : ' + '%Y年%m月%d日 %H:%M:%S' + '</update-at>')
    fix_contents = contents.replace(str(date), str(fix_date))
    fw = open('README.md', 'w', encoding='UTF-8')
    fw.write(fix_contents)
    fw.close()

if __name__=="__main__":
    main()