from gfxhat import lcd, fonts
from PIL import Image, ImageFont, ImageDraw
from click import getchar

def clearScreen(lcd):
    lcd.clear()
    lcd.show()

def convertToBinary(eightbit):
    list_char_binary_values = []
    for i in range(0,len(eightbit), 2):
        binary_rep = str(bin(int(eightbit[i:i+2], 16))[2:])  #binary representation of character's 8*8-bit representation
        if len(binary_rep) < 8:
            missing_num = 8 - len(binary_rep)
            to_append = missing_num * '0'
            binary_rep = to_append + binary_rep
        list_char_binary_values.append(list(binary_rep))
    return list_char_binary_values

def generateDictionary():
    dict_font = {}
    with open('font3.txt') as txt_font:
        for datum in txt_font.readlines():
            datum = datum.strip('0x\n')
            datum_parts = datum.split(',')
            dict_font[datum_parts[1]] = convertToBinary(datum_parts[0])
    return dict_font
avail_fonts = generateDictionary()

def displayObject(obj, x, y):
    selected_x = x
    for list in obj:
        for i in list:
            lcd.set_pixel(x, y, i)
            x = x + 1
        x = selected_x
        y = y + 1
    lcd.show()

while True:
    print("Your pressed keyboard character:")
    button = getchar()
    if button in avail_fonts.keys():
        print(button)  # Added because my Raspberry Pi is not working
        print(avail_fonts[button])  # Added because my Raspberry Pi is not working
        displayObject(avail_fonts[button], 10, 10)  # Will show the character at the specified position.
    else:
        print("Wrong input.")
