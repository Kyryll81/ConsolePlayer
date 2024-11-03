from audio_player import AudioPlayer
from menu import Menu
from http_audio_file import AudioFileGetter
from user_options import UserOption

menu = Menu()
start_menu = UserOption()
file_getter = AudioFileGetter()

start_menu_option = menu.pick_menu(start_menu, "Hello, from ConsolePlayer!")()
if type(start_menu_option) == str:
    url: str = start_menu_option
    file_getter.get_audio_file(url)

    
    player = AudioPlayer()
    menu.pick_menu(player, "Player: ")()
    while player.is_started:
        menu.pick_menu(player, "Player: ")()



