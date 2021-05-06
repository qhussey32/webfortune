from flask import Flask, render_template, request, session, redirect, url_for, jsonify, abort
import os 
import subprocess

app = Flask(__name__)
app.secret_key = b'dfvjwewonl_x#pi*CO0@^z'

@app.route('/')
def index():
    return redirect(url_for('fortune'))


@app.route('/fortune/')
def fortune():
    p = subprocess.run(['fortune'],stdout=subprocess.PIPE)
    fortuneMsg = p.stdout.decode()
    return '<pre>'+fortuneMsg+'</pre>'


@app.route('/cowsay/<message>/')
def cowsay(message):
    p = subprocess.run(['cowsay', message],stdout=subprocess.PIPE)
    cowMsg = p.stdout.decode()
    return '<pre>'+cowMsg+'</pre>'


@app.route('/cowfortune/')
def cowfortune():
    p = subprocess.run(['fortune'],stdout=subprocess.PIPE)
    fortuneMsg = p.stdout.decode()
    
    p = subprocess.run(['cowsay', fortuneMsg],stdout=subprocess.PIPE)
    cowMsg = p.stdout.decode()
    return '<pre>'+cowMsg+'</pre>'
