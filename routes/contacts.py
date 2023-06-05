from flask import Blueprint, flash, redirect, render_template, request, url_for

from models.contact import Contact
from utils.db import db

Contacts = Blueprint("contacts", __name__)


@Contacts.route("/")
def index():
    contacts: list = Contact.query.all()
    return render_template("index.html", contacts=contacts)


@Contacts.route("/new", methods=["POST"])
def add_contact():
    fullname: str = request.form["fullname"]
    email: str = request.form["email"]
    phone: str = request.form["phone"]

    new_contact: object = Contact(fullname, email, phone)

    db.session.add(new_contact)
    db.session.commit()

    flash("Contact added succesfully!")
    
    return redirect(url_for("contacts.index"))


@Contacts.route("/update/<id>", methods=["GET", "POST"])
def update(id):
    contact = Contact.query.get(id)
    if request.method == "POST":
        contact.fullname = request.form["fullname"]
        contact.email = request.form["email"]
        contact.phone = request.form["phone"]

        db.session.commit()

        flash("Contact updated succesfully!")
        
        return redirect(url_for("contacts.index"))
    else:
        return render_template("update_contact.html", contact=contact)


@Contacts.route("/delete/<id>")
def delete(id):
    contact = Contact.query.get(id)
    db.session.delete(contact)
    db.session.commit()

    flash("Contact deleted succesfully!")
    
    return redirect(url_for("contacts.index"))


@Contacts.route("/about")
def about():
    return render_template("about.html")
