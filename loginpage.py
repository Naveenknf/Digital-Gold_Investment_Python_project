#admin login page
import pygame as p
import time as t
import sys as s
import os
img = p.image.load('C:\\Users\\Naveen knf\\PycharmProjects\\pythonProject\\DGI\\admin login image.jpg')
size = img.get_rect().size
screen = p.display.set_mode(size)
screen.blit(img, (0, 0))
p.display.flip()
p.event.clear()
t.sleep(3)
p.display.quit()
t.sleep(5)
def play_music(file_path):
    p.init()
    p.mixer.init()
    p.mixer.music.load(file_path)
    p.mixer.music.play()
    music_info = p.mixer.Sound(file_path)
    duration = music_info.get_length()
    t.sleep(duration)
    p.mixer.quit()
    p.quit()
if __name__ == "__main__":
    music_file = "C:\\Users\\Naveen knf\\PycharmProjects\\pythonProject\\DGI\\admin password.mp3"
    if os.path.exists(music_file):
        play_music(music_file)
print('ADMIN LOGIN')
admin_username='naveenknf6555'
admin_password=('19ucn222523')
def admin_login():
    username=input('enter the username:')
    password=input('enter the password:')
    if username==admin_username and password==admin_password :
        print('ADMIN LOGIN SUCCESSFULLY')

        def play_music(file_path):
            p.init()
            p.mixer.init()
            p.mixer.music.load(file_path)
            p.mixer.music.play()
            music_info = p.mixer.Sound(file_path)
            duration = music_info.get_length()
            t.sleep(duration)
            p.mixer.quit()
            p.quit()
        if __name__ == "__main__":
            music_file = "C:\\Users\\Naveen knf\\PycharmProjects\\pythonProject\\DGI\\admin login successfully audio.mp3 "
            if os.path.exists(music_file):
                play_music(music_file)
    else:
        print('LOGIN FAILED')
        s.exit()
admin_login()
def play_music(file_path):
    p.init()
    p.mixer.init()
    p.mixer.music.load(file_path)
    p.mixer.music.play()
    music_info = p.mixer.Sound(file_path)
    duration = music_info.get_length()
    t.sleep(duration)
    p.mixer.quit()
    p.quit()
if __name__ == "__main__":
    music_file = "C:\\Users\\Naveen knf\\PycharmProjects\\pythonProject\\DGI\\user name.mp3"
    if os.path.exists(music_file):
        play_music(music_file)
print('CREATE USER DETAILS')
def create_username():
    Username = input('enter the user name:')
    Mobile_number = int(input('enter the mobile number:'))
    Date_of_birth = input('enter the date of birth:')
    Address = input('enter your address:')
    Email_address = input('enter your email address:')
    Pincode = int(input('enter your pincode:'))
    if len(Username) > 30:
        print('user login failed.name should be less than or equal to 30 characters.')
    elif not (Mobile_number) > 10:
        print('user login failed.mobile number should be less than or equal to 10 charactor')
    elif len(Date_of_birth) > 10:
        print('user login failed.date of birth should be less than or equal to 10 charactor')
    elif len(Address) > 60:
        print('user login failed.address should be less than or equal to 60 characters about.')
    elif len(Email_address) > 30:
        print('user login failed.emailed is alphabetic and numerical or special character must')
    elif not (0 >= Pincode <= 7):
        print('USER ACCOUNT CREATE SUCCESSFULLY')
    else:
        print('user login failed.pincode should be less than or equal to 7 charactor')
create_username()
def play_music(file_path):
    p.init()
    p.mixer.init()
    p.mixer.music.load(file_path)
    p.mixer.music.play()
    music_info = p.mixer.Sound(file_path)
    duration = music_info.get_length()
    t.sleep(duration)
    p.mixer.quit()
    p.quit()
if __name__ == "__main__":
    music_file = "C:\\Users\\Naveen knf\\PycharmProjects\\pythonProject\\DGI\\user account create success.mp3"  # Corrected path to your music file
    if os.path.exists(music_file):
        play_music(music_file)
    else:
        print("Music file not found!")
img = p.image.load('C:\\Users\\Naveen knf\\PycharmProjects\\pythonProject\\DGI\\user login page.png')
size = img.get_rect().size
screen = p.display.set_mode(size)
screen.blit(img, (0,0 ))
p.display.flip()
p.event.clear()
t.sleep(3)
p.display.quit()














