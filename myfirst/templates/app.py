from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/onclick', methods=['POST'])
def onclick():
    return 'Функція onclick виконана'


if __name__ == '__main__':
    app.run()
