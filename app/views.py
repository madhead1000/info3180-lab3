"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""
import smtplib
from app import app
from flask import render_template, request, redirect, url_for


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')


###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)

@app.route('/contact/', methods=["GET"])
def contact():
  """Render webpage contact"""
  status = "new"
  return render_template('contact.html')

def sent():
  return "Your message has been sent, please enter a new message to send."
    

@app.route('/contact/', methods=["POST"])
def sendmail():
  fromname = request.form["fromname"]
  fromaddr = request.form["fromemail"]
  subject = request.form["fromsubject"]
  msg = request.form["msg"]
  
  toaddrs = 'odanejackson12@gmail.com'
  message = """From: {} <{}>

  To: {} <{}>

  Subject: {}

  {}

  """
  toname = 'ODane Jackson'

  messagetosend = message.format(
   fromname,
   fromaddr,
   toname,
   toaddrs,
   subject,
   msg)
  
  # Credentials (if needed)

  username = 'odanejackson12@gmail.com'

  password = 'feorugimxdeaplob'

  # The actual mail send

  server = smtplib.SMTP('smtp.gmail.com:587')

  server.starttls()
  server.login(username,password)
  server.sendmail(fromaddr, toaddrs, messagetosend)

  server.quit()
  return render_template('contact.html', statusinfo=sent())


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
