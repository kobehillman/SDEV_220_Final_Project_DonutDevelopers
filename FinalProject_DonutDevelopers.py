# Author(s): The Donut Developers (Kobe, Yailyn, Alic)
# Date Written:
# FinalProject_DonutDevelopers

# Import the required Libraries
import tkinter as tk
from tkinter import messagebox
import PIL.ImageTk
from PIL import Image
import customtkinter
from CTkSpinbox import *
import random
from json import dumps

#
#
#
#
#   ===================== FUNCTIONS ======================
#
#
#
#

# CREATES A DICTIONARY THAT STORES CUSTOMER INFORMATION
customer_details = {'customer': ['info']}


# CREATES AN 'ON CHANGE' / 'ON EVENT CHANGED / TYPE OF FUNCTION
def generate_on_change(obj):
    obj.tk.eval('''
        proc widget_proxy {widget widget_command args} {

            # call the real tk widget command with the real args
            set result [uplevel [linsert $args 0 $widget_command]]

            # generate the event for certain types of commands
            if {([lindex $args 0] in {insert replace delete}) ||
                ([lrange $args 0 2] == {mark set insert}) || 
                ([lrange $args 0 1] == {xview moveto}) ||
                ([lrange $args 0 1] == {xview scroll}) ||
                ([lrange $args 0 1] == {yview moveto}) ||
                ([lrange $args 0 1] == {yview scroll})} {

                event generate  $widget <<Change>> -when tail
            }

            # return the result from the real widget command
            return $result
        }
        ''')
    obj.tk.eval('''
        rename {widget} _{widget}
        interp alias {{}} ::{widget} {{}} widget_proxy {widget} _{widget}
    '''.format(widget=str(obj)))


# FUNCTION THAT CHECKS A LABELS TEXT IN THE ORDER SUMMARY
# IF THE TEXT == $0.00, A BUTTONS STATE IS SET TO NORMAL, ELSE THE BUTTON STATE IS SET TO DISABLED
def get_label(label, button):
    if label.cget('text') != '$0.00':
        button.configure(state='normal')
    else:
        button.configure(state='disabled')


# FUNCTION THAT RESETS THE ORDER SUMMARY VALUES TO $0.00
def reset_cart(label1, label2, label3):
    label1.configure(text='$0.00')
    label2.configure(text='$0.00')
    label3.configure(text='$0.00')


# FUNCTION THAT RESETS SPINBOX VALUES TO 0
def reset_spinbox(spinbox_value1, spinbox_value2, spinbox_value3, spinbox_value4, spinbox_value5):
    spinbox_value1.set(0)
    spinbox_value2.set(0)
    spinbox_value3.set(0)
    spinbox_value4.set(0)
    spinbox_value5.set(0)


# FUNCTION THAT RETURNS UPDATED INTVAR VALUES
def reset_values(intvar_value1, intvar_value2, intvar_value3, intvar_value4, intvar_value5):
    intvar_value1.set(0)
    intvar_value2.set(0)
    intvar_value3.set(0)
    intvar_value4.set(0)
    intvar_value5.set(0)


# FUNCTION THAT RETURNS THE UPDATED SPINBOX VALUES
def update(value1, value2, value3, value4, value5):
    return value1.get() + value2.get() + value3.get() + value4.get() + value5.get()


