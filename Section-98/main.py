import smtplib
import requests
import schedule
import time

def get_bitcoin_price():
    url = 'https://api.coingecko.com/api/v3/simple/price'
    params = {
        'ids': 'bitcoin',
        'vs_currencies': 'usd'
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        return data['bitcoin']['usd']
    except Exception as e:
        print(f"Error fetching Bitcoin price: {e}")
        return None

def send_email(subject, message, to_email):
    smtp_server = 'smtp.example.com'
    smtp_port = 587
    sender_email = 'your_email@example.com'
    sender_password = 'your_password'

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, to_email, f'Subject: {subject}\n\n{message}')
    server.quit()

def job():
    btc_price = get_bitcoin_price()
    if btc_price:
        message = f"Good morning!\n\nToday's Bitcoin price is: ${btc_price}\nDon't forget the 2 PM meeting!"
    else:
        message = "Good morning!\n\nCould not fetch Bitcoin price today.\nDon't forget the 2 PM meeting!"
    send_email("Daily Update: Bitcoin Price & Meeting Reminder", message, "recipient@example.com")

# Schedule the job every day at 00:01
schedule.every().day.at("00:01").do(job)

while True:
    schedule.run_pending()
    time.sleep(60)
