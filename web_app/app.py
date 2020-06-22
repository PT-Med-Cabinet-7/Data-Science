from flask import Flask, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from pickle import load
# from model.model import *
from web_app.get_kush import kush_info


def app():
    app = Flask(__name__)
    #app.config['SQLALCHEMY_DATABASE_URI'] = config('SQLALCHEMY_URI')]
    #app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    db = SQLAlchemy(app)

    @app.route("/")
    def home():
        """Base Page, not to be used

        Returns:
        string --Link to project home.
        """
        return render_template('home.html')

    @app.route("/request/", methods=['GET', 'POST'])
    def search (user_input=None):
        """Takes user input and predicts recommended strain

        User Arguments:
            user_input {str}-- [effect, flavor and user_input to model]
                (defaults: {None})

        Returns:
            [ARRAY]--Returns a recomended strain (with a strength score? Maybe??(TODO))
            [EXAMPLE]--[{strain_id}, "score": 72}]

        """
        user_input = request.args['search']
        decode = decode(user_input)
        results = preds(decode) ## NEED INFO FROM Adi 
        indices = results[0]
        distance = results[1]
        kush_list = kush_info(distances, indices)
        return jsonify(kush_list)

    @app.errorhandler(404)
    def page_not_found(error):
        return 'GET OFF MY LAWN!!! Acutally this page does not exist.'

    @app.errorhandler(400)
    def Bad_Request(error):
        return 'I am working on it!!! Give me a break!'

    def preds(user_info):
         """Retrives prediction from users info

         Arguments:
            user_info {str} -- Returns a recomended strain (with a strength score? Maybe??(TODO))

        Retruns:
            Prediction
        """
        # model = Predictor()
        # pred_distances, pred_indices = model.predict(user_input=user_info)
        # return [pred_indices, pred_distances]

    def decode(input_str):
        return input_str.replace("%22", " ").replace("%20", " ").replace("%7B", " ").replace("%7D", " ")


    return app