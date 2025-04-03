import pickle 
import json 
import numpy as np
import config


class LoanApproval():
    def __init__(self,Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,
                 LoanAmount,Loan_Amount_Term,Credit_History,Property_Area):
        self.Gender            = Gender.title()
        self.Married           = Married.title()
        self.Dependents        = int(Dependents)
        self.Education         = Education.title()
        self.Self_Employed     = Self_Employed.title()
        self.ApplicantIncome   = int(ApplicantIncome)
        self.CoapplicantIncome = int(CoapplicantIncome)
        self.LoanAmount        = int(LoanAmount)
        self.Loan_Amount_Term  = int(Loan_Amount_Term)
        self.Credit_History    = int(Credit_History)
        self.Property_Area     = "Property_Area_" + Property_Area.title()

    def load_model(self):
        # Reading Pickle and JSON file
        with open(config.MODEL_FILE_PATH, "rb") as file:
            self.model = pickle.load(file)
        with open(config.JSON_FILE_PATH,"r") as file:
            self.json_data = json.load(file)

    def get_predict_results(self):
        self.load_model() # Calling above model function
        test_array = np.zeros(len(self.json_data["columns"]))
        test_array[0] = self.json_data["Gender"][self.Gender]
        test_array[1] = self.json_data["Married"][self.Married]
        test_array[2] = self.Dependents
        test_array[3] = self.json_data["Education"][self.Education]
        test_array[4] = self.json_data["Self_Employed"][self.Self_Employed]
        test_array[5] = self.ApplicantIncome
        test_array[6] = self.CoapplicantIncome
        test_array[7] = self.LoanAmount
        test_array[8] = self.Loan_Amount_Term
        test_array[9] = self.Credit_History
        property_area_index = self.json_data["columns"].index(self.Property_Area)
        test_array[property_area_index] = 1
        predict_result = self.model.predict([test_array])[0]
        return predict_result
    