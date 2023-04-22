
from .models import Emp, Asset, Package, PkgDevices
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
        elif request.form['action'] == 'packa':
            return redirect(url_for("views.packa"))
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


@views.route('/packa', methods=['GET', 'POST'])
@login_required
def packa():
    if request.method == 'POST':
        if request.form['action'] == 'search':
            pkg_id = request.form.get('id')
            pkg_ = Package.query.get(pkg_id)
            if pkg_:
                pkg_id_ = pkg_.pkg_id
                assets_ = pkg_.pkg_assets
                return render_template("package.html", search_list=assets_, pkg_name=pkg_id_, user=current_user)
            else:
                flash("No Package Found", category='error')
                return render_template("package.html", user=current_user)
        if request.form['action'] == 'MA':
            pkg_id_ = request.form.get('id')
            asset_id_ = request.form.get('asst_id')
            pks_ = Package.query.filter_by(pkg_id=pkg_id_).first()
            if pks_:
                pkg_ = Package.query.get(pkg_id_)
                asset = Asset.query.get(asset_id_)
                pkg_.pkg_assets.append(asset)
                db.session.commit()
            else:
                new_pkg = Package(pkg_id=pkg_id_)
                db.session.add(new_pkg)
                db.session.commit()
                pkg_ = Package.query.get(pkg_id_)
                asset = Asset.query.get(asset_id_)
                pkg_.pkg_assets.append(asset)
                db.session.commit()
            return render_template("package.html", user=current_user)
        if request.form['action'] == 'Delete-Asset':
            print("delete-asset")
            package_id = request.form.get('id')
            Package.query.filter_by(pkg_id=package_id).delete()
            PkgDevices.query.filter_by(pkg_id=package_id).delete()

            db.session.commit()
            return render_template("package.html", user=current_user)

    return render_template("package.html", user=current_user)


@views.route('/order')
@login_required
def order():
    if request.method == 'POST':
        # if request.form['action'] == 'search':
        return render_template("order.html", user=current_user)


@views.route('/searinventory', methods=['GET', 'POST'])
@login_required
def searinventory():
    search_list = request.args.getlist('search_list')
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
            print(asst_id)
            ass_results = db.session.query(Asset).filter(or_(Asset.asset_id.like(
                asst_id), Asset.asset_name.like(asst_name)))
            return render_template("inventory.html", search_list=ass_results, user=current_user)
        if request.form['action'] == 'Search-All':
            asst_id = request.form.get('id')
            asst_name = request.form.get('asstName')
            asst_status = request.form.get('asstStatus')
            asst_detail = request.form.get('asstDetail')
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
            if people_id == "":
                flash("Enter Employee ID", category='error')
                return render_template("inventory.html",  user=current_user)

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
                flash("asset id already available", category='error')
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
            emp_id = request.form.get('id')
            print("asst_id", emp_id)
            Emp.query.filter_by(id=emp_id).delete()
            db.session.commit()
            return render_template("onboard.html",  user=current_user)

    return render_template("onboard.html", user=current_user)
