# import emoji as em
# resposta=input('Você está feliz ou triste? (F/T): ')

# if resposta.upper() == 'F':
#     print(em.emojize('Fico feliz por você :grinning_face_with_big_eyes: '))
# elif resposta.upper() == 'T':
#     print(em.emojize('Espero que você fique bem! :pensive_face: '))
# else:
#     print('Resposta inválida...')
import pyautogui as pag
pag.press('win')
pag.typewrite('notepad')
pag.press('enter')
pag.typewrite('Olá, PyAutoGUI!')
pag.hotkey('ctrl','s')
pag.typewrite('exemplo.txt')
pag.press('enter')