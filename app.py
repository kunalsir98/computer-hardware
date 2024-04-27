from flask import Flask,request,render_template,jsonify
from src.pipeline.prediction_pipeline import CustomData,PredictPipeline

application=Flask(__name__)

app=application

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])

def predict_datapoint():
    if request.method=='GET':
        return render_template('form.html')
    

    else:
        # Create a CustomData instance with data from the form
        data = CustomData(
            MYCT=int(request.form.get('MYCT')),
            MMIN=int(request.form.get('MMIN')),
            MMAX=int(request.form.get('MMAX')),
            CACH=int(request.form.get('CACH')),
            CHMIN=int(request.form.get('CHMIN')),
            CHMAX=int(request.form.get('CHMAX')),
            PRP=int(request.form.get('PRP')),
            ERP=int(request.form.get('ERP'))
        )
        
        # Convert CustomData to DataFrame
        final_new_data = data.get_data_as_dataframe()
        
        # Use PredictPipeline to predict the result
        predict_pipeline = PredictPipeline()
        pred = predict_pipeline.predict(final_new_data)
        
        # Round the prediction result
        result = round(pred[0], 2)
        
        # Render the results template with the prediction result
        return render_template('results.html', final_result=result)
    

    

    







if __name__=="__main__":
     app.run(host='127.0.0.1',debug=True)
