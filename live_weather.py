import requests
api_key="YOUR_API_KEY"



while True:
 
 city_name =input("Type your city name here \nOr type exit to stop here :")



 if city_name == "exit":
       print("bye byee!")
       break
 
 url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
 response =requests.get(url) 
 if response.status_code == 200:
       data = response.json()
       print("City:" ,data["name"])
       print("Description:" ,data["weather"][0]["description"])
       print("Temperature:" ,data["main"]["temp"])
       print("Humidity:" ,data["main"]["humidity"])
       print("Visibility:" ,data["visibility"])
       print("Wind Speed: " ,data["wind"]["speed"])
 else:
       print("please enter a valid city name")
