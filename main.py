import datetime

def main(): 
    dt_now = datetime.datetime.now()

    f = open('README.md', 'a', encoding='UTF-8')

    f.write(dt_now.strftime('%Y年%m月%d日 %H:%M:%S') + '\n')

    f.close()

if __name__=="__main__":
    main()