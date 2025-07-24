# 🤖 Agente SENAI – Geração de Planos e Avaliações Educacionais

Este projeto implementa um **agente inteligente com interface gráfica em Streamlit** para gerar:

- 📘 **Planos de Ensino**
- 📋 **Planos de Aula**
- 📝 **Avaliações (com Taxonomia de Bloom e TRI)**

Tudo baseado na **Metodologia SENAI de Educação Profissional**.

---

## 🚀 Como executar localmente

### 1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/agente-senai-planos-aula.git
cd agente-senai-planos-aula
```

### 2. Instale as dependências:
```bash
pip install -r requirements.txt
```

### 3. Configure sua chave OpenAI:
Você pode:
- Definir como variável de ambiente:
```bash
export OPENAI_API_KEY=sua-chave
```
- Ou editar o arquivo `utils/gerador.py` diretamente.

### 4. Execute o app Streamlit:
```bash
streamlit run interface/app_streamlit.py
```

---

## 🌐 Hospedagem via Streamlit Cloud

1. Faça login em https://streamlit.io/cloud com sua conta GitHub
2. Selecione este repositório
3. Escolha o arquivo principal: `interface/app_streamlit.py`
4. Configure a variável `OPENAI_API_KEY` na aba "Secrets"

Pronto! Seu agente estará disponível online.

---

## 📁 Estrutura do Projeto

```plaintext
agente-senai-planos-aula/
├── interface/
│   └── app_streamlit.py      # Interface gráfica com abas
├── utils/
│   └── gerador.py            # Função que chama a API da OpenAI
├── requirements.txt          # Dependências do projeto
├── README.md                 # Instruções de uso
├── .gitignore                # Itens ignorados pelo Git
└── prompts/                  # (opcional) modelos de prompt
```

---

## 📚 Créditos
Desenvolvido por Karize Viecelli com apoio de IA para aplicação educacional da Metodologia SENAI. ✨
