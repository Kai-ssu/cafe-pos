import pandas as pd
import flet
from flet import (
    Column,
    ElevatedButton,
    FloatingActionButton,
    Checkbox,
    IconButton,
    Page,
    Row,
    colors,
    TextField,
    UserControl,
    icons,
    Text,
    MainAxisAlignment,
    AppView,
    ThemeMode,
    ScrollMode,
    AppBar,
    FontWeight,
    ScrollMode,
    alignment,
    MaterialState
)




class Order(UserControl):
    def __init__(self, order_name, order_price, order_qty, order_total, order_delete):
        super().__init__()
        self.order_name = order_name
        self.order_price = order_price
        self.order_qty = order_qty
        self.order_total = order_total
        self.order_delete = order_delete

    def build(self):
        self.display_order = Text(
            value=self.order_name
        )

        self.disply_qty = Text(value=self.order_qty)
        self.display_price = Text(value=self.order_price)
        self.display_total = Text(value=self.order_total)

        self.display_view = Column(
            controls=[
                Row(
                    alignment="start",
                    vertical_alignment="center",
                    controls=[
                        self.display_order,
                        self.disply_qty,
                        self.display_price,
                        self.display_total,
                        Row(
                            spacing=0,
                            controls=[
                                IconButton(
                                    icons.DELETE_OUTLINE,
                                    tooltip="Delete Order",
                                    on_click=self.delete_clicked,
                                )
                            ],
                        ),
                    ],
                )
            ],
            auto_scroll=True,
            scroll=ScrollMode.HIDDEN,
        )

        return Column(controls=[self.display_view])
  
        
    def delete_clicked(self, e):
        self.order_delete(self)


