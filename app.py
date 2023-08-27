from flask import Flask, request, render_template
from flask_cors import cross_origin
import pickle
import pandas as pd


app = Flask(__name__)
model = pickle.load(open("flight_rf.pkl", "rb"))


@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")


@app.route("/predict", methods=["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":

        # Date_of_Journey
        date_dep = request.form["Dep_Time"]
        journey_day = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").day)
        journey_month = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").month)
        # print("Journey Date : ",Journey_day, Journey_month)

        # Departure
        dep_hour = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").hour)
        dep_min = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").minute)
        # print("Departure : ",Dep_hour, Dep_min)

        # Arrival
        date_arr = request.form["Arrival_Time"]
        arrival_hour = int(pd.to_datetime(date_arr, format="%Y-%m-%dT%H:%M").hour)
        arrival_min = int(pd.to_datetime(date_arr, format="%Y-%m-%dT%H:%M").minute)
        # print("Arrival : ", Arrival_hour, Arrival_min)

        # Duration
        dur_hour = abs(arrival_hour - dep_hour)
        dur_min = abs(arrival_min - dep_min)
        # print("Duration : ", dur_hour, dur_min)

        # Total Stops
        total_stops = int(request.form["stops"])
        # print(Total_stops)

        # Airline
        # AIR ASIA = 0 (not in column)
        airline = request.form['airline']
        if airline == 'Jet Airways':
            jet_airways = 1
            indigo = 0
            air_india = 0
            multiple_carriers = 0
            spicejet = 0
            vistara = 0
            goair = 0
            multiple_carriers_premium_economy = 0
            jet_airways_business = 0
            vistara_premium_economy = 0
            trujet = 0

        elif airline == 'IndiGo':
            jet_airways = 0
            indigo = 1
            air_india = 0
            multiple_carriers = 0
            spicejet = 0
            vistara = 0
            goair = 0
            multiple_carriers_premium_economy = 0
            jet_airways_business = 0
            vistara_premium_economy = 0
            trujet = 0

        elif airline == 'Air India':
            jet_airways = 0
            indigo = 0
            air_india = 1
            multiple_carriers = 0
            spicejet = 0
            vistara = 0
            goair = 0
            multiple_carriers_premium_economy = 0
            jet_airways_business = 0
            vistara_premium_economy = 0
            trujet = 0

        elif airline == 'Multiple carriers':
            jet_airways = 0
            indigo = 0
            air_india = 0
            multiple_carriers = 1
            spicejet = 0
            vistara = 0
            goair = 0
            multiple_carriers_premium_economy = 0
            jet_airways_business = 0
            vistara_premium_economy = 0
            trujet = 0

        elif airline == 'SpiceJet':
            jet_airways = 0
            indigo = 0
            air_india = 0
            multiple_carriers = 0
            spicejet = 1
            vistara = 0
            goair = 0
            multiple_carriers_premium_economy = 0
            jet_airways_business = 0
            vistara_premium_economy = 0
            trujet = 0

        elif airline == 'Vistara':
            jet_airways = 0
            indigo = 0
            air_india = 0
            multiple_carriers = 0
            spicejet = 0
            vistara = 1
            goair = 0
            multiple_carriers_premium_economy = 0
            jet_airways_business = 0
            vistara_premium_economy = 0
            trujet = 0

        elif airline == 'GoAir':
            jet_airways = 0
            indigo = 0
            air_india = 0
            multiple_carriers = 0
            spicejet = 0
            vistara = 0
            goair = 1
            multiple_carriers_premium_economy = 0
            jet_airways_business = 0
            vistara_premium_economy = 0
            trujet = 0

        elif airline == 'Multiple carriers Premium economy':
            jet_airways = 0
            indigo = 0
            air_india = 0
            multiple_carriers = 0
            spicejet = 0
            vistara = 0
            goair = 0
            multiple_carriers_premium_economy = 1
            jet_airways_business = 0
            vistara_premium_economy = 0
            trujet = 0

        elif airline == 'Jet Airways Business':
            jet_airways = 0
            indigo = 0
            air_india = 0
            multiple_carriers = 0
            spicejet = 0
            vistara = 0
            goair = 0
            multiple_carriers_premium_economy = 0
            jet_airways_business = 1
            vistara_premium_economy = 0
            trujet = 0

        elif airline == 'Vistara Premium economy':
            jet_airways = 0
            indigo = 0
            air_india = 0
            multiple_carriers = 0
            spicejet = 0
            vistara = 0
            goair = 0
            multiple_carriers_premium_economy = 0
            jet_airways_business = 0
            vistara_premium_economy = 1
            trujet = 0

        elif airline == 'Trujet':
            jet_airways = 0
            indigo = 0
            air_india = 0
            multiple_carriers = 0
            spicejet = 0
            vistara = 0
            goair = 0
            multiple_carriers_premium_economy = 0
            jet_airways_business = 0
            vistara_premium_economy = 0
            trujet = 1

        else:
            jet_airways = 0
            indigo = 0
            air_india = 0
            multiple_carriers = 0
            spicejet = 0
            vistara = 0
            goair = 0
            multiple_carriers_premium_economy = 0
            jet_airways_business = 0
            vistara_premium_economy = 0
            trujet = 0

        # print(Jet_Airways,
        #     IndiGo,
        #     Air_India,
        #     Multiple_carriers,
        #     SpiceJet,
        #     Vistara,
        #     GoAir,
        #     Multiple_carriers_Premium_economy,
        #     Jet_Airways_Business,
        #     Vistara_Premium_economy,
        #     Trujet)

        # Source
        # Banglore = 0 (not in column)
        source = request.form["Source"]
        if source == 'Delhi':
            s_delhi = 1
            s_kolkata = 0
            s_mumbai = 0
            s_chennai = 0

        elif source == 'Kolkata':
            s_delhi = 0
            s_kolkata = 1
            s_mumbai = 0
            s_chennai = 0

        elif source == 'Mumbai':
            s_delhi = 0
            s_kolkata = 0
            s_mumbai = 1
            s_chennai = 0

        elif source == 'Chennai':
            s_delhi = 0
            s_kolkata = 0
            s_mumbai = 0
            s_chennai = 1

        else:
            s_delhi = 0
            s_kolkata = 0
            s_mumbai = 0
            s_chennai = 0

        # print(s_Delhi,
        #     s_Kolkata,
        #     s_Mumbai,
        #     s_Chennai)

        # Destination
        # Banglore = 0 (not in column)
        source = request.form["Destination"]
        if source == 'Cochin':
            d_cochin = 1
            d_delhi = 0
            d_new_delhi = 0
            d_hyderabad = 0
            d_kolkata = 0

        elif source == 'Delhi':
            d_cochin = 0
            d_delhi = 1
            d_new_delhi = 0
            d_hyderabad = 0
            d_kolkata = 0

        elif source == 'New_Delhi':
            d_cochin = 0
            d_delhi = 0
            d_new_delhi = 1
            d_hyderabad = 0
            d_kolkata = 0

        elif source == 'Hyderabad':
            d_cochin = 0
            d_delhi = 0
            d_new_delhi = 0
            d_hyderabad = 1
            d_kolkata = 0

        elif source == 'Kolkata':
            d_cochin = 0
            d_delhi = 0
            d_new_delhi = 0
            d_hyderabad = 0
            d_kolkata = 1

        else:
            d_cochin = 0
            d_delhi = 0
            d_new_delhi = 0
            d_hyderabad = 0
            d_kolkata = 0

        # print(
        #     d_Cochin,
        #     d_Delhi,
        #     d_New_Delhi,
        #     d_Hyderabad,
        #     d_Kolkata
        # )

        #     ['Total_Stops', 'Journey_day', 'Journey_month', 'Dep_hour',
        #    'Dep_min', 'Arrival_hour', 'Arrival_min', 'Duration_hours',
        #    'Duration_mins', 'Airline_Air India', 'Airline_GoAir', 'Airline_IndiGo',
        #    'Airline_Jet Airways', 'Airline_Jet Airways Business',
        #    'Airline_Multiple carriers',
        #    'Airline_Multiple carriers Premium economy', 'Airline_SpiceJet',
        #    'Airline_Trujet', 'Airline_Vistara', 'Airline_Vistara Premium economy',
        #    'Source_Chennai', 'Source_Delhi', 'Source_Kolkata', 'Source_Mumbai',
        #    'Destination_Cochin', 'Destination_Delhi', 'Destination_Hyderabad',
        #    'Destination_Kolkata', 'Destination_New Delhi']

        prediction = model.predict([[
            total_stops,
            journey_day,
            journey_month,
            dep_hour,
            dep_min,
            arrival_hour,
            arrival_min,
            dur_hour,
            dur_min,
            air_india,
            goair,
            indigo,
            jet_airways,
            jet_airways_business,
            multiple_carriers,
            multiple_carriers_premium_economy,
            spicejet,
            trujet,
            vistara,
            vistara_premium_economy,
            s_chennai,
            s_delhi,
            s_kolkata,
            s_mumbai,
            d_cochin,
            d_delhi,
            d_hyderabad,
            d_kolkata,
            d_new_delhi
        ]])

        output = round(prediction[0], 2)

        return render_template('home.html', prediction_text="Your Flight price is Rs. {}".format(output))

    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)
