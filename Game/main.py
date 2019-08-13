#sprint open source 0x72.itch.io/dungeontileset-ii (local onde peguei os personagens)

import sys, pygame
pygame.init()

personagem_nome = 'balu'
personagem_coracao_maximo = 10
personagem_coracao_inicial = 3
personagem_coracao_momento = personagem_coracao_inicial
personagem_avatar = pygame.image.load('personagens/heroi/h1.png')
personagem_posicao = personagem_avatar.get_rect()

tamanho = width, height = 800, 600
cor = 255, 255, 0
tela = pygame.display.set_mode(tamanho)



while 1:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT: sys.exit()
    tela.fill(cor)
    tela.blit(personagem_avatar, personagem_posicao)
    pygame.display.flip()
    

