import json
import pickle
import numpy as np

__data_columns = None
__model = None



def get_estimated_price(pregnancies,glucose,bloodpressure,skinthickness,insulin, bodymassindex, diabetespedigreefunction,age):
    X1 = np.zeros(len(__data_columns))
    X1[0] = pregnancies
    X1[1] = glucose
    X1[2] = bloodpressure
    X1[3] = skinthickness
    X1[4] = insulin
    X1[5] = bodymassindex
    X1[6] = diabetespedigreefunction
    X1[7] = age

    return round(__model.predict([X1])[0],2)

def load_saved_artifacts():
    print("Loading Saved Artifacts...start")
    global __data_columns

    with open("./artifacts/columns.json",'r') as f:
        __data_columns = json.load(f)['data_columns']

    global __model
    with open("./artifacts/diabetes_prediction.pickle",'rb') as f:
        __model = pickle.load(f)
    print("Loading Saved Artifacts...done")

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_estimated_price(6,148,72,35,0,33.6,0.627,50))
    print(get_estimated_price(1,85,66,29,0,26.6,0.351,31))


