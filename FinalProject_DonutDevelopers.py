# Author(s): The Donut Developers (Kobe, Yailyn, Alic)
# Date Written:
# FinalProject_DonutDevelopers

# Import the required Libraries
import tkinter as tk
import PIL.ImageTk
from PIL import Image
import customtkinter
from CTkSpinbox import *


def get_label(label, button):
    if label.cget('text') != '$0.00':
        button.configure(state='normal')
    else:
        button.configure(state='disabled')


def reset_cart(label1, label2, label3, spinbox_value1, spinbox_value2, spinbox_value3, spinbox_value4, spinbox_value5, spinbox_value6):
    label1.configure(text='$0.00')
    label2.configure(text='$0.00')
    label3.configure(text='$0.00')
    spinbox_value1.set(0)
    spinbox_value2.set(0)
    spinbox_value3.set(0)
    spinbox_value4.set(0)
    spinbox_value5.set(0)
    spinbox_value6.set(0)


def update(value1, value2, value3, value4, value5, value6):
    return value1.get() + value2.get() + value3.get() + value4.get() + value5.get() + value6.get()


def total_spinbox_quantity(*args):
    return sum(args)


# FUNCTION THAT CALCULATES THE ORDER SUBTOTAL
def calculate_subtotal(quantity, cost):
    subtotal = quantity * cost
    return float(subtotal)


# FUNCTION THAT CALCULATES THE ORDER TAX
def calculate_tax(quantity, cost, tax_total=0):
    subtotal = calculate_subtotal(quantity, cost)
    tax = 0.07
    tax_total = tax_total + subtotal * tax
    return float(tax_total)


# FUNCTION THAT CALCULATES THE ORDER TOTAL
def calculate_total(quantity, cost, tax_total=0):
    subtotal = calculate_subtotal(quantity, cost)
    tax_total = calculate_tax(quantity, cost, tax_total=0)
    total = subtotal + tax_total
    return float(total)


# FUNCTION THAT DISPLAYS THE ORDER TOTAL
def display_total(label, amount, cost):
    label.configure(text=f'${calculate_total(amount, cost, tax_total=0):.2f}')


# FUNCTION THAT DISPLAYS THE ORDER SUBTOTAL
def display_subtotal(label, amount, cost):
    label.configure(text=f'${calculate_subtotal(amount, cost):.2f}')


# FUNCTION THAT DISPLAYS THE ORDER TAX
def display_tax(label, amount, cost):
    label.configure(text=f'${calculate_tax(amount, cost):.2f}')


