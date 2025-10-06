import streamlit as st


# Dicionário relacionando estilos musicais as musicas
import streamlit as st

musicas_por_estilo = {
    "Funk": ["Baile de Favela", "Medley da Gaiola", "Rap da Felicidade"],
    "Sertanejo": ["Evidências", "Chico Mineiro", "Ai Se Eu Te Pego"],
    "Forró": ["Asa Branca", "Anjo Querubim", "Xote dos Milagres"],
    "Racionais": ["Diário de um Detento", "Negro Drama", "Vida Loka"]
}

# Pegar a lista de estilos (chaves do dicionário)
estilos = list(musicas_por_estilo.keys())

# Selectbox para escolher o estilo
st.sidebar.image("logo.png")
estilo_selecionado = st.sidebar.selectbox("Selecione o estilo:", estilos)


# Selectbox para escolher a música (apenas do estilo selecionado)
if estilo_selecionado:
    musica_selecionada = st.sidebar.selectbox(
        "Selecione a música:",
        musicas_por_estilo[estilo_selecionado]
    )

# Mostrar apenas a música selecionada
if estilo_selecionado and musica_selecionada:
    st.write(f"🎵 Música selecionada: **{musica_selecionada}**")
    st.write(f"🎶 Estilo: **{estilo_selecionado}**")
    st.image(f"{musica_selecionada}.png", width=700)

else:
        st.warning("⚠️ Nenhuma imagem disponível para esta música.")
