import keyboard
import time

# Defina o texto que você deseja "digitar"
texto = """
A JUVENTUDE NEM-NEM NO BRASIL
O fenômeno dos jovens nem-nem, que não trabalham nem estudam, tem se tornado uma preocupação crescente no Brasil. De acordo com uma pesquisa realizada pelo Instituto de Pesquisa Econômica Aplicada (Ipea), 23% dos jovens brasileiros se encontram nessa condição. Essa situação revela não apenas a falta de oportunidades educacionais e profissionais para essa parcela da população, mas também o impacto profundo que isso pode ter no desenvolvimento pessoal e na economia do país.

Uma das principais razões para o aumento dos jovens nem-nem é a falta de acesso a uma educação de qualidade, aliada à precariedade do mercado de trabalho. Muitos jovens, principalmente de classes sociais mais baixas, enfrentam dificuldades para continuar os estudos ou se inserir em um mercado de trabalho cada vez mais competitivo. Além disso, a desmotivação pode surgir como resultado de frustrações com um sistema que não oferece perspectivas concretas de melhoria de vida.

As consequências desse fenômeno são preocupantes. Para os jovens, a falta de envolvimento em atividades educacionais ou profissionais pode gerar estagnação no desenvolvimento de habilidades e perda de confiança em suas capacidades. Para a sociedade como um todo, o crescimento do número de jovens nem-nem representa uma diminuição da força de trabalho produtiva, aumentando, assim, a dependência de programas assistenciais e contribuindo para o crescimento da desigualdade social.

Para reverter esse cenário, é fundamental que políticas públicas sejam implementadas de forma eficaz. Investir em programas de qualificação profissional, além de ampliar o acesso à educação, são medidas que podem proporcionar novas oportunidades para esses jovens. Além disso, incentivos ao primeiro emprego e a criação de programas de estágio podem ser importantes para facilitar a transição dos jovens para o mercado de trabalho.

Portanto, a situação dos jovens nem-nem no Brasil exige atenção e ação urgente. A inclusão dessa parcela da juventude no mercado de trabalho e no sistema educacional não só beneficia os próprios jovens, mas também é essencial para o crescimento econômico e o desenvolvimento social do país.
"""

# Tempo para você selecionar o campo onde o texto será escrito
print("Você tem 5 segundos para selecionar o campo onde o texto será escrito...")
time.sleep(5)  # Tempo para selecionar o campo de texto

# Função para simular a digitação caractere por caractere
for caractere in texto:
    keyboard.write(caractere)  # Simula a digitação de cada caractere
    time.sleep(0.01)  # Pequena pausa entre cada caractere para simular a digitação humana

print("Texto escrito com sucesso!!")