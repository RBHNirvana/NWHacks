from flask import Flask, render_template
from flask_login import current_user, login_user, logout_user, login_required
#from app.forms import #imports here
from app.models import Organization, Position, Applicant


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

#Orginization login/register
@app.route('/orgregister', methods=['GET', 'POST'])
def orgregister():
    #regform = Registerform()
    #loginform = Loginform()
    if regform.validate_on_submit():
        NewOrg = Organization(org_name = form.FIELD.data,
                              org_email = form.FIELD.data)
        NewOrg.set_password(form.FIELD.data)
        NewOrg.id = Organization.query.count() + 1
        db.session.add(NewOrg)
        db.session.commit()
        return redirect(url_for('orgprofile'))
    elif loginform.validate_on_submit():
        user = Organization.query.filter_by(org_name = loginform.FIELD.data).first()
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
    #User has edited the organization summary section
    if form.validate_on_submit():
        #Update the summary
        current_org = Organization.query.filter_by(id = org_id)
        current_org.org_summary = form.FIELD.data
        positions = Organization.query.filter_by(org_name = current_user.org_name)
    #will need something to check if the organization page id matches the current_user id to dispaly the edit button for the mission
    return render_template('orgprofile.html', form=form)

         

#Volunteer position finder
@app.route('/volpositions')
def volpositions():
    return render_template('volpositions.html')