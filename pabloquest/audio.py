import pygame


audioInit = False

soundDBnames = ['door','drink','hit','inventory','magic','walk','miss','pickup','fire','glass','equip_item','teleport','thunder',
'step1','step2','step3','step4','step5','step6','step7','step8','step9',
'blade','monster_bite','walking_on_item','monster_die','magic_eye','weaken','throw','levelup1','levelup2','slug','fire_spell','equip_jewel',
'heal','human_die','human_get_hit','holy','tension','prepare_magic','monster_laugh','zombie']
soundDB =  {};

def initAudio():
	pygame.mixer.pre_init(44100, -16, 1, 512)
	pygame.mixer.init()
	for el in soundDBnames:
		soundDB[el] = pygame.mixer.Sound('audio/'+el+'.wav')

	pygame.mixer.music.load("audio/music_cave.wav")
	pygame.mixer.music.play(-1)
	 


if audioInit == False:
	audioInit = True
	initAudio();


def PlaySound(str):
	#pygame.mixer.music.load('audio/drink.wav')
	print str
	sound = soundDB[str]
	sound.play()


