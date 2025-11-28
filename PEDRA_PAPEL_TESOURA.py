import random

j1 = ['PEDRA', 'PAPEL', 'TESOURA']
jg = 0
pc = 0

print('SEJAM BEM VINDO AO PEDRA, PAPEL OU TESOURAAAA, TENTE GANHAR DA MAQUINA!!!')

while True:    
    print(f'ladies and gentlemens, o placar até o momento está {jg} para o jogador x {pc} para o computador')
        
    pc_escolha = random.choice(j1)
    jg_escolha = input('FAÇA SUA ESCOLHAAA! ').upper()

    if jg_escolha not in j1:
        print('REVEJA SUA ESCOLHA JOGADOR.')
        continue
    print(f'O computador escolheuuu {pc_escolha}!!')
    if pc_escolha == jg_escolha:
        print('EEEEEEEEEE TEMOS UM EMPATEEE, DE NOVO, SÓ UM IRÁ SAIR VIVO DAQUI.')
    elif (jg_escolha == 'PEDRA' and pc_escolha == 'TESOURA') or \
         (jg_escolha == 'PAPEL' and pc_escolha == 'PEDRA') or \
         (jg_escolha == 'TESOURA' and pc_escolha == 'PAPEL'):
        jg = jg + 1
        print('PONTOOOO DO JOGADORR')
    else:
        print('POOOOOOOOOOOOOONTO DA MAQUINAAAAAAAA')
        pc= pc + 1
    if jg == 3:
        print('VOCÊ É O GRANDE VENCEDOOOOR!!! ')
        break
    elif pc == 3:
        print('BRUTAL!! NÃO SOBROU NADA PARA O BETA')
        break