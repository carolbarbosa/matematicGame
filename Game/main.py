#sprint open source 0x72.itch.io/dungeontileset-ii (local onde peguei os personagens)

import sys, pygame
pygame.init()
pygame.display.set_caption('Mundo da Matemática')

personagem_nome = 'balu'
personagem_coracao_maximo = 10
personagem_coracao_inicial = 3
personagem_coracao_momento = personagem_coracao_inicial
personagem_avatar = pygame.image.load('personagens/heroi/h1.png')
personagem_posicao = personagem_avatar.get_rect()

tamanho = width, height = 800, 600
cor = 255, 255, 0
tela = pygame.display.set_mode(tamanho)
relogio = pygame.time.Clock()


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        
    if event.type == pygame.KEYDOWN:
        
        if event.key == pygame.K_LEFT:
            personagem_posicao.move_ip(-10,0)
            
        if event.key == pygame.K_RIGHT:
           personagem_posicao.move_ip(10,0)
            
        if event.key == pygame.K_UP:
            personagem_posicao.move_ip(0,-10)
            
        if event.key == pygame.K_DOWN:
            personagem_posicao.move_ip(0,10)
            
        if event.key == pygame.K_SPACE:
            personagem_posicao.move_ip(10,10)
            
        if event.key == pygame.K_BACKSPACE:
            personagem_posicao.move_ip(-10,-10)

   
    tela.fill(cor)
    tela.blit(personagem_avatar, personagem_posicao)
    relogio.tick(27)
    pygame.display.flip()

pygame.quit()
        
    

