import json
import pickle

#Load tfidf matrix
tfidf = pickle.load(open("./tfidf.pickle", "rb"))

#Load mnb model
mnb = pickle.load(open("./mnb.pickle", "rb"))


#Single string prediction
def test_model(list_string):
    tfidf_baru = tfidf.transform(list_string)
    hasil = mnb.predict(tfidf_baru)
    if hasil == 0:
        return 'negative'
    return 'positive'


#Contoh
print(test_model(['bagas ganteng banget']))