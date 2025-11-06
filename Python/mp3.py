import pygame
# importa o modulo pygames, uma biblioteca usada para jogos, sons imgens e muito mais
pygame.mixer.init()
# aqui inicializa o sistema de som da pygames
pygame.mixer.music.load("mao-zedong-propaganda-music-red-sun-in-the-sky.mp3")
# carregue esse arquivo de áudio na memoria do seu computador
pygame.mixer.music.play()
# aqui voce manda tocar oque foi carregado antes
input("Pressione ENTER para parar a musica.")
