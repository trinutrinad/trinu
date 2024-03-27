from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('survey_form.html')

@app.route('/submit_survey', methods=['POST'])
def submit_survey():
    if request.method == 'POST':
        # Retrieve form data
        owner_name = request.form['owner_name']
        owner_dob = request.form['owner_dob']
        owner_gender = request.form['owner_gender']
        owner_identity_proof = request.form['owner_identity_proof']
        owner_education = request.form['owner_education']
        owner_occupation = request.form['owner_occupation']
        owner_age = request.form['owner_age']

        # Process the form data (store it in the database, etc.)
        # For now, let's just print the data
        print("Owner Name:", owner_name)
        print("Date of Birth:", owner_dob)
        print("Gender:", owner_gender)
        print("Identity Proof Number:", owner_identity_proof)
        print("Education Level:", owner_education)
        print("Occupation:", owner_occupation)
        print("Age:", owner_age)

        # Redirect to a success page (or render a success template)
        return 'Survey submitted successfully!'
    else:
        return 'Invalid request method'

if __name__ == '__main__':
    app.run(debug=True)