class OrderApp(UserControl):
    
    def build(self):        
        self.new_order = TextField()
        self.new_order_price = Text(value="0")  
        self.new_order_qty = TextField(value="1", width=50)
        self.new_order_total = Text(value="0")
        self.new_order_size = ""
        self.new_order_temp = ""
    
        self.orders = Column(
            spacing=5,
            height=200,
            width=300,
            scroll= ScrollMode.ALWAYS
        )
        self.pay_total = Text(value="0", size=20, color='#3B2621')
        self.change = Text(value="0", size=20, color='#3B2621')
        self.received = Text(value="0", size=20, color='#3B2621')
        self.to_receive = TextField(label="Amount received", width=100)
        self.customer_name = TextField(label="Customer Name", width=150)
        self.item = Text(value="")

        self.pay = []
        self.order_list = []
        self.order_list_qty = []
        self.prev_order_list= Column(
            spacing=5,
            height=520,
            width=200,
            scroll= ScrollMode.ALWAYS
        )

        #self.prev_order = 
        
        self.prev_order = TextField(label="")

        self.completed = True
        


        self.ame_button = ElevatedButton(
            text="Americano", 
            width=125, height=200, 
            on_click=self.ame_clicked, 
            bgcolor='#895B4A',
            color=colors.WHITE
        )

        self.capp_button = ElevatedButton(
            text="Cappuccino", 
            width=125, height=200, 
            on_click=self.capp_clicked,
            bgcolor='#895B4A',
            color=colors.WHITE
        )
        
        self.latt_button = ElevatedButton(
            text="CafeLatte", 
            width=125, height=200, 
            on_click=self.latt_clicked,
            bgcolor='#895B4A',
            color=colors.WHITE
        )

        self.splatt_button = ElevatedButton(
            text="SpLatte", 
            width=125, height=200, 
            on_click=self.splatt_clicked,
            bgcolor='#895B4A',
            color=colors.WHITE
        )

        self.matcha_button = ElevatedButton(
            text="Matcha", 
            width=125, height=200, 
            on_click=self.matcha_clicked,
            bgcolor='#895B4A',
            color=colors.WHITE
        )

        self.choco_button = ElevatedButton(
            text="Chocolate", 
            width=125, height=200, 
            on_click=self.choco_clicked,
            bgcolor='#895B4A',
            color=colors.WHITE
        )

        self.reg_button = ElevatedButton(
            text="Reg", 
            width=125, height=100, 
            on_click=self.reg_clicked,
            bgcolor='#895B4A',
            color=colors.WHITE,
            disabled=True
        )

        self.lrg_button = ElevatedButton(
            text="Lrg", 
            width=125, height=100, 
            on_click=self.lrg_clicked,
            bgcolor='#895B4A',
            color=colors.WHITE,
            disabled=True
        )

        self.iced_button = ElevatedButton(
            text="Iced", 
            width=125, height=100, 
            on_click=self.iced_clicked,
            bgcolor='#895B4A',
            color=colors.WHITE,
            disabled=True
        )

        self.ok_button = FloatingActionButton(
            icon=icons.ADD,
            on_click=self.ok_clicked,
            bgcolor='#3B2621',
            width=200,
            disabled=True
        )

        self.next_order = ElevatedButton(
            text="Next Order", 
            width=260, height=50, 
            on_click=self.next_clicked,
            bgcolor='#895B4A',
            color=colors.WHITE,
            disabled=True
        )

        # application's root control (i.e. "view") containing all other controls
        return Column(
                alignment= alignment.center,
                controls=[#C1-R1
                    Row(
                        controls=[
                            #C1-R1-C1
                            Column(
                                #width=700, height=700,
                                alignment= MainAxisAlignment.START,
                                controls=[
                                    #C1-R1-C1-R1 - Americano, Cappuccino, Latte
                                    Row(
                                        controls=[
                                            self.ame_button,
                                            self.capp_button,
                                            self.latt_button
                                        ],
                                        #width=300
                                    ),
                                    Row(
                                        controls=[
                                            self.splatt_button,
                                            self.matcha_button,
                                            self.choco_button
                                        ]
                                    ),
                                    Row(
                                        controls=[
                                            self.reg_button,
                                            self.lrg_button,
                                            self.iced_button
                                        ]
                                    ),
                                    Row(
                                        controls=[
                                            IconButton(
                                                icon=icons.REMOVE,
                                                on_click=self.minus_clicked,
                                                bgcolor='#9F8C86'
                                            ),
                                            self.new_order_qty,
                                            IconButton(
                                                icon=icons.ADD,
                                                on_click=self.plus_clicked,
                                                bgcolor='#9F8C86'
                                            ),
                                            self.ok_button,
                                        ],
                                        alignment= MainAxisAlignment.START
                                    )
                                ]
                            ),
                            Column(
                                alignment= MainAxisAlignment.START,
                                controls=[
                                    
                                    Row(
                                        controls=[
                                            Text(value="ORDER:", weight="bold", size=30, color='#3B2621'),
                                            self.customer_name,
                                        ]
                                    ),
                                    self.orders,
                                    Text(value="TOTAL: ", weight="bold", color='#3B2621'), self.pay_total,
                                    Text(value="RECEIVED: ", weight="bold", color='#3B2621'),self.received,
                                    Text(value="CHANGE: ", weight="bold", color='#3B2621'),self.change,
                                    Row(
                                        controls=[
                                            self.to_receive,
                                            ElevatedButton(
                                                text="Pay",
                                                width=150, height=50,
                                                on_click=self.pay_clicked,
                                                bgcolor='#3B2621',
                                                color=colors.WHITE
                                            )
                                        ]
                                    ),
                                    self.next_order
                                ] 
                            ),
                            Column(
                                alignment= MainAxisAlignment.START,
                                controls=[
                                    Text(value="Previous orders", weight="bold", size=30, color='#3B2621'),
                                    Row(
                                        controls=[
                                            self.prev_order_list,
                                        ]
                                    )
                                ]
                            )
                        ]
                    ),
                ]
            )

    def status_changed(self, e):
        self.itemlist.value = self.completed
        self.update()

    def order_delete(self, order):
        self.pay.remove(int(order.order_total))
        self.total = sum(self.pay)
        self.pay_total.value = str(self.total)
        self.orders.controls.remove(order)
        orders_qty = order.order_name + order.order_qty
        self.order_list_qty.remove(orders_qty)
        self.update()

    def update(self):
        if self.new_order.value != "" and self.new_order_size != "" :
            self.ok_button.disabled = False
        else:
            self.ok_button.disabled = True
        
        for item in self.prev_order_list.controls:
            if self.itemlist.value == True:
                self.prev_order_list.controls.remove(item)
                self.itemlist.value = False
        super().update()

    def ok_clicked(self, e):        
        self.new_order_total.value = str(int(self.new_order_price.value) * int(self.new_order_qty.value))
        self.new_order_qty.value = self.new_order_qty.value + "x"
        self.pay.append(int(self.new_order_total.value))
        self.total = sum(self.pay)
        self.pay_total.value = str(self.total)
        
        order = Order(
            self.new_order.value,
            self.new_order_price.value,
            self.new_order_qty.value,
            self.new_order_total.value, 
            self.order_delete)
        
        orders = self.new_order.value + self.new_order_qty.value + self.new_order_price.value + " " + self.new_order_total.value
        orders_qty = self.new_order.value + self.new_order_qty.value

        self.order_list.append(orders)
        self.order_list_qty.append(orders_qty)
        self.orders.controls.append(order)

        self.ame_button.disabled = False
        self.capp_button.disabled = False
        self.latt_button.disabled = False
        self.splatt_button.disabled = False
        self.matcha_button.disabled = False
        self.choco_button.disabled = False

        self.reg_button.disabled = True
        self.lrg_button.disabled = True
        self.iced_button.disabled = True

        self.ame_button.bgcolor = '#895B4A'
        self.capp_button.bgcolor = '#895B4A'
        self.latt_button.bgcolor = '#895B4A'
        self.splatt_button.bgcolor = '#895B4A'
        self.matcha_button.bgcolor = '#895B4A'
        self.choco_button.bgcolor = '#895B4A'
        
        self.reg_button.bgcolor = '#895B4A'
        self.lrg_button.bgcolor = '#895B4A'
        self.iced_button.bgcolor = '#895B4A'

        self.new_order.value = ""
        self.new_order_price.value = "0"
        self.new_order_qty.value = "1"
        
        self.update()

        

    def reg_clicked(self, e):
        self.lrg_button.disabled = True
        self.new_order.value = self.new_order.value + "Reg"
        

        if self.new_order_size == "Reg" and self.lrg_button.disabled == True:
            self.lrg_button.disabled = False
            self.new_order.value = self.new_order.value.replace("Reg", "")
            self.new_order_size = ""
            self.reg_button.bgcolor = '#895B4A'

        else:
            self.reg_button.bgcolor = colors.ORANGE
            self.new_order_size = "Reg"
            self.update()
        
        self.update()

    def lrg_clicked(self, e):
        self.reg_button.disabled = True
        self.new_order.value = self.new_order.value + "Lrg"
        self.new_order_price.value = str(int(self.new_order_price.value) + 10)

        if self.new_order_size == "Lrg" and self.reg_button.disabled == True:
            self.reg_button.disabled = False
            self.new_order_size = ""
            self.new_order_price.value = str(int(self.new_order_price.value) - 10)
            self.new_order.value = self.new_order.value.replace("Lrg", "")
            self.lrg_button.bgcolor = '#895B4A'
        else:
            self.lrg_button.bgcolor = colors.ORANGE
            self.new_order_size = "Lrg"
            self.update()

        self.update()
        
    def iced_clicked(self,e):        
        if self.new_order_temp == "Iced":
            self.new_order.value = self.new_order.value.replace("Iced", "")
            self.new_order_price.value = str(int(self.new_order_price.value) - 5)
            self.iced_button.bgcolor = '#895B4A'
            self.new_order_temp = ""
        else:
            self.iced_button.bgcolor = colors.ORANGE
            self.new_order_temp = "Iced"
            self.new_order.value = "Iced" + self.new_order.value
            self.new_order_price.value = str(int(self.new_order_price.value) + 5)
        self.update()
        
    def minus_clicked(self, e):
        self.new_order_qty.value = str(int(self.new_order_qty.value) - 1)
        if self.new_order_qty.value >= "0":
            self.new_order_qty.value = "1"
        self.update()

    def plus_clicked(self, e):
        self.new_order_qty.value = str(int(self.new_order_qty.value) + 1)
        self.update()

    def pay_clicked(self, e):
        self.received.value = self.to_receive.value
        self.change.value = str(int(self.received.value) - int(self.pay_total.value))
        
        self.next_order.disabled = False

        #records orders in order summary.csv
        data = open('order-summary.csv', 'a')
        data.write("\n")
        data.write(','.join([str(pd.Timestamp.now()), str(self.order_list_qty), self.pay_total.value, self.received.value, self.change.value, self.customer_name.value]))
        data.close()

        self.update()

    def next_clicked(self, e):
        self.prev_order.value = "\n".join(map(str, self.order_list_qty))
        self.item.value = self.customer_name.value.upper() + "\n" + self.prev_order.value
        self.itemlist = Checkbox(value=False, label=self.item.value, on_change=self.status_changed)
        self.prev_order_list.controls.append(self.itemlist)
        self.order_list.clear()
        self.pay.clear()
        self.order_list_qty.clear()
        self.pay_total.value = "0"
        self.to_receive.value = ""
        self.received.value = "0"
        self.change.value = "0"
        self.customer_name.value = ""
        self.orders.controls.clear()
        #self.item.value = ""
        self.next_order.disabled = True
        self.ok_button.disabled = True
        self.update()

    def ame_clicked(self, e):
        if self.new_order.value == "Americano" and self.capp_button.disabled == True:
            self.capp_button.disabled = False
            self.latt_button.disabled = False
            self.splatt_button.disabled = False
            self.matcha_button.disabled = False
            self.choco_button.disabled = False

            self.reg_button.disabled = True
            self.lrg_button.disabled = True
            self.iced_button.disabled = True

            self.ame_button.bgcolor = '#895B4A'

        else:
            self.ame_button.bgcolor = colors.ORANGE

            self.capp_button.disabled = True
            self.latt_button.disabled = True
            self.splatt_button.disabled = True
            self.matcha_button.disabled = True
            self.choco_button.disabled = True

            self.reg_button.disabled = False
            self.lrg_button.disabled = False
            self.iced_button.disabled = False


        self.new_order.value = "Americano"
        self.new_order_price.value = "100"
        self.update()

    def capp_clicked(self, e):
        if self.new_order.value == "Cappuccino" and self.ame_button.disabled == True:
            self.ame_button.disabled = False
            self.latt_button.disabled = False
            self.splatt_button.disabled = False
            self.matcha_button.disabled = False
            self.choco_button.disabled = False
            
            self.reg_button.disabled = True
            self.lrg_button.disabled = True
            self.iced_button.disabled = True

            self.capp_button.bgcolor = '#895B4A'
            
        else:
            self.capp_button.bgcolor = colors.ORANGE

            self.ame_button.disabled = True
            self.latt_button.disabled = True
            self.splatt_button.disabled = True
            self.matcha_button.disabled = True
            self.choco_button.disabled = True
            
            self.reg_button.disabled = False
            self.lrg_button.disabled = False
            self.iced_button.disabled = False

        self.new_order.value = "Cappuccino"
        self.new_order_price.value = "110"      
        self.update()

    def latt_clicked(self, e):
        if self.new_order.value == "CafeLatte" and self.ame_button.disabled == True:
            self.ame_button.disabled = False
            self.capp_button.disabled = False
            self.splatt_button.disabled = False
            self.matcha_button.disabled = False
            self.choco_button.disabled = False
            
            self.reg_button.disabled = True
            self.lrg_button.disabled = True
            self.iced_button.disabled = True

            self.latt_button.bgcolor = '#895B4A'
            
        else:
            self.latt_button.bgcolor = colors.ORANGE

            self.capp_button.disabled = True
            self.ame_button.disabled = True
            self.splatt_button.disabled = True
            self.matcha_button.disabled = True
            self.choco_button.disabled = True
            
            self.reg_button.disabled = False
            self.lrg_button.disabled = False
            self.iced_button.disabled = False

        self.new_order.value = "CafeLatte"
        self.new_order_price.value = "110"      
        self.update()

    def splatt_clicked(self, e):
        if self.new_order.value == "SpLatte" and self.ame_button.disabled == True:
            self.ame_button.disabled = False
            self.capp_button.disabled = False
            self.latt_button.disabled = False
            self.matcha_button.disabled = False
            self.choco_button.disabled = False
            
            self.reg_button.disabled = True
            self.lrg_button.disabled = True
            self.iced_button.disabled = True

            self.splatt_button.bgcolor = '#895B4A'

        else:
            self.splatt_button.bgcolor = colors.ORANGE

            self.capp_button.disabled = True
            self.latt_button.disabled = True
            self.ame_button.disabled = True
            self.matcha_button.disabled = True
            self.choco_button.disabled = True
            
            self.reg_button.disabled = False
            self.lrg_button.disabled = False
            self.iced_button.disabled = False

        self.new_order.value = "SpLatte"
        self.new_order_price.value = "120"      
        self.update()
        
    def matcha_clicked(self, e):
        if self.new_order.value == "Matcha" and self.ame_button.disabled == True:
            self.ame_button.disabled = False
            self.capp_button.disabled = False
            self.latt_button.disabled = False
            self.splatt_button.disabled = False
            self.choco_button.disabled = False
            
            self.reg_button.disabled = True
            self.lrg_button.disabled = True
            self.iced_button.disabled = True

            self.matcha_button.bgcolor = '#895B4A'
        
        else:
            self.matcha_button.bgcolor = colors.ORANGE

            self.capp_button.disabled = True
            self.latt_button.disabled = True
            self.splatt_button.disabled = True
            self.ame_button.disabled = True
            self.choco_button.disabled = True
            
            self.reg_button.disabled = False
            self.lrg_button.disabled = False
            self.iced_button.disabled = False

        self.new_order.value = "Matcha"
        self.new_order_price.value = "120"      
        self.update()

    def choco_clicked(self, e):
        if self.new_order.value == "Chocolate" and self.ame_button.disabled == True:
            self.ame_button.disabled = False
            self.capp_button.disabled = False
            self.latt_button.disabled = False
            self.splatt_button.disabled = False
            self.matcha_button.disabled = False
            
            self.reg_button.disabled = True
            self.lrg_button.disabled = True
            self.iced_button.disabled = True

            self.choco_button.bgcolor = '#895B4A'
        
        else:
            self.choco_button.bgcolor = colors.ORANGE

            self.capp_button.disabled = True
            self.latt_button.disabled = True
            self.splatt_button.disabled = True
            self.matcha_button.disabled = True
            self.ame_button.disabled = True
            
            self.reg_button.disabled = False
            self.lrg_button.disabled = False
            self.iced_button.disabled = False

        self.new_order.value = "Chocolate"
        self.new_order_price.value = "120"      
        self.update()
        

def main(page: Page):
    page.title = "XKP POS"
    page.theme_mode = ThemeMode.LIGHT
    page.bgcolor = '#DACCBA'
    #page.auto_scroll=False
    #page.scroll = ScrollMode.HIDDEN
    page.appbar = AppBar(
        title=Text(
            "XKP Cafe", 
            weight=FontWeight.BOLD,
            color= colors.WHITE
        ),
        bgcolor= colors.BROWN,
        center_title=True,
    )

    page.horizontal_alignment = "center"
    page.vertical_alignment = "start"

    page.update()

    # create application instance
    app = OrderApp()

    page.add(app)


#flet.app(target=main)

import os

DEFAULT_FLET_PATH = ''  # or 'ui/path'
DEFAULT_FLET_PORT = 8000

# flet.app(port=8000, target=main, view=AppView.WEB_BROWSER)
flet_path = os.getenv("FLET_PATH", DEFAULT_FLET_PATH)
flet_port = int(os.getenv("FLET_PORT", DEFAULT_FLET_PORT))
flet.app(name=flet_path, target=main, view=None, port=flet_port)