import requests, json
#Code by Mohammed ==> YouTube /onclick1
#github.com : MohammedNajih
#instagram.com :4t_ig 
username = input('ENTER USERNAME')
password = input('ENTER PASSWORD') 
url = 'https://www.instagram.com/accounts/login/ajax/'
headers = {
'Host':'www.instagram.com', 
'content-length':'314',
'sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="101"',
'x-ig-app-id':'1217981644879628',
'x-ig-www-claim':'0',
'sec-ch-ua-mobile':'?1',
'x-instagram-ajax':'684510d5f3c6',
'content-type':'application/x-www-form-urlencoded',
'accept':'*/*',
'x-requested-with':'XMLHttpRequest',
'user-agent':'Mozilla/5.0 (Linux; Android 10; YAL-L21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36',
'x-csrftoken':'h5gdBq2oMUHmHkKiqBTYLBJhFlcAHokl',
'sec-ch-ua-platform':'"Android"',
'origin':'https://www.instagram.com',
'sec-fetch-site':'same-origin',
'sec-fetch-mode':'cors',
'sec-fetch-dest':'empty',
'referer':'https://www.instagram.com/',
'accept-encoding':'gzip, deflate, br',
'accept-language':'en-IQ,en;q=0.9',
'cookie':'csrftoken=h5gdBq2oMUHmHkKiqBTYLBJhFlcAHokl',
'cookie':'mid=YpE8xwABAAHvKOft4YlzSxsGOTnu',
'cookie':'ig_did=BF4642BA-9B4C-4174-831F-3575B5411180',
'cookie':'ig_nrcb=1'
}

data = {
'enc_password':'#PWD_INSTAGRAM_BROWSER:'+str(password), 
'username':str(username), 
'queryParams':'{}', 
'stopDeletionNonce':'', 
'trustedDeviceRecords':'{}'
}

req = requests.post(url, headers=headers,data=data)
login = Json.loads(req.content)['userId']
print(login)

