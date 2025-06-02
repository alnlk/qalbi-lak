from flask import Flask, render_template, request
import smtplib

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def send():
    message = request.form['herMessage']

    your_email = "almlk00000n@gmail.com"
    your_password = "ضع_كلمة_مرور_بريدك_هنا"

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.starttls()
            smtp.login(your_email, your_password)
            smtp.sendmail(your_email, your_email, f"Subject: رسالة من حبيبتك\n\n{message}")
        return "تم إرسال رسالتها إلى بريدك ❤️"
    except Exception as e:
        return f"حدث خطأ: {e}"

if __name__ == '__main__':
    app.run(debug=True)
