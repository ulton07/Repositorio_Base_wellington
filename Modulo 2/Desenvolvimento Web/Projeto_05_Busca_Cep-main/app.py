import streamlit as st
import requests
import json
import BuscarCep
import pandas as pd


##### TÍTULO DA APLICAÇÃO #####
st.title("Aplicação de busca e descoberta de cep")
st.image("principal.png")


##### Lista de Opções #####

opcoes = ["Buscar CEP", "Descobrir CEP"]



##### BARRA LATERAL #####
st.sidebar.image("logo.png")
escolha = st.sidebar.selectbox("escolha uma opcao:", opcoes)

##### BOTÃO BUSCAR CEP #####
if escolha == "Buscar CEP":
    cep = st.text_input("digite o cep:")


    if st.button("Buscar"):
        if len(cep) != 8 or not cep.isdigit():
            st.error("por favor< insira um cep válido com 8 digitos numéricos.")
        else:
            try:
                endereco = BuscarCep.buscar_cep(cep)
                if endereco:
                    st.success("endereço encontrado:")
                    st.write(f"CEP: {endereco[0]}")
                    st.write(f"Endereço: {endereco[1]}")
                    st.write(f"Bairro: {endereco[2]}")
                    st.write(f"cidade: {endereco[3]}")
                    st.write(f"estado: {endereco[4]}")
                    ## mapas
                    st.success("Endereço encontrado:")
                    st.title("localização no Mapa")
                    df = pd.DataFrame({"latitude":[endereco[5]],"longitude":[endereco[6]]})
                    st.map(df,zoom=15)
             
                else:
                    st.error("CEP não encontrado.")

            except Exception as e:
                st.error(f"Ocorreu um erro ao buscar o CEP: {e}")


    

##### BOTÃO DESCOBRIR CEP #####
elif escolha == "Descobrir CEP":
   
    st.header("descobrir CEP pelo Endereço")
    endereco_usuario = st.text_input("digite o endereço (ex: rua olga, Barueri, sp):")
    if st.button("Descobrir"):
        if not endereco_usuario.strip():
            st.error("por favor, insira p endereço válido.")
        else:
            try:
                resultado = BuscarCep.descobrir_cep(endereco_usuario)
                st.success("link de Busca no google:")
                st.write(resultado)
            except Exception as e:
                st.error(f"Ocorreu um erro ao descobrir o CEP: {e}")