#customer choose options
a=1
while (a<=2):
    print('WELCOME TO DIGITAL GOLD INVESTMENT ')
    print('1,DIGITAL GOLD')
    print('2,Exit')
    choice=int(input("enter your choice:"))
    import pygame as p
    import time as t
    import random as r
    import os
    if choice == 1:
        print('customer explain in demat account opening process')
        def play_music(file_path):
            p.init()
            p.mixer.init()
            try:
                p.mixer.music.load(file_path)
                p.mixer.music.play()
                music_info = p.mixer.Sound(file_path)
                duration = music_info.get_length()
                t.sleep(duration)
            except p.error as e:
                print("An error occurred while playing the music:", e)
            finally:
                p.mixer.quit()
                p.quit()
        if __name__ == "__main__":
            music_file = "C:\\Users\\Naveen knf\\PycharmProjects\\pythonProject\\DGI\\demat account open audio.mp3"
            if os.path.exists(music_file):
                play_music(music_file)
        print('OPEN DEMAT ACCOUNT')
        img = p.image.load('C:\\Users\\Naveen knf\\PycharmProjects\\pythonProject\\DGI\\how-to-open-a-demat-account.jpeg')
        size = img.get_rect().size
        screen = p.display.set_mode(size)
        screen.blit(img, (0, 0))
        p.display.flip()
        p.event.clear()
        t.sleep(3)
        p.display.quit()
        fist_name = input('enter your first name:')
        last_name=input('enter your last name:')
        Mobile_number = input('enter the mobile number:')
        if len(Mobile_number) == 10:
            Nationality = input('enter your nationality:')
            aadharcard_details = int(input('enter your aadhar number:'))
            if (aadharcard_details>=16):
                pancard_details = input('enter your pan-card number:')
                if len(pancard_details)==12:
                    Email_address = input('enter your email address:')
                    Pincode = (input('enter your pincode:'))
                    if len (Pincode)==6:
                        print('DEMAT ACCOUNT CREATE SUCCESSFULLY')
                        def play_music(file_path):
                            p.init()
                            p.mixer.init()
                            try:
                                p.mixer.music.load(file_path)
                                p.mixer.music.play()
                                music_info = p.mixer.Sound(file_path)
                                duration = music_info.get_length()
                                t.sleep(duration)
                            except p.error as e:
                                print("An error occurred while playing the music:", e)
                            finally:
                                p.mixer.quit()
                                p.quit()
                        if __name__ == "__main__":
                            music_file = "C:\\Users\\Naveen knf\\PycharmProjects\\pythonProject\\DGI\\demat account creat success audio.mp3"
                            if os.path.exists(music_file):
                                play_music(music_file)
                        img = p.image.load('C:\\Users\\Naveen knf\\PycharmProjects\\pythonProject\\DGI\\demat-account.png')
                        size = img.get_rect().size
                        screen = p.display.set_mode(size)
                        screen.blit(img, (0, 0))
                        p.display.flip()
                        p.event.clear()
                        t.sleep(5)
                        p.display.quit()
                        i = 1
                        while (i <= 3):
                            print('user digital gold saving option')
                            print('1,Digital Gold Investment')
                            print('2,Exit')
                            choice = int(input("enter your choice:"))
                            if choice == 1:
                                img = p.image.load('C:\\Users\\Naveen knf\\PycharmProjects\\pythonProject\\DGI\\digital gold image.jpg')
                                size = img.get_rect().size
                                screen = p.display.set_mode(size)
                                screen.blit(img, (0, 0))
                                p.display.flip()
                                p.event.clear()
                                t.sleep(3)
                                p.display.quit()
                                j = 1
                                while (j <= 3):
                                    print('investment time periods')
                                    print('1,Daily investment')
                                    print('2,Monthly investment')
                                    print('3,yearly investment')
                                    print('4,exit')
                                    print('user investment time periods option(1/2/3/4)')
                                    def play_music(file_path):
                                        p.init()
                                        p.mixer.init()
                                        try:
                                            p.mixer.music.load(file_path)
                                            p.mixer.music.play()
                                            music_info = p.mixer.Sound(file_path)
                                            duration = music_info.get_length()
                                            t.sleep(duration)
                                        except p.error as e:
                                            print("An error occurred while playing the music:", e)
                                        finally:
                                            p.mixer.quit()
                                            p.quit()
                                    if __name__ == "__main__":
                                        music_file = "C:\\Users\\Naveen knf\\PycharmProjects\\pythonProject\\DGI\\select options audio.mp3"
                                        if os.path.exists(music_file):
                                            play_music(music_file)
                                    choice = int(input("enter your choice:"))
                                    if choice == 1:
                                        print('user select Daily investment')
                                        import random
                                        def generate_daily_investment_amount(min_amount, max_amount):
                                            return random.uniform(min_amount, max_amount)
                                        min_investment = float(input("Enter the minimum investment amount: "))
                                        max_investment = float(input("Enter the maximum investment amount: "))
                                        daily_investment = generate_daily_investment_amount(min_investment,max_investment)
                                        print(f"Today's investment amount in gold: {daily_investment:.2f}")
                                        print('payment option')
                                        print('1,upi')
                                        choice = int(input('enter your choice:'))
                                        if choice == 1:
                                            img = p.image.load('C:\\Users\\Naveen knf\\PycharmProjects\\pythonProject\\DGI\\UPI IMAGE.jpg')
                                            size = img.get_rect().size
                                            screen = p.display.set_mode(size)
                                            screen.blit(img, (0, 0))
                                            p.display.flip()
                                            p.event.clear()
                                            t.sleep(3)
                                            p.display.quit()
                                            user_amount = int(input('Please enter your amount: '))
                                            user_mobile_number = input('Please enter your mobile number: ')
                                            def otpgen():
                                                otp = ''
                                                for i in range(4):
                                                    otp += str(r.randint(1, 9))
                                                print("Your One Time Password is ")
                                                print(otp)
                                                return otp
                                            generated_otp = otpgen()
                                            entered_otp = input('Enter your OTP: ')
                                            if entered_otp == generated_otp:
                                                print('Payment successful')
                                                img = p.image.load('C:\\Users\\Naveen knf\\PycharmProjects\\pythonProject\\DGI\\Paymentsuccessful21.png')
                                                size = img.get_rect().size
                                                screen = p.display.set_mode(size)
                                                screen.blit(img, (0, 0))
                                                p.display.flip()
                                                p.event.clear()
                                                t.sleep(3)
                                                p.display.quit()
                                                def play_music(file_path):
                                                    p.init()
                                                    p.mixer.init()
                                                    try:
                                                        p.mixer.music.load(file_path)
                                                        p.mixer.music.play()
                                                        music_info = p.mixer.Sound(file_path)
                                                        duration = music_info.get_length()
                                                        t.sleep(duration)
                                                    except p.error as e:
                                                        print("An error occurred while playing the music:", e)
                                                    finally:
                                                        p.mixer.quit()
                                                        p.quit()
                                                if __name__ == "__main__":
                                                    music_file = "C:\\Users\\Naveen knf\\PycharmProjects\\pythonProject\\DGI\\investment complete.mp3"
                                                    if os.path.exists(music_file):
                                                        play_music(music_file)
                                            else:
                                                print('Payment failed')
                                                exit()
                                    if choice == 2:
                                        print('2,Monthly investment')
                                        import random
                                        def generate_daily_investment_amount(min_amount, max_amount):
                                            return round(random.uniform(min_amount, max_amount), 2)
                                        def simulate_monthly_investment():
                                            min_investment = float(
                                                input("Enter the minimum daily investment amount: "))
                                            max_investment = float(
                                                input("Enter the maximum daily investment amount: "))
                                            days_in_month = int(input("Enter the number of days in the month: "))
                                            monthly_investment = 0
                                            for day in range(1, days_in_month + 1):
                                                daily_investment = generate_daily_investment_amount(min_investment, max_investment)
                                                monthly_investment += daily_investment
                                                print(f"Day {day}: Invested {daily_investment} in gold.")
                                            return monthly_investment
                                        total_monthly_investment = simulate_monthly_investment()
                                        print(f"\nTotal monthly investment: {total_monthly_investment} in gold.")
                                        print('payment option')
                                        print('1,upi')
                                        choice = int(input('enter your choice:'))
                                        if choice == 1:
                                            img = p.image.load('C:\\Users\\Naveen knf\\PycharmProjects\\pythonProject\\DGI\\UPI IMAGE.jpg')
                                            size = img.get_rect().size
                                            screen = p.display.set_mode(size)
                                            screen.blit(img, (0, 0))
                                            p.display.flip()
                                            p.event.clear()
                                            t.sleep(3)
                                            p.display.quit()
                                            user_amount = int(input('Please enter your amount: '))
                                            user_mobile_number = input('Please enter your mobile number: ')
                                            def otpgen():
                                                otp = ''
                                                for i in range(4):
                                                    otp += str(r.randint(1, 9))
                                                print("Your One Time Password is ")
                                                print(otp)
                                                return otp
                                            generated_otp = otpgen()
                                            entered_otp = input('Enter your OTP: ')
                                            if entered_otp == generated_otp:
                                                print('Payment successful')
                                                img = p.image.load('C:\\Users\\Naveen knf\\PycharmProjects\\pythonProject\\DGI\\Paymentsuccessful21.png')
                                                size = img.get_rect().size
                                                screen = p.display.set_mode(size)
                                                screen.blit(img, (0, 0))
                                                p.display.flip()
                                                p.event.clear()
                                                t.sleep(3)
                                                p.display.quit()
                                                def play_music(file_path):
                                                    p.init()
                                                    p.mixer.init()
                                                    try:
                                                        p.mixer.music.load(file_path)
                                                        p.mixer.music.play()
                                                        music_info = p.mixer.Sound(file_path)
                                                        duration = music_info.get_length()
                                                        t.sleep(duration)
                                                    except p.error as e:
                                                        print("An error occurred while playing the music:", e)
                                                    finally:
                                                        p.mixer.quit()
                                                        p.quit()
                                                if __name__ == "__main__":
                                                    music_file = "C:\\Users\\Naveen knf\\PycharmProjects\\pythonProject\\DGI\\investment complete.mp3"
                                                    if os.path.exists(music_file):
                                                        play_music(music_file)
                                            else:
                                                print('Payment failed')
                                                quit()
                                    if choice == 3:
                                        import random
                                        def generate_daily_investment_amount(min_amount, max_amount):
                                            return round(random.uniform(min_amount, max_amount), 2)
                                        def simulate_yearly_investment():
                                            min_investment = float(
                                                input("Enter the minimum daily investment amount: "))
                                            max_investment = float(
                                                input("Enter the maximum daily investment amount: "))
                                            days_in_month = int(input("Enter the number of days in a month: "))
                                            months_in_year = int(input("Enter the number of months in a year: "))
                                            yearly_investment = 0
                                            for month in range(1, months_in_year + 1):
                                                monthly_investment = 0
                                                for day in range(1, days_in_month + 1):
                                                    daily_investment = generate_daily_investment_amount(min_investment, max_investment)
                                                    monthly_investment += daily_investment
                                                    print(f"Day {day}, Month {month}: Invested ${daily_investment} in gold.")
                                                yearly_investment += monthly_investment
                                            return yearly_investment
                                        total_yearly_investment = simulate_yearly_investment()
                                        print(f"\nTotal yearly investment: ${total_yearly_investment} in gold.")
                                        print('payment option')
                                        print('1,upi')
                                        choice = int(input('enter your choice:'))
                                        if choice == 1:
                                            img = p.image.load('C:\\Users\\Naveen knf\\PycharmProjects\\pythonProject\\DGI\\UPI IMAGE.jpg')
                                            size = img.get_rect().size
                                            screen = p.display.set_mode(size)
                                            screen.blit(img, (0, 0))
                                            p.display.flip()
                                            p.event.clear()
                                            t.sleep(3)
                                            p.display.quit()
                                            user_amount = int(input('Please enter your amount: '))
                                            user_mobile_number = input('Please enter your mobile number: ')
                                            def otpgen():
                                                otp = ''
                                                for i in range(4):
                                                    otp += str(r.randint(1, 9))
                                                print("Your One Time Password is ")
                                                print(otp)
                                                return otp
                                            generated_otp = otpgen()
                                            entered_otp = input('Enter your OTP: ')
                                            if entered_otp == generated_otp:
                                                print('Payment successful')
                                                img = p.image.load('C:\\Users\\Naveen knf\\PycharmProjects\\pythonProject\\DGI\\Paymentsuccessful21.png')
                                                size = img.get_rect().size
                                                screen = p.display.set_mode(size)
                                                screen.blit(img, (0, 0))
                                                p.display.flip()
                                                p.event.clear()
                                                t.sleep(3)
                                                p.display.quit()
                                                def play_music(file_path):
                                                    p.init()
                                                    p.mixer.init()
                                                    try:
                                                        p.mixer.music.load(file_path)
                                                        p.mixer.music.play()
                                                        music_info = p.mixer.Sound(file_path)
                                                        duration = music_info.get_length()
                                                        t.sleep(duration)
                                                    except p.error as e:
                                                        print("An error occurred while playing the music:", e)
                                                    finally:
                                                        p.mixer.quit()
                                                        p.quit()
                                                if __name__ == "__main__":
                                                    music_file = "C:\\Users\\Naveen knf\\PycharmProjects\\pythonProject\\DGI\\investment complete.mp3"
                                                    if os.path.exists(music_file):
                                                        play_music(music_file)
                                            else:
                                                print('Payment failed')
                                    if choice == 4:
                                        print()
                                    exit()
                            if choice == 2:
                                print()
                            exit()
                        else:
                          print('user login failed.pincode should be less than or equal to 7 charactor')
                else:
                  print('login failed.pan-card number is invalid')
            else:
                print('login failed.aadhar details should be less than or equal to 16.')
        else:
            print('login failed.mobile number should be less than or equal to 10 charactor')
    if choice == 2:
        print()
    exit()















