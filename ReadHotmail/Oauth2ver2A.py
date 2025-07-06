import requests,re,time

from urllib.parse import unquote

import codecs
#https://login.microsoftonline.com/common/oauth2/v2.0/authorize?client_id=9e5f94bc-e8a4-4e73-b8be-63364c29d753&response_type=code&redirect_url=http://localhost&scope=https://outlook.office.com/IMAP.AccessAsUser.All offline_access&response_mode=query&state=12345

#8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2
#https://login.microsoftonline.com/common/oauth2/v2.0/authorize?client_id=9e5f94bc-e8a4-4e73-b8be-63364c29d753&response_type=code&redirect_url=http://localhost&scope=https://outlook.office.com/IMAP.AccessAsUser.All https://outlook.office.com/POP.AccessAsUser.All https://outlook.office.com/SMTP.Send https://outlook.office.com/Mail.Read offline_access&response_mode=query&state=12345
#urlMsaSignUp

class GetRefreshToken:
    def __init__(self,email,password,proxy = 'none'):
        self.clientID = "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2"
        self.cookie = ""
        self.req = requests.Session()
        self.urlMsaSignUp = ""
        self.AuthCode = ""
        self.email = email
        self.password = password
        
        if proxy != 'none':
        
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
            
            self.req.proxies.update(data)
    
    
    def GetAuthCode(self):
        


            """Initial Url Auth"""
            
            headers = {
                
                'Accept-Language': 'vi-VN,vi;q=0.9',
            
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
            
            }
            response = self.req.get(f"https://login.microsoftonline.com/common/oauth2/v2.0/authorize?client_id={self.clientID}&response_type=code&redirect_url=http://localhost&scope=https://outlook.office.com/IMAP.AccessAsUser.All https://outlook.office.com/EAS.AccessAsUser.All https://outlook.office.com/EWS.AccessAsUser.All https://outlook.office.com/SMTP.Send https://outlook.office.com/POP.AccessAsUser.All offline_access&response_mode=query&state=12345")
            
            
            self.cookie = "; ".join([f"{key}={value}" for key, value in self.req.cookies.get_dict().items()])
        
            self.urlMsaSignUp = unquote(re.findall(r'"urlGoToAADError":"(.*?)"',response.text)[0].replace("\\u0026","&").replace("jshs=0","jshs=1") + f"&jsh=&jshp=&username={self.email}&login_hint={self.email}")
            

            """Prepare Login"""

            headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Accept-Language': 'vi-VN,vi;q=0.9',
                'Connection': 'keep-alive',
                'Cookie':self.cookie,
                'Referer': 'https://login.microsoftonline.com/',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'cross-site',
                'Sec-Fetch-User': '?1',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
                'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"'
            }

            response = self.req.get(self.urlMsaSignUp, headers=headers)
            PPFT = re.findall(r'id="i0327" value="(.*?)"',response.text)[0]
            self.cookie = "; ".join([f"{key}={value}" for key, value in self.req.cookies.get_dict().items()])
            url_stay = re.findall(r"urlPost:'(.*?)'",response.text)[0]
            
    
            
            headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Accept-Language': 'vi-VN,vi;q=0.9',
                'Cache-Control': 'max-age=0',
                'Connection': 'keep-alive',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Cookie':self.cookie,
                'Origin': 'https://login.live.com',
                #'Referer': self.urlMsaSignUp,
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-User': '?1',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
                'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
            }

        
            data = {
                "ps": 2,
                "psRNGCDefaultType": "",
                "psRNGCEntropy": "",
                "psRNGCSLK": "",
                "canary": "",
                "ctx": "",
                "hpgrequestid": "",
                "PPFT": PPFT,
                "PPSX": "Passport",
                "NewUser": 1,
                "FoundMSAs": "",
                "fspost": 0,
                "i21": 0,
                "CookieDisclosure": 0,
                "IsFidoSupported": 1,
                "isSignupPost": 0,
                "isRecoveryAttemptPost": 0,
                "i13": 1,
                "login": self.email,
                "loginfmt": self.email,
                "type": 11,
                "LoginOptions": 1,
                "lrt": "",
                "lrtPartition": "",
                "hisRegion": "",
                "hisScaleUnit": "",
                "passwd": self.password
            }


            response = self.req.post(url_stay, headers=headers, data=data,allow_redirects=True)

            self.cookie = "; ".join([f"{key}={value}" for key, value in self.req.cookies.get_dict().items()])
            action = re.findall(r'action="(.*?)"',response.text)[0]
            pprid = re.findall(r'id="pprid" value="(.*?)"',response.text)[0]
            idp = re.findall(r'id="ipt" value="(.*?)"',response.text)[0]
            uaid = re.findall(r'id="uaid" value="(.*?)"',response.text)[0]
            client_id = re.findall(r'id="client_id" value="(.*?)"',response.text)[0]
            scope = re.findall(r'id="scope" value="(.*?)"',response.text)[0]

            
            """Post scope"""

            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'vi-VN,vi;q=0.9',
                'cache-control': 'max-age=0',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': self.cookie,
                'origin': 'https://login.live.com',
                'priority': 'u=0, i',
                'referer': 'https://login.live.com/',
                'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-site',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
            }

            data = {
                "rd": "none",
                "pprid": pprid,
                "ipt": idp,
                "uaid": uaid,
                "client_id": client_id,
                "scope": scope
                }

            #name="canary" value="v39eCBTo2uxF7q3j4U+jOMuzRw9yjYens0qAoP4awNk=1;dNuQzEJt0KbWAijuxfvVwGOWJ8rFRXZZDYZPeaHrBTU=1"

            response = self.req.post(
                action,
                headers=headers,
                data=data,
            )
            
            
            self.cookie = "; ".join([f"{key}={value}" for key, value in self.req.cookies.get_dict().items()])
            canary = re.findall(r'"sCanary":"(.*?)"',response.text)[0]
            
            """Action Auth"""
        
            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'vi-VN,vi;q=0.9',
                'cache-control': 'max-age=0',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': self.cookie,
                'origin': 'https://account.live.com',
                'priority': 'u=0, i',
                #'referer': 'https://account.live.com/Consent/Update?mkt=VI-VN&uiflavor=host&id=292841&lqsp=ntprob%3d-1&ru=https://login.live.com/oauth20_authorize.srf%3fuaid%3d9301d2bee31c4848a6337b9455cda972%26client_id%3d9e5f94bc-e8a4-4e73-b8be-63364c29d753%26opid%3d0476F5345C465523%26mkt%3dVI-VN%26opidt%3d1735174129',
                'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
            }

            data = {
                'canary': codecs.decode(canary, 'unicode_escape'),
                'client_id': client_id,
                'scope': scope,
                'cscope': '',
                'ucaction': 'Yes',
            }

            response = self.req.post(
                action,
            
                headers=headers,
                data=data,
                
            )
            #id="reply_params" value="code%3dM.C542_BAY.2.U.c5f1ed81-c448-038a-6009-8c692e54dcc2%26state%3d12345">
            
        
            authcode = re.findall(r'id="reply_params" value="(.*?)"',response.text)[0]
            
            authcode =  re.search(r'code%3d([a-zA-Z0-9\.\-_]+)(?=%26|$)', authcode)
            
    
            
            token_url = "https://login.microsoftonline.com/common/oauth2/v2.0/token"
            data = {
                'client_id': self.clientID,
                'grant_type': 'authorization_code',
                'code': authcode.group(1),
                'redirect_url': 'http://localhost',
                'scope' :'https://outlook.office.com/IMAP.AccessAsUser.All https://outlook.office.com/EAS.AccessAsUser.All https://outlook.office.com/EWS.AccessAsUser.All https://outlook.office.com/SMTP.Send https://outlook.office.com/POP.AccessAsUser.All offline_access' 
            }
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded'
            }
            response = requests.post(token_url, data=data, headers=headers)

            return response.json()['refresh_token']
       
