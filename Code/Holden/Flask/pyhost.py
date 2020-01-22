from flask import Flask, render_template, request, redirect
import rotn
import unitconverter
app = Flask(__name__)

path_list = ["/", "/rotN/", "/UnitConvert/"]

@app.route('/')
def index():
    return render_template('index.html', path_list=path_list)

@app.route('/rotN/', methods=['GET', 'POST'])
def rot13():
    textout = ''
    encdec = 'encode'
    textin = ''
    rot = 13
    if request.method == 'POST':
        textin = request.form['textin']
        encdec = request.form['encdec']
        rot = request.form['rotn']
        textout = rotn.exec(textin, encdec, rot)
    return render_template('rot13.html', textout=textout, encdec=encdec, textin=textin, rot=rot)

@app.route('/UnitConvert/', methods=['GET', 'POST'])
def uniconv():
    unitin = 'feet'
    unitout = 'meters'
    distance = None
    distout = None
    invalid = False
    if request.method == 'POST':
        unitin = request.form['unitin']
        unitout = request.form['unitout']
        distance = request.form['distance']
        distout = unitconverter.convert(unitin=unitin, unitout=unitout, distance=distance)
        if distout == None:
            invalid = True
            distance = None
    return render_template('UnitConvert.html', distout=distout, unitin=unitin, unitout=unitout, distance=distance, invalid=invalid)

@app.route('/PassGen/', methods=['GET', 'POST'])
def passgen():
    return redirect('/')
