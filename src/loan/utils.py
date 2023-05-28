import pickle

model = pickle.load(open('../models/model.pkl', 'rb'))

gender = {'female': 0, 'male': 1, 'nan': 2}
married = {'no': 0, 'yes': 1, 'nan': 2}
dependents = {'0': 0, '1': 1, '2': 2, '3+': 3, 'nan': 4}
education = {'graduate': 0, 'notgraduate': 1}
self_employed = {'no': 0, 'yes': 1, 'nan': 2}
property_area = {'rural': 0, 'semiurban': 1, 'urban': 2}

encoders = [gender, married, dependents, education, self_employed, property_area]

def predict_loan_status(data):
    # load the model
    # predict
    
    # decode the data using the dictionary
    for i in range(len(data)):
        if isinstance(data[i], str):
            data[i] = encoders[i][data[i]]

    # Convert the data to 2D array since sklearn requires 2D input
    data = [data]

    prediction = model.predict(data)
    return prediction
