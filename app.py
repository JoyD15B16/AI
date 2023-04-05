from flask import Flask, render_template,request
import sales_prediction
app = Flask(__name__)

@app.route('/')
def about():
    return render_template('about.html')

@app.route('/graph')
def graph():
    return render_template('graph.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/result')
def result():
    item_Identifier = request.args.get('Item_Identifier')
    item_Weight = request.args.get('Item_Weight')
    item_Visibility = request.args.get('Item_Visibility')
    item_Fat_Content = request.args.get('Item_Fat_Content')
    item_Type = request.args.get('Item_Type')
    item_MRP = request.args.get('Item_MRP')
    outlet_ID = request.args.get('Outlet_ID')
    outlet_Establishment_Year = request.args.get('Outlet_Establishment_Year')
    outlet_Size = request.args.get('Outlet_Size')
    outlet_Location = request.args.get('Outlet_Location')
    outlet_Type = request.args.get('Outlet_Type')
    sales = sales_prediction.predict_sales(
     Item_Identifier = item_Identifier,
     Item_Weight = item_Weight,
     Item_Visibility = item_Visibility,
     Item_Fat_Content = item_Fat_Content,
     Item_Type = item_Type,
     Item_MRP = item_MRP,
     Outlet_ID = outlet_ID,
     Outlet_Establishment_Year = outlet_Establishment_Year,
     Outlet_Size = outlet_Size,
     Outlet_Location = outlet_Location,
     Outlet_Type = outlet_Type
    )
    return render_template('result.html',res = sales)

if __name__ == '__main__':
    app.run(debug=True)