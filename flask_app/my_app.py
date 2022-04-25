from flask import Flask, request, render_template

import tensorflow as tf
from tensorflow import keras

import pickle

app = Flask(__name__)


@app.route('/')
def choose_prediction_method():
    return render_template('main.html')


def mn_prediction(params):

    return 0

def pr_prediction(params):

    return 0

def upr_prediction(params):
    #model = tf.keras.models.load_model('models/upr_model_2.67')
    #pred = model.predict([params])
    pkl_filename = '.\\models\RSCV_rfr_upr.pkl'
    # Load from file
    with open(pkl_filename, 'rb') as file:
        pickle_model = pickle.load(file)
    #pred = pickle_model.predict([params])
    params = [0.781616, 0.312088, 0.27006, 0.686552, 0.214688, 0.311714, 0.619993, 0.0, 0.284227, 0.269145],
    pred = pickle_model.predict([params])
    return pred


@app.route('/mn/', methods=['POST', 'GET'])
def mn_predict():
    message = ''
    if request.method == 'POST':
        plot = request.form.get('plot')
        
        mup = request.form.get('mup')
        
        ko = request.form.get('ko')
        
        seg = request.form.get('seg')
        
        tv = request.form.get('tv')
        
        pp = request.form.get('pp')
        
        mup = request.form.get('mup')
        
        pr = request.form.get('pr')
        
        ps = request.form.get('ps')
        
        yn = request.form.get('yn')
        
        shn = request.form.get('shn')
        
        pln = request.form.get('pln')
        
        params = [plot, mup, ko, seg, tv, pp, mup, pr, ps, yn, shn, pln]
        params = [float(i) for i in params]

        message = f'Спрогнозированное Соотношение матрица-наполнитель для введенных параметров: {mn_prediction(params)}'
    return render_template('mn.html', message=message)

@app.route('/pr/', methods=['POST', 'GET'])
def pr_predict():
    message = ''
    if request.method == 'POST':
        mn = request.form.get('mn')
        
        plot = request.form.get('plot')
        
        mup = request.form.get('mup')
        
        ko = request.form.get('ko')
        
        seg = request.form.get('seg')
        
        tv = request.form.get('tv')
        
        pp = request.form.get('pp')
        
        mup = request.form.get('mup')
        
        ps = request.form.get('ps')
        
        yn = request.form.get('yn')
        
        shn = request.form.get('shn')
        
        pln = request.form.get('pln')
        
        params = [mn, plot, mup, ko, seg, tv, pp, mup, ps, yn, shn, pln]
        params = [float(i) for i in params]

        message = f'Спрогнозированное значение Прочности при растяжении для введенных параметров: {pr_prediction(params)} МПа'
    return render_template('pr.html', message=message)

@app.route('/upr/', methods=['POST', 'GET'])
def upr_predict():
    message = ''
    if request.method == 'POST':
      #  mn = request.form.get('mn')
        
        plot = request.form.get('plot')
        
        mup = request.form.get('mup')
        
        ko = request.form.get('ko')
        
        seg = request.form.get('seg')
        
        tv = request.form.get('tv')
        
        pp = request.form.get('pp')
        
     #   pr = request.form.get('pr')
        
        ps = request.form.get('ps')
        
        yn = request.form.get('yn')
        
        shn = request.form.get('shn')
        
        pln = request.form.get('pln')
        
        #params = [mn, plot, mup, ko, seg, tv, pp, pr, ps, yn, shn, pln]
        params = [plot, mup, ko, seg, tv, pp, ps, yn, shn, pln]
        params = [0.781616, 0.312088, 0.27006, 0.686552, 0.214688, 0.311714, 0.619993, 0.0, 0.284227, 0.269145]
        params = [float(i) for i in params]

        message = f'Спрогнозированное значение Модуля упругости при растяжении для введенных параметров: {upr_prediction(params)} ГПа'
    return render_template('upr.html', message=message)

if __name__ == '__main__':
    app.run()
