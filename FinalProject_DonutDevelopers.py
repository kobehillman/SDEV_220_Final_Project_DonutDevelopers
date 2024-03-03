# Author(s): The Donut Developers (Kobe, Yailyn, Alic)
# Date Written:
# FinalProject_DonutDevelopers

# Import the required Libraries
import tkinter as tk
import PIL.ImageTk
from PIL import Image
import customtkinter

# NEED TO MAKE CALCULATE TOTAL FUNCTION UPDATE/ADD TOTAL - Kobe
#
#


def calculate_total(quantity, cost, tax_total=0):
    tax = 0.07
    subtotal = quantity * cost
    tax_total = tax_total + subtotal * tax
    total = subtotal + tax_total
    return total

 # def display_total():


class DonutApp(tk.Tk):

    def __init__(self):
        super().__init__()

        bold_font = customtkinter.CTkFont(family='Arabella', size=12, weight='bold')

        def exit_app():
            tk.Tk.destroy(self)

        class MenuPage(DonutApp):

            @staticmethod
            def load_menu():
                menu_window = tk.Toplevel()
                menu_window.iconbitmap("donut.ico")
                menu_window.geometry("750x400")
                menu_window.title = 'Welcome to Mary Lou Donuts!'
                # Create Button(s)
                menu_label = tk.Label(menu_window, text="Here's our collection of Donuts!")
                menu_label.pack(pady=20)

                menu_button_one = tk.Button(menu_window, text="Glazed Ring", width=20)
                menu_button_one.pack(pady=15)

                menu_button_two = tk.Button(menu_window, text="Sprinkled Ring", width=20)
                menu_button_two.pack(pady=15)

                menu_button_three = tk.Button(menu_window, text="Chocolate Cake", width=20)
                menu_button_three.pack(pady=15)

                menu_button_four = tk.Button(menu_window, text="Tiger Tail", width=20)
                menu_button_four.pack(pady=15)

                menu_button_five = tk.Button(menu_window, text="Vanilla Cake", width=20)
                menu_button_five.pack(pady=15)

        class AboutUsPage(DonutApp):

            @staticmethod
            def load_about_us():
                about_us_window = tk.Toplevel(bg='#11c4ff')
                about_us_window.resizable(False, False)
                about_us_window.iconbitmap("donut.ico")
                about_us_window.geometry("950x600")
                about_us_window.title = 'Welcome to Mary Lou Donuts!'
                # Create Label & Button(s)
                about_us_text = tk.Label(about_us_window, fg='#FFFFFF', text="Welcome to Mary Lou Donuts, where "
                                                                             "tradition meets taste"
                                                                             " in every bite!\n\n"
                                                                             "Since 1961, our cozy shop in Lafayette, "
                                                                             "Indiana,"
                                                                             "\n has been"
                                                                             "a community staple, serving up "
                                                                             "delectable,"
                                                                             "freshly-made\n"
                                                                             "donuts that evoke the sweet nostalgia "
                                                                             "of home.\n\n"
                                                                             "Here, every donut is a piece of our "
                                                                             "story, crafted with"
                                                                             "love and the finest ingredients.\nAs "
                                                                             "you explore our"
                                                                             "app,"
                                                                             "discover our diverse menu, learn about "
                                                                             "our specials,"
                                                                             "and order online.\n"
                                                                             "\nJoin us in celebrating the joy of "
                                                                             "simple, delicious"
                                                                             "donuts and more made just for you.",
                                         font='Helvetica', bg='#f06eaa')
                about_us_text.pack(pady=20)

                # Loads background image and resizes it
                image_path = PIL.Image.open('about_us_image.png')
                image = PIL.ImageTk.PhotoImage(image_path.resize((300, 300)))

                # Creates a 'background' label and attaches the image to the label
                about_image_label = tk.Label(about_us_window, bg='#ed7dd4', bd=1, image=image)
                about_image_label.image = image
                about_image_label.place(x=330, y=250)
                # Loads background image and resizes it

        class PlaceOrderPage(DonutApp):
            # WORK IN PROGRESS
            #
            #
            #
            #

            # order_total = calculate_total(amount, price)

            @staticmethod
            def place_order():
                place_order_window = tk.Toplevel()
                place_order_window.iconbitmap("donut.ico")
                place_order_window.geometry("750x500")
                place_order_window.configure(bg='#FFFFFF')

                # ADD IMAGES - Kobe
                sb_one = tk.Spinbox(place_order_window, from_=0, to=20, state='readonly')
                sb_one.pack()

                price = 1.25

            # Create Label & Button(s)
                place_order_text = tk.Label(place_order_window, text="Place your order here!", font=bold_font)
                place_order_text.pack(pady=20)

                add_to_order_button = customtkinter.CTkButton(place_order_window, text='Add To Order',
                                                              fg_color='#f06eaa', hover_color='#11c4ff',
                                                              font=bold_font,
                                                              command=lambda: print(calculate_total(int(sb_one.get()),
                                                                                                    price)))
                add_to_order_button.place(x=120, y=400)

                order_option_two = tk.Button(place_order_window, text="Sprinkled Ring", width=20)
                order_option_two.pack(pady=10)
                sb_two = tk.Spinbox(place_order_window, from_=0, to=20)
                sb_two.pack()

                order_option_three = tk.Button(place_order_window, text="Chocolate Cake", width=20)
                order_option_three.pack(pady=10)

                sb_three = tk.Spinbox(place_order_window, from_=0, to=20)
                sb_three.pack()

                finish_order_button = customtkinter.CTkButton(place_order_window, text='Finish Order',
                                                              fg_color='#f06eaa', hover_color='#35fda6',
                                                              command=exit_app, font=bold_font)
                finish_order_button.place(x=300, y=400)

    # prices = {"Glazed Ring": 1.25, "Sprinkled Ring": 1.25, "Chocolate Cake": 1.25}

        # Changes size of the main window, adds app icon to window, window resizable T/F
        # Sets the title of the main window.
        # Sets the background color to white.

        main_logo_path = PIL.Image.open('mary_lou_donuts.png')
        main_logo = PIL.ImageTk.PhotoImage(main_logo_path.resize((200, 200)))

        main_logo_label = tk.Label(self, bg='#FFFFFF', image=main_logo)
        main_logo_label.image = main_logo
        main_logo_label.place(x=500, y=35)

        self.title("Mary Lou Donuts")
        self.geometry("750x250")
        self.iconbitmap("donut.ico")
        self.resizable(False, False)
        self.configure(bg='#FFFFFF')

        # Label that displays text on main window
        welcome_label = tk.Label(self, bg='#FFFFFF', text="Welcome to Mary Lou Donuts!", fg='#11c4ff', font=(bold_font, 14, "bold"))
        welcome_label.pack(pady=10)

        # Defines Place Order button image
        # Adds a "Place Order" button that takes the user to our order window allowing them to place an order.
        place_order_image = customtkinter.CTkImage(Image.open('place_order.png'), size=(30, 30))

        place_order_button = customtkinter.CTkButton(self, image=place_order_image, text="Place Order",
                                                     command=PlaceOrderPage.place_order, compound='left',
                                                     fg_color='#f06eaa', hover_color='#11c4ff', font=bold_font)
        place_order_button.pack(pady=5)

        # Defines About Us button image
        # Adds an "About Us" button that takes the user to our About Us page.
        about_us_button_image = customtkinter.CTkImage(Image.open('about_us_button_image.png'), size=(30, 30))

        about_button = customtkinter.CTkButton(self, image=about_us_button_image, text="About Us",
                                               command=AboutUsPage.load_about_us, compound='right', fg_color='#f06eaa',
                                               hover_color='#11c4ff', font=bold_font)
        about_button.pack(pady=5)

        # Defines Menu button image
        # Adds a "Menu" button that loads our menu in a different window.
        menu_button_image = customtkinter.CTkImage(Image.open('menu_button_image.png'), size=(30, 30))

        menu_button = customtkinter.CTkButton(self, image=menu_button_image, text="Menu", command=MenuPage.load_menu,
                                              compound='left', fg_color='#f06eaa', hover_color='#11c4ff', font=bold_font)
        menu_button.pack(pady=5)

        # Adds an "Exit" button that closes the application.
        exit_button = customtkinter.CTkButton(self, fg_color="#E50000", hover_color='#FF0000', text="Exit",
                                              command=self.destroy, font=bold_font)
        exit_button.pack(pady=5)


def main():
    DonutApp().mainloop()


if __name__ == '__main__':
    main()

    # DO NOT DELETE - BELOW IS THE BASE SETUP FOR ANY WINDOW
    # Replace all '?'s with the variable you want set up for the window
    # Make sure that the '!' matches the command listed in the button that goes to this window
    # def !():
    #   ? = tk.Toplevel()
    #   ?.geometry("750x250")
    #   ?.title = ('Text')
    # Create Label & Button(s)
    #   ? = tk.Label(?, text="Text").pack(pady=20)
    #   ? = tk.Button(?, text=("Text"), width=20).pack(pady=15)
    #
    # FOR CUSTOM TKINTER BUTTONS ETC!!!
    # ? = customtkinter.CTkButton(?, text='Text')
    # ?.pack() or .place()
    #
