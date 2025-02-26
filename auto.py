import requests, rich, os, sys, re, random, string,uuid,time,asyncio
import httpx
import itertools
from time import sleep as sp
from os import system as sm
from datetime import datetime
from rich import print as rp
from bs4 import BeautifulSoup as bsoup
from rich.panel import Panel as pan
from concurrent.futures import ThreadPoolExecutor as ter
####sm("xdg-open https://www.facebook.com/pabloyjoaquin.75")
try:
  os.mkdir("/sdcard/atc")
except:
  pass
def clear():
    if sys.platform in ['win32','win64']:
        os.system('cls')
    else:
        os.system('clear')
#ual=requests.get("https://gist.githubusercontent.com/pzb/b4b6f57144aea7827ae4/raw/cf847b76a142955b1410c8bcef3aabe221a63db1/user-agents.txt").text.splitlines()
ok=[]
loop=0
def logo():
    rp(pan("""[bold cyan]
              █▀▀█ ▀▀█▀▀ ▒█▀▀█ ░░ ▒█▀▀▀ ▒█▀▀█
              █▄▄█ ░▒█░░ ▒█░░░ ▀▀ ▒█▀▀▀ ▒█▀▀▄
              █░▒█ ░▒█░░ ▒█▄▄█ ░░ ▒█░░░ ▒█▄▄█
    """,title="[bold yellow]AUTO CREATE FB",border_style="bold magenta"))
    rp(pan("[bold cyan]DEVLOPER: [bold red]PABLO/ANDREW DEV\n[bold cyan]FACEBOOK: [bold blue][u]https://m.facebook.com/pabloyjoaquin.75[/u]\n[bold cyan]GITHUB: [bold green]  Scammur",border_style="bold magenta"))
emails=0
def main():
    global l, methy
    clear()
    logo()
    rp(pan("[bold cyan][[bold yellow]1[bold cyan]] [bold green]WIFI\n[bold cyan][[bold yellow]2[bold cyan]] [bold green]DATA(Has Auto Reminder For Airplane Mode)",border_style="bold purple"))
    methy=int(input(" \033[1;32mChoose: \033[1;36m"))
    #x=int(input(" How Many Acc: "))
    cc=0
    clear()
    logo()
    rp(pan("[bold cyan][[bold yellow]1[bold cyan]] [bold green]TEMPMAIL API 1\n[bold cyan][[bold yellow]2[bold cyan]] [bold green]TEMPMAIL API 2\n[bold cyan][[bold yellow]3[bold cyan]] [bold green]TEMPMAIL API 3",border_style="bold purple"))
    tempapi=int(input("\033[1;36m Choose API: \033[1;33m"))
    l=int(input("\033[1;36mHOW MANY ACC: \033[1;32m"))
    with ter(max_workers=1) as autoc:
      clear()
      logo()
      rp(pan("[bold cyan]SAVE IN:\n/sdcard/atc/auto-create-cookies.txt(format: email|uid|password|cookies)\n/sdcard/code.txt(format: email|password|activation_code)\n/sdcard/atc/auto-create-ok.txt(format: email|password)\n[bold magenta]MAGENTA [bold cyan]= [bold yellow]SUCCESS\n[bold green]GREEN [bold cyan]= [bold yellow]SUCCESS BUT AUTO APPROVE FAIL\n[bold red]RED [bold cyan]= [bold yellow]CHECKPOINT",border_style="bold purple"))
      fnn=open("fname.txt","r").read().splitlines()
      lnn=open("lname.txt","r").read().splitlines()
      rp(pan("[bold cyan][[bold yellow]1[bold cyan]][bold green] Default Password\n[bold cyan][[bold yellow]2[bold cyan]][bold green] Custom Password",border_style="bold magenta"))
      passlist=input(" \033[1;37mChoose Number: ")
      pl=[]
      if passlist == "2":
            pasl=input(" Enter Custom Password: ")
            pl.append(pasl)
      for i in range(l):
        firstn=random.choice(fnn)
        lastn=random.choice(lnn)
        if passlist == "1":
          passw="%s"%(random.choice(open("words.txt","r").read().splitlines()))+''.join(random.choices(string.ascii_letters+string.digits+"_"+"-"+"-"+"$"+"@"+"("+")"+"&"+"{"+"}"+"/",k=random.randint(6,15)))
        else:
          passw=pl[0]
        #passw=str(firstn).lower()+str(lastn).lower()+''.join(random.choices(string.ascii_letters+string.digits+"_"+"-"+"-",k=random.randint(10,15)))
        if tempapi == 1:
          autoc.submit(autocr,firstn,lastn,passw)
        elif tempapi == 2:
          autoc.submit(autocr2,firstn,lastn,passw)
        else:
          autoc.submit(autocr3,firstn,lastn,passw)
          
       
proxi=["N"]
proxyi=open("prox.txt","r").read().splitlines()
apm=0

###################################

API_URL = "https://www.inboxpro-mail.com/api/messages/{}/7SkcprAF6NGnyohsZiR1"

domains = itertools.cycle(["inboxpro-mail.com", "socialmediaboosting.store"])

def generate_random_email():
    prefix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    domain = next(domains) 
    return f"{prefix}@{domain}"

def fetch_email_code(email):
    timeout = 25
    start_time = time.time()

    while time.time() - start_time < timeout:
        response = requests.get(API_URL.format(email))
        
        if response.status_code == 200:
            try:
                messages = response.json()
            except ValueError:
                print("Invalid JSON")
                return None

            for msg in messages:
                subject = msg.get('subject', '')
                print(" CHECKING SUBJECT:", subject)  # Debugging line
                
                # Extract any 5-digit code from the subject
                match = re.search(r'(\d{5})', subject)
                if match:
                    code = match.group(1)
                    print(f" CONFIRMATION CODE FOUND: {code}")  
                    return code  # Stop function after finding the code

        time.sleep(3)  # Check every 3 seconds

    print(" No confirmation code found within the timeout period.")
    return None




