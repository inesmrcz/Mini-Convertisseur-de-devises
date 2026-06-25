import streamlit as st
import requests
from app_functions import convert

st.title("Convertisseur de devises")

API_KEY = "96c3c6cdd2e5fb7dcd8b5726"

url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/EUR"
response = requests.get(url)
data = response.json()
rates = data["conversion_rates"]

if "historique" not in st.session_state:
    st.session_state.historique = []

amount = st.number_input("Montant :", min_value=0.0, format="%.2f")
from_currency = st.selectbox("De :", list(rates.keys()))
to_currency = st.selectbox("Vers :", list(rates.keys()))

if st.button("Convertir"):
    result = convert(amount, from_currency, to_currency, rates)
    if result is None:
        st.error("Veuillez saisir une valeur supérieure à 0.")
    elif from_currency == to_currency:
        st.error("Veuillez sélectionner 2 devises différentes.")
    else:
        st.success(f"{amount} {from_currency} = {result:.2f} {to_currency}")
        st.session_state.historique.insert(0, f"{amount} {from_currency} = {result:.2f} {to_currency}")

if st.button("Échanger"):
    result = convert(amount, to_currency, from_currency, rates)
    if result is None:
        st.error("Veuillez saisir une valeur supérieure à 0.")
    elif from_currency == to_currency:
        st.error("Veuillez sélectionner 2 devises différentes.")
    else:
        st.success(f"{amount:.2f} {to_currency} = {result:.2f} {from_currency}")
        st.session_state.historique.insert(0, f"{amount:.2f} {to_currency} = {result:.2f} {from_currency}")

if st.session_state.historique:
    st.subheader("Historique des conversions")

    for item in st.session_state.historique:
        st.write(item)
