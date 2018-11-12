from flask import Flask

app=Flask(__name__)

app.run()

@app.route('/inicio')
def ola():
    return '<h1>Ola</h1>'