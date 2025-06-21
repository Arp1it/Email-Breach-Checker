from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    email = request.args.get('email')
    leakornot = None
    leakfrom = None
    found = None
    fields = None

    if email:
        # You can use email here — e.g., send email, render with it, etc.
        url = f'https://leakcheck.net/api/public?check={email}'

        response = requests.get(url)
        # print(response.status_code)
        # print(response.text)

        if response.json().get('success'):
            leakornot = True
            leakfrom = response.json().get('sources')
            found = response.json().get('found')
            fields = response.json().get('fields')
        
        else:
            leakornot = False

        print(f"Email from redirect: {email}")
    return render_template('base.html', leak=leakornot, leakfrom=leakfrom, found=found, fields=fields)


if __name__ == '__main__':
    app.run(debug=True)