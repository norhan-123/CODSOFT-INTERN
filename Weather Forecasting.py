from tkinter import *
import requests

window = Tk()
window.resizable(False, False)
window.geometry("800x600+400+80")


# function
def forecast_weather():
    key = "34fbd2e04d3c4ec5f638229f994ae183"
    City = E1.get()
    link = f'http://api.openweathermap.org/data/2.5/weather?q={City}&appid={key}'
    forecasting = requests.get(link)

    if forecasting.status_code==200:
        data = forecasting.json()
        t = data['main']['temp']
        temperature=round(t-273.15)
        humidity=data['main']['humidity']
        wind=data['wind']['speed']
        description = data['weather'][0]['description']

        L2.config(text=f"Temperature: {temperature} C \n Short Description: {description} \n Humidity: {humidity} \n Wind Speed: {wind}")
    else:
        L2.config(text="Error in weather data")

# design
window.title("Weather Forecasting App")
L = Label(window, text="Weather Forecasting App", font=('Helvetica bold', 26, "bold italic"), bg="LightPink2", height=2,width=90)
L.pack()
L1 = Label(window, text="Enter City Name :-", font=("arial", 15))
L1.pack(padx=(0, 595), pady=(30, 0))
E1 = Entry(window, bd=0.5, highlightthickness=2)
E1.config(highlightbackground="grey", highlightcolor="grey", width=40, font=("Helvetica", "14"))
E1.pack(padx=(0, 308), pady=(10))
B1 = Button(text="Display weather forecast", width=25, border=0, bg="LightPink2", font=("Helvetica", "12"),command=forecast_weather)
B1.pack(padx=(30,0), pady=(10, 0))
L2 = Label(window,font=("arial", 15))
L2.pack(pady=(20, 0))
window.mainloop()
