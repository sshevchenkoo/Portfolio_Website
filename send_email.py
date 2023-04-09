import smtplib, ssl

def send_message(message):
    host = "smtp.gmail.com"
    port = 465

# Write your gmail and password
    username = "your_email@gmail.com"
    password = "your_password"

# Write your gmail or receive email
    receiver = "your_email@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)