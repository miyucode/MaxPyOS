from tkinter import *
from tkinter.ttk import *
from tkinter import ttk

import tkinter.messagebox as mb

import sys, os, requests

def weatherapp():
	def getWeather(canvas):
			city = namecity.get()
			api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=06c921750b9a82d8f5d1294e1586276f"

			json_data = requests.get(api).json()
			condition = json_data['weather'][0]['main']
			temp = int(json_data['main']['temp'] - 273.15)
			min_temp = int(json_data['main']['temp_min'] - 273.15)
			max_temp = int(json_data['main']['temp_max'] - 273.15)
			pressure = json_data['main']['pressure']
			humidity = json_data['main']['humidity']
			wind = json_data['wind']['speed']
			final_info = condition + "\n" + str(temp) + "°C"
			final_data = "\n" + "Minimal temperature: " + str(min_temp) + "°C" + "\n" + "Maximal temperature: " + str(max_temp) + "°C" + "\n" + "Pression: " + str(pressure) + "\n" + "Humidity: " + str(humidity) + "\n"
			label1.config(text=final_info)
			label2.config(text=final_data)

	weatherapp = Tk()
	weatherapp.title("MaxPyOS - Weather App")
	weatherapp.geometry("600x500")
	weatherapp.resizable(False, False)
	weatherapp.iconbitmap("Apps/WeatherApp/icons/weatherapp-icon.ico")

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