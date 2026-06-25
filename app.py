import streamlit as st
import requests

st.title("Convertisseur de devises")

API_KEY = "96c3c6cdd2e5fb7dcd8b5726"
DEVISES = ["EUR", "USD", "GBP", "JPY", "CHF", "MAD", "CAD", "TND"]

@st.cache_data(ttl=3600)
def get_rates():
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/EUR"
    response = requests.get(url)
    data = response.json()
    return {d: data["conversion_rates"][d] for d in DEVISES}

rates = get_rates()

amount = st.number_input("Montant :", min_value=0.0, format="%.2f")
from_currency = st.selectbox("De :", list(rates.keys()))
to_currency = st.selectbox("Vers :", list(rates.keys()))

if st.button("Convertir"):
    if amount <= 0 :
        st.error("Veuillez saisir une valeur supérieure à 0.")
    elif from_currency == to_currency :
        st.error("Veuillez sélectionner 2 devises différentes.")
    else :
        result = amount * rates[to_currency] / rates[from_currency]
        st.success(f"{amount} {from_currency} = {result:.2f} {to_currency}")
