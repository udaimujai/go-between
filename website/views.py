
from .models import Emp, Asset
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from . import db
from sqlalchemy import and_, or_
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


@views.route('/people', methods=['GET', 'POST'])
@login_required
def people():
    if request.method == 'POST':
        if request.form['action'] == 'onboard':
            return redirect(url_for("views.omboard"))
    return render_template("people.html", user=current_user)


@views.route('/package')
@login_required
def package():
    return render_template("package.html", user=current_user)


@views.route('/order')
@login_required
def order():
    return render_template("order.html", user=current_user)


@views.route('/searinventory', methods=['GET', 'POST'])
@login_required
def searinventory():
    search_list = request.args.getlist('search_list')
    # print("searchInventory")
    # for a in search_list:
    #     # print(a[0])
    #     print(a.asset_name)
    #     print(a.asset_status)
    # print("search_list***", search_list)
    return render_template("searinventory.html", search_list=search_list, user=current_user)


@views.route('/addinventory', methods=['GET', 'POST'])
@login_required
def addinventory():
    if request.method == 'POST':
        if request.form['action'] == 'add-inventory':

            return redirect(url_for("views.addinventory", user=current_user))
    return render_template("addInventory.html", user=current_user)


@ views.route('/inventory', methods=['GET', 'POST'])
@ login_required
def inventory():
    if request.method == 'POST':
        if request.form['action'] == 'search':
            asst_id = request.form.get('id')
            asst_name = request.form.get('asstName')
            asst_status = request.form.get('asstStatus')
            asst_detail = request.form.get('asstDetail')
            # ass_results = Asset.query.filter_by(asset_id=asst_id)
            # ass_results = Asset.query.filter(
            #     Asset.asset_id == asst_id, Asset.asset_name == asst_name).all()
            print(asst_id)
            ass_results = db.session.query(Asset).filter(or_(Asset.asset_id.like(
                asst_id), Asset.asset_name.like(asst_name)))
            # for ass_result in ass_results:
            #     print(ass_result.asset_id)
            #     print(ass_result.asset_name)
            #     print(ass_result.asset_status)
            # print("ass_results****", ass_results)
            return render_template("inventory.html", search_list=ass_results, user=current_user)
        if request.form['action'] == 'Search-All':
            asst_id = request.form.get('id')
            asst_name = request.form.get('asstName')
            asst_status = request.form.get('asstStatus')
            asst_detail = request.form.get('asstDetail')
            # ass_result = Asset.query.filter_by(asset_id=asst_id).filter_by(asset_name=asst_name).filter_by(
            #     asset_status=asst_status).filter_by(asset_detail=asst_detail).all()
            ass_results = Asset.query.all()
            return render_template("inventory.html", search_list=ass_results, user=current_user)

        if request.form['action'] == 'Delete-Asset':
            print("delete-asset")
            asst_id = request.form.get('id')
            print("asst_id", asst_id)
            Asset.query.filter_by(asset_id=asst_id).delete()
            db.session.commit()
            return render_template("inventory.html",  user=current_user)
        if request.form['action'] == 'Search-MA':
            people_id = request.form.get('EmpID')
            print("debug")
            emp_ = Emp.query.get(people_id)
            people_list = emp_.emp_assets
            emp_name = emp_.first_name
            print(people_list)
            return render_template("inventory.html", search_list=people_list, Emp_name=emp_name, user=current_user)
            # TODO cehck duplicate and empth validation
        if request.form['action'] == 'MA':
            asset_id_ = request.form.get('id')
            people_id = request.form.get('EmpID')
            emp_ = Emp.query.get(people_id)
            asset = Asset.query.get(asset_id_)
            emp_.emp_assets.append(asset)
            db.session.commit()
        if request.form['action'] == 'Add-Asset':
            asset_id_ = request.form.get('id')
            asset_name_ = request.form.get('asstName')
            asset_status_ = request.form.get('asstStatus')
            asset_detail_ = request.form.get('asstDetail')
            asset_id__ = Asset.query.filter_by(asset_id=asset_id_).first()
            if asset_id__:
                flash("asset id already available", catagory='error')
            else:
                print("asset id", asset_id_)
                new_asset = Asset(asset_id=asset_id_,
                                  asset_name=asset_name_,
                                  asset_status=asset_status_,
                                  asset_detail=asset_detail_
                                  )
                db.session.add(new_asset)
                db.session.commit()
                flash("added successfully", category='success')
            return render_template("inventory.html", user=current_user)
    return render_template("inventory.html", user=current_user)


@ views.route('/delivery')
@ login_required
def delivery():
    return render_template("delivery.html", user=current_user)


@ views.route('/omboard', methods=['GET', 'POST'])
@ login_required
def omboard():
    if request.method == 'POST':
        if request.form['action'] == 'add':
            id = request.form.get('id')
            name = request.form.get('Name')
            email = request.form.get('email')
            dept = request.form.get('dept')
            package = request.form.get('package')
            asset = request.form.get('asset')
            jdate = request.form.get('jdate')
            address = request.form.get('address')
            swag = request.form.get('swag')
            emp = Emp.query.filter_by(email=email).first()
            if emp:
                flash('Email already exists.', category='success')
            else:
                new_emp = Emp(id=id,
                              email=email,
                              first_name=name,
                              department=dept,
                              package=package,
                              asset_list=asset,
                              join_date=jdate,
                              address=address,
                              swags=swag
                              )
                db.session.add(new_emp)
                db.session.commit()
                flash("account created successfully", category='success')
                return redirect(url_for("views.omboard"))
        if request.form['action'] == 'search-all':
            people_results = Emp.query.all()
            print("debug")
            print("people_results", people_results)
            return render_template("onboard.html", search_list=people_results, user=current_user)
            # return redirect(url_for("views.omboard"))
        if request.form['action'] == 'delete':
            print("delete-asset")
            asst_id = request.form.get('id')
            print("asst_id", asst_id)
            Emp.query.filter_by(id=asst_id).delete()
            db.session.commit()
            return render_template("onboard.html",  user=current_user)

    return render_template("onboard.html", user=current_user)
