#class Mobile:
#     __color = 'red'
#     ram = 4
#     storage = 32
#     model = 'Xiaomi'
#
#     def change_ram(self,new_ram):
#         self.ram = new_ram
#
#     def change_color(self,new_color):
#         self.__color = new_color
#
#     def change_storage(self,new_storage):
#         self.storage = new_storage
#
#     @property
#     def color(self): #getter
#         return self.__color
#
#     @color.setter
#     def color(self,new_color):
#
#
#
#
# mi11 = Mobile()
# print(mi11.ram)
# print(mi11.color)


#_________________________________________
#
# class Mobile:
#     __color = 'Black'
#     imei = 123112313
#     model = 'IPhone X'
#     cpu = 'Avalanche'
#     def change_color(self, new_color):
#         self.color = new_color
#
#     def change_imei(self, new_imei):
#         self.imei = new_imei
#
#     @property
#     def color(self):#getter
#         return self.__color
#
#     @color.setter
#     def color(self,new_color):
#         if new_color in ['Black','White','Pink']:
#             self.__color = new_color
#
#     @color.deleter
#     def color(self):
#         self.__color = 'metal'
#
# iphone14 = Mobile()
# print(iphone14.color)
# iphone14.color = 'Green'
# print(iphone14.color)
# iphone14.color = 'White'
# print(iphone14.color)
# del iphone14.color

class Site():
    __url = 'www.google.com'

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self,new_url):
        if new_url not in ['http://' , 'https://']:
            self.__url = 'http://' + new_url

web = Site()
print(web.url)
web.url = 'www.youtube.com'
print(web.url)
web.url = 'www.python.com'
print(web.url)