def autocr(firstn,lastn,passw):
  global loop, ok, apm
  try:
        sys.stdout.write("\r \33[1;35mPABLO \033[1;37m(\033[1;36m%s\033[1;37m/\033[1;31m%s\033[1;35m) \033[1;32mSUCCESS:-%s"%(loop,l,len(ok)));sys.stdout.flush()
        ua=random.choice(open("ua.txt","r").read().splitlines())
        session = requests.Session()
        #session=httpx.Client()
        proxyl=random.choice(proxyi)
        proxmi={"http": "%s"%(proxyl),"https": "%s"%(proxyl)}
        headersi = {
          'authority': 'm.facebook.com',
          'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
          'accept-language': 'en-US,en;q=0.9,es-US;q=0.8,es;q=0.7',
          'cache-control': 'no-cache',
          # 'cookie': 'datr=inFuZ9STTbCrji-CeQ2khzQ8; ps_l=1; ps_n=1; sb=GT1vZ-c2G9smOGJ2Bf2HPssP; dpr=3.2983407974243164; locale=en_US; vpd=v1%3B688x360x3; wl_cbv=v2%3Bclient_version%3A2701%3Btimestamp%3A1735987855; m_pixel_ratio=3; wd=360x688; fr=0HlqlDFNecU6G2zfr.AWXUyebpT8x2tz54D4Ic5eRI9O8.Bnbz0Z..AAA.0.0.BnekGl.AWXYPoGPXfY',
          'dpr': '3',
          'pragma': 'no-cache',
          'referer': 'https://m.facebook.com/',
          'sec-ch-prefers-color-scheme': 'dark',
          'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="34", "Google Chrome";v="34"',
          'sec-ch-ua-mobile': '?1',
          'sec-ch-ua-platform': '"Android"',
          'sec-fetch-dest': 'document',
          'sec-fetch-mode': 'navigate',
          'sec-fetch-site': 'same-origin',
          'sec-fetch-user': '?1',
          'upgrade-insecure-requests': '1',
          'user-agent': ua,
          'viewport-width': '980',
          
        }
        if "Y" in proxi:
          getlog=session.get("https://m.facebook.com/reg/",headers=headersi,proxies=proxmi, timeout=20)
          open("fb_proxy.txt","a").write(str(proxyl)+"\n")
        else:
          getlog=session.get("https://m.facebook.com/reg/",headers=headersi)
          
        print("\n\033[1;37m CREATING  ACCOUNT")
        headers = {
          'authority': 'm.facebook.com',
          'accept': '*/*',
          'accept-language': 'en-US,en;q=0.9,es-US;q=0.8,es;q=0.7',
          'cache-control': 'no-cache',
          'content-type': 'application/x-www-form-urlencoded',
          # 'cookie': 'datr=inFuZ9STTbCrji-CeQ2khzQ8; ps_l=1; ps_n=1; sb=GT1vZ-c2G9smOGJ2Bf2HPssP; dpr=3.2983407974243164; locale=en_US; vpd=v1%3B688x360x3; wl_cbv=v2%3Bclient_version%3A2701%3Btimestamp%3A1735987855; m_pixel_ratio=3; wd=360x688; x-referer=eyJyIjoiL3JlZy8%2FaXNfdHdvX3N0ZXBzX2xvZ2luPTAmY2lkPTEwMyZyZWZzcmM9ZGVwcmVjYXRlZCZzb2Z0PWhqayIsImgiOiIvcmVnLz9pc190d29fc3RlcHNfbG9naW49MCZjaWQ9MTAzJnJlZnNyYz1kZXByZWNhdGVkJnNvZnQ9aGprIiwicyI6Im0ifQ%3D%3D; rs=5%7C1%7C2000%7C1%7Chahaha%40gmail.com%7CVv%7CVg%7CVv+Vg%7C3%7C%7C%7C1; fr=0HlqlDFNecU6G2zfr.AWWAxrvdjM2j5KVonR_DsCioIwY.Bnbz0Z..AAA.0.0.BnekLU.AWWDGUp45DE',
          'origin': 'https://m.facebook.com',
          'pragma': 'no-cache',
          'referer': 'https://m.facebook.com/reg/?is_two_steps_login=0&cid=103',
          'sec-ch-prefers-color-scheme': 'dark',
          'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="34", "Google Chrome";v="34"',
          'sec-ch-ua-mobile': '?1',
          'sec-ch-ua-platform': '"Android"',
          'sec-fetch-dest': 'empty',
          'sec-fetch-mode': 'cors',
          'sec-fetch-site': 'same-origin',
          'user-agent': ua,
          'x-asbd-id': '%s'%(random.randint(1e5,199999)),
          'x-fb-lsd': re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),
          'x-requested-with': 'XMLHttpRequest',
          'x-response-format': 'JSONStream',
          
        }
        fetchmail=requests.Session()
        #sessionid=re.search('var sessionid="(.*?)"', emailapi.text).group(1)
        print("\033[1;37m FILLING UP CREDENTIALS")
        #sid=str(uuid.uuid4()).replace("-","")
        #sid=''.join(random.choices("abcdef"+"123456789",k=32))
        #email=str(firstn).lower()+str(lastn).lower()+"%s@mailbox.in.ua"%(''.join(random.choices(string.digits,k=5)))
        dom=fetchmail.get("https://inboxes.com/api/v2/domain").json()
        #rp(dom)
        dummynum="+6393119%s"%(''.join(random.choices(string.digits,k=5)))
        dummymail=str("%s@%s"%(''.join(random.choices(string.ascii_letters,k=random.randint(6,8)))+''.join(random.choices(string.digits,k=random.randint(1,4))),random.choice(["gmail.com","yahoo.com","msn.com","mail.com","live.com","inbox.com","aol.com","outlook.com","hotmail.com"]))).lower()
        dummys=random.choice([dummymail,dummynum])
        print("\033[1;37m DUMMY: \033[1;36m%s"%(dummys))
        time.sleep(1)
        ##############email=str(firstn).lower()+''.join(random.choices(string.digits,k=4))+"@%s"%(dom['domains'][random.choice([0,1,2,10,11])]['qdn'])
        email = generate_random_email()
        print("\033[1;37m EMAIL: \033[1;36m%s"%(email))
        time.sleep(1)
        print("\033[1;37m Firstname: \033[1;36m%s"%(firstn))
        time.sleep(1)
        print("\033[1;37m Lasttname: \033[1;36m%s"%(lastn))
        time.sleep(1)
        print("\033[1;37m Password: \033[1;36m%s"%(passw))
        data = {
                'lsd': re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),
                'jazoest': re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),
                'ccp': '2',
                'reg_instance': re.search('name="reg_instance" value="(.*?)"', str(getlog.text)).group(1),
                'submission_request': 'true',
                'helper': '',
                'reg_impression_id': re.search('name="reg_impression_id" value="(.*?)"', str(getlog.text)).group(1),
                'ns': '0',
                'zero_header_af_client': '',
                'app_id': '',
                'logger_id': '',
                'field_names[]': [
                    'firstname',
                    'reg_email__',
                    'sex',
                    'birthday_wrapper',
                    'reg_passwd__',
                    ],
                'firstname': firstn,
                'lastname': lastn,
                'reg_email__': dummys,#str(email),
                'sex': str(random.randint(1,2)),
                'custom_gender': '',
                'did_use_age': 'false',
                'birthday_month': str(random.randint(1,12)),
                'birthday_day': str(random.randint(10,26)),
                'birthday_year': str(random.randint(1970,1999)),
                'age_step_input': '',
                'reg_passwd__': passw,
                'submit': 'Sign Up',
                #'fb_dtsg': re.search('"dtsg":{"token":"(.*?")', str(getlog.text)).group(1),
                }
        #rp(data)
        if "Y" in proxi:
          po=session.post('https://m.facebook.com/reg/submit/?privacy_mutation_token=eyJ0eXBlIjowLCJjcmVhdGlvbl90aW1lIjoxNzM4MzM0OTE3LCJjYWxsc2l0ZV9pZCI6OTA3OTI0NDAyOTQ4MDU4fQ%3D%3D&multi_step_form=1&skip_suma=0&shouldForceMTouch=1&ref=dbl',headers=headers,data=data, allow_redirects=True,proxies=proxmi, timeout=20)
        else:
          po=session.post('https://m.facebook.com/reg/submit/?privacy_mutation_token=eyJ0eXBlIjowLCJjcmVhdGlvbl90aW1lIjoxNzM4MzM0OTE3LCJjYWxsc2l0ZV9pZCI6OTA3OTI0NDAyOTQ4MDU4fQ%3D%3D&multi_step_form=1&skip_suma=0&shouldForceMTouch=1&ref=dbl',headers=headers,data=data, allow_redirects=True)
        rp(po.request.url)   
        print("\033[1;37m FILLING CREDENTIALS \033[1;32mDONE")
        Aking=session.cookies.get_dict().keys()
        #Aking=session.cookies.keys()
        time.sleep(1)
        print("\033[1;36m BYPASSING EMAIL RESTRICTION")
        uid=session.cookies.get_dict()['c_user']
        confirmemail=session.get("https://m.facebook.com/confirmemail.php",headers=headers,allow_redirects=True)
        #rp(confirmemail.request.url)
        changeemaillog=session.get("https://m.facebook.com/changeemail",headers=headers,allow_redirects=True)
        #rp(changeemaillog.request.url)
        #open("/sdcard/scrap.txt","a").write(changeemaillog.text)
        #data9=re.search('name="reg_instance" value="(.*?)"',changeemaillog.text).group(1)
        data9 = {
          'next': '',
          'old_email': dummys,
          'reg_instance': re.search('name="reg_instance" value="(.*?)"',changeemaillog.text).group(1),
          'new': email,
          'submit': 'Add',
          'fb_dtsg': re.search('name="fb_dtsg" value="(.*?)"',changeemaillog.text).group(1),
          'jazoest': re.search('name="jazoest" value="(.*?)"',changeemaillog.text).group(1),
          'lsd': re.search('{"token":"(.*?)"}',changeemaillog.text).group(1),
          '__dyn': '1KQdAG1mws8-t0BBBzEnwSwgE98nwgU2owSwMxW0Horx60lW4o3Bw4Ewk9E4W0qa0FE6S082x60na1gwGwcq0RE2IwcK0iC1qw8W1uwa-10w5Nxy0gq0Lo6-1FwLw5jw7zwde',
          '__csr': '',
          '__req': '2',
          '__fmt': '1',
          '__a': re.search('"encrypted":"(.*?)"}',changeemaillog.text).group(1),
          '__user': session.cookies.get_dict()['c_user'],
          
        }
        cookiell=str(session.cookies.get_dict()).replace("{","").replace("}","").replace(": ","=").replace(", ",";").replace("'","")
        #rp(data9)
        changeemailapi=session.post("https://m.facebook.com/setemail",headers=headers,data=data9,allow_redirects=True)
        #rp(changeemailapi.request.url)
        cookielll=str(session.cookies.get_dict()).replace("{","").replace("}","").replace(": ","=").replace(", ",";").replace("'","")
        chemail=session.get("https://m.facebook.com/confirmemail.php?email_changed&soft=hjk",headers=headers,allow_redirects=True)
        #rp(chemail.request.url)
        open("/sdcard/scrap2.txt","w").write(chemail.text)
        print("\033[1;37m BYPASSING EMAIL RESTRICTION \033[1;32mDONE")
        print("\033[1;37m RESENDING CODE")
        params = {
          'type': 'resend',
          'resend_type': 'message',
          'is_soft_cliff': 'false',
          'contact': email,
          
        }
        data8 = {
          'fb_dtsg': re.search('"dtsg":{"token":"(.*?)"',chemail.text).group(1),
          'jazoest': re.search('name="jazoest" value="(.*?)"',changeemaillog.text).group(1),
          'lsd': re.search('{"token":"(.*?)"}',chemail.text).group(1),
          '__dyn': '1KQdAG1mws8-t0BBBwno4a2i5U4e1FwKwSwMxW0Horx60zU3ex60Vo1a852q1ew2io0D24o1sE9k2C2G0pS0H83bw4FwmE2ewnE2Lwg81soow46wbS1LwqobU1kU1UU7u1rwGw',
          '__csr': '',
          '__req': '1',
          '__fmt': '1',
          '__a': re.search('"encrypted":"(.*?)"}',chemail.text).group(1),
          '__user': session.cookies.get_dict()['c_user'],
          
        }
        #rp(data8)
        cookiellll=str(session.cookies.get_dict()).replace("{","").replace("}","").replace(": ","=").replace(", ",";").replace("'","")
        
        #########mail1=fetchmail.get("https://inboxes.com/api/v2/inbox/%s"%(email)).json()
        print("\033[1;37m FINDING CONFIRMATION CODE")
        mail1 = fetch_email_code(email)
        
        if mail1:
        	rp("\n",pan("[bold green]DATE & TIME: [bold cyan]%s\n[bold green]Name: [bold cyan]%s %s\n[bold green]UID: [bold cyan]%s\n[bold green]EMAIL: [bold cyan]%s\n[bold green]PASSWORD: [bold cyan]%s\n[bold green]VERIFICATION CODE: %s\n[bold green]COOKIES: [bold red]%s"%(datetime.now(),firstn,lastn,session.cookies.get_dict()['c_user'],email,passw,mail1,cookiellll),border_style="bold magenta",subtitle="[bold yellow]CREATED"))
        	open("/sdcard/atc/auto-create-cookies.txt","a").write("%s|%s|%s|%s\n"%(email,session.cookies.get_dict()['c_user'],passw,cookiellll))
        	open("/sdcard/atc/code.txt","a").write("%s|%s|%s\n"%(email,passw,mail1))
        	open("/sdcard/atc/auto-create-ok.txt","a").write("%s|%s\n"%(email,passw))
        	print()
        else:
        	return
        
        
        
        #mail1=fetchmail.get("https://tempmail.plus/api/mails?email=%s"%(str(email).replace("@","%40"))).json()['mail_list']
        ####rp(mail1)
        return
        if 'c_user' in Aking:
            if "confirmation code" in str(mail1):
                ok.append(email)
                cookiel=str(session.cookies.get_dict()).replace("{","").replace("}","").replace(": ","=").replace(", ",";").replace("'","")
                rp("\n",pan("[bold green]DATE & TIME: [bold cyan]%s\n[bold green]Name: [bold cyan]%s %s\n[bold green]UID: [bold cyan]%s\n[bold green]EMAIL: [bold cyan]%s\n[bold green]PASSWORD: [bold cyan]%s\n[bold green]VERIFICATION CODE: %s\n[bold green]COOKIES: [bold red]%s"%(datetime.now(),firstn,lastn,session.cookies.get_dict()['c_user'],email,passw,str(''.join(mail1['msgs'][0]['s'])).replace("FB-","").replace("is your Facebook confirmation code","").replace("is your confirmation code",""),cookiel),border_style="bold magenta",subtitle="[bold yellow]CREATED"))
                open("/sdcard/atc/auto-create-cookies.txt","a").write("%s|%s|%s|%s\n"%(email,session.cookies.get_dict()['c_user'],passw,cookiel))
                open("/sdcard/atc/code.txt","a").write("%s|%s|%s\n"%(email,passw,str(''.join(mail1['msgs'][0]['s'])).replace("FB-","").replace("is your Facebook confirmation code","").replace("is your confirmation code","")))
                open("/sdcard/atc/auto-create-ok.txt","a").write("%s|%s\n"%(email,passw))
                if "Y" in proxi:
                    try:
                      open("good_proxy.txt","r").read()
                    except:
                      os.system("touch good_proxy.txt")
                    if proxyl in open("good_proxy.txt","r").read():
                      pass
                    else:
                      open("good_proxy.txt","a").write(str(proxyl)+"\n")
                else:
                    pass
            else:
                print("\r\033[1;31mFAILED TO CREATE")
        else:
            rp("\n",pan("[bold red]Email: [bold cyan]%s\n[bold red]Password: [bold cyan]%s"%(email,passw),subtitle="[bold green]SUSPENDED",border_style="bold red"))
  except Exception as e:
      print(e)
      print("\033[1;36mPLS WAIT FOR 5 SEC")
      time.sleep(5)
  loop+=1
  if methy == 1:
    pass
  else:
    apm+=1
    if apm >= 2:
      rp(" [bold cyan]PLS ON & OFF YOUR AIRPLANE MODE")
      while True:
        try:
            requests.get("https://www.google.com")
        except:
            rp("[bold cyan]ON & OFF AIRPLANE MODE [bold green]DONE\n[bold cyan] Pls wait for 5 sec")
            time.sleep(5)
            apm=0
            break
  
