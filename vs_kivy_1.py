from kivy.app import App
from kivy.uix.button import Button
import random
import requests

def get_weather():
    city = 'Новосибирск'

    key = '5ee41fc7cd4f6ef8e9b6092ab67ecba4'
    url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': key, 'q': city, 'units': 'metric'}
    result = requests.get(url, params=params)
    weather = result.json()

    info = f'{str(weather["name"])}: {weather["main"]["temp"]}'

    return info


class MyApp(App):
    def build(self):
        return Button(text = 'button',
                      font_size = 30,
                      on_press = self.btn_press,
                      background_color = [1, 0, 0, 1])

    def btn_press(self, instance):
        print('btn is pressed')
        instance.text = get_weather()

if __name__ == '__main__':
    MyApp().run()