# FUNCTION THAT RETURNS THE SUM OF THE SPINBOXES
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

        #
        #
        #
        #
        #   ===================== DONUT MENU WINDOW ======================
        #
        #
        #
        #
        class MenuPage(DonutApp):
            # FUNCTION THAT LOADS THE MENU PAGE
            @staticmethod
            def load_menu():
                menu_window = tk.Toplevel()
                menu_window.iconbitmap("donut.ico")
                menu_window.geometry("750x400")
                menu_window.title = 'Welcome to Mary Lou Donuts!'
                menu_window.configure(bg='#FFFFFF')

                # CREATES AND PLACES A LABEL THAT DISPLAYS THE TEXT 'Here's our collection of donuts!'
                menu_label = tk.Label(menu_window, text="Here's our collection of Donuts!", bg='#FFFFFF')
                menu_label.pack(pady=20)

                # CREATES AND PLACES A LABEL THAT DISPLAYS THE TEXT 'Glazed Ring'
                menu_donut_label_one = tk.Label(menu_window, text="Glazed Ring", width=20, bg='#FFFFFF',
                                                font=(bold_font, 14, 'bold'))
                menu_donut_label_one.pack(pady=15)

                # CREATES AND PLACES A LABEL THAT DISPLAYS THE TEXT 'Sprinkled Ring'
                menu_donut_label_two = tk.Label(menu_window, text="Sprinkled Ring", width=20, bg='#FFFFFF',
                                                font=(bold_font, 14, 'bold'))
                menu_donut_label_two.pack(pady=15)

                # CREATES AND PLACES A LABEL THAT DISPLAYS THE TEXT 'Chocolate Cake'
                menu_donut_label_three = tk.Label(menu_window, text="Chocolate Cake", width=20, bg='#FFFFFF',
                                                  font=(bold_font, 14, 'bold'))
                menu_donut_label_three.pack(pady=15)

                # CREATES AND PLACES A LABEL THAT DISPLAYS THE TEXT 'Tiger Tail'
                menu_donut_label_four = tk.Label(menu_window, text="Tiger Tail", width=20, bg='#FFFFFF',
                                                 font=(bold_font, 14, 'bold'))
                menu_donut_label_four.pack(pady=15)

                # CREATES AND PLACES A LABEL THAT DISPLAYS THE TEXT 'Vanilla Cake'
                menu_donut_label_five = tk.Label(menu_window, text="Vanilla Cake", width=20, bg='#FFFFFF',
                                                 font=(bold_font, 14, 'bold'))
                menu_donut_label_five.pack(pady=15)

        #
        #
        #
        #
        #   ===================== ABOUT US WINDOW ======================
        #
        #
        #
        #
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
                                                                             " a community staple, serving up "
                                                                             "delectable,"
                                                                             " freshly-made\n"
                                                                             "donuts that evoke the sweet nostalgia "
                                                                             "of home.\n\n"
                                                                             "Here, every donut is a piece of our "
                                                                             "story, crafted with"
                                                                             " love and the finest ingredients.\nAs "
                                                                             "you explore our"
                                                                             "app,"
                                                                             " discover our diverse menu, learn about "
                                                                             "our specials,"
                                                                             " and order online.\n"
                                                                             "\n Join us in celebrating the joy of "
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

        #
        #
        #
        #
        #   ===================== PLACE ORDER WINDOW ======================
        #
        #
        #
        #
        class PlaceOrderPage(DonutApp):
            # WORK IN PROGRESS
            #
            #
            #
            #
            # FUNCTION THAT OPENS THE PLACE ORDER WINDOW
            @staticmethod
            def place_order():
                place_order_window = tk.Toplevel()
                place_order_window.iconbitmap("donut.ico")
                place_order_window.geometry("1000x500")
                place_order_window.configure(bg='#FFFFFF')
                place_order_window.resizable(False, False)

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
                order_total_label = customtkinter.CTkLabel(place_order_window, fg_color='#FFFFFF', text_color='black',
                                                           text='Order Total', font=(bold_font, 14, "bold"))
                order_total_label.place(x=500, y=402)

                # CREATES AND PLACES A LABEL THAT DISPLAYS THE ORDER TOTAL AMOUNT
                total_label = customtkinter.CTkLabel(place_order_window, text='$0.00', fg_color='#FFFFFF',
                                                     text_color='black', width=100,
                                                     font=(bold_font, 14, "bold"))
                total_label.place(x=600, y=402)
                # CREATES AND PLACES LABEL THAT DISPLAYS THE TEXT 'Tax'
                tax_label = customtkinter.CTkLabel(place_order_window, fg_color='#FFFFFF', text_color='black',
                                                   text='Tax')
                tax_label.place(x=500, y=365)

                # CREATES AND PLACES A LABEL THAT DISPLAYS THE TOTAL AMOUNT OF TAX
                tax_amount_label = customtkinter.CTkLabel(place_order_window, fg_color='#FFFFFF', text_color='black',
                                                          text='$0.00', width=100,
                                                          font=(bold_font, 12))

                tax_amount_label.place(x=600, y=365)

                # CREATES AND PLACES A LABEL THAT DISPLAYS THE TEXT 'Order Subtotal'
                subtotal_label = customtkinter.CTkLabel(place_order_window, fg_color='#FFFFFF', text_color='black',
                                                        text='Order Subtotal', font=(bold_font, 12))
                subtotal_label.place(x=500, y=335)

                # CREATES AND PLACES A LABEL THAT DISPLAYS THE ORDER SUBTOTAL
                subtotal_amount_label = customtkinter.CTkLabel(place_order_window, fg_color='#FFFFFF',
                                                               text_color='black', text='$0.00',
                                                               height=30, width=100, font=(bold_font, 12))

                subtotal_amount_label.place(x=600, y=335)

                # CREATES A VARIABLE THAT STORES THE COST OF OUR DONUTS
                price = 1.25

                # CONSTRUCTS INT VARIABLE FOR VALUES IN THE SPINBOXES ON THE PLACE ORDER PAGE
                first_box_value = customtkinter.IntVar(value=0)
                second_box_value = customtkinter.IntVar(value=0)
                third_box_value = customtkinter.IntVar(value=0)
                fourth_box_value = customtkinter.IntVar(value=0)
                fifth_box_value = customtkinter.IntVar(value=0)

                # LOADS THE PICTURES OF DONUTS AND RESIZES THEM
                glazed_ring_path = PIL.Image.open('donut_images/glazed_ring.png')
                glazed_ring = PIL.ImageTk.PhotoImage(glazed_ring_path.resize((150, 150)))

                chocolate_cake_path = PIL.Image.open('donut_images/chocolate_cake_donut.png')
                chocolate_cake = PIL.ImageTk.PhotoImage(chocolate_cake_path.resize((150, 150)))

                tiger_tail_path = PIL.Image.open('donut_images/tiger_tail.png')
                tiger_tail = PIL.ImageTk.PhotoImage(tiger_tail_path.resize((150, 150)))

                sprinkled_ring_path = PIL.Image.open('donut_images/sprinkled_ring.png')
                sprinkled_ring = PIL.ImageTk.PhotoImage(sprinkled_ring_path.resize((150, 150)))

                vanilla_cake_path = PIL.Image.open('donut_images/vanilla_cake_donut.png')
                vanilla_cake = PIL.ImageTk.PhotoImage(vanilla_cake_path.resize((150, 150)))

                # CREATES AND PLACES A LABEL THAT DISPLAYS THE NAME OF EACH DONUT ABOVE EACH IMAGE
                glazed_ring_name = tk.Label(place_order_window, text='Glazed Ring', font=(bold_font, 12, 'bold'),
                                            bg='#f06eaa', fg='#FFFFFF')
                glazed_ring_name.place(x=80, y=50)

                chocolate_cake_name = tk.Label(place_order_window, text='Chocolate Cake', font=(bold_font, 12, 'bold'),
                                               bg='#f06eaa', fg='#FFFFFF')
                chocolate_cake_name.place(x=240, y=50)

                tiger_tail_name = tk.Label(place_order_window, text='Tiger Tail', font=(bold_font, 12, 'bold'),
                                           bg='#f06eaa', fg='#FFFFFF')
                tiger_tail_name.place(x=430, y=50)

                sprinkled_ring_name = tk.Label(place_order_window, text='Sprinkled Ring', font=(bold_font, 12, 'bold'),
                                               bg='#f06eaa', fg='#FFFFFF')
                sprinkled_ring_name.place(x=580, y=50)

                vanilla_cake_name = tk.Label(place_order_window, text='Vanilla Cake', font=(bold_font, 12, 'bold'),
                                             bg='#f06eaa', fg='#FFFFFF')
                vanilla_cake_name.place(x=760, y=50)

                # CREATES AND PLACES A LABEL FOR EACH DONUT AND HOLDS THE IMAGES OF EACH DONUT FOR THE PLACE ORDER PAGE
                glazed_ring_label = tk.Label(place_order_window, image=glazed_ring)
                glazed_ring_label.image = glazed_ring
                glazed_ring_label.place(x=50, y=80)

                chocolate_cake_label = tk.Label(place_order_window, image=chocolate_cake)
                chocolate_cake_label.image = chocolate_cake
                chocolate_cake_label.place(x=220, y=80)

                tiger_tail_label = tk.Label(place_order_window, image=tiger_tail)
                tiger_tail_label.image = tiger_tail
                tiger_tail_label.place(x=390, y=80)

                sprinkled_ring_label = tk.Label(place_order_window, image=sprinkled_ring)
                sprinkled_ring_label.image = sprinkled_ring
                sprinkled_ring_label.place(x=560, y=80)

                vanilla_cake_label = tk.Label(place_order_window, image=vanilla_cake)
                vanilla_cake_label.image = vanilla_cake
                vanilla_cake_label.place(x=730, y=80)

                # CREATES AND PLACES LABEL WITH TEXT 'QUANTITY' FOR EACH DONUT
                quantity_label1 = tk.Label(place_order_window, text='Quantity:', font=(bold_font, 8, 'bold'),
                                           bg='#FFFFFF')
                quantity_label1.place(x=80, y=235)

                quantity_label2 = tk.Label(place_order_window, text='Quantity:', font=(bold_font, 8, 'bold'),
                                           bg='#FFFFFF')
                quantity_label2.place(x=250, y=235)

                quantity_label3 = tk.Label(place_order_window, text='Quantity:', font=(bold_font, 8, 'bold'),
                                           bg='#FFFFFF')
                quantity_label3.place(x=420, y=235)

                quantity_label4 = tk.Label(place_order_window, text='Quantity:', font=(bold_font, 8, 'bold'),
                                           bg='#FFFFFF')
                quantity_label4.place(x=590, y=235)

                quantity_label5 = tk.Label(place_order_window, text='Quantity:', font=(bold_font, 8, 'bold'),
                                           bg='#FFFFFF')
                quantity_label5.place(x=760, y=235)

                # CREATES AND PLACES SPINBOXES TO GET THE QUANTITIES OF EACH DONUT
                sb_one = CTkSpinbox(place_order_window, fg_color='#f06eaa', button_hover_color='#11c4ff',
                                    button_color='#f06eaa', border_width=2, button_border_width=1,
                                    button_border_color='#11c4ff', border_color='#11c4ff', start_value=0, max_value=20,
                                    scroll_value=1, height=25, width=100, variable=first_box_value,
                                    font=(bold_font, 12))
                sb_one.place(x=80, y=255)

                sb_two = CTkSpinbox(place_order_window, fg_color='#f06eaa', button_hover_color='#11c4ff',
                                    button_color='#f06eaa', border_width=2, button_border_width=1,
                                    button_border_color='#11c4ff', border_color='#11c4ff', start_value=0, max_value=20,
                                    scroll_value=1, height=25, width=100, variable=second_box_value,
                                    font=(bold_font, 12))
                sb_two.place(x=250, y=255)

                sb_three = CTkSpinbox(place_order_window, fg_color='#f06eaa', button_hover_color='#11c4ff',
                                      button_color='#f06eaa', border_width=2, button_border_width=1,
                                      button_border_color='#11c4ff', border_color='#11c4ff', start_value=0,
                                      max_value=20, scroll_value=1, height=25, width=100, variable=third_box_value,
                                      font=(bold_font, 12))
                sb_three.place(x=420, y=255)

                sb_four = CTkSpinbox(place_order_window, fg_color='#f06eaa', button_hover_color='#11c4ff',
                                     button_color='#f06eaa', border_width=2, button_border_width=1,
                                     button_border_color='#11c4ff', border_color='#11c4ff', start_value=0,
                                     max_value=20, scroll_value=1, height=25, width=100, variable=fourth_box_value,
                                     font=(bold_font, 12))
                sb_four.place(x=590, y=255)

                sb_five = CTkSpinbox(place_order_window, fg_color='#f06eaa', button_hover_color='#11c4ff',
                                     button_color='#f06eaa', border_width=2, button_border_width=1,
                                     button_border_color='#11c4ff', border_color='#11c4ff', start_value=0,
                                     max_value=20, scroll_value=1, height=25, width=100, variable=fifth_box_value,
                                     font=(bold_font, 12))
                sb_five.place(x=760, y=255)

                # CREATES AND PLACES A EMPTY CART BUTTON THAT RESETS THE TOTAL VALUES AS WELL AS ALL THE SPINBOX
                # VALUES
                empty_cart_button = customtkinter.CTkButton(place_order_window, state='disabled', text='Empty Cart',
                                                            height=5, width=20, fg_color='#f06eaa',
                                                            hover_color='#FF0000', font=bold_font,
                                                            command=lambda: [reset_cart(subtotal_amount_label,
                                                                                        tax_amount_label, total_label),
                                                                             reset_spinbox(sb_one, sb_two, sb_three,
                                                                                           sb_four, sb_five),
                                                                             reset_values(first_box_value,
                                                                                          second_box_value,
                                                                                          third_box_value,
                                                                                          fourth_box_value,
                                                                                          fifth_box_value),
                                                                             update(first_box_value, second_box_value,
                                                                                    third_box_value, fourth_box_value,
                                                                                    fifth_box_value),
                                                                             empty_cart_button.configure(
                                                                                 state='disabled')])
                empty_cart_button.place(x=625, y=300)

                # CREATES AND PLACES A LABEL THAT DISPLAYS THE TEXT 'Place your order here!'
                place_order_text = tk.Label(place_order_window, text="Place your order here!", bg='#FFFFFF',
                                            fg='#11c4ff', font=(bold_font, 14, "bold"))
                place_order_text.pack(pady=10)

                # CREATES AND PLACES A 'Add To Order' BUTTON THAT ALLOWS THE USER TO ADD AN ITEM TO THE ORDER
                add_to_order_button = customtkinter.CTkButton(place_order_window, text='Add To / Update Order',
                                                              fg_color='#f06eaa', hover_color='#11c4ff',
                                                              font=bold_font,
                                                              command=lambda: [update(first_box_value, second_box_value,
                                                                                      third_box_value, fourth_box_value,
                                                                                      fifth_box_value),
                                                                               display_total(total_label,
                                                                                             update(first_box_value,
                                                                                                    second_box_value,
                                                                                                    third_box_value,
                                                                                                    fourth_box_value,
                                                                                                    fifth_box_value),
                                                                                             price),
                                                                               display_subtotal(subtotal_amount_label,
                                                                                                update(first_box_value,
                                                                                                       second_box_value,
                                                                                                       third_box_value,
                                                                                                       fourth_box_value,
                                                                                                       fifth_box_value),
                                                                                                price),
                                                                               display_tax(tax_amount_label,
                                                                                           update(first_box_value,
                                                                                                  second_box_value,
                                                                                                  third_box_value,
                                                                                                  fourth_box_value,
                                                                                                  fifth_box_value),
                                                                                           price),
                                                                               get_label(total_label,
                                                                                         empty_cart_button),
                                                                               DonutApp.update_idletasks(self)])
                add_to_order_button.place(x=120, y=400)

                # CREATES AND PLACES A LABEL THAT DISPLAYS THE TEXT '* Required'
                requirements_label = customtkinter.CTkLabel(place_order_window, text='* Required', text_color='black',
                                                            fg_color='#FFFFFF', font=(bold_font, 12, "bold"))
                requirements_label.place(x=120, y=310)

                # CREATES AND PLACES LABELS ABOVE EACH ENTRY BOX
                first_name_label = tk.Label(place_order_window, text='First Name*', font=(bold_font, 10, 'bold'),
                                            bg='#FFFFFF')
                first_name_label.place(x=120, y=330)

                last_name_label = tk.Label(place_order_window, text='Last Name*', font=(bold_font, 10, 'bold'),
                                           bg='#FFFFFF')
                last_name_label.place(x=210, y=330)

                email_label = tk.Label(place_order_window, text='Email*', font=(bold_font, 10, 'bold'),
                                       bg='#FFFFFF')
                email_label.place(x=325, y=330)

                phone_number_label = tk.Label(place_order_window, text='Phone #', font=(bold_font, 10, 'bold'),
                                              bg='#FFFFFF')
                phone_number_label.place(x=410, y=330)

                # CREATES AND PLACES AN ENTRY THAT RECEIVES THE USER'S FIRST NAME
                first_name_entry = customtkinter.CTkEntry(place_order_window,
                                                          placeholder_text_color='#FFFFFF', height=10, width=85,
                                                          fg_color='#f06eaa', bg_color='#FFFFFF',
                                                          font=(bold_font, 12, 'bold'))
                first_name_entry.place(x=120, y=350)

                # CREATES AND PLACES AN ENTRY THAT RECEIVES THE USER'S LAST NAME
                last_name_entry = customtkinter.CTkEntry(place_order_window,
                                                         placeholder_text_color='#FFFFFF', height=10, width=85,
                                                         fg_color='#f06eaa', bg_color='#FFFFFF',
                                                         font=(bold_font, 12, 'bold'))
                last_name_entry.place(x=210, y=350)

                # CREATES AND PLACES AN ENTRY THAT RECEIVES THE USER'S EMAIL ADDRESS
                email_entry = customtkinter.CTkEntry(place_order_window,
                                                     placeholder_text_color='#FFFFFF', height=10, width=100,
                                                     fg_color='#f06eaa', bg_color='#FFFFFF',
                                                     font=(bold_font, 12, 'bold'))
                email_entry.place(x=300, y=350)

                # CREATES AND PLACES AN ENTRY THAT RECEIVES THE USER'S PHONE NUMBER
                phone_number_entry = customtkinter.CTkEntry(place_order_window,
                                                            placeholder_text_color='#FFFFFF', height=10, width=80,
                                                            fg_color='#f06eaa', bg_color='#FFFFFF',
                                                            font=(bold_font, 12, 'bold'))
                phone_number_entry.place(x=405, y=350)

                # FUNCTION THAT RECORDS CUSTOMER INFORMATION TO A JSON FILE
                def get_customer_info():
                    last_name = last_name_entry.get()
                    email = email_entry.get()
                    customer_details['customer'].append(last_name)
                    customer_details['customer'].append(email)
                    save()

                def save():
                    with open('emails.txt', 'w') as handle:
                        handle.write(dumps(customer_details))
                        handle.close()

                # FUNCTION THAT VALIDATES ENTRY INPUT FROM THE USER IN ORDER TO COMPLETE THE ORDER
                # DISPLAYS A MESSAGE WHEN ORDER IS PLACED THAT GENERATES A RANDOM ORDER NUMBER
                def on_click_place_order():
                    first_name = first_name_entry.get()
                    last_name = last_name_entry.get()
                    email = email_entry.get()
                    order_number = random.randint(1, 1000)
                    order_time = random.randint(10, 20)

                    if first_name and last_name and email and (total_label.cget('text') != '$0.00'):
                        messagebox.showinfo('Status',
                                            f'Order Confirmed!\nYour order will be ready in {order_time} minutes. '
                                            f'\n\nORDER NUMBER: {order_number}')
                        get_customer_info()
                    if not first_name and not last_name and not email:
                        messagebox.showwarning('Warning', 'Please fill the required * fields!')

                    elif total_label.cget('text') == '$0.00':
                        messagebox.showwarning('Warning', 'Please add donuts to your order!')



                # CREATES AND PLACES A BUTTON THAT ALLOWS THE USER TO COMPLETE THEIR ORDER AND SEND THEM TO THE ORDER
                # CONFIRMATION WINDOW
                finish_order_button = customtkinter.CTkButton(place_order_window, text='Place Order',
                                                              fg_color='#f06eaa', hover_color='#35fda6',
                                                              command=lambda: on_click_place_order(), font=bold_font,
                                                              text_color_disabled='#BABABA')
                finish_order_button.place(x=300, y=400)

        #
        #
        #
        #
        #   ===================== MAIN WINDOW ======================
        #
        #
        #
        #
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
                                              command=exit_app, font=bold_font)
        exit_button.pack(pady=5)


def main():
    DonutApp().mainloop()


if __name__ == '__main__':
    main()
