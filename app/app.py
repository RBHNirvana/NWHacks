 from flask import Flask, render_template
from flask_login import current_user, login_user, logout_user, login_required
#from app.forms import #imports here
from app.models import Organization, Position, Applicant


app = Flask(__name__)



@app.before_first_request
def initDB(*args, **kwargs):
    db.create_all()



@app.route('/')
def index():
    return render_template('index.html')



#Orginization login/register
@app.route('/orgregister', methods=['GET', 'POST'])
def orgregister():
    regform = OrgRegisterform()
    loginform = OrgLogin()
    if regform.validate_on_submit():
        NewOrg = Organization(org_name = form.org_name.data,
                              org_email = form.org_email.data)
        NewOrg.set_password(form.password.data)
        NewOrg.id = Organization.query.count() + 1
        db.session.add(NewOrg)
        db.session.commit()
        return redirect(url_for('orgprofile'))
    elif loginform.validate_on_submit():
        user = Organization.query.filter_by(org_name = loginform.org_email.data).first()
        login_user(user)
        #If the user is logged in
        if not user is None or not user.check_password(loginform.FIELD.data):
            return redirect(url_for('orgprofile'), org_id = current_user.id)
    return render_template('orgregister.html', regform=regform,
                          loginform = loginform)
                       #org_id is for the /orgprofile so we know which profile to display



#Orginization Profile
@app.route('/orgprofile<org_id>', methods=['GET', 'POST'])
def orgprofile(org_id):
    org = Organization.query.filter_by(id=org_id)
    form = OrgSummaryForm() #NEED TO MAKE AN OrgSummaryForm ======================

    #if the summary was edited...
    if form.validate_on_submit():
        #Retrive the correct item from db, set summary equal to new summary, commmit
        current_org = Organization.query.filter_by(id = org_id)
        current_org.org_summary = form.summary.data
        db.session.add(current_org)
        db.session.commit()

    #Only show the form if the org owner is on the page
    if(current_user.id == org_id):
        return render_template('orgprofile.html', form=form, org = org)
        #using jinja 2 we need to say something like {% if form %}
    else:
        return render_template('orgprofile.html', org=org)
   
    

@app.route('/orgpostings<org_id>', methods = ['GET', 'POST'])
def ortpostings(org_id):
    #If the user's id doesn't match the page ID, redirect them back to that orgs page
    if(current_user.id != org_id):
        return redirect(url_for('/orgprofile<org_id>'))
    current_org = Organization.query.filter_by(id = org_id)
    return render_template('orgpostings.html', current_ort = current_org)



#Volunteer position finder
@app.route('/volpositions')
def volpositions():
    #We need a boolean form for the filters
    form = FilterForm()
    #orgs = Organization.query().all() #query might be wrong?
    #positions = []
    #for org in orgs:
        #print(type(org))
        #for position in org.positions.query().all():
            #if(form.FILTER1.data == position.TAG1
               #and form.FILTER2.data == position.TAG2)
            #positions.append(position)
    positions = Organization.query().join(Position).filter().all()

    return render_template('volpositions.html', positions=positions)