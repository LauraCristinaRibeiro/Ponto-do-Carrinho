import firebase_admin
from firebase_admin import credentials, firestore

# Configuração do Firebase
cred = credentials.Certificate("credentials/ponto-carrinho-firebase.json")
firebase_admin.initialize_app(cred)

# Conexão com o Firestore
db = firestore.client()

# Funções relacionadas ao usuário
def add_user(name, email, cargo, senha):
    user_ref = db.collection('users').document(email)
    user_ref.set({
        'name': name,
        'email': email,
        'cargo': cargo,
        'senha': senha
    })

def get_user(email):
    user_ref = db.collection('users').document(email).get()
    if user_ref.exists:
        return user_ref.to_dict()
    return None

# Funções relacionadas aos produtos
def add_product(name, marca, price):
    product_ref = db.collection('products').document()
    product_ref.set({
        'name': name,
        'marca': marca,
        'price': price
    })

def search_product(name):
    products = db.collection('products').where('name', '==', name).stream()
    return [prod.to_dict() for prod in products]
