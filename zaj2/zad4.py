from flask import Flask

# Inicjalizacja aplikacji Flask
app = Flask(__name__)

# Trasa dla strony głównej
@app.route('/')
def home():
    return 'Witaj w mojej aplikacji Flask!'

# Trasa dla strony "O mnie"
@app.route('/about')
def about():
    return 'Zaprogramowano przez Michał Ślifierski.'

# Trasa dla strony kontaktowej
@app.route('/contact')
def contact():
    return 'Email: m.slifierski@gmail.com.'

if __name__ == '__main__':
    app.run(debug=True)
