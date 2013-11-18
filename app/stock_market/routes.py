from stock_market import app
from flask import render_template, request, flash, send_from_directory
from forms import ContactForm
from flask.ext.mail import Message, Mail

# initialization
mail = Mail()

#controllers
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'ico/favicon.ico')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
  form = ContactForm()
 
  if request.method == 'POST':
    if form.validate() == False:
      return render_template('contact.html', form=form)
    else:
      msg = Message(form.subject.data, sender=app.config["MAIL_USERNAME"], recipients=['michael@delano.com'])
      msg.body = "From: %s <%s> %s" % (form.name.data, form.email.data, form.message.data)
      mail.send(msg)
      #flash('Message sent. Thank you!')
 
      return render_template('contact.html', success=True)
 
  elif request.method == 'GET':
    return render_template('contact.html', form=form)