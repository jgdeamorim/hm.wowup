import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def gerar_descricao_produto(nome_produto, categoria, especificacoes, publico_alvo, beneficios):
    prompt = f"""
    Gere uma descrição profissional e otimizada para SEO do seguinte produto:

    - **Nome:** {nome_produto}
    - **Categoria:** {categoria}
    - **Especificações:** {especificacoes}
    - **Público-alvo:** {publico_alvo}
    - **Principais benefícios:** {beneficios}

    **Requisitos do texto:**
    1. **Descrição envolvente e persuasiva** destacando o diferencial do produto.
    2. **Linguagem clara e profissional**, evitando exageros como "o melhor do mundo".
    3. **Palavras-chave otimizadas para SEO** para maior visibilidade em marketplaces.
    4. **Escreva em formato de parágrafos curtos e fáceis de ler.**
    5. **Inclua um CTA no final**, incentivando a compra.

    **Exemplo de saída esperada:**
    "O {nome_produto} é ideal para {publico_alvo}. Com {especificacoes}, proporciona {beneficios}. Garanta já o seu!"
    """

    resposta = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "Você é um especialista em e-commerce e descrição de produtos."},
                  {"role": "user", "content": prompt}],
        max_tokens=500,
        temperature=0.7,
    )

    return resposta['choices'][0]['message']['content']
