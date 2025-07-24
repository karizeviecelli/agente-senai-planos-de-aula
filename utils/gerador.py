import openai
import os

# Use variável de ambiente ou defina sua chave diretamente (não recomendado em produção)
openai.api_key = os.getenv("OPENAI_API_KEY")  # ou substitua por "sua-chave"

# Função que envia prompt e retorna resposta do modelo GPT-4 (ou outro especificado)
def gerar_conteudo(prompt_usuario: str, modelo="gpt-4") -> str:
    try:
        resposta = openai.ChatCompletion.create(
            model=modelo,
            messages=[
                {"role": "system", "content": "Você é um especialista em educação técnica profissional usando a Metodologia SENAI."},
                {"role": "user", "content": prompt_usuario}
            ],
            temperature=0.7,
            max_tokens=1500
        )
        return resposta.choices[0].message['content'].strip()
    except Exception as e:
        return f"Erro ao gerar conteúdo: {str(e)}"
