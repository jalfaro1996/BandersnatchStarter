from datetime import datetime
from pandas import DataFrame
from sklearn.ensemble import RandomForestClassifier
import joblib


class Machine:

    def __init__(self, df: DataFrame):
        #properly initialize the machine learning model and store it as an attribute
        self.name = "Random Forest Classifier"
        target = df["Rarity"]
        features = df.drop(columns=["Rarity"])
        self.model = RandomForestClassifier(n_estimators=100, n_jobs=-1, max_depth=30,
                                            bootstrap=False, criterion='gini', max_features='log2',
                                            min_samples_leaf=1, min_samples_split=2)
        self.model.fit(features, target)

    def __call__(self, pred_basis: DataFrame):
        #take in a DataFrame of feature data and return a prediction and the probability of the prediction
        prediction, *_ = self.model.predict(pred_basis)
        confidence, *_ = self.model.predict_proba(pred_basis)
        return prediction, max(confidence)

    def save(self, filepath):
        #save the machine learning model to the specified filepath using joblib
        try:
            joblib.dump(self.model, filepath)
            print("Model saved successfully at", filepath)
        except Exception as e:
            print("Error occurred while saving the model:", e)

    @staticmethod
    def open(filepath):
        #load a saved machine learning model from the specified filepath using joblib
        try:
            model = joblib.load(filepath)
            print("Model loaded successfully from", filepath)
            return model
        except Exception as e:
            print("Error occurred while loading the model,", e)
            return None

    def info(self):
        model_name = type(self.model).__name__
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        info_string = f"Base Model: {model_name}, Initialized at: {timestamp}"
        return info_string
        #return a string with the name of the base model and the timestamp of when it was initialize
