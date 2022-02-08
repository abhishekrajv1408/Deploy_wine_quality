from flask import Flask , render_template, request
app =Flask(__name__)

import wineQualityPre as pr
import pandas as pd




@app.route("/")
def hello():
    return render_template( "index.html" )




@app.route("/sub", methods = ['POST'] )
def submit():
    # data is transfer from html to py
    if request.method == "POST":
        a = request.form["a"]
        b = request.form["b"]
        c = request.form["c"]
        d = request.form["d"]
        e = request.form["e"]
        f = request.form["f"]
        g = request.form["g"]
        h = request.form["h"]
        data={
            "fixed acidity"	  :[a],
            "volatile acidity"  :[b],	
            "citric acid"  :[c]	,
            "chlorides"  :[d],	
            "total sulfur dioxide"  :[e],	
            "density"  :[f]	,
            "sulphates"  :[g],	
            "alcohol"  :[h],

        }
        df=pd.DataFrame(data)
        num=pr.quality_chec(df)


# data is transfer from py to html
        return render_template("sub.html", n=num ,df=data)




if __name__ == "__main__":
    app.run(debug=True)



