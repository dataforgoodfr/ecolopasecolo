import streamlit as st
import random
import os
import openai
from dotenv import load_dotenv

st.set_page_config(page_title="Ecolo ou pas écolo", page_icon="🌎")


# --------------------------------------------------------------------------------------------------------
# Environment
load_dotenv()
openai.api_key = os.environ["OPENAI_KEY"] 

# --------------------------------------------------------------------------------------------------------
# OPENAI
# Inspired from De Gauche ou de droite
# https://github.com/TheoDlmz/degaucheoudedroite


base_prompt = "Écolo ou Pas écolo ?\n\n"
training_set = [{"name":"Sarkozy", "out":"Pas écolo"},
             {"name":"Le vélo", "out":"Écolo"},
             {"name":"L'école", "out":"Les deux"}, 
             {"name":"Le logement", "out":"Les deux"},
             {"name":"Le pétrole", "out":"Pas écolo"},
             {"name":"La voiture", "out":"Pas écolo"},
             {"name":"Mélenchon", "out":"Écolo"},
             {"name":"La viande", "out":"Pas écolo"},
             {"name":"Le sexe", "out":"Écolo"},
             {"name":"La décroissance", "out":"Écolo"},
             {"name":"La politique", "out":"Les deux"},
             {"name":"Le patriarcat", "out":"Pas écolo"},
             {"name":"Les énergies renouvelables", "out":"Écolo"}, 
             {"name":"La sobriété", "out":"Écolo"},
             {"name":"Macron", "out":"Pas écolo"},
             {"name":"La ZAD", "out":"Écolo"},
             {"name":"Le ciment", "out":"Pas écolo"}] 

for x in training_set:
    base_prompt += "%s => %s\n"%(x["name"], x["out"])


def ecolopasecolo(prompt):
    g = openai.Completion.create(
          model="davinci",
          prompt=base_prompt+prompt+" =>",
          max_tokens=20,
          stop="\n",
          temperature=0.6
        )
    
    return g["choices"][0]["text"].strip()

# ​
# exemples = ["Trump", "Poutine", "Le champagne", "Le caviar", "Être vegan", "Le cassoulet", "CNews", "Le journal Libération",
#            "Philippe Poutou", "La grève", "Les riches", "La manif pour tous", "Le parti socialiste", "La France Insoumise",
#             "Les républicains", "La Suisse", "Le féminisme", "L'écologie", "Le cannabis", "La coke", "Le tennis", "La révolte",
#            "Le tofu", "Un bon gros steak", "Un bon gros steak vegan", "Une manif", "Une manif d'identitaire", "Les gateaux"]
# ​

# for exemple in exemples:
#     result = degaucheoudedroite(exemple)
#     print("%s : %s"%(exemple, result))





# --------------------------------------------------------------------------------------------------------
# APPLICATION


st.write("# Écolo ou pas écolo ?")
# st.info("Ce site a été construit en inspiration par De gauche ou de droite")
# st.sidebar.info("Copyright Eclaircies")

query = st.text_input("L'intelligence artificielle vous répond")

if query != "":

    # Algorithme
    # result = random.choice(["Écolo","Pas écolo"]) # For tests
    result = ecolopasecolo(query)

    if result == "Écolo":
        st.success('Écolo', icon="🌎")

    elif result == "Pas écolo":
        st.error('Pas écolo', icon="🚨")

    else:
        st.info('Comme les normands, ça dépend', icon="❓")



    st.write("""
    Pour aller plus loin et avoir les bons ordres de grandeur, calculez votre bilan carbone https://datagir.ademe.fr/apps/nos-gestes-climat/ 
    
    """)