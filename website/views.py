import email
from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from .models import Note, Tax, User
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')
    
    
    return render_template("home.html", user=current_user)

@views.route('/taxes', methods=['GET', 'POST'])
@login_required
def taxes():
    if request.method == 'POST':
        tax_id = request.form.get('steuerid')
        salary = request.form.get('bruttolohn')
        way_to_work = request.form.get('arbeitsweg')
        days_homeoffice = request.form.get('homeoffice')

        new_tax = Tax(tax_id=tax_id, salary=salary, way_to_work=way_to_work, days_homeoffice=days_homeoffice)
        db.session.add(new_tax)
        db.session.commit()
        flash('Steuererklärung gespeichert')

        print(new_tax.tax_id)
        print(new_tax.salary)
        # return redirect(url_for('views.home'))

    return render_template("taxes.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})