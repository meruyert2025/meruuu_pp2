
import pygame, sys, glob, os

pygame.init()
pygame.mixer.init(frequency=44100, channels=2)


W, H = 720, 180
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Music Player (keyboard)")
font = pygame.font.SysFont(None, 28)


MUSIC_DIR = r"/Users/meruert/Desktop"
extensions = ("*.mp3", "*.wav", "*.ogg", "*.flac")

playlist = []
for ext in extensions:
    playlist.extend(glob.glob(os.path.join(MUSIC_DIR, ext)))

playlist.sort()

if not playlist:
    print("В папке нет аудиофайлов. Укажи путь в MUSIC_DIR.")
    pygame.quit(); sys.exit()

idx = 0
paused = False
volume = 0.7
pygame.mixer.music.set_volume(volume)


TRACK_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(TRACK_END)

def load_play(i: int):
    global idx, paused
    idx = i % len(playlist)
    pygame.mixer.music.load(playlist[idx])
    pygame.mixer.music.play()
    paused = False

load_play(idx)

clock = pygame.time.Clock()
running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        elif e.type == TRACK_END:           
            load_play(idx + 1)
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE:     
                if pygame.mixer.music.get_busy() and not paused:
                    pygame.mixer.music.pause(); paused = True
                elif paused:
                    pygame.mixer.music.unpause(); paused = False
                else:
                    load_play(idx)          
            elif e.key == pygame.K_s:       
                pygame.mixer.music.stop(); paused = False
            elif e.key in (pygame.K_RIGHT, pygame.K_n):   
                load_play(idx + 1)
            elif e.key in (pygame.K_LEFT, pygame.K_p):    
                load_play(idx - 1)
            elif e.key == pygame.K_UP:
                volume = min(1.0, volume + 0.1)
                pygame.mixer.music.set_volume(volume)
            elif e.key == pygame.K_DOWN:
                volume = max(0.0, volume - 0.1)
                pygame.mixer.music.set_volume(volume)

    
    screen.fill((245, 245, 245))
    now = os.path.basename(playlist[idx])
    lines = [
        "SPACE: Play/Pause   S: Stop   ←/P: Prev   →/N: Next   ↑/↓: Volume",
        f"Track: {now}",
        f"State: {'Paused' if paused else ('Playing' if pygame.mixer.music.get_busy() else 'Stopped')}",
        f"Volume: {int(volume*100)}%"
    ]
    y = 30
    for t in lines:
        screen.blit(font.render(t, True, (20,20,20)), (20, y))
        y += 32

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
