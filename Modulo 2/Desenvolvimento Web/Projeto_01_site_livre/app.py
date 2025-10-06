import streamlit as st

## comando para iniciar o site
## python -m streamlit run app.py

# ----------------------- SIDEBAR
st.sidebar.image("logo.png", width=700)
st.sidebar.title("cela beauty")

produtos = ['óleo capilar elséve','sabonete liquido nivea','esmalte risqué','agua micelar l oreal','protetor labial nivea','corretivo liquido maybelline']

opcao = st.sidebar.selectbox('escolha o produto que deseja comprar', produtos)

#----------------------------principal------------------------------------
st.title("cela beauty loja online")
st.markdown(f"## voce selecionou: **{opcao}**")
st.markdown("---")
st.image(f"{opcao}.png", width=500)

#quantidade de produtos
qtd = st.number_input(f"quantas unidades de {opcao} voce deseja comprar?", min_value=1, value=1)

#--------------------calcular--------------------
if opcao == 'óleo capilar elséve':
    preco = 35
    
elif opcao == 'sabonete liquido nivea':
    preco = 20
elif opcao == 'esmalte risqué':
    preco = 8
   
elif opcao == 'agua micelar l oreal':
    preco = 40
  
elif opcao == 'protetor labial nivea':
    preco = 15
    
elif opcao == 'corretivo liquido maybelline':
    preco = 25


if st.button('calcular'):
     preco = float(preco)
     qtd = int(qtd)

     total = preco * qtd

     st.warning(f'você comprou {qtd} unidades do produto {opcao} o valor total a pagar é R${total:.2f}')               
