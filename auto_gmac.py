# GASpec_auto_ЖМАК
# версия 1.1
# добавлена возможность прерывать цикл клавишей ESC

import keyboard
from time import sleep
import sys

delay = 0.5

def seven_enters():
    sleep(3)
    keyboard.press("Enter")
    keyboard.release("Enter")
    sleep(delay)
    
    for count in range(number_spectors):
        print('')
        print('Начало обработки ' + str(count+1) + ' спектра')
        
        if keyboard.is_pressed('esc'):
            print('Цикл прерван')
            break
        else:
            for down in range(count+1):
                keyboard.press("down")
                keyboard.release("down")
            
            sleep(delay)
        if keyboard.is_pressed('esc'):
            print('Цикл прерван')
            break
        else:    
            for i in range(4):
                if keyboard.is_pressed('esc'):
                    break
                else:
                    keyboard.press("Enter")
                    keyboard.release("Enter")
                    sleep(delay)
        if keyboard.is_pressed('esc'):
            print('Цикл прерван')
            break
        else:    
            keyboard.write(str(count+1).zfill(4))
            sleep(delay)
        if keyboard.is_pressed('esc'):
            print('Цикл прерван')
            break
        else:
            keyboard.press("Enter")
            keyboard.release("Enter")
            sleep(delay)
        if keyboard.is_pressed('esc'):
            print('Цикл прерван')
            break
        else:
            print('Я обработала ' + str(count+1) + ' из ' + str(number_spectors) + ' спектров')
    print('')
    print('Для выхода из программы нажми клавишу "x" (икс)')

print('Привет, тебя приветсвует программа GASpec_auto_ЖМАК версия 1.1, которая поможет тебе с GASpec.')
print('Для начала введи количество спектров, которое ты хочешь, чтобы программа за тебя посчитала:')
number_spectors = int(input())
print('')
print('Отлично! Выбрано рассчитать ' + str(number_spectors) + ' спектров')
sleep(delay)
print('')
print('Чтобы активировать меня нужно нажать горячую клавишу, и через 3 секунды я автоматически заработаю.')
sleep(delay)
print('Я работаю не быстро, но автоматически. Убедись, что я делаю все верно на одном спектре и можешь сходить попить чайку')
sleep(delay)
print('Теперь перейди в GASpec и выбери необходимые спектры, а затем нажми горячую клавишу "ctrl+alt+a"(контрол+альт+эй)')

keyboard.add_hotkey("ctrl+alt+a", seven_enters)

print('')
sleep(delay)
print('Если ты случайно запустил(а) цикл с большим числом спектров, можно отменить это действие.')
sleep(delay)
print('Для прерываения работы цикла зажми и удерживай клавишу "esc"(эскейп)')

sleep(delay)
print('')
print('Для выхода из программы нажми клавишу "x"(икс)')
keyboard.wait('x')
keyboard.remove_hotkey("ctrl+alt+a")

exit()

#keyboard.add_hotkey("ctrl+alt+s", seven_enters())
#keyboard.write("\n The key 's' was presses!")