class DonutApp(tk.Tk):

    def __init__(self):
        super().__init__()

        # INITIALIZES CUSTOM FONT
        bold_font = customtkinter.CTkFont(family='Arabella', size=12, weight='bold')

        # FUNCTION THAT DESTROYS/EXITS THE APPLICATION
        def exit_app():
            tk.Tk.destroy(self)

        class MenuPage(DonutApp):
            # FUNCTION THAT LOADS THE MENU PAGE
            @staticmethod
            def load_menu():
                menu_window = tk.Toplevel()
                menu_window.iconbitmap("donut.ico")
                menu_window.geometry("750x400")
                menu_window.title = 'Welcome to Mary Lou Donuts!'

                # CREATES AND PLACES A LABEL THAT DISPLAYS THE TEXT 'Here's our collection of donuts!'
                menu_label = tk.Label(menu_window, text="Here's our collection of Donuts!")
                menu_label.pack(pady=20)

                # CREATES AND PLACES A LABEL THAT DISPLAYS THE TEXT 'Glazed Ring'
                menu_button_one = tk.Button(menu_window, text="Glazed Ring", width=20)
                menu_button_one.pack(pady=15)

                # CREATES AND PLACES A LABEL THAT DISPLAYS THE TEXT 'Sprinkled Ring'
                menu_button_two = tk.Button(menu_window, text="Sprinkled Ring", width=20)
                menu_button_two.pack(pady=15)

                # CREATES AND PLACES A LABEL THAT DISPLAYS THE TEXT 'Chocolate Cake'
                menu_button_three = tk.Button(menu_window, text="Chocolate Cake", width=20)
                menu_button_three.pack(pady=15)

                # CREATES AND PLACES A LABEL THAT DISPLAYS THE TEXT 'Tiger Tail'
                menu_button_four = tk.Button(menu_window, text="Tiger Tail", width=20)
                menu_button_four.pack(pady=15)

                # CREATES AND PLACES A LABEL THAT DISPLAYS THE TEXT 'Vanilla Cake'
                menu_button_five = tk.Button(menu_window, text="Vanilla Cake", width=20)
                menu_button_five.pack(pady=15)

        class AboutUsPage(DonutApp):
            # FUNCTION THAT LOADS THE ABOUT US PAGE
            @staticmethod
            def load_about_us():
                about_us_window = tk.Toplevel(bg='#11c4ff')
                about_us_window.resizable(False, False)
                about_us_window.iconbitmap("donut.ico")
                about_us_window.geometry("950x600")
                about_us_window.title = 'Welcome to Mary Lou Donuts!'

                # CREATES AND PLACES A LABEL THAT DISPLAYS A SHORT BIO ABOUT US
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
                                                                             " donuts and more made just for you.",
                                         font='Helvetica', bg='#f06eaa')
                about_us_text.pack(pady=20)

                # LOADS ABOUT US PAGE IMAGE AND RESIZES IT
                image_path = PIL.Image.open('about_us_image.png')
                image = PIL.ImageTk.PhotoImage(image_path.resize((300, 300)))

                # CREATES AND PLACES A LABEL AND ATTACHES THE ABOUT US IMAGE TO IT
                about_image_label = tk.Label(about_us_window, bg='#ed7dd4', bd=1, image=image)
                about_image_label.image = image
                about_image_label.place(x=330, y=250)

        class PlaceOrderPage(DonutApp):
            # WORK IN PROGRESS
            #
            #
            #
            #
            # def entry_check(self, entry, button):
            # if entry.get() == '':

            # FUNCTION THAT OPENS THE PLACE ORDER WINDOW
            @staticmethod
            def place_order():
                place_order_window = tk.Toplevel()
                place_order_window.iconbitmap("donut.ico")
                place_order_window.geometry("750x500")
                place_order_window.configure(bg='#FFFFFF')

                # CREATES ORDER SUMMARY CANVAS
                order_details_canvas = customtkinter.CTkCanvas(place_order_window, bg='#FFFFFF', height=150,
                                                               width=230, borderwidth=0, highlightthickness=0)
                # CREATES HORIZONTAL LINES ON ORDER SUMMARY CANVAS & PLACES ORDER SUMMARY CANVAS
                order_details_canvas.create_line(1, 25, 200, 25)
                order_details_canvas.create_line(1, 100, 205, 100)
                order_details_canvas.place(x=495, y=300)

                # CREATES AND PLACES ORDER SUMMARY LABEL THAT SAYS 'Order Summary'
                order_summary_label = customtkinter.CTkLabel(place_order_window, fg_color='#FFFFFF',
                                                             text_color='#f06eaa', text='Order Summary',
                                                             font=(bold_font, 16, 'bold'), height=10)
                order_summary_label.place(x=500, y=300)

                # CREATES AND PLACES LABEL THAT DISPLAYS THE ORDER TOTAL
                order_total_label = customtkinter.CTkLabel(place_order_window, fg_color='red',
                                                           text='Order Total', font=(bold_font, 14, "bold"))
                order_total_label.place(x=500, y=402)



                # CREATES AND PLACES A LABEL THAT DISPLAYS THE ORDER TOTAL AMOUNT
                total_label = customtkinter.CTkLabel(place_order_window, text='$0.00', fg_color='red', width=100,
                                                     font=(bold_font, 14, "bold"))
                total_label.place(x=600, y=402)
                # CREATES AND PLACES LABEL THAT DISPLAYS THE TEXT 'Tax'
                tax_label = customtkinter.CTkLabel(place_order_window, fg_color='green',
                                                   text='Tax')
                tax_label.place(x=500, y=370)

                # CREATES AND PLACES A LABEL THAT DISPLAYS THE TOTAL AMOUNT OF TAX
                tax_amount_label = customtkinter.CTkLabel(place_order_window, fg_color='green', text='$0.00', width=100,
                                                          font=(bold_font, 12))

                tax_amount_label.place(x=600, y=370)

                # CREATES AND PLACES A LABEL THAT DISPLAYS THE TEXT 'Order Subtotal'
                subtotal_label = customtkinter.CTkLabel(place_order_window, fg_color='blue',
                                                        text='Order Subtotal')
                subtotal_label.place(x=500, y=340)

                # CREATES AND PLACES A LABEL THAT DISPLAYS THE ORDER SUBTOTAL
                subtotal_amount_label = customtkinter.CTkLabel(place_order_window, fg_color='blue', text='$0.00',
                                                               height=30, width=100, font=(bold_font, 12))

                subtotal_amount_label.place(x=600, y=340)

                # CREATES A VARIABLE THAT STORES THE COST OF OUR DONUTS
                price = 1.25

                # CONSTRUCTS INT VARIABLE FOR VALUES IN THE SPINBOXES ON THE PLACE ORDER PAGE
                first_box_value = customtkinter.IntVar(value=0)
                second_box_value = tk.IntVar(value=0)
                third_box_value = tk.IntVar(value=0)
                fourth_box_value = tk.IntVar(value=0)
                fifth_box_value = tk.IntVar(value=0)
                sixth_box_value = tk.IntVar(value=0)

                # ADD IMAGES - Kobe
                sb_one = CTkSpinbox(place_order_window, fg_color='#f06eaa', button_hover_color='#11c4ff', button_color='#f06eaa', border_width=2, button_border_width=1, button_border_color='#11c4ff', border_color='#11c4ff', start_value=0, max_value=20, scroll_value=1, height=25, width=100, variable=first_box_value, font=(bold_font, 12))
                sb_one.place(x=120, y=200)

                sb_two = tk.Spinbox(place_order_window, from_=0, to=20, state='readonly', width=5, wrap=True, textvariable=second_box_value)
                sb_two.place(x=170, y=250)

                sb_three = tk.Spinbox(place_order_window, from_=0, to=20, state='readonly', width=5, wrap=True, textvariable=third_box_value)
                sb_three.place(x=220, y=250)

                sb_four = tk.Spinbox(place_order_window, from_=0, to=20, state='readonly', width=5, wrap=True, textvariable=fourth_box_value)
                sb_four.place(x=270, y=250)

                sb_five = tk.Spinbox(place_order_window, from_=0, to=20, state='readonly', width=5, wrap=True, textvariable=fifth_box_value)
                sb_five.place(x=320, y=250)

                sb_six = tk.Spinbox(place_order_window, from_=0, to=20, state='readonly', width=5, wrap=True, textvariable=sixth_box_value)
                sb_six.place(x=370, y=250)

                # sb_amount = total_spinbox_quantity(int(sb_one.get()), int(sb_two.get()), int(sb_three.get()),
                 #                                  int(sb_four.get()), int(sb_five.get()), int(sb_six.get()))

                # print(sb_amount)

                # THIS IS A TEST BUTTON FOR TESTING ORDER TOTAL FUNCTIONALITY
                test_button = customtkinter.CTkButton(place_order_window, text='Test',
                                                      command=lambda: [reset_cart(subtotal_amount_label, tax_amount_label, total_label, first_box_value, second_box_value, third_box_value, fourth_box_value, fifth_box_value, sixth_box_value)])
                test_button.place(x=120, y=100)

                empty_cart_button = customtkinter.CTkButton(place_order_window, state='disabled', text='Empty Cart', height=5, width=20, fg_color='#f06eaa', hover_color='#FF0000', font=bold_font, command=lambda: [reset_cart(subtotal_amount_label, tax_amount_label, total_label, sb_one, second_box_value, third_box_value, fourth_box_value, fifth_box_value, sixth_box_value), empty_cart_button.configure(state='disabled')])
                empty_cart_button.place(x=625, y=300)

                # CREATES AND PLACES A LABEL THAT DISPLAYS THE TEXT 'Place your order here!'
                place_order_text = tk.Label(place_order_window, text="Place your order here!", bg='#FFFFFF',
                                            fg='#11c4ff', font=(bold_font, 12, "bold"))
                place_order_text.pack(pady=20)

                # CREATES AND PLACES A 'Add To Order' BUTTON THAT ALLOWS THE USER TO ADD AN ITEM TO THE ORDER
                add_to_order_button = customtkinter.CTkButton(place_order_window, text='Add To / Update Order',
                                                              fg_color='#f06eaa', hover_color='#11c4ff',
                                                              font=bold_font,
                                                              command=lambda: [update(first_box_value, second_box_value, third_box_value, fourth_box_value, fifth_box_value, sixth_box_value), display_total(total_label, update(first_box_value, second_box_value, third_box_value, fourth_box_value, fifth_box_value, sixth_box_value), price),
                                                                       display_subtotal(subtotal_amount_label, update(first_box_value, second_box_value, third_box_value, fourth_box_value, fifth_box_value, sixth_box_value),
                                                                                        price), display_tax(tax_amount_label, update(first_box_value, second_box_value, third_box_value, fourth_box_value, fifth_box_value, sixth_box_value), price), get_label(total_label, empty_cart_button)])
                add_to_order_button.place(x=120, y=400)

                # CREATES AND PLACES A LABEL THAT DISPLAYS THE TEXT '* Required'
                requirements_label = customtkinter.CTkLabel(place_order_window, text='* Required', text_color='black',
                                                            fg_color='#FFFFFF', font=(bold_font, 12, "bold"))
                requirements_label.place(x=120, y=320)

                # CREATES AND PLACES AN ENTRY THAT RECEIVES THE USER'S FIRST NAME
                first_name_entry = customtkinter.CTkEntry(place_order_window, placeholder_text='First Name*',
                                                          placeholder_text_color='#FFFFFF', height=10, width=85,
                                                          fg_color='#f06eaa', bg_color='#FFFFFF',
                                                          font=(bold_font, 12, 'bold'))
                first_name_entry.place(x=120, y=350)

                # CREATES AND PLACES AN ENTRY THAT RECEIVES THE USER'S LAST NAME
                last_name_entry = customtkinter.CTkEntry(place_order_window, placeholder_text='Last Name*',
                                                         placeholder_text_color='#FFFFFF', height=10, width=85,
                                                         fg_color='#f06eaa', bg_color='#FFFFFF',
                                                         font=(bold_font, 12, 'bold'))
                last_name_entry.place(x=210, y=350)

                # CREATES AND PLACES AN ENTRY THAT RECEIVES THE USER'S EMAIL ADDRESS
                email_entry = customtkinter.CTkEntry(place_order_window, placeholder_text='Email Address*',
                                                     placeholder_text_color='#FFFFFF', height=10, width=100,
                                                     fg_color='#f06eaa', bg_color='#FFFFFF',
                                                     font=(bold_font, 12, 'bold'))
                email_entry.place(x=300, y=350)

                # CREATES AND PLACES AN ENTRY THAT RECEIVES THE USER'S PHONE NUMBER
                phone_number_entry = customtkinter.CTkEntry(place_order_window, placeholder_text='Phone #',
                                                            placeholder_text_color='#FFFFFF', height=10, width=80,
                                                            fg_color='#f06eaa', bg_color='#FFFFFF',
                                                            font=(bold_font, 12, 'bold'))
                phone_number_entry.place(x=405, y=350)

                customer_details = {'name': first_name_entry.get(), 'email': email_entry.get()}

                # CREATES AND PLACES A BUTTON THAT ALLOWS THE USER TO COMPLETE THEIR ORDER AND SEND THEM TO THE ORDER
                # CONFIRMATION WINDOW
                finish_order_button = customtkinter.CTkButton(place_order_window, text='Place Order',
                                                              fg_color='#f06eaa', hover_color='#35fda6',
                                                              command=exit_app, font=bold_font, state='disabled',
                                                              text_color_disabled='#BABABA')
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

        # CREATES AND PLACES A LABEL THAT DISPLAYS 'Welcome To Mary Lou Donuts' ON THE MAIN PAGE
        welcome_label = tk.Label(self, bg='#FFFFFF', text="Welcome to Mary Lou Donuts!", fg='#11c4ff',
                                 font=(bold_font, 14, "bold"))
        welcome_label.pack(pady=10)

        # DEFINES PLACE ORDER BUTTON IMAGE
        # CREATES AND PLACES a "Place Order" BUTTON THAT TAKES THE USER TO THE PLACE ORDER WINDOW
        place_order_image = customtkinter.CTkImage(Image.open('place_order.png'), size=(30, 30))

        place_order_button = customtkinter.CTkButton(self, image=place_order_image, text="Place Order",
                                                     command=PlaceOrderPage.place_order, compound='left',
                                                     fg_color='#f06eaa', hover_color='#11c4ff', font=bold_font)
        place_order_button.pack(pady=5)

        # DEFINES ABOUT_US IMAGE
        # CREATES AND PLACES AN ABOUT US BUTTON THAT TAKES THE USER TO THE ABOUT US PAGE
        about_us_button_image = customtkinter.CTkImage(Image.open('about_us_button_image.png'), size=(30, 30))

        about_button = customtkinter.CTkButton(self, image=about_us_button_image, text="About Us",
                                               command=AboutUsPage.load_about_us, compound='right', fg_color='#f06eaa',
                                               hover_color='#11c4ff', font=bold_font)
        about_button.pack(pady=5)

        # DEFINES MENU BUTTON IMAGE
        # CREATES AND PLACES A MENU BUTTON THAT LOADS OUR MENU IN A DIFFERENT WINDOW
        menu_button_image = customtkinter.CTkImage(Image.open('menu_button_image.png'), size=(30, 30))

        menu_button = customtkinter.CTkButton(self, image=menu_button_image, text="Menu", command=MenuPage.load_menu,
                                              compound='left', fg_color='#f06eaa', hover_color='#11c4ff',
                                              font=bold_font)
        menu_button.pack(pady=5)

        # CREATES AND PLACES AN EXIT BUTTON THAT ALLOWS USERS TO EXIT THE APPLICATION
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
