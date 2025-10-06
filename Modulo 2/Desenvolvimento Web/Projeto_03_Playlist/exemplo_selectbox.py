import streamlit as st

# Dados de exemplo
generos = ["Romance", "Ficção Científica", "Fantasia", "Terror"]

# Dicionário relacionando gêneros aos seus livros
livros_por_genero = {
    "Romance": ["Dom Casmurro", "Orgulho e Preconceito", "A Moreninha"],
    "Ficção Científica": ["1984", "Duna", "Fundação"],
    "Fantasia": ["O Senhor dos Anéis", "Harry Potter", "As Crônicas de Nárnia"],
    "Terror": ["It: A Coisa", "O Iluminado", "Drácula"]
}

# Selectbox para escolher o gênero                
genero_selecionado = st.sidebar.selectbox("Selecione o gênero:", generos)

# Selectbox para escolher o livro (apenas do gênero selecionado)
if genero_selecionado:
    livro_selecionado = st.sidebar.selectbox(
        "Selecione o livro:", 
        livros_por_genero[genero_selecionado]
    )

# Mostrar apenas o livro selecionado
if genero_selecionado and livro_selecionado:
    st.write(f"**Livro selecionado:** {livro_selecionado}")
    st.write(f"**Gênero:** {genero_selecionado}")
    st.image(f"{livro_selecionado}.png")