from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        flash("successd", category='success')
        if request.form['action'] == 'Delivery':
            return redirect(url_for("views.delivery"))
        elif request.form['action'] == 'Inventory':
            return redirect(url_for("views.inventory"))
        elif request.form['action'] == 'Order':
            return redirect(url_for("views.order"))
        elif request.form['action'] == 'Package':
            return redirect(url_for("views.package"))
        elif request.form['action'] == 'People':
            return redirect(url_for("views.people"))
        elif request.form['action'] == 'Ticket':
            return redirect(url_for("views.ticket"))
    return render_template("home.html", user=current_user)


@views.route('/ticket')
@login_required
def ticket():
    return render_template("ticket.html", user=current_user)


@views.route('/people')
@login_required
def people():
    return render_template("people.html", user=current_user)


@views.route('/package')
@login_required
def package():
    return render_template("package.html", user=current_user)


@views.route('/order')
@login_required
def order():
    return render_template("order.html", user=current_user)


@views.route('/inventory')
@login_required
def inventory():
    return render_template("inventory.html", user=current_user)


@views.route('/delivery')
@login_required
def delivery():
    return render_template("delivery.html", user=current_user)
