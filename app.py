from flask import Flask, request, make_response
from flask_cors import CORS
from flask_mail import Mail, Message
from datetime import date, datetime
import pytz


app = Flask(__name__)
app.config["MAIL_SERVER"] = "smtp.googlemail.com"
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'dom.portfolio.bot@gmail.com'
app.config['MAIL_DEFAULT_SENDER'] = 'dom.portfolio.bot@gmail.com'
app.config['MAIL_PASSWORD'] = 'thegreendoorhouse1'
mail = Mail(app)
CORS(app)


@app.route('/')
def index():
    return 'Portfolio Notifier'


@app.route('/api/sendVisitEmail', methods=['POST'])
def send_email():
    request_body = dict(request.get_json())
    pst = pytz.timezone('America/Los_Angeles')
    today = date.today()
    current_time = datetime.now(pst).strftime("%H:%M:%S")
    message = Message("Your Portfolio was just Viewed on " + str(today),
                      sender=app.config["MAIL_USERNAME"],
                      recipients=["dominic.fernandez1023@gmail.com"])
    ip_address = request_body.get("ip")
    ip_version = request_body.get("version")
    city = request_body.get("city")
    region = request_body.get("region")
    country = request_body.get("country_name")
    body = "Portfolio was viewed on " + str(today) + " at " + str(current_time) + "\n"
    body += "\nVisitor Details\n"
    body += "-------------------------\n"
    body += "# IP Address: " + str(ip_address) + "\n"
    body += "# IP Version: " + str(ip_version) + "\n"
    body += "# City: " + str(city) + "\n"
    body += "# Region/State: " + str(region) + "\n"
    body += "# Country: " + str(country) + "\n"
    message.body = body
    mail.send(message)
    return make_response({}, 200)


app.run(threaded=True)
