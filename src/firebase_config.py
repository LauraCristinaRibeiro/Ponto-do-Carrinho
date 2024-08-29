import firebase_admin
import pyrebase
from firebase_admin import credentials, firestore, db


def iniciar_firebase():
  firebaseConfig = {
    "apiKey": "AIzaSyA-I8er0Fttq2Pe8wrxFDNUXPVJaXiysj4",
    "authDomain": "ponto-do-carrinho.firebaseapp.com",
    "databaseURL": "https://console.firebase.google.com/project/ponto-do-carrinho/firestore/databases/-default-/data?hl=pt-br",
    "projectId": "ponto-do-carrinho",
    "storageBucket": "ponto-do-carrinho.appspot.com",
    "messagingSenderId": "129982363572",
    "appId": "1:129982363572:web:9ad5ad2e43232a60d564e1"
  }


  # cred = credentials.Certificate("credentials/ponto-do-carrinho-firebase-adminsdk-75r4y-2314d9ff24.json")
  # firebase_admin.initialize_app(cred)
  #
  # conexão com o firestore
  # db = firestore.client()

  firebase = pyrebase.initialize_app(firebaseConfig)
  auth = firebase.auth()

  db = firebase.database()
  return auth,db


auth, db = iniciar_firebase()


#função para adicionar usuários
def add_user(nomeUser, email, cargo):
  user = db.collection('users').document()
  user.set({
    'nomeUser': nomeUser,
    'email': email,
    'cargo': cargo
  })


#função de recuperar dados do usuário
def recuperar_user(user_id):
  try:
    user_ref = db.collection('users').document(user_id)
    user_doc = user_ref.get()

    if user_doc.exists:
      user_data = user_doc.to_dict()
      nome = user_data.get('nome')
      email = user_data.get('email')
      cargo = user_data.get('cargo')
      return {"nome": nome, "email": email, "cargo": cargo}
    else:
      print("Usuário não encontrado")
      return None
  except Exception as e:
    print(f"Erro ao recuperar os dados do usuário: {e}")
    return None


#função para adicionar um produto
def add_produto(nome, marca, preco):
  produto_ref = db.collection('produtos').document()
  produto_ref.set({
    'nome': nome,
    'marca': marca,
    'preco': preco
  })


#função para procurar um produto
def procurar_produto(nome):
  produtos = db.collection('produtos').where('nome', '==', nome).stream()
  return [prod.to_dict() for prod in produtos]