domi=[]
domm=requests.get("https://api.internal.temp-mail.io/api/v4/domains").json()
for dommn in domm['domains']:
    domi.append(dommn['name'])

###################################

def autocr2(firstn,lastn,passw):
  global loop, ok
  try:
        sys.stdout.write("\r \33[1;35mPABLO \033[1;37m(\033[1;36m%s\033[1;37m/\033[1;31m%s\033[1;35m) \033[1;32mSUCCESS:-%s"%(loop,l,len(ok)));sys.stdout.flush()
        ua=random.choice(open("ua.txt","r").read().splitlines())
        session = requests.Session()
        #session=httpx.Client()
        proxyl=random.choice(proxyi)
        proxmi={"http": "socks5://%s"%(proxyl)}
        headersi = {
          'authority': 'm.facebook.com',
          'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
          'accept-language': 'en-US,en;q=0.9,es-US;q=0.8,es;q=0.7',
          'cache-control': 'no-cache',
          # 'cookie': 'datr=inFuZ9STTbCrji-CeQ2khzQ8; ps_l=1; ps_n=1; sb=GT1vZ-c2G9smOGJ2Bf2HPssP; dpr=3.2983407974243164; locale=en_US; vpd=v1%3B688x360x3; wl_cbv=v2%3Bclient_version%3A2701%3Btimestamp%3A1735987855; m_pixel_ratio=3; wd=360x688; fr=0HlqlDFNecU6G2zfr.AWXUyebpT8x2tz54D4Ic5eRI9O8.Bnbz0Z..AAA.0.0.BnekGl.AWXYPoGPXfY',
          'dpr': '3',
          'pragma': 'no-cache',
          'referer': 'https://m.facebook.com/',
          'sec-ch-prefers-color-scheme': 'dark',
          'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="34", "Google Chrome";v="34"',
          'sec-ch-ua-mobile': '?1',
          'sec-ch-ua-platform': '"Android"',
          'sec-fetch-dest': 'document',
          'sec-fetch-mode': 'navigate',
          'sec-fetch-site': 'same-origin',
          'sec-fetch-user': '?1',
          'upgrade-insecure-requests': '1',
          'user-agent': ua,
          'viewport-width': '980',
          
        }
        if "Y" in proxi:
          getlog=session.get("https://m.facebook.com/reg/",headers=headersi,proxies=proxmi)
        else:
          getlog=session.get("https://m.facebook.com/reg/",headers=headersi)
          
        print("\n\033[1;37m CREATING  ACCOUNT")
        headers = {
          'authority': 'm.facebook.com',
          'accept': '*/*',
          'accept-language': 'en-US,en;q=0.9,es-US;q=0.8,es;q=0.7',
          'cache-control': 'no-cache',
          'content-type': 'application/x-www-form-urlencoded',
          # 'cookie': 'datr=inFuZ9STTbCrji-CeQ2khzQ8; ps_l=1; ps_n=1; sb=GT1vZ-c2G9smOGJ2Bf2HPssP; dpr=3.2983407974243164; locale=en_US; vpd=v1%3B688x360x3; wl_cbv=v2%3Bclient_version%3A2701%3Btimestamp%3A1735987855; m_pixel_ratio=3; wd=360x688; x-referer=eyJyIjoiL3JlZy8%2FaXNfdHdvX3N0ZXBzX2xvZ2luPTAmY2lkPTEwMyZyZWZzcmM9ZGVwcmVjYXRlZCZzb2Z0PWhqayIsImgiOiIvcmVnLz9pc190d29fc3RlcHNfbG9naW49MCZjaWQ9MTAzJnJlZnNyYz1kZXByZWNhdGVkJnNvZnQ9aGprIiwicyI6Im0ifQ%3D%3D; rs=5%7C1%7C2000%7C1%7Chahaha%40gmail.com%7CVv%7CVg%7CVv+Vg%7C3%7C%7C%7C1; fr=0HlqlDFNecU6G2zfr.AWWAxrvdjM2j5KVonR_DsCioIwY.Bnbz0Z..AAA.0.0.BnekLU.AWWDGUp45DE',
          'origin': 'https://m.facebook.com',
          'pragma': 'no-cache',
          'referer': 'https://m.facebook.com/reg/?is_two_steps_login=0&cid=103',
          'sec-ch-prefers-color-scheme': 'dark',
          'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="34", "Google Chrome";v="34"',
          'sec-ch-ua-mobile': '?1',
          'sec-ch-ua-platform': '"Android"',
          'sec-fetch-dest': 'empty',
          'sec-fetch-mode': 'cors',
          'sec-fetch-site': 'same-origin',
          'user-agent': ua,
          'x-asbd-id': '%s'%(random.randint(1e5,199999)),
          'x-fb-lsd': re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),
          'x-requested-with': 'XMLHttpRequest',
          'x-response-format': 'JSONStream',
          
        }
        fetchmail=requests.Session()
        #emailapi=fetchmail.get('https://temp-mail.io/en')
        #sessionid=re.search('var sessionid="(.*?)"', emailapi.text).group(1)
        print("\033[1;37m FILLING UP CREDENTIALS")
        sid=str(uuid.uuid4()).replace("-","")
        #sid=''.join(random.choices("abcdef"+"123456789",k=32))
        #email=str(firstn).lower()+str(lastn).lower()+"%s@mailbox.in.ua"%(''.join(random.choices(string.digits,k=5)))
        dummynum="+6393119%s"%(''.join(random.choices(string.digits,k=5)))
        dummymail=str("%s@%s"%(''.join(random.choices(string.ascii_letters,k=random.randint(6,8)))+''.join(random.choices(string.digits,k=random.randint(1,4))),random.choice(["gmail.com","yahoo.com","msn.com","mail.com","live.com","inbox.com","aol.com","outlook.com","hotmail.com"]))).lower()
        dummys=random.choice([dummymail,dummynum])
        namea=firstn+''.join(random.choices(string.digits,k=random.randint(1,5)))
        domain=random.choice(domi)
        empayload={"name": namea, "domain": domain}
        email=fetchmail.post("https://api.internal.temp-mail.io/api/v3/email/new",data=empayload).json()["email"]
        #rp(email)
        print("\033[1;37m DUMMY EMAIL: %s"%(dummys))
        time.sleep(1)
        print("\033[1;37m EMAIL: \033[1;36m%s"%(email))
        time.sleep(1)
        print("\033[1;37m Firstname: \033[1;36m%s"%(firstn))
        time.sleep(1)
        print("\033[1;37m Lasttname: \033[1;36m%s"%(lastn))
        time.sleep(1)
        print("\033[1;37m Password: \033[1;36m%s"%(passw))
        data = {
                'lsd': re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),
                'jazoest': re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),
                'ccp': '2',
                'reg_instance': re.search('name="reg_instance" value="(.*?)"', str(getlog.text)).group(1),
                'submission_request': 'true',
                'helper': '',
                'reg_impression_id': re.search('name="reg_impression_id" value="(.*?)"', str(getlog.text)).group(1),
                'ns': '0',
                'zero_header_af_client': '',
                'app_id': '',
                'logger_id': '',
                'field_names[]': [
                    'firstname',
                    'reg_email__',
                    'sex',
                    'birthday_wrapper',
                    'reg_passwd__',
                    ],
                'firstname': firstn,
                'lastname': lastn,
                'reg_email__': dummys,#str(email),
                'sex': str(random.randint(1,2)),
                'custom_gender': '',
                'did_use_age': 'false',
                'birthday_month': str(random.randint(3,12)),
                'birthday_day': str(random.randint(10,30)),
                'birthday_year': str(random.randint(1990,2003)),
                'age_step_input': '',
                'reg_passwd__': passw,
                'submit': 'Sign Up',
                #'fb_dtsg': re.search('"dtsg":{"token":"(.*?")', str(getlog.text)).group(1),
                }
        if "Y" in proxi:
          po=session.post('https://m.facebook.com/reg/submit/',headers=headers,data=data, allow_redirects=True,proxies=proxmi)
        else:
          po=session.post('https://m.facebook.com/reg/submit/',headers=headers,data=data, allow_redirects=True)
          
        print("\033[1;37m FILLING CREDENTIALS \033[1;32mDONE")
        Aking=session.cookies.get_dict().keys()
        print("\033[1;37m BYPASSING EMAIL")
        uid=session.cookies.get_dict()['c_user']
        confirmemail=session.get("https://m.facebook.com/confirmemail.php",headers=headers,allow_redirects=True)
        rp(confirmemail.request.url)
        changeemaillog=session.get("https://m.facebook.com/changeemail",headers=headers,allow_redirects=True)
        rp(changeemaillog.request.url)
        #open("/sdcard/scrap.txt","a").write(changeemaillog.text)
        #data9=re.search('name="reg_instance" value="(.*?)"',changeemaillog.text).group(1)
        data9 = {
          'next': '',
          'old_email': dummys,
          'reg_instance': re.search('name="reg_instance" value="(.*?)"',changeemaillog.text).group(1),
          'new': email,
          'submit': 'Add',
          'fb_dtsg': re.search('name="fb_dtsg" value="(.*?)"',changeemaillog.text).group(1),
          'jazoest': re.search('name="jazoest" value="(.*?)"',changeemaillog.text).group(1),
          'lsd': re.search('{"token":"(.*?)"}',changeemaillog.text).group(1),
          '__dyn': '1KQdAG1mws8-t0BBBzEnwSwgE98nwgU2owSwMxW0Horx60lW4o3Bw4Ewk9E4W0qa0FE6S082x60na1gwGwcq0RE2IwcK0iC1qw8W1uwa-10w5Nxy0gq0Lo6-1FwLw5jw7zwde',
          '__csr': '',
          '__req': '2',
          '__fmt': '1',
          '__a': re.search('"encrypted":"(.*?)"}',changeemaillog.text).group(1),
          '__user': session.cookies.get_dict()['c_user'],
          
        }
        cookiell=str(session.cookies.get_dict()).replace("{","").replace("}","").replace(": ","=").replace(", ",";").replace("'","")
        rp(data9)
        changeemailapi=session.post("https://m.facebook.com/setemail",headers=headers,data=data9,allow_redirects=True)
        rp(changeemailapi.request.url)
        cookielll=str(session.cookies.get_dict()).replace("{","").replace("}","").replace(": ","=").replace(", ",";").replace("'","")
        chemail=session.get("https://m.facebook.com/confirmemail.php?email_changed&soft=hjk",headers=headers,allow_redirects=True)
        rp(chemail.request.url)
        open("/sdcard/scrap2.txt","w").write(chemail.text)
        print("\033[1;37m CHANGING EMAIL SUCCESS")
        print("\033[1;37m RESENDING CODE")
        params = {
          'type': 'resend',
          'resend_type': 'message',
          'is_soft_cliff': 'false',
          'contact': email,
          
        }
        data8 = {
          'fb_dtsg': re.search('"dtsg":{"token":"(.*?)"',chemail.text).group(1),
          'jazoest': re.search('name="jazoest" value="(.*?)"',changeemaillog.text).group(1),
          'lsd': re.search('{"token":"(.*?)"}',chemail.text).group(1),
          '__dyn': '1KQdAG1mws8-t0BBBwno4a2i5U4e1FwKwSwMxW0Horx60zU3ex60Vo1a852q1ew2io0D24o1sE9k2C2G0pS0H83bw4FwmE2ewnE2Lwg81soow46wbS1LwqobU1kU1UU7u1rwGw',
          '__csr': '',
          '__req': '1',
          '__fmt': '1',
          '__a': re.search('"encrypted":"(.*?)"}',chemail.text).group(1),
          '__user': session.cookies.get_dict()['c_user'],
          
        }
        rp(data8)
        cookiellll=str(session.cookies.get_dict()).replace("{","").replace("}","").replace(": ","=").replace(", ",";").replace("'","")
        while True:
          response = session.post('https://m.facebook.com/confirmation_cliff/',params=params,headers=headers,data=data8, allow_redirects=True)
          rp(response.request.url)
          mail1=fetchmail.get("https://api.internal.temp-mail.io/api/v3/email/%s/messages"%(email)).json()
          rp(mail1)
          if "subject" in str(mail1):
            break
          else:
            continue
        #Aking=session.cookies.keys()
        time.sleep(1)
        tmna=5
        print("\033[1;37m PLS WAIT FOR %s seconds"%(tmna))
        for ___ in range(tmna):
          print(" TIME:%s"%(tmna), end="\r\r")
          tmna-=1
          time.sleep(1)
        print("\033[1;37m FINDING CONFIRMATION CODE")
        #mail1=fetchmail.get("https://tempmail.plus/api/mails?email=%s"%(str(email).replace("@","%40"))).json()['mail_list']
        mail1=fetchmail.get("https://api.internal.temp-mail.io/api/v3/email/%s/messages"%(email)).json()
        rp(mail1)
        if 'c_user' in Aking:
            if "confirmation code" in mail1[0]['subject']:
                ok.append(email)
                cookiel=str(session.cookies.get_dict()).replace("{","").replace("}","").replace(": ","=").replace(", ",";").replace("'","")
                rp("\n",pan("[bold green]DATE & TIME: [bold cyan]%s\n[bold green]Name: [bold cyan]%s %s\n[bold green]UID: [bold cyan]%s\n[bold green]EMAIL: [bold cyan]%s\n[bold green]PASSWORD: [bold cyan]%s\n[bold green]VERIFICATION CODE: %s\n[bold green]COOKIES: [bold red]%s"%(datetime.now(),firstn,lastn,session.cookies.get_dict()['c_user'],email,passw,str(''.join(mail1[0]['subject'])).split("-")[1].replace("is your Facebook confirmation code","").replace("is your confirmation code",""),cookiel),border_style="bold magenta",subtitle="[bold yellow]CREATED"))
                open("/sdcard/atc/auto-create-cookies.txt","a").write("%s|%s|%s|%s\n"%(email,session.cookies.get_dict()['c_user'],passw,cookiel))
                open("/sdcard/atc/code.txt","a").write("%s|%s|%s"%(email,passw,str(''.join(mail1[0]['subject'])).split("-")[1].replace("is your Facebook confirmation code","").replace("is your confirmation code","")))
                open("/sdcard/atc/auto-create-ok.txt","a").write("%s|%s"%(email,passw))
            else:
                print("\r\033[1;31mFAILED TO CREATE")
        else:
            rp("\n",pan("[bold red]Email: [bold cyan]%s\n[bold red]Password: [bold cyan]%s"%(email,passw),subtitle="[bold green]SUSPENDED",border_style="bold red"))
  except Exception as e:
      print(e)