# X = GetRefreshToken("diannekxrikju@hotmail.com","sCtDkIujgcwR")

# print(X.GetAuthCode())

if __name__ == '__main__':
    email = 'kali_otts1984@hotmail.com'
    pwd = 'QNdApJqQYU'
    print(GetRefreshToken(email , password = pwd).GetAuthCode())
    auth_code = 'M.C553_BAY.0.U.-CmkEDJuhpTumgG8mjXQ1jXKxhDMGVDP7l!dKxXeWmPP3ui*53*piU4nb3kfOrI9OCOddFrsrkOB0UbVvpYFVJAeovlwPub*h25WGthE5ndchYEF!6n9YjTDMOZ667c!9P4UcAPxNBgGbINPJpNsopI08TO1LglqBfEbP*kBiu2K8EtmOm4WPk8eaAsIana2xAbw9EfhfsxryG3dYWaBy!2fvymZgjYg1yqmcJaGsuV5nrP5sh5ViUtkuwiJzV*3HaZfKzXVpstH*Bb0npqsX7DZcCGOXIgQC*TZXWD3I60xLZgcfu8sT!1AuYexOGOCY1GXvjqEFb1HoU4A09oxrLhuLEaO2Z!vxYLm92loRLQgMCHr7LW1kZUUoM2lGQY0hmK671NI7oQ9M!4v!PG0ptZAzDFTiW!pklM6Q2b1NhRqui!0g8J4v7UHtIV4LudhVkw$$'
    