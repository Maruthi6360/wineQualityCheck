from flask import Flask, request, render_template
import pickle  # Assume your model is saved as a pickle file
import numpy as np
import os

app = Flask(__name__)

# Load your trained regression model
with open('wineQualityCheckModel.pkl','rb') as file:
    model = pickle.load(file)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        try:
            # Collect inputs from the form
            features = [eval(request.form[f'i{i}']) for i in range(1, 12)]
            prediction = model.predict([features])[0]  # Predict using the model
            
            # Storytelling explanation
            if prediction < 4:
                 result_message = "The predicted wine quality is very low. This wine is likely not suitable for most people’s tastes."
            elif 4 <= prediction < 6:
                result_message = "The predicted wine quality is average. It might be acceptable, but it’s not likely to impress anyone."
            elif 6 <= prediction < 8:
                result_message = "The predicted wine quality is good. Many would find this wine enjoyable."
            else:
                result_message = "The predicted wine quality is excellent. This is a high-quality wine, likely to be appreciated by wine enthusiasts."
            
            return render_template('result.html', prediction=prediction, result_message=result_message)
        
        except ValueError:
            return "Invalid input. Please enter valid numbers."

    return render_template('regression.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

