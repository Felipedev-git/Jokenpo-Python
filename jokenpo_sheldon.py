import random

acoes = {
    'TESOURA_PAPEL': 'corta',
    'PAPEL_PEDRA': 'cobre',
    'PEDRA_LAGARTO': 'esmaga',
    'LAGARTO_SPOCK': 'envenena',
    'SPOCK_TESOURA': 'esmaga',
    'TESOURA_LAGARTO': 'decapita',
    'LAGARTO_PAPEL': 'come',
    'PAPEL_SPOCK': 'refuta',
    'SPOCK_PEDRA': 'vaporiza',
    'PEDRA_TESOURA': 'quebra'
}

j1 = ['PEDRA', 'PAPEL', 'TESOURA', 'LAGARTO', 'SPOCK']
pc = 0
jg = 0
print('Sejam bem vindo ao PEDRA, PAPEL, TESOURA, LAGARTO e SPOCK, AS REGRAS SÃO SIMPLES.')
print('Tesoura corta Papel ' \
'\nPapel cobre Pedra ' \
'\nPedra esmaga Lagarto ' \
'\nLagarto envenena Spock ' \
'\nSpock esmaga Tesoura ' \
'\nTesoura decapita Lagarto ' \
'\nLagarto come Papel ' \
'\nPapel refuta Spock ' \
'\nSpock vaporiza Pedra ' \
'\n(E como sempre) Pedra quebra Tesoura'.upper())
print('-----------------------------------------------')

while True:
    print(f'O PLACAR ESTÁ: \nJOGADOR {jg} x MAQUINA {pc}')

    escolha_jogador = input('FAÇA SUA JOGADA: ').upper()
    escolha_maquina = random.choice(j1)

    
    if escolha_jogador not in j1:
        print('REVEJA SUA ESCOLHA JOGADOR! ')
        continue
    print(f'A MAQUINA ESCOLHEU {escolha_maquina}')
    if escolha_jogador == escolha_maquina:
        print('EMPATE, DE NOVO! ')
        print('-----------------------------------------------')
    elif (escolha_jogador == 'TESOURA' and escolha_maquina == 'PAPEL') or \
         (escolha_jogador == 'PAPEL' and escolha_maquina == 'PEDRA') or \
         (escolha_jogador == 'PEDRA' and escolha_maquina == 'LAGARTO') or \
         (escolha_jogador == 'LAGARTO' and escolha_maquina == 'SPOCK') or \
         (escolha_jogador == 'SPOCK' and escolha_maquina == 'TESOURA') or \
         (escolha_jogador == 'TESOURA' and escolha_maquina == 'LAGARTO')or \
         (escolha_jogador == 'LAGARTO' and escolha_maquina == 'PAPEL') or \
         (escolha_jogador == 'PAPEL' and escolha_maquina == 'SPOCK') or \
         (escolha_jogador == 'SPOCK' and escolha_maquina == 'PEDRA') or \
         (escolha_jogador == 'PEDRA' and escolha_maquina == 'TESOURA'):
        jg = jg +1
        chave = f"{escolha_jogador}_{escolha_maquina}"
        chave1 = acoes[chave]
        print(f'WOW! {escolha_jogador} {chave1} {escolha_maquina}!  ')
        print('-----------------------------------------------')
    else:
        pc = pc + 1
        chave = f"{escolha_maquina}_{escolha_jogador}"
        chave2 = acoes[chave]
        print(f'VISH! {escolha_maquina} {chave2} {escolha_jogador}!  ')
        print('-----------------------------------------------')
    if jg == 3:
        print('PARABÉNS JOGADOR!! VOCÊ VENCEU!!')
        break
    elif pc == 3:
        print('SOBRA NADA PRO BETINHA! ')
        break