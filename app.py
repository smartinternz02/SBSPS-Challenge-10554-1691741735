from flask import Flask, request, render_template
import pickle


model = pickle.load(popPred.pkl,'rb')
app = Flask(__name__)

@app.route('/')
def show_year_form():
    return render_template('ml.html')

@app.route('/process_year', methods=['POST'])
def process_year():
    year = request.form.get('year')
    
    # Do something with the year data
    result = f"You entered the year: {year}"
    print(result)
    r2 = model.predict([[year]])
    return render_template('ml.html', o1=result, o2 = r2)

if __name__ == '__main__':
    app.run(debug=True)
