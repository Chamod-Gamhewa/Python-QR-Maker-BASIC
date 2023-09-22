# import libraries
import os
import json
import qrcode
from os.path import exists as path_exists

"""
aliceblue,      antiquewhite,           aqua,               aquamarine,         azure,
beige,          bisque,                 black,              blanchedalmond,     blue,
blueviolet,     brown,                  burlywood,          cadetblue,          chartreuse,
chocolate,      coral,                  cornflowerblue,     cornsilk,           crimson,
cyan,           darkblue,               darkcyan,           darkgoldenrod,      darkgray,
darkgreen,      darkkhaki,              darkmagenta,        darkolivegreen,     darkorange,
darkorchid,     darkred,                darksalmon,         darkseagreen,       darkslateblue,
darkslategray,  darkturquoise,          darkviolet,         deeppink,           deepskyblue,
dimgray,        dodgerblue,             firebrick,          floralwhite,        forestgreen,
fuchsia,        gainsboro,              ghostwhite,         gold,               goldenrod,
gray,           green,                  greenyellow,        honeydew,           hotpink,
indianred,      indigo,                 ivory,              khaki,              lavender,
lavenderblush,  lawngreen,              lemonchiffon,       lightblue,          lightcoral,
lightcyan,      lightgoldenrodyellow,   lightgray,          lightgreen,         lightpink,
lightsalmon,    lightseagreen,          lightskyblue,       lightslategray,     lightsteelblue,
lightyellow,    lime,                   limegreen,          linen,              magenta,
maroon,         mediumaquamarine,       mediumblue,         mediumorchid,       mediumpurple,
mediumseagreen, mediumslateblue,        mediumspringgreen,  mediumturquoise,    mediumvioletred,
midnightblue,   mintcream,              mistyrose,          moccasin,           navajowhite,
navy,           oldlace,                olive,              olivedrab,          orange,
orangered,      orchid,                 palegoldenrod,      palegreen,          paleturquoise,
palevioletred,  papayawhip,             peachpuff,          peru,               pink,
plum,           powderblue,             purple,             rebeccapurple,      red,
rosybrown,      royalblue,              saddlebrown,        salmon,             sandybrown,
seagreen,       seashell,               sienna,             silver,             skyblue,
slateblue,      slategray,              snow,               springgreen,        steelblue,
tan,            teal,                   thistle,            tomato,             turquoise,
violet,         wheat,                  white,              whitesmoke,         yellow,
yellowgreen
"""

if not path_exists("Generated QRs"):
    os.mkdir("Generated QRs")
if not path_exists("config.json"):
    base_data= str('''{
    "qr_forground": "black",
    "qr_background": "white",
    "box_size": 10,
    "border": 10
}''')
    with open("config.json", "w") as config:
        config.write(base_data)
    config.close()
if not path_exists("details.txt"):
    with open("details.txt", "w") as f:
        f.write("")
    f.close()

with open("config.json") as config_json:
    json_data= json.loads(config_json.read())
    qr_forground= json_data["qr_forground"]
    qr_background= json_data["qr_background"]
    qr_box_size= json_data["box_size"]
    qr_border= json_data["border"]

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=qr_box_size,
    border=qr_border
)

def single(user_input):
    qr.add_data(user_input.strip())
    qr.make(
        fit= True
    )
    img= qr.make_image(
        fill_color= qr_forground,
        back_color= qr_background
    )
    try:
        img.save(f"Generated QRs/{user_input}.png")
        print(f" > QR created for: {user_input}")
    except:
        print(f" > Failed to create QR file: {user_input}")

def bulk():
    with open("details.txt", "r") as bulk_text:
        bulk_text_lines = bulk_text.readlines()

    for line in bulk_text_lines:
        line = line.strip()
        qr.add_data(line)
        qr.make(fit=True)
        img = qr.make_image(
            fill_color=qr_forground,
            back_color=qr_background
        )

        try:
            img.save(f"Generated QRs/{line}.png")
            print(f"> QR created for: {line}")
        except Exception as e:
            print(f"> Failed to create QR file for {line}: {str(e)}")

if __name__ == "__main__":
    user_choice= int(input("""
1. Single QR Create
2. Bulk QR Create

Enter choice (1/2): """))

    if user_choice==1:
        user_input= input("Enter detail for the QR: ")
        single(user_input)
    elif user_choice==2:
        print("Fill details.txt with qr details!")
        bulk()
    else:
        print("Invalid input!")