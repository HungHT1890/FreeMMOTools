import requests,time,re

import uuid
import random

class ImapPopEnbale:
    
    def __init__(self,mail,pwd, proxy = 'none'):
        
        self.mail = mail,
        self.pwd = pwd
        self.proxy = proxy
        self.mscv = ""
        self.r = requests.Session()
        
        
        if self.proxy != 'none':
            if len(proxy.split(":")) == 2:
                            
                proxyies = proxy
                        
            else:
            
                
                proxyies = proxy.split(":")[2] + ":" + proxy.split(":")[3] + "@" + proxy.split(":")[0] + ":" +proxy.split(":")[1]
                                

            data =  {
                        'http': f'http://{proxyies}',
                        'https': f'http://{proxyies}',
                        'socks4': f'socks4://{proxyies}',
                        'socks5': f'socks5://{proxyies}'
                    }
            
            self.r.proxies.update(data)

    

        
    def LoginToTurnXOWA(self):
   
            for _ in range(10):
                
                
                try:
                    
                    self.r.cookies.clear()
                    headers = {
                                        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                                        'accept-language': 'en-US,en;q=0.9',
                                        # 'cookie': 'OH.DCAffinity=OH-sea; OH.FLID=beda8113-d327-44f6-8942-aa657810528a; .AspNetCore.OpenIdConnect.Nonce.0CFLyH9ZR0LklVJ2scyKz5oa3tf5EH2bZleIr-4Yeg3E_aHjedOHVFPWj5BrIft1fTN77Co20ZWdaJnsW3CqhR__KozWfcBkKvIpntqdV76cjMK4ZB6k76hwNpQEWjqv0l8i1DVMMjzxHt-TqpCfC7XTPa0eVjzV80-OXQ_61Tp-5_2vf3jigOmYlQgF_76bX1iUG5ylEE4vcozrsRmaOvTcEitdZXxa1L7bxafcdbauEptfb-4xZvEMnBvLDg5f=N; .AspNetCore.Correlation.T-ZzTaxClvdrttOU3MkRHYYkGI6zp3QN-dwYrbhWoX0=N; MUID=24254E5D61146FF23B755A2D60AB6E8C',
                                        'priority': 'u=0, i',
                                        'sec-ch-ua': '"Chromium";v="124", "Microsoft Edge";v="124", "Not-A.Brand";v="99"',
                                        'sec-ch-ua-mobile': '?0',
                                        'sec-ch-ua-platform': '"Windows"',
                                        'sec-ch-ua-platform-version': '"10.0.0"',
                                        'sec-fetch-dest': 'document',
                                        'sec-fetch-mode': 'navigate',
                                        'sec-fetch-site': 'none',
                                        'sec-fetch-user': '?1',
                                        'upgrade-insecure-requests': '1',
                                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0',
                                        'x-edge-shopping-flag': '0',
                                    }

                    timeis = int(time.time())


                    response = self.r.get(f'https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=156&ct={timeis}&rver=7.0.6738.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26cobrandid%3dab0455a0-8d03-46b9-b18b-df2f57b9e44c%26deeplink%3dowa%252f%26RpsCsrfState%3d{uuid.uuid4()}&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=ab0455a0-8d03-46b9-b18b-df2f57b9e44c',  headers=headers)


                    ppft = re.findall(r'name="PPFT" id="i0327" value="(.*?)"',response.text)[0]
                    #urlStaySignIn:'
                    url_stay = re.findall(r"urlPostMsa:'(.*?)'",response.text)[0]
                    cookie_str = "; ".join([f"{key}={value}" for key, value in self.r.cookies.get_dict().items()])


                    headers = {
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                        'Accept-Language': 'en-US,en;q=0.9',
                        'Cache-Control': 'max-age=0',
                        'Connection': 'keep-alive',
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'Cookie': cookie_str,
                        'Origin': 'https://login.live.com',
                        'Referer': url_stay,
                        'Sec-Fetch-Dest': 'document',
                        'Sec-Fetch-Mode': 'navigate',
                        'Sec-Fetch-Site': 'same-origin',
                        'Sec-Fetch-User': '?1',
                        'Upgrade-Insecure-Requests': '1',
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0',
                        'X-Edge-Shopping-Flag': '0',
                        'sec-ch-ua': '"Chromium";v="124", "Microsoft Edge";v="124", "Not-A.Brand";v="99"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"Windows"',
                        'sec-ch-ua-platform-version': '"10.0.0"',
                    }





                    data = {
                        "psRNGCDefaultType": "",
                        "psRNGCEntropy": "",
                        "psRNGCSLK": "",
                        "canary": "",
                        "ctx": "",
                        "hpgrequestid": "",
                        "PPFT": ppft,
                        "PPSX": "Passpo",
                        "NewUser": "1",
                        "FoundMSAs": "",
                        "fspost": "0",
                        "i21": "0",
                        "CookieDisclosure": "0",
                        "IsFidoSupported": "1",
                        "isSignupPost": "0",
                        "isRecoveryAttemptPost": "0",
                        "i13": "0",
                        "login": self.mail,
                        "loginfmt": self.mail,
                        "type": "11",
                        "LoginOptions": "3",
                        "lrt": "",
                        "lrtPartition": "",
                        "hisRegion": "",
                        "hisScaleUnit": "",
                        "passwd": self.pwd
                    }



                    response = self.r.post(url_stay,headers=headers,data=data)

                    cookie_str = "; ".join([f"{key}={value}" for key, value in self.r.cookies.get_dict().items()])


                    ppft = re.findall(r"sFT:'(.*?)'",response.text)[0]
                    #urlStaySignIn:'
                    url_stay = re.findall(r"urlPost:'(.*?)'",response.text)
                    for url in url_stay:
                        if "route" in url:
                            url_stay = url
                            break
                        



                    headers = {
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                        'Accept-Language': 'en-US,en;q=0.9',
                        'Cache-Control': 'max-age=0',
                        'Connection': 'keep-alive',
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'Cookie': cookie_str,
                        'Origin': 'https://login.live.com',
                        'Referer': url_stay,
                        'Sec-Fetch-Dest': 'document',
                        'Sec-Fetch-Mode': 'navigate',
                        'Sec-Fetch-Site': 'same-origin',
                        'Sec-Fetch-User': '?1',
                        'Upgrade-Insecure-Requests': '1',
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0',
                        'X-Edge-Shopping-Flag': '0',
                        'sec-ch-ua': '"Chromium";v="124", "Microsoft Edge";v="124", "Not-A.Brand";v="99"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"Windows"',
                        'sec-ch-ua-platform-version': '"10.0.0"',
                    }

                    data = {
                        "LoginOptions": "1",
                        "type": "28",
                        "ctx": "",
                        "hpgrequestid": "",
                        "PPFT": ppft,
                        "canary": ""
                    }

                    response = self.r.post(url_stay,headers=headers,data=data)

                    cookie_str = "; ".join([f"{key}={value}" for key, value in self.r.cookies.get_dict().items()])


                    nap =  re.findall(r'id="NAP" value="(.*?)"',response.text)[0]
                                
                    #nap = urllib.parse.unquote(nap)
                            
                    anon = re.findall(r'id="ANON" value="(.*?)"',response.text)[0]
                    #anon = urllib.parse.unquote(anon)

                    anonexp = re.findall(r'id="ANONExp" value="(.*?)"',response.text)[0]

                    wlssc = re.findall(r'id="t" value="(.*?)"',response.text)[0]
                    #wlssc = urllib.parse.unquote(wlssc)
                                
                    NAPExp = re.findall(r'id="NAPExp" value="(.*?)"',response.text)[0]

                    pprid = re.findall(r"'MSPCID': '(.*?)'",str(self.r.cookies.get_dict()))[0]

                    url_owa = re.findall(r'action="(.*?)"',response.text)[0]



                    headers = {
                        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                        'accept-language': 'en-US,en;q=0.9',
                        'cache-control': 'max-age=0',
                        'content-type': 'application/x-www-form-urlencoded',
                        'cookie':cookie_str,
                        'origin': 'https://login.live.com',
                        'priority': 'u=0, i',
                        'referer': 'https://login.live.com/',
                        'sec-ch-ua': '"Chromium";v="124", "Microsoft Edge";v="124", "Not-A.Brand";v="99"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"Windows"',
                        'sec-ch-ua-platform-version': '"10.0.0"',
                        'sec-fetch-dest': 'document',
                        'sec-fetch-mode': 'navigate',
                        'sec-fetch-site': 'same-site',
                        'upgrade-insecure-requests': '1',
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0',
                        'x-edge-shopping-flag': '0',
                    }


                    data = {
                        'NAPExp': NAPExp,
                        'wbids': '0',
                        'pprid': pprid,
                        'wbid': 'MSFT',
                        'NAP': nap,
                        'ANON': anon,
                        'ANONExp': anonexp,
                        't': wlssc,
                    }



                    response = self.r.post(url_owa,headers=headers,data=data)
                    owa_canary = self.r.cookies.get_dict().get('X-OWA-CANARY')

                    self.mscv = response.headers.get('MS-CV')
                    if owa_canary != None:
                        break
                    
                    time.sleep(5)
                except:
                    pass

    
    
    def TurnImapPop3(self):
        
        
        
        try:
        
            self.LoginToTurnXOWA()
            
            owa_canary = self.r.cookies.get_dict().get('X-OWA-CANARY')
            
            if owa_canary == None:
                return f"Turn Imap Fail Error: OWA_CANARY"
            cookie_str = "; ".join([f"{key}={value}" for key, value in self.r.cookies.get_dict().items()])

        
            headers = {
                'accept': '*/*',
                'accept-language': 'vi-VN,vi;q=0.9',
                'action': 'SetConsumerMailbox',
                # 'content-length': '0',
                'content-type': 'application/json; charset=utf-8',
                'ms-cv': self.mscv,
                'origin': 'https://outlook.live.com',
                'prefer': 'exchange.behavior="IncludeThirdPartyOnlineMeetingProviders"',
                'priority': 'u=1, i',
                'referer': 'https://outlook.live.com/',
                'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
                'x-owa-canary': owa_canary,
                'x-owa-correlationid': str(uuid.uuid4()),
                'x-owa-hosted-ux': 'false',
                'x-owa-sessionid': str(uuid.uuid4()),
                'x-owa-urlpostdata': '%7B%22__type%22%3A%22SetConsumerMailboxRequest%3A%23Exchange%22%2C%22Header%22%3A%7B%22__type%22%3A%22JsonRequestHeaders%3A%23Exchange%22%2C%22RequestServerVersion%22%3A%22V2018_01_08%22%2C%22TimeZoneContext%22%3A%7B%22__type%22%3A%22TimeZoneContext%3A%23Exchange%22%2C%22TimeZoneDefinition%22%3A%7B%22__type%22%3A%22TimeZoneDefinitionType%3A%23Exchange%22%2C%22Id%22%3A%22Greenwich%20Standard%20Time%22%7D%7D%7D%2C%22Options%22%3A%7B%22PopEnabled%22%3Atrue%2C%22PopMessageDeleteEnabled%22%3Afalse%2C%22ImapEnabled%22%3Atrue%7D%7D',
                'x-req-source': 'Mail',
                'cookie': cookie_str,
            }

            params = {
                'action': 'SetConsumerMailbox',
                'app': 'Mail',
                'n': str(random.randint(20,100)),
            }

            response = self.r.post('https://outlook.live.com/owa/0/service.svc', params=params, headers=headers)

            if '"WasSuccessful":true' in response.text:
                return "IMAP|POP3 Enable Success"
            
            else:
                return f"IMAP|POP3 Enable Fail {response.text}"
        
        except Exception as e:
        
            return f"Turn Imap Fail Error: {str(e)}"
            