def autocr3(firstn,lastn,passw):
  global loop, ok
  try:
        sys.stdout.write("\r \33[1;35mPABLO \033[1;37m(\033[1;36m%s\033[1;37m/\033[1;31m%s\033[1;35m) \033[1;32mSUCCESS:-%s"%(loop,l,len(ok)));sys.stdout.flush()
        ua=random.choice(open("ua.txt","r").read().splitlines())
        session = requests.Session()
        #session=httpx.Client()
        proxyl=random.choice(proxyi)
        proxmi={"http": "socks5://%s"%(proxyl)}
        headersi = {
          'authority': 'm.facebook.com',
          'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
          'accept-language': 'en-US,en;q=0.9,es-US;q=0.8,es;q=0.7',
          'cache-control': 'no-cache',
          # 'cookie': 'datr=inFuZ9STTbCrji-CeQ2khzQ8; ps_l=1; ps_n=1; sb=GT1vZ-c2G9smOGJ2Bf2HPssP; dpr=3.2983407974243164; locale=en_US; vpd=v1%3B688x360x3; wl_cbv=v2%3Bclient_version%3A2701%3Btimestamp%3A1735987855; m_pixel_ratio=3; wd=360x688; fr=0HlqlDFNecU6G2zfr.AWXUyebpT8x2tz54D4Ic5eRI9O8.Bnbz0Z..AAA.0.0.BnekGl.AWXYPoGPXfY',
          'dpr': '3',
          'pragma': 'no-cache',
          'referer': 'https://m.facebook.com/',
          'sec-ch-prefers-color-scheme': 'dark',
          'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="34", "Google Chrome";v="34"',
          'sec-ch-ua-mobile': '?1',
          'sec-ch-ua-platform': '"Android"',
          'sec-fetch-dest': 'document',
          'sec-fetch-mode': 'navigate',
          'sec-fetch-site': 'same-origin',
          'sec-fetch-user': '?1',
          'upgrade-insecure-requests': '1',
          'user-agent': ua,
          'viewport-width': '980',
          
        }
        if "Y" in proxi:
          getlog=session.get("https://m.facebook.com/reg/",headers=headersi,proxies=proxmi)
        else:
          getlog=session.get("https://m.facebook.com/reg/",headers=headersi)
          
        print("\n\033[1;37m CREATING  ACCOUNT")
        headers = {
          'authority': 'm.facebook.com',
          'accept': '*/*',
          'accept-language': 'en-US,en;q=0.9,es-US;q=0.8,es;q=0.7',
          'cache-control': 'no-cache',
          'content-type': 'application/x-www-form-urlencoded',
          # 'cookie': 'datr=inFuZ9STTbCrji-CeQ2khzQ8; ps_l=1; ps_n=1; sb=GT1vZ-c2G9smOGJ2Bf2HPssP; dpr=3.2983407974243164; locale=en_US; vpd=v1%3B688x360x3; wl_cbv=v2%3Bclient_version%3A2701%3Btimestamp%3A1735987855; m_pixel_ratio=3; wd=360x688; x-referer=eyJyIjoiL3JlZy8%2FaXNfdHdvX3N0ZXBzX2xvZ2luPTAmY2lkPTEwMyZyZWZzcmM9ZGVwcmVjYXRlZCZzb2Z0PWhqayIsImgiOiIvcmVnLz9pc190d29fc3RlcHNfbG9naW49MCZjaWQ9MTAzJnJlZnNyYz1kZXByZWNhdGVkJnNvZnQ9aGprIiwicyI6Im0ifQ%3D%3D; rs=5%7C1%7C2000%7C1%7Chahaha%40gmail.com%7CVv%7CVg%7CVv+Vg%7C3%7C%7C%7C1; fr=0HlqlDFNecU6G2zfr.AWWAxrvdjM2j5KVonR_DsCioIwY.Bnbz0Z..AAA.0.0.BnekLU.AWWDGUp45DE',
          'origin': 'https://m.facebook.com',
          'pragma': 'no-cache',
          'referer': 'https://m.facebook.com/reg/?is_two_steps_login=0&cid=103',
          'sec-ch-prefers-color-scheme': 'dark',
          'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="34", "Google Chrome";v="34"',
          'sec-ch-ua-mobile': '?1',
          'sec-ch-ua-platform': '"Android"',
          'sec-fetch-dest': 'empty',
          'sec-fetch-mode': 'cors',
          'sec-fetch-site': 'same-origin',
          'user-agent': ua,
          'x-asbd-id': '%s'%(random.randint(1e5,199999)),
          'x-fb-lsd': re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),
          'x-requested-with': 'XMLHttpRequest',
          'x-response-format': 'JSONStream',
          
        }
        fetchmail=requests.Session()
        #emailapi=fetchmail.get('https://temp-mail.io/en')
        #sessionid=re.search('var sessionid="(.*?)"', emailapi.text).group(1)
        print("\033[1;37m FILLING UP CREDENTIALS")
        
        #sid=''.join(random.choices("abcdef"+"123456789",k=32))
        #email=str(firstn).lower()+str(lastn).lower()+"%s@mailbox.in.ua"%(''.join(random.choices(string.digits,k=5)))
        sid=str(uuid.uuid4()).replace("-","")
        email=fetchmail.get("https://10minutemail.net/address.api.php?new=1&sessionid=%s"%(sid)).json()['mail_get_mail']
        #print(emapi.request.url)
        rp(email)
        #rp(emtok)
        dummynum="+6393119%s"%(''.join(random.choices(string.digits,k=5)))
        dummymail=str("%s@%s"%(''.join(random.choices(string.ascii_letters,k=random.randint(6,8)))+''.join(random.choices(string.digits,k=random.randint(1,4))),random.choice(["gmail.com","yahoo.com","msn.com","mail.com","live.com","inbox.com","aol.com","outlook.com","hotmail.com"]))).lower()
        dummys=random.choice([dummymail,dummynum])
        print("\033[1;37m DUMMY EMAIL: \033[1;36m%s"%(str(dummys).lower()))
        print("\033[1;37m EMAIL: \033[1;36m%s"%(str(email).lower()))
        time.sleep(1)
        print("\033[1;37m Firstname: \033[1;36m%s"%(firstn))
        time.sleep(1)
        print("\033[1;37m Lasttname: \033[1;36m%s"%(lastn))
        time.sleep(1)
        print("\033[1;37m Password: \033[1;36m%s"%(passw))
        data = {
                'lsd': re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),
                'jazoest': re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),
                'ccp': '2',
                'reg_instance': re.search('name="reg_instance" value="(.*?)"', str(getlog.text)).group(1),
                'submission_request': 'true',
                'helper': '',
                'reg_impression_id': re.search('name="reg_impression_id" value="(.*?)"', str(getlog.text)).group(1),
                'ns': '0',
                'zero_header_af_client': '',
                'app_id': '',
                'logger_id': '',
                'field_names[]': [
                    'firstname',
                    'reg_email__',
                    'sex',
                    'birthday_wrapper',
                    'reg_passwd__',
                    ],
                'firstname': firstn,
                'lastname': lastn,
                'reg_email__': str(dummys),
                'sex': str(random.randint(1,2)),
                'custom_gender': '',
                'did_use_age': 'false',
                'birthday_month': str(random.randint(3,12)),
                'birthday_day': str(random.randint(10,30)),
                'birthday_year': str(random.randint(1990,2003)),
                'age_step_input': '',
                'reg_passwd__': passw,
                'submit': 'Sign Up',
                #'fb_dtsg': re.search('"dtsg":{"token":"(.*?")', str(getlog.text)).group(1),
                }
        if "Y" in proxi:
          po=session.post('https://m.facebook.com/reg/submit/',headers=headers,data=data, allow_redirects=True,proxies=proxmi)
        else:
          po=session.post('https://m.facebook.com/reg/submit/',headers=headers,data=data, allow_redirects=True)
        rp(po.request.url)
        print("\033[1;37m FILLING CREDENTIALS \033[1;32mDONE")
        Aking=session.cookies.get_dict().keys()
        #Aking=session.cookies.keys()
        time.sleep(1)
        print("\033[1;37m BYPASSING EMAIL")
        time.sleep(1)
        uid=session.cookies.get_dict()['c_user']
        confirmemail=session.get("https://m.facebook.com/confirmemail.php",headers=headers,allow_redirects=True)
        #rp(confirmemail.request.url)
        changeemaillog=session.get("https://m.facebook.com/changeemail",headers=headers,allow_redirects=True)
        #rp(changeemaillog.request.url)
        #open("/sdcard/scrap.txt","a").write(changeemaillog.text)
        #data9=re.search('name="reg_instance" value="(.*?)"',changeemaillog.text).group(1)
        data9 = {
          'next': '',
          'old_email': dummys,
          'reg_instance': re.search('name="reg_instance" value="(.*?)"',changeemaillog.text).group(1),
          'new': email,
          'submit': 'Add',
          'fb_dtsg': re.search('name="fb_dtsg" value="(.*?)"',changeemaillog.text).group(1),
          'jazoest': re.search('name="jazoest" value="(.*?)"',changeemaillog.text).group(1),
          'lsd': re.search('{"token":"(.*?)"}',changeemaillog.text).group(1),
          '__dyn': '1KQdAG1mws8-t0BBBzEnwSwgE98nwgU2owSwMxW0Horx60lW4o3Bw4Ewk9E4W0qa0FE6S082x60na1gwGwcq0RE2IwcK0iC1qw8W1uwa-10w5Nxy0gq0Lo6-1FwLw5jw7zwde',
          '__csr': '',
          '__req': '2',
          '__fmt': '1',
          '__a': re.search('"encrypted":"(.*?)"}',changeemaillog.text).group(1),
          '__user': session.cookies.get_dict()['c_user'],
          
        }
        cookiell=str(session.cookies.get_dict()).replace("{","").replace("}","").replace(": ","=").replace(", ",";").replace("'","")
        #rp(data9)
        changeemailapi=session.post("https://m.facebook.com/setemail",headers=headers,data=data9,allow_redirects=True)
        #rp(changeemailapi.request.url)
        cookielll=str(session.cookies.get_dict()).replace("{","").replace("}","").replace(": ","=").replace(", ",";").replace("'","")
        chemail=session.get("https://m.facebook.com/confirmemail.php?email_changed&soft=hjk",headers=headers,allow_redirects=True)
        #rp(chemail.request.url)
        open("/sdcard/scrap2.txt","w").write(chemail.text)
        print("\033[1;37m EMAIL BYPASS \033[1;32m SUCCESS")
        print("\033[1;37m RESENDING CODE")
        params = {
          'type': 'resend',
          'resend_type': 'message',
          'is_soft_cliff': 'false',
          'contact': email,
          
        }
        data8 = {
          'fb_dtsg': re.search('"dtsg":{"token":"(.*?)"',chemail.text).group(1),
          'jazoest': re.search('name="jazoest" value="(.*?)"',changeemaillog.text).group(1),
          'lsd': re.search('{"token":"(.*?)"}',chemail.text).group(1),
          '__dyn': '1KQdAG1mws8-t0BBBwno4a2i5U4e1FwKwSwMxW0Horx60zU3ex60Vo1a852q1ew2io0D24o1sE9k2C2G0pS0H83bw4FwmE2ewnE2Lwg81soow46wbS1LwqobU1kU1UU7u1rwGw',
          '__csr': '',
          '__req': '1',
          '__fmt': '1',
          '__a': re.search('"encrypted":"(.*?)"}',chemail.text).group(1),
          '__user': session.cookies.get_dict()['c_user'],
          
        }
        while True:
          response = session.post('https://m.facebook.com/confirmation_cliff/',params=params,headers=headers,data=data8, allow_redirects=True)
          #rp(response.request.url)
          mail1=fetchmail.get("https://10minutemail.net/address.api.php?sessionid=%s"%(sid)).json()['mail_list'][0]
          #rp(mail1)
          if "confirmation code" in str(mail1):
            break
          else:
            continue
        #Aking=session.cookies.keys()
        time.sleep(1)
        tmna=5
        print("\033[1;37m PLS WAIT FOR %s seconds"%(tmna))
        for ___ in range(tmna):
          print(" TIME:%s"%(tmna), end="\r\r")
          tmna-=1
          time.sleep(1)
        print("\033[1;37m FINDING CONFIRMATION CODE")
        mail1=fetchmail.get("https://10minutemail.net/address.api.php?sessionid=%s"%(sid)).json()['mail_list']
        if 'c_user' in Aking:
            if "confirmation code" in str(mail1[0]):
                cookiel=str(session.cookies.get_dict()).replace("{","").replace("}","").replace(": ","=").replace(", ",";").replace("'","")
                rp("\n",pan("[bold green]DATE & TIME: [bold cyan]%s\n[bold green]Name: [bold cyan]%s %s\n[bold green]UID: [bold cyan]%s\n[bold green]EMAIL: [bold cyan]%s\n[bold green]PASSWORD: [bold cyan]%s\n[bold green]VERIFICATION CODE: %s\n[bold green]COOKIES: [bold red]%s"%(datetime.now(),firstn,lastn,session.cookies.get_dict()['c_user'],email,passw,str(mail1[0]['subject']).split("-")[1].replace("is your Facebook confirmation code","").replace("is your confirmation code",""),cookiel),border_style="bold magenta",subtitle="[bold yellow]CREATED"))
                open("/sdcard/atc/auto-create-cookies.txt","a").write("%s|%s|%s|%s\n"%(email,session.cookies.get_dict()['c_user'],passw,cookiel))
                open("/sdcard/atc/code.txt","a").write("%s|%s|%s"%(email,passw,str(''.join(mail1[0]['subject'])).split("-")[1].replace("is your Facebook confirmation code","").replace("is your confirmation code","")))
                open("/sdcard/atc/auto-create-ok.txt","a").write("%s|%s"%(email,passw))
            else:
                print("\r\033[1;31mFAILED TO CREATE")
        else:
            rp("\n",pan("[bold red]Email: [bold cyan]%s\n[bold red]Password: [bold cyan]%s"%(email,passw),subtitle="[bold green]SUSPENDED",border_style="bold red"))
  except Exception as e:
      print(e)
