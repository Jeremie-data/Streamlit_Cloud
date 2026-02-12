import streamlit as st
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu
import pandas as pd

df_login = pd.read_csv("login.csv")               # Création DF du fichier csv                      

data_login = {'usernames' : {}}                   # Création dictionnaire pour respecter le format de streamlit-authenticator         
colonne_list = df_login.columns                   # liste des noms de colonnes pour le dictionnaire

for i in range(len(df_login)) :                   # double boucle pour créer les dictionnairres au format streamlit-authenticator   
    data_user = {}
    for j in range(len(colonne_list)) :
        colonne =  colonne_list[j]
        data_user[colonne] = df_login.iloc[i][j]  
    data_login['usernames'][df_login.iloc[i][0]] = data_user

authenticator = Authenticate(data_login,"cookie name", "cookie key",30)         # lignes de code pour créer une instance d'authentification

authenticator.login()                                                           # affiche l'instance dans la page

if st.session_state["authentication_status"]:
    
    with st.sidebar:
        st.success(f"Bienvenue {st.session_state['name']}")

        selection = option_menu(
            menu_title="Menu",
            options=["Accueil", "Photos"],
            icons=["house", "image"],
            default_index=0,
        )

        authenticator.logout("Déconnexion")
    
    if selection == "Accueil":
        st.title("Bienvenue sur ma page 🪂")
        st.image('https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3aG05cmVodGp3NWdudGozZjN2bHRtd3ZqZ3R1Z21qcnBhOXQ4MzJ1dSZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/l0jheIW46oxDgLXPYi/giphy.gif')

    elif selection == "Photos":
        st.title("Bienvenue dans mon album photos 🪂")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.image("https://septiemeciel-parachutisme.fr/wp-content/uploads/2018/02/IMG_0475.jpg")
        with col2:
            st.image("https://i.pinimg.com/736x/96/b1/b5/96b1b5b806d98bad1fb34aecde3604ad.jpg")
        with col3:
            st.image("https://newton-parachutisme.com/wp-content/uploads/2019/03/Saut-en-parachute-PACA-PAC.jpg")



elif st.session_state["authentication_status"] is False :
    st.error("L'username ou le password est/sont incorrect")


elif st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être remplie')
    st.text("Username : Jérémie  &  Password : 1234m")




