from flask import Flask, jsonify

app = Flask(__name__)

from products import dispositivo


@app.route('/testing')
def testing():
    return jsonify({"mensaje":'correcto!'})

@app.route('/products')
def getproducts():
    return jsonify({"products": dispositivo, "message": "Lista de productos"})

@app.route('/products/<string:nombre_de_equipo>')
def getProduct(nombre_de_equipo):
    productsFound = [dispositivo for dispositivo in products if dispositivo['nombre_de_equipo'] == nombre_de_equipo]
    if (len(productsFound) > 0):   
        return jsonify({"dispositivo": productsFound[0]})
    return jsonify({"message": "product not Found"})
    
@app.route('/saludo')
def hello_world():
    # print("hola consola") el resultado lo imprime en la consola
    return "<p>Hello World!!!</p> <h2>y algo mas</h2>"
  
@app.route('/algo')
def algo():
    # print("hola consola") el resultado lo imprime en la consola
    return "<p>Estas en el espacio de algo</p> <h2>Espacio algo mas</h2>"
  


if __name__ == '__main__':
    app.run(debug=True, port=4000)

#@app.route('/products')
#def getproducts():
#    return jsonify({"products": catatipodis})

#@app.route('/products')
#def getProducts():
#    return jsonify({"products": catstatus})

#@app.route('/products')
#def getProducts():
#    return jsonify({"products": modetablalec})



    
    