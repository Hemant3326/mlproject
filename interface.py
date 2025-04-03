from flask import Flask, request, jsonify
import config
from Project.utils import LoanApproval
import numpy as np 


app = Flask(__name__)
@app.route("/")
def get_home():
    return "Hello"

@app.route("/predict_result", methods = ["POST","GET"])
def get_results():
    if request.method == "POST":
        data = request.form
        print("User input data is >>>",data)
        Gender = data["Gender"]
        Married = data["Married"]
        Dependents = data["Dependents"]
        Education = data["Education"]
        Self_Employed = data["Self_Employed"]
        ApplicantIncome = eval(data["ApplicantIncome"])
        CoapplicantIncome = eval(data["CoapplicantIncome"])
        LoanAmount = eval(data["LoanAmount"])
        Loan_Amount_Term = eval(data["Loan_Amount_Term"])
        Credit_History = data["Credit_History"]
        Property_Area = data["Property_Area"]
        loan_obj = LoanApproval(Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area)
        result =  loan_obj.get_predict_results()
        
        if result == 1:
            return jsonify({"Result":"Loan Approved"})
        else:
            return jsonify({"Result":"Loan Rejected"})



if __name__ == "__main__":
    app.run(debug=True)


