import requests
import json
import datetime
import os

store_data = None

def Current_Weathers():
   global store_data
   try:
      city_name = input("Enter the City Name - ")
      weather_api = f"https://wttr.in/{city_name}?format=j1"
      response = requests.get(weather_api)
      data  = response.json()
      
      current = data["current_condition"][0]
      
      Temparature = current["temp_C"]
      Humidity = current["humidity"]
      Wind_Speed = current["windspeedKmph"]
      Weather_Condition = current["weatherDesc"][0]["value"]
      Date_Time = datetime.datetime.now()
      
      print("------ Weather Report ------")
      print(f"City: {city_name}")
      print(f"Temperature: {Temparature}°C")
      print(f"Humidity: {Humidity}%")
      print(f"Wind Speed: {Wind_Speed}km/h")
      print(f"Condition: {Weather_Condition}")
      print(f'Fetched At: {Date_Time.strftime("%d-%m-%Y %H:%M %p")}')
      print("----------------------------")
      
      store_data = {
         "type": "weather",
         "city": city_name,
         "temperature": Temparature,
         "humidity": Humidity,
         "Wind Speed":Wind_Speed,
         "condition": Weather_Condition,
         "time": Date_Time.strftime("%d-%m-%Y %H:%M %p")
      }
   except Exception as e:
      print("Error",e)


def Currency_Exchange_Rate():
   global store_data
   try:
      Base_Currency = input("Enter the Base Currency : ").upper()
      Target_Currency = input("Enter the Target Currency : ").upper()
      currency_api = f"https://open.er-api.com/v6/latest/{Base_Currency}"
      response = requests.get(currency_api)
      data = response.json()
      value = data["rates"][Target_Currency]
      date_time = datetime.datetime.now()
      print(f"1 {Base_Currency} = {value} {Target_Currency}")
      print(f'Fetched At: {date_time.strftime("%d-%m-%Y %H:%M %p")}')
      
      store_data = {
            "type": "currency",
            "base": Base_Currency,
            "target": Target_Currency,
            "rate": value,
            "time": date_time.strftime("%d-%m-%Y %H:%M %p")
         }
   except Exception as e:
      print("Error - ",e)
   
def save_result():
   global store_data
   if store_data is None:
      print("No Data Available")
      return
   try:
      with open("data.json","w") as file:
         json.dump(store_data,file,indent=4)
      print("Data saved successfully.")
   except Exception as e:
      print("Error - ",e)


def view_save_data():
   if not os.path.exists("data.json"):
      print("This file is not exists....")
      return
   
   try:
      with open("data.json","r") as file:
         data = json.load(file)
      
      print("\n------ Last Saved Data ------")
      
      if data["type"] == "weather":
         print("Type: Weather")
         print(f"City: {data['city']}")
         print(f"Temperature: {data['temperature']}°C")
         print(f"Humidity: {data['humidity']}%")
         print(f"Wind Speed: {data['Wind Speed']} km/h")
         print(f"Condition: {data['condition']}")
         print(f"Saved Time: {data['time']}")
      
      elif data["type"] == "currency":
         print("Type: Currency")
         print(f"Base Currency: {data['base']}")
         print(f"Target Currency: {data['target']}")
         print(f"Rate: {data['rate']}")
         print(f"Saved Time: {data['time']}")
      
      print("-----------------------------")
   except Exception as e:
         print("Error - ",e)


def main():
   while True:
      print("==============Data Fetcher===============")
      print(" Option - 1 : Current Weather ")
      print(" Option - 2 : Currency Exchange Rate ")
      print(" Option - 3 : Save Result to JSON File ")
      print(" Option - 4 : View Previous Saved Data ")
      print(" Option - 5 : Exit ")
      print("==========================================")
      op = int(input("Choose the Option - "))
      if op == 1:
         Current_Weathers()
      elif op == 2:
         Currency_Exchange_Rate()
      elif op == 3:
         save_result()
      elif op == 4:
         view_save_data()
      elif op == 5:
         break
      else:
         print("This choise is Not Available")

main()