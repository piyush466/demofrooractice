# import time
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# import requests
# import json
#
#
# chrome = Service(r"C:\\Users\\Cliffex-Lead\\Desktop\\test\\chromedriver.exe")
# driver = webdriver.Chrome(service=chrome)
#
# driver.get("https://business.docufend.com/sign-in")
#
# driver.find_element(By.NAME, "email").send_keys("piyushtest@yopmail.com")
# driver.find_element(By.NAME, "password").send_keys("1234567890")
# time.sleep(2)
# driver.find_element(By.ID, "kt_sign_in_submit").click()
#
# time.sleep(2)
#
# responce_API = requests.get("https://api.docufend.com/admin/admin_login")
# data =responce_API.text
#
# print(responce_API.status_code)
# print(data)
#


# import requests
# import json
#
# api_response = requests.get('https://jsonplaceholder.typicode.com/todos')
# print(api_response.status_code)
# data = api_response.text
# parse_json = json.loads(data)
#
# print("Todos:", parse_json)

# from twilio.rest import Client
#
# # Your Twilio account SID and auth token
# account_sid = 'AC5bfc6658a8b2b379998b5e1452a568db'
# auth_token = '6895cb175868110f8205451cfea68ed5'
#
# # Create a Twilio client
# client = Client(account_sid, auth_token)
#
# # Retrieve the most recent SMS message sent to your Twilio number
# message = client.messages.list(to='+16206229061')[1]
#
# # Extract the verification code from the message body
# verification_code = message.body.split(': ')[1]
#
# print(verification_code)


# from twilio.rest import Client
#
# # Your Twilio account SID and auth token
# account_sid = 'AC5bfc6658a8b2b379998b5e1452a568db'
# auth_token = '6895cb175868110f8205451cfea68ed5'
#
# # Create a Twilio client
# client = Client(account_sid, auth_token)
#
# # Retrieve the most recent SMS message sent to your Twilio number
# messages = client.messages.list(to='+16206229061')
# if len(messages) >= 2:
#     message = messages[1]
#     verification_code = message.body.split(': ')[1]
#     print(verification_code)
# else:
#     print("No SMS messages found")

