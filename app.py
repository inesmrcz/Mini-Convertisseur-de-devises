import streamlit as st

st.title("Convertisseur de devises")

rates = {
    "EUR": 1,
    "USD": 1.1,
    "JPY": 130,
    "TND": 3.37
}

if "historique" not in st.session_state:
    st.session_state.historique = []

amount = st.number_input("Montant :", min_value=0.0, format="%.2f")
from_currency = st.selectbox("De :", rates.keys())
to_currency = st.selectbox("Vers :", rates.keys())

if st.button("Convertir"):
    if amount <= 0 :
        st.error("Veuillez saisir une valeur supérieure à 0.")
    elif from_currency == to_currency :
        st.error("Veuillez sélectionner 2 devises différentes.")
    else :
        result = amount * rates[to_currency] / rates[from_currency]
        st.success(f"{amount} {from_currency} = {result:.2f} {to_currency}")
        st.session_state.historique.insert(0, f"{amount} {from_currency} = {result:.2f} {to_currency}")

if st.button("Échanger"):
    if amount <= 0 :
        st.error("Veuillez saisir une valeur supérieure à 0.")
    elif from_currency == to_currency :
        st.error("Veuillez sélectionner 2 devises différentes.")
    else :
        result = amount * rates[from_currency] / rates[to_currency]
        st.success(f"{amount:.2f} {to_currency} = {result:.2f} {from_currency}")
        st.session_state.historique.insert(0, f"{amount:.2f} {to_currency} = {result:.2f} {from_currency}")

if st.session_state.historique:
    st.subheader("Historique des conversions")

    for item in st.session_state.historique:
        st.write(item)