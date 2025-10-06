import streamlit as st

## comando para iniciar o site
## python -m streamlit run app.py

# ----------------------- SIDEBAR
st.sidebar.image("logo.png")
st.sidebar.title("Ulton Motors ")

carro = ['ferrari','bugatti','corolla cross','fusca','toro']

opcao = st.sidebar.selectbox('escolha o carro que foi alugado', carro)




#------------------------principal
st.title('Ulton motors - aluguel de carros')

st.image(f'{opcao}.png')
st.markdown(f'## você alugou o modelo: {opcao}')
st.markdown('---')

dias = st.text_input(f'por quantos dias o {opcao} foi alugado?')
km = st.text_input(f'quantos km você rodou com o {opcao}?')

#--------------calcular
if opcao == 'bugatti':
    diaria =  600

elif opcao == 'corolla cross':
     diaria = 400

elif opcao == 'ferrari':
     diaria = 700

elif opcao == 'fusca':
     diaria = 350
elif opcao == 'toro':
     diaria = 850

if st.button('calcular'):
     dias = int(dias)
     km = float(km)

     total_dias = dias * diaria
     total_km = km * 0.15
     aluguel_total = total_dias+total_km

     st.warning(f'você alugou {opcao} por {dias} dias e rodou {km}km. o valor total a pagar é R${aluguel_total:.2f}')               

