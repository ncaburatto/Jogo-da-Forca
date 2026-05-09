# Jogo da Forca em Python

Objetivo do Jogo: Adivinhar qual é a palavra oculta, tendo como dica, o número de letras.

Regras Princiapis: 
- Um jogador define uma palavra, frase ou tema, desenhando traços correspondentes ao número de letras.
- O outro jogador diz uma letra por vez.
- Se a letra existir, o responsável pela forca escreve-a em todos os espaços corretos.
- Se a letra não existir, desenha-se uma parte do corpo (cabeça, tronco, braços, pernas) e a letra errada fica à parte como referência.

Condições:
- Vitória: A palavra é descoberta antes do boneco ser totalmente desenhado.
- Derrota: Término do preenchimento das partes corpóreas do enforcado

Limitações: 
-  Tentativas: 6 erros (cabeça, tronco, braços, pernas)
-  Palavras curtas com letras incomuns são mais difíceis de adivinhar, enquanto palavras longas e comuns são mais fáceis.
-  Uma letra por vez


## Descrição
O jogo escolhe aleatoriamente uma palavra secreta de uma lista predefinida (PYTHON, PROGRAMACAO, DESENVOLVIMENTO). O objetivo do jogador é descobrir a palavra oculta adivinhando uma letra por vez antes que suas tentativas se esgotem.

## Regras
1. O jogador tem no máximo **6 tentativas** de erro.
2. Apenas **letras individuais** são aceitas como entrada.
3. O jogo ignora se a letra é maiúscula ou minúscula.
4. Caracteres especiais, números ou múltiplas letras são considerados entradas inválidas e não descontam pontos, graças ao tratamento de erros.
5. O jogo termina quando o jogador completa a palavra (vitória) ou atinge 6 erros (derrota).

## Instruções de Execução
Para rodar o jogo, você precisa ter o Python 3 instalado em sua máquina.

1. Baixe o arquivo `jogo.py`.
2. Abra o terminal ou prompt de comando na pasta do arquivo.
3. Execute o comando:
   ```bash
   python jogo.py
   ```

## Exemplo de Utilização
```text
*********************************
***Bem vindo ao jogo da Forca!***
*********************************
Qual letra? a
Ops, você errou! Faltam 5 tentativas.
['_', '_', '_', '_', '_', '_']

Qual letra? p
Boa! Letra encontrada.
['P', '_', '_', '_', '_', '_']
```

