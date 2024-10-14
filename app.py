import requests
import smtplib
from email.message import EmailMessage
from datetime import datetime
import os
from dotenv import load_dotenv

def get_infos():
    # Get result of url for the Caxias do Sul city
    request = requests.get('https://api.weatherapi.com/v1/forecast.json?key=77062b398241431797f20436242707&q=Caxias+do+Sul&lang=pt')

    # Transform to json
    dict_json = request.json()

    # Get only the main values
    day = {
        'date': dict_json['forecast']['forecastday'][0]['date'],
        'min_temp': dict_json['forecast']['forecastday'][0]['day']['mintemp_c'],
        'max_temp': dict_json['forecast']['forecastday'][0]['day']['maxtemp_c'],
        'precip_total': dict_json['forecast']['forecastday'][0]['day']['totalprecip_mm'],
        'chance_of_rain': str(dict_json['forecast']['forecastday'][0]['day']['daily_chance_of_rain']),
        'condition': dict_json['forecast']['forecastday'][0]['day']['condition']['text'],
        'sunrise': dict_json['forecast']['forecastday'][0]['astro']['sunrise'],
        'sunset': dict_json['forecast']['forecastday'][0]['astro']['sunset']
    }
    
    return day

def sendmail(day):
    date = datetime.strptime(day['date'], '%Y-%m-%d')
    date = date.strftime("%d/%m/%Y")
    
    # content of message
    content = f"""Avaliação do clima do dia {date}:
    
    Temperatura Mínima: {str(day['min_temp'])}°C
    Temperatura Máxima: {str(day['max_temp'])}°C
    
    Possibilidade de chuva: {day['chance_of_rain']}%
    Precipitação Total: {str(day['precip_total'])}mm
    
    Condição: {day['condition']}.
    
    Nascer-do-sol: {day['sunrise']}
    Pôr-do-sol: {day['sunset']}
    """
    
    # infos
    load_dotenv()
    email_address = os.getenv('EMAIL_ADDRESS')
    email_password = os.getenv('EMAIL_PASSWORD')
    
    # message
    mgs = EmailMessage()
    mgs['Subject'] = f'Avaliação do clima do dia {date}'
    mgs['From'] = email_address # email of who will send it
    mgs['To'] = 'isslermatheus0@gmail.com' # email that receives the weather information
    mgs.set_content(content)
    
    # send mail
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_address, email_password)
        smtp.send_message(mgs)
    
def main():
    day = get_infos()
    
    sendmail(day)
main()