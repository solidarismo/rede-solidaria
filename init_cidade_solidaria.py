import os
from dotenv import load_dotenv
from opencage.geocoder import OpenCageGeocode
import yaml
from yaml import SafeLoader
import streamlit as st
import streamlit_authenticator as stauth

def load_environment():
    environment = st.secrets["general"]["ENVIRONMENT"]
    if not environment:
        raise Exception("ENVIRONMENT variável não definida ou inválida!")
    return environment


def load_secrets():
    try:
        secrets = {
            "api_key": st.secrets["general"]["api_key"],
            "database_url": st.secrets["database"]["database_url"]
        }
        return secrets
    except KeyError as e:
        raise Exception(
            f"Segredo {e} não encontrado. Verifique o arquivo secrets.toml ou as configurações de segredos no Streamlit Cloud.")


def initialize_geocoder(api_key):
    return OpenCageGeocode(api_key)




def initialize():
    secrets = load_secrets()
    db_url = secrets["database_url"]
    geocoder = initialize_geocoder(secrets["api_key"])
    return db_url, geocoder
