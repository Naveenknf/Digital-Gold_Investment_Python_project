print('welcome to gold purchase page')
print('show live gold price')
a=1
if (a)==1:
    import time as t
    import webbrowser as w
    import pygame as p
    import time as t
    import os
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
        music_file = "C:\\Users\\Naveen knf\\PycharmProjects\\pythonProject\\DGI\\live gold prize.mp3"
        if os.path.exists(music_file):
            play_music(music_file)
        else:
            print("The specified music file does not exist.")
    a = dir(w)
    print(a)
    w.open('https://www.goodreturns.in/gold-rates/salem.html')
    t.sleep(25)
else:
     print('Invalid program')
     exit()
def buy_your_gold():
    print('buy & store gold online')
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
        music_file = "C:\\Users\\Naveen knf\\PycharmProjects\\pythonProject\\DGI\\gold select.mp3"
        if os.path.exists(music_file):
            play_music(music_file)
        else:
            print("The specified music file does not exist.")
    p.display.quit()
    w.open_new_tab('https://www.googleadservices.com/pagead/aclk?sa=L&ai=DChcSEwjGxo2I-4yEAxUyCHsHHcHqDOwYABACGgJ0bQ&ase=2&gclid=Cj0KCQiAwvKtBhDrARIsAJj-kTgR1r0D5N0EQPHjttK6MBD2M6a8n2O9gX499pjIxhafz4SwsC0-a5YaApDEEALw_wcB&ohost=www.google.com&cid=CAESVuD2lsUbEZfNcQXTpA8gMG_usdtQJD9uMdjBhygTikGCiYmd-vVuwLwXInusFs6CEQ8lXmCjkMifykelLwIDdONJVRzwm2nRmkJlPH66PjbJdcdNjspL&sig=AOD64_0Wjg72ZlnR_wEZStpJsmobFc1m1w&q&nis=4&adurl&ved=2ahUKEwjJkoSI-4yEAxVaYvUHHQMxCF4Q0Qx6BAgKEAE')
    t.sleep(25)
    class Customer:
        def __init__(self, name, balance=0, savings_balance=0):
            self.name = name
            self.balance = balance
            self.savings_balance = savings_balance
        def deposit(self, amount, account_type="default"):
            if account_type.lower() == "savings":
                self.savings_balance += amount
                print(
                    f"Deposit of ${amount} to savings account successful. Current savings balance: ${self.savings_balance}")
            else:
                self.balance += amount
                print(f"Deposit of ${amount} to default account successful. Current balance: ${self.balance}")
        def withdraw(self, amount, account_type="default"):
            if account_type.lower() == "savings":
                if amount <= self.savings_balance:
                    self.savings_balance -= amount
                    print(
                        f"Withdrawal of ${amount} from savings account successful. Current savings balance: ${self.savings_balance}")
                else:
                    print("Insufficient funds in savings account. Withdrawal unsuccessful.")
            else:
                if amount <= self.balance:
                    self.balance -= amount
                    print(f"Withdrawal of ${amount} from default account successful. Current balance: ${self.balance}")
                else:
                    print("Insufficient funds in default account. Withdrawal unsuccessful.")
    class GoldPurchaseProgram:
        def __init__(self, gold_price_per_gram, production_charge_percentage=14, gst_percentage=5):
            self.gold_price_per_gram = gold_price_per_gram
            self.production_charge_percentage = production_charge_percentage
            self.gst_percentage = gst_percentage
            self.gold_balance = 0
        def purchase_gold(self, grams):
            cost_of_gold = grams * self.gold_price_per_gram
            production_charge = (self.production_charge_percentage / 100) * cost_of_gold
            gst_amount = (self.gst_percentage / 100) * (cost_of_gold + production_charge)
            total_cost = cost_of_gold + production_charge + gst_amount
            self.gold_balance += grams
            print(f"Gold purchase of {grams} grams successful.")
            print(f"Cost of Gold: ${cost_of_gold}")
            print(f"Production Charge: ${production_charge}")
            print(f"GST (5%): ${gst_amount}")
            print(f"Total Cost: ${total_cost}")
            print(f"Total gold balance: {self.gold_balance} grams.")
    customer1 = Customer("naveenknf", balance=50000, savings_balance=500)
    customer1.deposit(26500, account_type="default")
    customer1.withdraw(10000, account_type="default")
    customer1.deposit(10000, account_type="savings")
    gold_program = GoldPurchaseProgram(gold_price_per_gram=5830)
    gold_program.purchase_gold(8)
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
        music_file = "C:\\Users\\Naveen knf\\PycharmProjects\\pythonProject\\DGI\\gold purchese.mp3"
        if os.path.exists(music_file):
            play_music(music_file)
        else:
            print("The specified music file does not exist.")
    print('Payment successful')
    img = p.image.load('C:\\Users\\Naveen knf\\PycharmProjects\\pythonProject\\DGI\\Paymentsuccessful21.png')
    size = img.get_rect().size
    screen = p.display.set_mode(size)
    screen.blit(img, (0, 0))
    p.display.flip()
    p.event.clear()
    t.sleep(5)
    p.display.quit()
    print('Get Your Gold')
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
        music_file = "C:\\Users\\Naveen knf\\PycharmProjects\\pythonProject\\DGI\\get gold.mp3"
        if os.path.exists(music_file):
            play_music(music_file)
        else:
            print("The specified music file does not exist.")
    img = p.image.load('C:\\Users\\Naveen knf\\PycharmProjects\\pythonProject\\DGI\\get your gold.jpg')
    size = img.get_rect().size
    screen = p.display.set_mode(size)
    screen.blit(img, (0, 0))
    p.display.flip()
    p.event.clear()
    t.sleep(10)
    p.display.quit()
buy_your_gold()














