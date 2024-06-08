import pygame as p
import sys
def welcome_screen(duration=3):
    p.init()
    width = 600
    height = 600
    s = p.display.set_mode((width, height))
    p.display.set_caption('DIGITAL GOLD INVESTMENT')
    font = p.font.Font(None, 30)
    t1 = "Hi, welcome to my DIGITAL GOLD INVESTMENT Project"
    textsurface = font.render(t1, True, (0, 0, 0))
    img = p.image.load('C:\\Users\\Naveen knf\\PycharmProjects\\pythonProject\\DGI\\welcome page.jpg')
    size = img.get_rect().size
    display_start_time = p.time.get_ticks()
    while p.time.get_ticks() - display_start_time <= duration * 1000:  # Display for 'duration' seconds
        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()
                sys.exit()
        s.fill((255, 231, 200))
        s.blit(textsurface, (width // 2 - textsurface.get_width() // 2, height // 2 - textsurface.get_height() // 2))
        s.blit(img, (150, 70))
        p.display.flip()
    p.quit()
'''
def main_menu():
    print('1. Login Page'
          '\n2. Investment Options'
          '\n3. Show User Update'
          '\n4. Purchase Gold'
          '\n5. Exit')
    i = 1
    while i <= 3:
        choice = int(input('Enter your choice: '))
        if choice == 1:
            print("Redirecting to Login Page...")
            import loginpage
        elif choice == 2:
            print("Redirecting to Investment Options...")
            import investmentoptions
        elif choice == 3:
            print("Redirecting to Show User Update...")
            import showuserupdate
        elif choice == 4:
            print("Redirecting to Purchase Gold...")
            import purchasegold
        elif choice == 5:
            print("Exiting program...")
            break
        else:
            print('Please enter a valid choice.')
        i += 1
'''
welcome_screen()
#main_menu()
