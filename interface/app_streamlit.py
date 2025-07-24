import streamlit as st
from utils.gerador import gerar_conteudo
from utils.exportador_docx import exportar_para_docx

st.set_page_config(page_title="Agente SENAI - Gerador de Conteúdos Educacionais", layout="wide")
st.title("🤖 Agente SENAI – Geração de Planos e Avaliações")

aba = st.sidebar.radio("Escolha o que deseja gerar:", ["Plano de Ensino", "Plano de Aula", "Avaliações"])

if aba == "Plano de Ensino":
    st.header("📘 Gerador de Plano de Ensino")
    disciplina = st.text_input("Disciplina:")
    carga_horaria = st.number_input("Carga Horária Total (em horas)", 1, 200)
    competencias = st.text_area("Competências a serem desenvolvidas:")
    publico_alvo = st.text_area("Perfil da turma ou público-alvo:")

    if st.button("Gerar Plano de Ensino"):
        prompt = f"""
Você é um especialista na Metodologia SENAI e deve gerar um PLANO DE ENSINO estruturado para a seguinte disciplina:

Disciplina: {disciplina}
Carga Horária: {carga_horaria} horas
Competências: {competencias}
Público-alvo: {publico_alvo}

Estruture o plano com: objetivos de aprendizagem, conteúdo programático, estratégias metodológicas SENAI, critérios de avaliação e produtos esperados.
"""
        resposta = gerar_conteudo(prompt)
        st.text_area("Plano de Ensino Gerado:", resposta, height=400)

        if st.button("📥 Baixar em .docx"):
            caminho = exportar_para_docx(resposta, titulo="plano_ensino")
            with open(caminho, "rb") as f:
                st.download_button("Clique para baixar", f, file_name="plano_ensino.docx")

elif aba == "Plano de Aula":
    st.header("📋 Gerador de Plano de Aula")
    tema = st.text_input("Tema da Aula:")
    duracao = st.number_input("Duração da Aula (em horas)", 1, 8)
    objetivos = st.text_area("Objetivos de Aprendizagem:")
    metodologia = st.text_area("Estratégias Metodológicas (pode deixar em branco para aplicar SENAI padrão):")

    if st.button("Gerar Plano de Aula"):
        prompt = f"""
Gere um PLANO DE AULA com base na Metodologia SENAI para:

Tema: {tema}
Duração: {duracao} horas
Objetivos: {objetivos}
Estratégias Metodológicas: {metodologia or 'Aplique a Metodologia SENAI com foco em metodologias ativas.'}

O plano deve conter: etapas da aula com tempos, conteúdo, estratégias, produtos esperados e critérios de avaliação.
"""
        resposta = gerar_conteudo(prompt)
        st.text_area("Plano de Aula Gerado:", resposta, height=400)

        if st.button("📥 Baixar em .docx"):
            caminho = exportar_para_docx(resposta, titulo="plano_aula")
            with open(caminho, "rb") as f:
                st.download_button("Clique para baixar", f, file_name="plano_aula.docx")

elif aba == "Avaliações":
    st.header("📝 Gerador de Avaliações")
    tema = st.text_input("Tema da Avaliação:")
    disciplina = st.text_input("Disciplina:")
    nivel = st.selectbox("Nível da questão (Taxonomia de Bloom):", ["Conhecer", "Compreender", "Aplicar", "Analisar", "Avaliar", "Criar"])
    qtd = st.slider("Número de Questões:", 1, 20, 5)

    if st.button("Gerar Avaliação"):
        prompt = f"""
Gere {qtd} questões objetivas sobre o tema "{tema}" da disciplina "{disciplina}" seguindo a Metodologia SENAI. 
Use critérios da Taxonomia de Bloom (nível: {nivel}) e estrutura conforme o padrão da Teoria de Resposta ao Item (TRI), 
com 4 alternativas e feedback individual por alternativa. Gere em formato texto estruturado.
"""
        resposta = gerar_conteudo(prompt)
        st.text_area("Avaliação Gerada:", resposta, height=400)

        if st.button("📥 Baixar em .docx"):
            caminho = exportar_para_docx(resposta, titulo="avaliacoes")
            with open(caminho, "rb") as f:
                st.download_button("Clique para baixar", f, file_name="avaliacoes.docx")

st.markdown("---")
st.caption("Desenvolvido para aplicação da Metodologia SENAI com apoio de IA ✨")
