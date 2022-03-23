from tkinter import *
from tkinter.ttk import *
from tkinter import ttk

import tkinter.messagebox as mb

import sys, os, requests

def weatherapp():
	def closeweatherapp():
		file = open('Apps/WeatherApp/src/weather-condition.txt', 'w')
		file.write("")
		file.close()
		weatherapp.destroy()

	def getWeather(canvas):
			def readintoweatherconditionfile():
				file = open('Apps/WeatherApp/src/weather-condition.txt', 'r')
				content = file.read()

				if content == "Clear":
					weatherapp.iconbitmap("Apps/WeatherApp/icons/sun-icon.ico")
				elif content == "Rain":	
					weatherapp.iconbitmap("Apps/WeatherApp/icons/rain-icon.ico")
				elif content == "Clouds":
					weatherapp.iconbitmap("Apps/WeatherApp/icons/clouds-icon.ico")
				elif content == "Stormy":
					weatherapp.iconbitmap("Apps/WeatherApp/icons/stormyrain-icon.ico")
				elif content == "Haze":
					weatherapp.iconbitmap("Apps/WeatherApp/icons/windy-icon.ico")
				else:
					pass

				file.close()

			city = namecity.get()
			api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=06c921750b9a82d8f5d1294e1586276f"
			try:
				weatherapp.iconbitmap("Apps/WeatherApp/icons/weatherapp-icon.ico")

				json_data = requests.get(api).json()
				condition = json_data['weather'][0]['main']

				file = open('Apps/WeatherApp/src/weather-condition.txt', 'w')
				file.write(condition)
				file.close()

				temp = int(json_data['main']['temp'] - 273.15)
				min_temp = int(json_data['main']['temp_min'] - 273.15)
				max_temp = int(json_data['main']['temp_max'] - 273.15)
				pressure = json_data['main']['pressure']
				humidity = json_data['main']['humidity']
				wind = json_data['wind']['speed']
				final_info = condition + "\n" + str(temp) + "°C"
				final_data = "\n" + "Minimal temperature: " + str(min_temp) + "°C" + "\n" + "Maximal temperature: " + str(max_temp) + "°C" + "\n" + "Pression: " + str(pressure) + "\n" + "Humidity: " + str(humidity) + "\n"
				
				readintoweatherconditionfile()
				
				label1.config(text=final_info)
				label2.config(text=final_data)
			except:
				weatherapp.iconbitmap("Apps/WeatherApp/icons/weatherapp-icon.ico")

				file = open('Apps/WeatherApp/src/weather-condition.txt', 'w')
				file.write("")
				file.close()
				label1.config(text="This city doesn't exist !")
				label2.config(text="")

	weatherapp = Tk()
	weatherapp.title("MaxPyOS - Weather App")
	weatherapp.geometry("600x500")
	weatherapp.resizable(False, False)
	weatherapp.iconbitmap("Apps/WeatherApp/icons/weatherapp-icon.ico")
	weatherapp.protocol("WM_DELETE_WINDOW", lambda: closeweatherapp())

	f = ("poppins", 15, "bold")
	t = ("poppins", 35, "bold")

	namecity = Entry(weatherapp, justify='center', width=20, font=t)
	namecity.pack(pady=20)
	namecity.focus()
	namecity.bind('<Return>', getWeather)

	label1 = Label(weatherapp, font=t)
	label1.pack()
	label2 = Label(weatherapp, font=f)
	label2.pack()