try:
  open("/sdcard/.adm.txt","r").read()
except FileNotFoundError:
  sm("cd /sdcard && touch .adm.txt")
async def bypass():
  file = open('/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/api.py','r')
  file2 = open('/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/sessions.py','r')
  file3 = open('/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/models.py','r')
  data = file.read()
  sess = file2.read()
  approve = file3.read()
  keyword =("print(url)")
  keyword2 = ("print(data)")
  if keyword in data or "echo" in data or "pprint" in data:
    sm('clear')
    print(10*"\n\033[1;31mBYPASS???? HAHAHAHAHAHAHA NOOB")
    print("\n\033[1;33mBYE BYE FILES AHAHAHHAHA")
    exit()
  elif keyword in sess or "echo" in sess or keyword2 in sess or "pprint" in sess or "print(headers)" in sess or "{url}" in sess or "{data}" in sess or "{headers}" in sess or "Console" in sess or "rich" in sess or "exec" in sess or "sys.stdout.write" in sess or "%(" in sess or "%(data)" in sess or "%(headers)" in sess:
    sm('clear')
    if "ADMIN" not in open("/sdcard/.adm.txt","r").read():
      print(20*"\nCAPTURE DATA????? NOOB KID")
      print("\n\033[1;31mBYE BYE FILES")
      exit()
    else:
      await key()
  else:
      await key()
keyy=uuid.uuid4()
try:
  keyys=open("/sdcard/.atc-m.txt","r").read()
except FileNotFoundError:
  open("/sdcard/.atc-m.txt","a").write("PABLO[%s]"%(str(keyy).upper()))
async def key():
    clear()
    logo()
    keyys=open("/sdcard/.atc-m.txt","r").read()
    keys2=httpx.get("https://pastebin.com/raw/j2Ghch9B").text
    if keyys not in keys2:
      os.system('xdg-open https://m.facebook.com/angbo.bomo.75')
      rp("Your Key Is: %s"%(keyys))
    else:
      main()
#asyncio.run(bypass())
main()
