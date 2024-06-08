import pygame as p
import time as t
import os
print('user login')
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
    music_file = "C:\\Users\\Naveen knf\\PycharmProjects\\pythonProject\\DGI\\user profile audio.mp3"
    if os.path.exists(music_file):
        play_music(music_file)
username='naveenknf'
userpassword='password123'
mobile_number=9688214680
def user_login():
    user_name=input('enter your user name:')
    user_password=input('enter your user name password:')
    mobile_number=input('enter user mobile number:')
    if len(mobile_number)== 10:
        import random as r
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
            print()
            if username == user_name and userpassword == user_password :
                print('user login successfull')
                import pygame as p
                import time as t
                import random as r
                img = p.image.load('C:\\Users\\Naveen knf\\PycharmProjects\\pythonProject\\DGI\\user login page.png')
                size = img.get_rect().size
                screen = p.display.set_mode(size)
                screen.blit(img, (0, 0))
                p.display.flip()
                p.event.clear()
                t.sleep(5)
                p.display.quit()
            else:
                print('login failed')
                exit()
        else:
            print('Invalid OTP. Exiting.')
            exit()
    else:
        print('in-void user login failed.mobile number should be less than or equal to 10 charactor')
        exit()
user_login()
a=1
while (a <= 3):
    print("\nOptions:")
    print("1.show your daily invest amount")
    print("2.show your monthly invest amount")
    print("3.show your yearly invest amount  ")
    print("4.exit")
    print('user choice(1/2/3/4)')
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
        else:
            print("The specified music file does not exist.")
    choice=str(input('enter your choice: '))
    import matplotlib.pyplot as plt
    import numpy as np
    if choice =='1':
        print('user daily invest amount')
        def calculate_total_investment_with_profit(daily_amount, days, profit_percentage):
            total_amount = daily_amount * days * (1 + profit_percentage / 100)
            return total_amount
        def calculate_return_on_investment(daily_amount, days, profit_percentage):
            total_investment = daily_amount * days
            total_return = total_investment * (profit_percentage / 100)
            return total_return
        def simulate_daily_investment(daily_investment, days_per_year, volatility):
            np.random.seed(42)
            daily_returns = np.random.normal(0, volatility, days_per_year) / 100 + 1
            cumulative_returns = np.cumprod(daily_returns) * daily_investment
            return cumulative_returns
        def plot_simulation(yearly_returns):
            plt.plot(range(1, len(yearly_returns) + 1), yearly_returns, marker='o')
            plt.title('Yearly Daily Investment Simulation')
            plt.xlabel('Trading Days')
            plt.ylabel('Portfolio Value')
            plt.grid(True)
            plt.show()
        print('daily investment page')
        daily_investment = float(input("Enter the daily investment amount(minimum 100): "))
        investment_days = int(input("Enter the number of days(maximum 252 days): "))
        profit_percentage = 5  # You can adjust the profit percentage as needed
        total_investment_with_profit = calculate_total_investment_with_profit(daily_investment, investment_days, profit_percentage)
        print(  f"The total amount after {investment_days} days with a daily investment of {daily_investment} and a {profit_percentage}% profit is: {total_investment_with_profit}")
        total_return = calculate_return_on_investment(daily_investment, investment_days, profit_percentage)
        print(  f"The total return after {investment_days} days with a daily investment of {daily_investment} and a {profit_percentage}% profit is: {total_return}")
        days_per_year =252  # Assuming 252 trading days in a year
        volatility = 1.5  # Adjust the volatility based on market conditions
        simulation_years = 5  # Adjust the number of simulation years
        daily_returns = simulate_daily_investment(daily_investment, days_per_year * simulation_years, volatility)
        daily_returns_reshaped = daily_returns.reshape((simulation_years, days_per_year))
        yearly_returns = np.sum(daily_returns_reshaped, axis=1)
        plot_simulation(yearly_returns)
        exit()
    if choice=='2':
        def calculate_total_investment_with_profit(monthly_amount, months, profit_percentage):
            total_amount = monthly_amount * months * (1 + profit_percentage / 100)
            return total_amount
        def calculate_return_on_investment(monthly_amount, months, profit_percentage):
            total_investment = monthly_amount * months
            total_return = total_investment * (profit_percentage / 100)
            return total_return
        def simulate_monthly_investment(monthly_investment, monthly_per_year, volatility):
            np.random.seed(42)
            monthly_returns = np.random.normal(0, volatility, monthly_per_year) / 100 + 1
            cumulative_returns = np.cumprod(monthly_returns) * monthly_investment
            return cumulative_returns
        def plot_simulation(yearly_returns):
            plt.plot(range(1, len(yearly_returns) + 1), yearly_returns, marker='o')
            plt.title('Yearly monthly Investment Simulation')
            plt.xlabel('Trading monthly')
            plt.ylabel('Portfolio Value')
            plt.grid(True)
            plt.show()
        print('monthly investment page')
        monthly_investment = float(input("Enter the monthly investment amount(minimum 1000): "))
        investment_months = int(input("Enter the number of months(maximum 36): "))
        profit_percentage = 5  # You can adjust the profit percentage as needed
        total_investment_with_profit = calculate_total_investment_with_profit(monthly_investment, investment_months, profit_percentage)
        print( f"The total amount after {investment_months} month with a monthly investment of {investment_months} and a {profit_percentage}% profit is: {total_investment_with_profit}")
        total_return = calculate_return_on_investment(monthly_investment, investment_months, profit_percentage)
        print( f"The total return after {investment_months} month with a monthly investment of {monthly_investment} and a {profit_percentage}% profit is: {total_return}")
        months_per_year = 12  # Assuming 252 trading days in a year
        volatility = 3.5  # Adjust the volatility based on market conditions
        simulation_years = 5  # Adjust the number of simulation years
        monthly_returns = simulate_monthly_investment(monthly_investment, months_per_year * simulation_years, volatility)
        monthly_returns_reshaped = monthly_returns.reshape((simulation_years, months_per_year))
        yearly_returns = np.sum(monthly_returns_reshaped, axis=1)
        plot_simulation(yearly_returns)
    if choice=='3':
        print('yearly investment page')
        def calculate_total_investment_with_profit(yearly_amount, years, profit_percentage):
            total_amount = yearly_amount * years * (1 + profit_percentage / 100)
            return total_amount
        def calculate_return_on_investment(yearly_amount, years, profit_percentage):
            total_investment = yearly_amount * years
            total_return = total_investment * (profit_percentage / 100)
            return total_return
        def simulate_yearly_investment(yearly_investment, years_per_year, volatility):
            np.random.seed(42)
            yearly_returns = np.random.normal(0, volatility, years_per_year) / 100 + 1
            cumulative_returns = np.cumprod(yearly_returns) * yearly_investment
            return cumulative_returns
        def plot_simulation(yearlys_returns):
            plt.plot(range(1, len(yearlys_returns) + 1), yearlys_returns, marker='o')
            plt.title('Yearly Investment Simulation')
            plt.xlabel('Trading years')
            plt.ylabel('Portfolio Value')
            plt.grid(True)
            plt.show()
        print('yearly investment page')
        # Example usage for total investment with profit
        yearly_investment = float(input("Enter the yearly investment amount(minimum 10000): "))
        investment_years = int(input("Enter the number of years(maximum 10) : "))
        profit_percentage = 5  # You can adjust the profit percentage as needed
        total_investment_with_profit = calculate_total_investment_with_profit(yearly_investment, investment_years,profit_percentage)
        print(  f"The total amount after {investment_years} years with a yearly investment of {yearly_investment} and a {profit_percentage}% profit is: {total_investment_with_profit}")
        total_return = calculate_return_on_investment(yearly_investment, investment_years, profit_percentage)
        print(  f"The total return after {investment_years} years with a yearly investment of {yearly_investment} and a {profit_percentage}% profit is: {total_return}")
        yearly_per_year = 6  # Assuming 252 trading days in a year
        volatility = 2.5  # Adjust the volatility based on market conditions
        simulation_years = 10  # Adjust the number of simulation years
        yearlys_returns = simulate_yearly_investment(yearly_investment, yearly_per_year * simulation_years, volatility)
        yearlys_returns_reshaped = yearlys_returns.reshape((simulation_years, yearly_per_year))
        yearlys_returns = np.sum(yearlys_returns_reshaped, axis=1)
        plot_simulation(yearlys_returns)
    if choice =='4':
        print()
    exit()














