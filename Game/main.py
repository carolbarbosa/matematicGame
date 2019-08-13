#sprint open source 0x72.itch.io/dungeontileset-ii (local onde peguei os personagens)

import sys, pygame

tamanho = width, height = 800, 600
tela = pygame.display.set_mode(tamanho)
personagem_nome = 'balu'
personagem_coracao_maximo = 10
personagem_coracao_inicial = 3
personagem_coracao_momento = personagem_coracao_inicial

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()


