from flask import render_template, url_for, redirect, flash, flash

from lennonwall import db, app
from lennonwall.forms import MemoForm
from lennonwall.models import Message

@app.route('/', methods=['GET', 'POST'])
def index():
	form = MemoForm()
	if form.validate_on_submit():
		name=form.name.data
		body=form.body.data
		message=Message(name=name,body=body)
		db.session.add(message)
		db.session.commit()
		flash('Memo Posted')
		return redirect(url_for('index'))
	messages = Message.query.order_by(Message.time.desc()).all()
	return render_template('index.html', form=form, messages=messages)