import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "onePieceTCG.settings")
django.setup()

from catalog.models import Producto, Type, Images, Idioma, Moneda

tipos = ["STARTER DECK", "BOOSTER PACK"]
for tipo in tipos:
    tipo_obj, created = Type.objects.get_or_create(type=tipo)
    if created:
        print(f"Tipo {tipo_obj.type} agregado a la base de datos.")
    else:
        print(f"Tipo {tipo_obj.type} ya existe en la base de datos.")

imagenes = [
    "https://m.media-amazon.com/images/I/612Tn48L90L._AC_SL1200_.jpg",
    "https://m.media-amazon.com/images/I/611-iR6cfpL._AC_SL1200_.jpg",
    "https://m.media-amazon.com/images/I/61Ztrh6aFuL._AC_SL1200_.jpg",
    "https://m.media-amazon.com/images/I/71ksCUbPIuL._AC_SL1200_.jpg",
    "https://m.media-amazon.com/images/I/81UG8MAcmeL._AC_SL1500_.jpg",
    "https://m.media-amazon.com/images/I/61w12MF71yL._AC_SL1000_.jpg",
    "https://m.media-amazon.com/images/I/715t8fd83LL._AC_SL1500_.jpg",
    "https://m.media-amazon.com/images/I/81fNYpxI1pL._AC_SL1500_.jpg",
    "https://m.media-amazon.com/images/I/81muMg7eGeL._AC_SL1500_.jpg",
    "https://m.media-amazon.com/images/I/81ZIvaR-uPL._AC_SL1500_.jpg",
    "https://m.media-amazon.com/images/I/718n-IGcYdL._AC_SL1500_.jpg",
    "https://m.media-amazon.com/images/I/81qcks9pL4L._AC_SL1500_.jpg",
    "https://m.media-amazon.com/images/I/91E45IrnyDL._AC_SL1500_.jpg",
    "https://m.media-amazon.com/images/I/81pEhtjSSVL._AC_SL1500_.jpg",
    "https://m.media-amazon.com/images/I/91Agw8ffdUL._AC_SL1500_.jpg",
    "https://carduniverse.cl/cdn/shop/files/DoublePackSetVol.3_DP-03_2_600x.png?v=1698620478",
    "https://carduniverse.cl/cdn/shop/files/WingsoftheCaptainpng_600x.png?v=1698620241",
    "https://m.media-amazon.com/images/I/61AZext6huL._AC_.jpg",
    "https://m.media-amazon.com/images/I/61UwkNeROvL._AC_SL1200_.jpg",
    "https://m.media-amazon.com/images/I/61SgFEw2SUL._AC_.jpg",
    "https://m.media-amazon.com/images/I/71qvgIHlPcL._AC_SL1500_.jpg",
    "https://m.media-amazon.com/images/I/51G78ZwYgFL._AC_.jpg",
    "https://m.media-amazon.com/images/I/61MdqVLDEdL._AC_SL1309_.jpg",
    "https://dojiw2m9tvv09.cloudfront.net/29535/product/X_display-op0470111804.jpg?57&time=1700761976.jpg",
    "https://progaming.cl/wp-content/uploads/2023/09/one-piece-1-1bedba2c-0b01-4660-8f88-f4c26374cb85.jpg"
]

for imagen in imagenes:
    imagen_obj, created = Images.objects.get_or_create(image=imagen)
    if created:
        print(f"Imagen {imagen_obj.image} agregada a la base de datos.")
    else:
        print(f"Imagen {imagen_obj.image} ya existe en la base de datos.")

idiomas = ["INGLES", "JAPONES"]
for idioma in idiomas:
    idioma_obj, created = Idioma.objects.get_or_create(idioma=idioma)
    if created:
        print(f"Idioma {idioma_obj.idioma} agregado a la base de datos.")
    else:
        print(f"Idioma {idioma_obj.idioma} ya existe en la base de datos.")

monedas = ["USD", "JPY", "CLP"]
for moneda in monedas:
    moneda_obj, created = Moneda.objects.get_or_create(moneda=moneda)
    if created:
        print(f"Tipo {moneda_obj.moneda} agregado a la base de datos.")
    else:
        print(f"Tipo {moneda_obj.moneda} ya existe en la base de datos.")

productos_data = [
    {"nombre": "MAZO SH LUFFY (ST-01)", "precio": 37.57, "idioma": Idioma.objects.get(idioma="INGLES"),
     "descripcion": "",
     "url": "https://www.amazon.com/-/es/TCG-una-pieza-Sombrero-Starter/dp/B0BNLQ6QX4/ref=sr_1_4?__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2MEAQZU1QT7WL&keywords=One+Piece+TCG&qid=1698619615&sprefix=one+piece+tc%2Caps%2C198&sr=8-4",
     "type": Type.objects.get(type="STARTER DECK"),
     "image": Images.objects.get(image="https://m.media-amazon.com/images/I/612Tn48L90L._AC_SL1200_.jpg"),
     "moneda": Moneda.objects.get(moneda="USD"),
     "set": "",
     "color": "RED"},

    {"nombre": "MAZO KIDD (ST-02)", "precio": 42.61, "idioma": Idioma.objects.get(idioma="INGLES"),
     "descripcion": "",
     "url": "https://www.amazon.com/-/es/TCG-una-pieza-Baraja-generaci%C3%B3n/dp/B0BNLKF4QT/ref=sr_1_3?__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2MEAQZU1QT7WL&keywords=One+Piece+TCG&qid=1698619615&sprefix=one+piece+tc%2Caps%2C198&sr=8-3",
     "type": Type.objects.get(type="STARTER DECK"),
     "image": Images.objects.get(image="https://m.media-amazon.com/images/I/611-iR6cfpL._AC_SL1200_.jpg"),
     "moneda": Moneda.objects.get(moneda="USD"),
     "set": "",
     "color": "GREEN"},

    {"nombre": "MAZO CROCODILE (ST-03)", "precio": 40.12, "idioma": Idioma.objects.get(idioma="INGLES"),
     "descripcion": "",
     "url": "https://www.amazon.com/-/es/One-Piece-TCG-Cubierta-Iniciaci%C3%B3n/dp/B0BNLKVHY8/ref=sr_1_7?__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2MEAQZU1QT7WL&keywords=One+Piece+TCG&qid=1698619615&sprefix=one+piece+tc%2Caps%2C198&sr=8-7",
     "type": Type.objects.get(type="STARTER DECK"),
     "image": Images.objects.get(image="https://m.media-amazon.com/images/I/61Ztrh6aFuL._AC_SL1200_.jpg"),
     "moneda": Moneda.objects.get(moneda="USD"),
     "set": "",
     "color": "BLUE"},

    {"nombre": "MAZO ONE PIECE RED (ST-05)", "precio": 53.61, "idioma": Idioma.objects.get(idioma="INGLES"),
     "descripcion": "",
     "url": "https://www.amazon.com/-/es/BANDAI-NAMCO-Entertainment-Cubierta-inicio/dp/B0BTKKKRJ7/ref=sr_1_5?__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2MEAQZU1QT7WL&keywords=One+Piece+TCG&qid=1698619615&sprefix=one+piece+tc%2Caps%2C198&sr=8-5",
     "type": Type.objects.get(type="STARTER DECK"),
     "image": Images.objects.get(image="https://m.media-amazon.com/images/I/71ksCUbPIuL._AC_SL1200_.jpg"),
     "moneda": Moneda.objects.get(moneda="USD"),
     "set": "",
     "color": "PURPLE"},

    {"nombre": "MAZO BIG MOM (ST-07)", "precio": 32.00, "idioma": Idioma.objects.get(idioma="INGLES"),
     "descripcion": "",
     "url": "https://www.amazon.com/-/es/One-Piece-TCG-Pirates-BCL2677501/dp/B0C7VKY132/ref=sr_1_29?__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2MEAQZU1QT7WL&keywords=One+Piece+TCG&qid=1698619615&sprefix=one+piece+tc%2Caps%2C198&sr=8-29",
     "type": Type.objects.get(type="STARTER DECK"),
     "image": Images.objects.get(image="https://m.media-amazon.com/images/I/81UG8MAcmeL._AC_SL1500_.jpg"),
     "moneda": Moneda.objects.get(moneda="USD"),
     "set": "",
     "color": "YELLOW"},

    {"nombre": "MAZO LUFFY (ST-08)", "precio": 27.45, "idioma": Idioma.objects.get(idioma="INGLES"), "descripcion": "",
     "url": "https://www.amazon.com/-/es/One-Piece-TCG-Monkey-D-Luffy-Starter/dp/B0C7VFJ8LB/ref=sr_1_6?__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2MEAQZU1QT7WL&keywords=One+Piece+TCG&qid=1698619615&sprefix=one+piece+tc%2Caps%2C198&sr=8-6",
     "type": Type.objects.get(type="STARTER DECK"),
     "image": Images.objects.get(image="https://m.media-amazon.com/images/I/61w12MF71yL._AC_SL1000_.jpg"),
     "moneda": Moneda.objects.get(moneda="USD"),
     "set": "",
     "color": "BLACK"},

    {"nombre": "MAZO YAMATO (ST-09)", "precio": 32.43, "idioma": Idioma.objects.get(idioma="INGLES"), "descripcion": "",
     "url": "https://www.amazon.com/-/es/One-Piece-TCG-Cubierta-inicio/dp/B0C7VGHF3J/ref=sr_1_48?__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2MEAQZU1QT7WL&keywords=One+Piece+TCG&qid=1698619615&sprefix=one+piece+tc%2Caps%2C198&sr=8-48",
     "type": Type.objects.get(type="STARTER DECK"),
     "image": Images.objects.get(image="https://m.media-amazon.com/images/I/715t8fd83LL._AC_SL1500_.jpg"),
     "moneda": Moneda.objects.get(moneda="USD"),
     "set": "",
     "color": "YELLOW"},

    {"nombre": "MAZO SH LUFFY (ST-01)", "precio": 25.56, "idioma": Idioma.objects.get(idioma="JAPONES"),
     "descripcion": "",
     "url": "https://www.amazon.com/-/es/BANDAI-One-Piece-TCG-Sombrero/dp/B09VKTBKMS/ref=sr_1_19?__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2MEAQZU1QT7WL&keywords=One+Piece+TCG&qid=1698619615&sprefix=one+piece+tc%2Caps%2C198&sr=8-19",
     "type": Type.objects.get(type="STARTER DECK"),
     "image": Images.objects.get(image="https://m.media-amazon.com/images/I/612Tn48L90L._AC_SL1200_.jpg"),
     "moneda": Moneda.objects.get(moneda="USD"),
     "set": "",
     "color": "RED"},

    {"nombre": "MAZO KIDD (ST-02)", "precio": 24.48, "idioma": Idioma.objects.get(idioma="JAPONES"),
     "descripcion": "",
     "url": "https://www.amazon.com/-/es/BANDAI-One-Piece-TCG-generaci%C3%B3n/dp/B09VKVFQMD/ref=sr_1_45?__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2MEAQZU1QT7WL&keywords=One+Piece+TCG&qid=1698619615&sprefix=one+piece+tc%2Caps%2C198&sr=8-45",
     "type": Type.objects.get(type="STARTER DECK"),
     "image": Images.objects.get(image="https://m.media-amazon.com/images/I/611-iR6cfpL._AC_SL1200_.jpg"),
     "moneda": Moneda.objects.get(moneda="USD"),
     "set": "",
     "color": "GREEN"},

    {"nombre": "MAZO CROCODILE (ST-03)", "precio": 24.42, "idioma": Idioma.objects.get(idioma="JAPONES"),
     "descripcion": "",
     "url": "https://www.amazon.com/-/es/BANDAI-One-Piece-TCG-Cubierta/dp/B09VKX8N65/ref=sr_1_20?__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2MEAQZU1QT7WL&keywords=One+Piece+TCG&qid=1698619615&sprefix=one+piece+tc%2Caps%2C198&sr=8-20",
     "type": Type.objects.get(type="STARTER DECK"),
     "image": Images.objects.get(image="https://m.media-amazon.com/images/I/61Ztrh6aFuL._AC_SL1200_.jpg"),
     "moneda": Moneda.objects.get(moneda="USD"),
     "set": "",
     "color": "BLUE"},

    {"nombre": "MAZO KAIDO (ST-04)", "precio": 27.56, "idioma": Idioma.objects.get(idioma="JAPONES"), "descripcion": "",
     "url": "https://www.amazon.com/-/es/BANDAI-Cubierta-iniciaci%C3%B3n-piratas-japon%C3%A9s/dp/B09VKWZJWZ/ref=sr_1_12?__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2MEAQZU1QT7WL&keywords=One+Piece+TCG&qid=1698619615&sprefix=one+piece+tc%2Caps%2C198&sr=8-12",
     "type": Type.objects.get(type="STARTER DECK"),
     "image": Images.objects.get(image="https://m.media-amazon.com/images/I/81fNYpxI1pL._AC_SL1500_.jpg"),
     "moneda": Moneda.objects.get(moneda="USD"),
     "set": "",
     "color": "PURPLE"},

    {"nombre": "MAZO ONE PIECE RED (ST-05)", "precio": 32.31, "idioma": Idioma.objects.get(idioma="JAPONES"),
     "descripcion": "",
     "url": "https://www.amazon.com/-/es/Bandai-One-Piece-Edici%C3%B3n-pel%C3%ADcula/dp/B09VKS64CD/ref=sr_1_50?__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2MEAQZU1QT7WL&keywords=One+Piece+TCG&qid=1698619764&sprefix=one+piece+tc%2Caps%2C198&sr=8-50",
     "type": Type.objects.get(type="STARTER DECK"),
     "image": Images.objects.get(image="https://m.media-amazon.com/images/I/71ksCUbPIuL._AC_SL1200_.jpg"),
     "moneda": Moneda.objects.get(moneda="USD"),
     "set": "",
     "color": "PURPLE"},

    {"nombre": "MAZO BIG MOM (ST-07)", "precio": 23.87, "idioma": Idioma.objects.get(idioma="JAPONES"),
     "descripcion": "",
     "url": "https://www.amazon.com/-/es/BANDAI-NAMCO-Entertainment-One-Piece/dp/B0BKKSYCB4/ref=sr_1_16?__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2MEAQZU1QT7WL&keywords=One+Piece+TCG&qid=1698619615&sprefix=one+piece+tc%2Caps%2C198&sr=8-16",
     "type": Type.objects.get(type="STARTER DECK"),
     "image": Images.objects.get(image="https://m.media-amazon.com/images/I/81UG8MAcmeL._AC_SL1500_.jpg"),
     "moneda": Moneda.objects.get(moneda="USD"),
     "set": "",
     "color": "YELLOW"},

    {"nombre": "MAZO LUFFY (ST-08)", "precio": 22.31, "idioma": Idioma.objects.get(idioma="JAPONES"), "descripcion": "",
     "url": "https://www.amazon.com/-/es/BANDAI-Entertainment-Monkey-%E3%80%90ST-8%E3%80%91-Japon%C3%A9s/dp/B0BNPDYVD8/ref=sr_1_58?__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2MEAQZU1QT7WL&keywords=One+Piece+TCG&qid=1698619615&sprefix=one+piece+tc%2Caps%2C198&sr=8-58",
     "type": Type.objects.get(type="STARTER DECK"),
     "image": Images.objects.get(image="https://m.media-amazon.com/images/I/61w12MF71yL._AC_SL1000_.jpg"),
     "moneda": Moneda.objects.get(moneda="USD"),
     "set": "",
     "color": "BLACK"},

    {"nombre": "MAZO YAMATO (ST-09)",
     "precio": 21.49,
     "idioma": Idioma.objects.get(idioma="JAPONES"),
     "descripcion": "",
     "url": "https://www.amazon.com/-/es/One-Piece-TCG-Cubierta-inicio/dp/B0C7VGHF3J/ref=sr_1_48?__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2MEAQZU1QT7WL&keywords=One+Piece+TCG&qid=1698619615&sprefix=one+piece+tc%2Caps%2C198&sr=8-48",
     "type": Type.objects.get(type="STARTER DECK"),
     "image": Images.objects.get(image="https://m.media-amazon.com/images/I/715t8fd83LL._AC_SL1500_.jpg"),
     "moneda": Moneda.objects.get(moneda="USD"),
     "set": "",
     "color": "YELLOW"},

    {"nombre": "MAZO AKAINU (ST-06)", "precio": 3674, "idioma": Idioma.objects.get(idioma="JAPONES"),
     "descripcion": "",
     "url": "https://www.amazon.co.jp/-/en/BANDAI-ST-06-PIECE-Card-Start/dp/B0B588N7NW/ref=sr_1_26?crid=1Z6AZ7CJIOJ7I&keywords=One+Piece+TCG&qid=1698621165&sprefix=one+piece+tcg%2Caps%2C313&sr=8-26",
     "type": Type.objects.get(type="STARTER DECK"),
     "image": Images.objects.get(image="https://m.media-amazon.com/images/I/81muMg7eGeL._AC_SL1500_.jpg"),
     "moneda": Moneda.objects.get(moneda="JPY"),
     "set": "",
     "color": "BLACK"},

    {"nombre": "MAZO 3 CAPITANES (ST-10)", "precio": 5826, "idioma": Idioma.objects.get(idioma="JAPONES"),
     "descripcion": "",
     "url": "https://www.amazon.co.jp/-/en/BANDAI-ST-10-Ultimate-Captains-Gathering/dp/B0BV136NMY/ref=sr_1_12?crid=1Z6AZ7CJIOJ7I&keywords=One+Piece+TCG&qid=1698621165&sprefix=one+piece+tcg%2Caps%2C313&sr=8-12",
     "type": Type.objects.get(type="STARTER DECK"),
     "image": Images.objects.get(image="https://m.media-amazon.com/images/I/81ZIvaR-uPL._AC_SL1500_.jpg"),
     "moneda": Moneda.objects.get(moneda="JPY"),
     "set": "",
     "color": "RED&PURPLE"},

    {"nombre": "MAZO UTA (ST-11)", "precio": 3992, "idioma": Idioma.objects.get(idioma="JAPONES"),
     "descripcion": "",
     "url": "https://www.amazon.co.jp/-/en/BANDAI-ST-11-PIECE-Card-Start/dp/B0CFX88NSQ/ref=sr_1_10?crid=1Z6AZ7CJIOJ7I&keywords=One+Piece+TCG&qid=1698621165&sprefix=one+piece+tcg%2Caps%2C313&sr=8-10",
     "type": Type.objects.get(type="STARTER DECK"),
     "image": Images.objects.get(image="https://m.media-amazon.com/images/I/718n-IGcYdL._AC_SL1500_.jpg"),
     "moneda": Moneda.objects.get(moneda="JPY"),
     "set": "",
     "color": "GREEN"},

    {"nombre": "MAZO ZORO & SANJI (ST-12)", "precio": 4507, "idioma": Idioma.objects.get(idioma="JAPONES"),
     "descripcion": "",
     "url": "https://www.amazon.co.jp/-/en/BANDAI-ST-12-PIECE-Start-Sanji/dp/B0CFWYBXZZ/ref=sr_1_7?crid=1Z6AZ7CJIOJ7I&keywords=One+Piece+TCG&qid=1698621165&sprefix=one+piece+tcg%2Caps%2C313&sr=8-7",
     "type": Type.objects.get(type="STARTER DECK"),
     "image": Images.objects.get(image="https://m.media-amazon.com/images/I/81qcks9pL4L._AC_SL1500_.jpg"),
     "moneda": Moneda.objects.get(moneda="JPY"),
     "set": "",
     "color": "GREEN&BLUE"},

    {"nombre": "FAMILY DECK BOX", "precio": 5620, "idioma": Idioma.objects.get(idioma="JAPONES"),
     "descripcion": "",
     "url": "https://www.amazon.co.jp/-/en/BANDAI-PIECE-Card-Game-Family/dp/B0BV13PTNF/ref=sr_1_16?crid=1Z6AZ7CJIOJ7I&keywords=One+Piece+TCG&qid=1698621165&sprefix=one+piece+tcg%2Caps%2C313&sr=8-16",
     "type": Type.objects.get(type="STARTER DECK"),
     "image": Images.objects.get(image="https://m.media-amazon.com/images/I/91E45IrnyDL._AC_SL1500_.jpg"),
     "moneda": Moneda.objects.get(moneda="JPY"),
     "set": "",
     "color": "RED&GREEN&PURPLE"},

    {"nombre": "MAZO YAMATO (ST-09)", "precio": 0, "idioma": Idioma.objects.get(idioma="JAPONES"),
     "descripcion": "",
     "url": "https://www.amazon.com/-/es/BANDAI-Entertainment-Cartas-Cubierta-Japon%C3%A9s/dp/B0BNPFQV8J/ref=sr_1_50?__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=one+piece+tcg&qid=1699303854&sr=8-50",
     "type": Type.objects.get(type="STARTER DECK"),
     "image": Images.objects.get(image="https://m.media-amazon.com/images/I/715t8fd83LL._AC_SL1500_.jpg"),
     "moneda": Moneda.objects.get(moneda="USD"),
     "set": "",
     "color": "YELLOW"},

    {"nombre": "MAZO ONE PIECE RED (ST-05)", "precio": 0, "idioma": Idioma.objects.get(idioma="JAPONES"),
     "descripcion": "",
     "url": "https://www.amazon.com/-/es/Bandai-One-Piece-Edici%C3%B3n-pel%C3%ADcula/dp/B09VKS64CD/ref=sr_1_59?__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=one+piece+tcg&qid=1699303854&sr=8-59",
     "type": Type.objects.get(type="STARTER DECK"),
     "image": Images.objects.get(image="https://m.media-amazon.com/images/I/71ksCUbPIuL._AC_SL1200_.jpg"),
     "moneda": Moneda.objects.get(moneda="USD"),
     "set": "",
     "color": "PURPLE"},

    {"nombre": "MAZO CROCODILE (ST-03)", "precio": 0, "idioma": Idioma.objects.get(idioma="JAPONES"),
     "descripcion": "",
     "url": "https://www.amazon.co.jp/-/en/BANDAI-ST-03-PIECE-Start-Nanabuumi/dp/B09VKX8N65/ref=sr_1_47?crid=3NE2ILLSLWGU8&keywords=one+piece+tcg&qid=1699304092&sprefix=%2Caps%2C565&sr=8-47",
     "type": Type.objects.get(type="STARTER DECK"),
     "image": Images.objects.get(image="https://m.media-amazon.com/images/I/61Ztrh6aFuL._AC_SL1200_.jpg"),
     "moneda": Moneda.objects.get(moneda="JPY"),
     "set": "",
     "color": "BLUE"},

    {"nombre": "MAZO LUFFY (ST-08)", "precio": 0, "idioma": Idioma.objects.get(idioma="JAPONES"),
     "descripcion": "",
     "url": "https://www.amazon.co.jp/-/en/BANDAI-ST-8-PIECE-Start-Monkey/dp/B0BNPDYVD8/ref=sr_1_7?crid=28HEMNG197NVP&keywords=one+piece+tcg+Start+Deck&qid=1699304167&sprefix=one+piece+tcg+start+deck%2Caps%2C258&sr=8-7",
     "type": Type.objects.get(type="STARTER DECK"),
     "image": Images.objects.get(image="https://m.media-amazon.com/images/I/61w12MF71yL._AC_SL1000_.jpg"),
     "moneda": Moneda.objects.get(moneda="JPY"),
     "set": "",
     "color": "BLACK"},

    {"nombre": "MAZO BIG MOM (ST-07)", "precio": 0, "idioma": Idioma.objects.get(idioma="JAPONES"),
     "descripcion": "",
     "url": "https://www.amazon.co.jp/-/en/BANDAI-ST-07-Piece-Start-Pirates/dp/B0BKKSYCB4/ref=sr_1_2?crid=28HEMNG197NVP&keywords=one+piece+tcg+Start+Deck&qid=1699304167&sprefix=one+piece+tcg+start+deck%2Caps%2C258&sr=8-2",
     "type": Type.objects.get(type="STARTER DECK"),
     "image": Images.objects.get(image="https://m.media-amazon.com/images/I/81UG8MAcmeL._AC_SL1500_.jpg"),
     "moneda": Moneda.objects.get(moneda="JPY"),
     "set": "",
     "color": "YELLOW"},

    {"nombre": "MAZO YAMATO (ST-09)",
     "precio": 17990,
     "idioma": Idioma.objects.get(idioma="INGLES"),
     "descripcion": "",
     "url": "https://www.guildreams.com/product/one-piece-tcg-starter-deck-yamato",
     "type": Type.objects.get(type="STARTER DECK"),
     "image": Images.objects.get(image="https://m.media-amazon.com/images/I/715t8fd83LL._AC_SL1500_.jpg"),
     "moneda": Moneda.objects.get(moneda="CLP"),
     "set": "",
     "color": "YELLOW"},

    {"nombre": "MAZO LUFFY (ST-08)",
     "precio": 17990,
     "idioma": Idioma.objects.get(idioma="INGLES"),
     "descripcion": "",
     "url": "https://www.guildreams.com/product/one-piece-tcg-starter-deck-monkey-d-luffy",
     "type": Type.objects.get(type="STARTER DECK"),
     "image": Images.objects.get(image="https://m.media-amazon.com/images/I/61w12MF71yL._AC_SL1000_.jpg"),
     "moneda": Moneda.objects.get(moneda="CLP"),
     "set": "",
     "color": "BLACK"},

    {"nombre": "MAZO BIG MOM (ST-07)",
     "precio": 17990,
     "idioma": Idioma.objects.get(idioma="INGLES"),
     "descripcion": "",
     "url": "https://www.guildreams.com/product/one-piece-tcg-starter-deck-big-mom",
     "type": Type.objects.get(type="STARTER DECK"),
     "image": Images.objects.get(image="https://m.media-amazon.com/images/I/81UG8MAcmeL._AC_SL1500_.jpg"),
     "moneda": Moneda.objects.get(moneda="CLP"),
     "set": "",
     "color": "YELLOW"},

    {"nombre": "Kingdoms of Intrigue - Booster Pack (OP-04)",
     "precio": 5000,
     "idioma": Idioma.objects.get(idioma="INGLES"),
     "descripcion": "",
     "url": "https://www.guildreams.com/product/one-piece-tcg-kingdoms-of-intrigue-booster-pack",
     "type": Type.objects.get(type="BOOSTER PACK"),
     "image": Images.objects.get(image="https://m.media-amazon.com/images/I/81pEhtjSSVL._AC_SL1500_.jpg"),
     "moneda": Moneda.objects.get(moneda="CLP"),
     "set": "OP04",
     "color": ""},

    {"nombre": "Kingdoms of Intrigue - Double Pack (DP-01)",
     "precio": 10990,
     "idioma": Idioma.objects.get(idioma="INGLES"),
     "descripcion": "",
     "url": "https://www.guildreams.com/product/one-piece-tcg-kingdoms-of-intrigue-double-pack",
     "type": Type.objects.get(type="BOOSTER PACK"),
     "image": Images.objects.get(image="https://progaming.cl/wp-content/uploads/2023/09/one-piece-1-1bedba2c-0b01-4660-8f88-f4c26374cb85.jpg"),
     "moneda": Moneda.objects.get(moneda="CLP"),
     "set": "OP04",
     "color": ""},

    {"nombre": "Kingdoms of Intrigue - Booster Box (OP-04)",
     "precio": 104990,
     "idioma": Idioma.objects.get(idioma="INGLES"),
     "descripcion": "",
     "url": "https://www.guildreams.com/product/one-piece-tcg-kingdoms-of-intrigue-booster-box",
     "type": Type.objects.get(type="BOOSTER PACK"),
     "image": Images.objects.get(image="https://dojiw2m9tvv09.cloudfront.net/29535/product/X_display-op0470111804.jpg?57&time=1700761976.jpg"),
     "moneda": Moneda.objects.get(moneda="CLP"),
     "set": "OP04",
     "color": ""},

    {"nombre": "Romance Dawn - Booster Pack (OP-01)",
     "precio": 6000,
     "idioma": Idioma.objects.get(idioma="INGLES"),
     "descripcion": "",
     "url": "https://www.guildreams.com/product/one-piece-tcg-romance-dawn-booster-pack",
     "type": Type.objects.get(type="BOOSTER PACK"),
     "image": Images.objects.get(image="https://m.media-amazon.com/images/I/51G78ZwYgFL._AC_.jpg"),
     "moneda": Moneda.objects.get(moneda="CLP"),
     "set": "OP01",
     "color": ""},

    {"nombre": "Paramount War - Booster Pack (OP-02)",
     "precio": 5000,
     "idioma": Idioma.objects.get(idioma="INGLES"),
     "descripcion": "",
     "url": "https://www.guildreams.com/product/one-piece-tcg-paramount-war-booster-pack",
     "type": Type.objects.get(type="BOOSTER PACK"),
     "image": Images.objects.get(image="https://m.media-amazon.com/images/I/71qvgIHlPcL._AC_SL1500_.jpg"),
     "moneda": Moneda.objects.get(moneda="CLP"),
     "set": "OP02",
     "color": ""},

    {"nombre": "Pillars Of Strength - Booster Pack (OP-03)",
     "precio": 5000,
     "idioma": Idioma.objects.get(idioma="INGLES"),
     "descripcion": "",
     "url": "https://www.guildreams.com/product/one-piece-tcg-pillars-of-strength-booster-pack",
     "type": Type.objects.get(type="BOOSTER PACK"),
     "image": Images.objects.get(image="https://m.media-amazon.com/images/I/61SgFEw2SUL._AC_.jpg"),
     "moneda": Moneda.objects.get(moneda="CLP"),
     "set": "OP03",
     "color": ""},

    {"nombre": "MAZO ZORO & SANJI (ST-12)",
     "precio": 14990,
     "idioma": Idioma.objects.get(idioma="INGLES"),
     "descripcion": "",
     "url": "https://elreinodelosduelos.cl/producto/starter-deck-12-zoro-and-sanji-st-12/",
     "type": Type.objects.get(type="STARTER DECK"),
     "image": Images.objects.get(image="https://m.media-amazon.com/images/I/81qcks9pL4L._AC_SL1500_.jpg"),
     "moneda": Moneda.objects.get(moneda="CLP"),
     "set": "",
     "color": "GREEN&BLUE"},

    {"nombre": "MAZO LUFFY (ST-08)",
     "precio": 19990,
     "idioma": Idioma.objects.get(idioma="INGLES"),
     "descripcion": "",
     "url": "https://elreinodelosduelos.cl/producto/starter-deck-8-monkey-d-luffy-st-08/",
     "type": Type.objects.get(type="STARTER DECK"),
     "image": Images.objects.get(image="https://m.media-amazon.com/images/I/61w12MF71yL._AC_SL1000_.jpg"),
     "moneda": Moneda.objects.get(moneda="CLP"),
     "set": "",
     "color": "BLACK"},

    {"nombre": "MAZO YAMATO (ST-09)",
     "precio": 19990,
     "idioma": Idioma.objects.get(idioma="INGLES"),
     "descripcion": "",
     "url": "https://elreinodelosduelos.cl/producto/starter-deck-9-yamato-st-09/",
     "type": Type.objects.get(type="STARTER DECK"),
     "image": Images.objects.get(image="https://m.media-amazon.com/images/I/715t8fd83LL._AC_SL1500_.jpg"),
     "moneda": Moneda.objects.get(moneda="CLP"),
     "set": "",
     "color": "YELLOW"},

    {"nombre": "Kingdoms of Intrigue - Booster Box (OP-04)",
     "precio": 119990,
     "idioma": Idioma.objects.get(idioma="INGLES"),
     "descripcion": "",
     "url": "https://elreinodelosduelos.cl/producto/one-piece-card-game-kingdoms-of-intrigue-op-04/",
     "type": Type.objects.get(type="BOOSTER PACK"),
     "image": Images.objects.get(image="https://dojiw2m9tvv09.cloudfront.net/29535/product/X_display-op0470111804.jpg?57&time=1700761976.jpg"),
     "moneda": Moneda.objects.get(moneda="CLP"),
     "set": "OP04",
     "color": ""},

    {"nombre": "Paramount War - Booster Box (OP-02)",
     "precio": 124990,
     "idioma": Idioma.objects.get(idioma="INGLES"),
     "descripcion": "",
     "url": "https://elreinodelosduelos.cl/producto/one-piece-card-game-paramount-war-booster-box-op-02/",
     "type": Type.objects.get(type="BOOSTER PACK"),
     "image": Images.objects.get(image="https://m.media-amazon.com/images/I/61MdqVLDEdL._AC_SL1309_.jpg"),
     "moneda": Moneda.objects.get(moneda="CLP"),
     "set": "OP02",
     "color": ""},

    {"nombre": "Gift Collection 2023 (GC-01)",
     "precio": 39990,
     "idioma": Idioma.objects.get(idioma="INGLES"),
     "descripcion": "",
     "url": "https://elreinodelosduelos.cl/producto/one-piece-card-game-gift-collection-2023-gc01/",
     "type": Type.objects.get(type="BOOSTER PACK"),
     "image": Images.objects.get(image="https://m.media-amazon.com/images/I/61AZext6huL._AC_.jpg"),
     "moneda": Moneda.objects.get(moneda="CLP"),
     "set": "OP04",
     "color": ""},

    {"nombre": "MAZO ZORO & SANJI (ST-12)",
     "precio": 11990,
     "idioma": Idioma.objects.get(idioma="INGLES"),
     "descripcion": "",
     "url": "https://carduniverse.cl/collections/one-piece-card-game/products/reserva-starter-deck-zoro-and-sanji-st-12",
     "type": Type.objects.get(type="STARTER DECK"),
     "image": Images.objects.get(image="https://m.media-amazon.com/images/I/81qcks9pL4L._AC_SL1500_.jpg"),
     "moneda": Moneda.objects.get(moneda="CLP"),
     "set": "",
     "color": "GREEN&BLUE"},

    {"nombre": "MAZO LUFFY (ST-08)",
     "precio": 17990,
     "idioma": Idioma.objects.get(idioma="INGLES"),
     "descripcion": "",
     "url": "https://carduniverse.cl/collections/one-piece-card-game/products/reserva-starter-deck-monkey-d-luffy-st-08",
     "type": Type.objects.get(type="STARTER DECK"),
     "image": Images.objects.get(image="https://m.media-amazon.com/images/I/61w12MF71yL._AC_SL1000_.jpg"),
     "moneda": Moneda.objects.get(moneda="CLP"),
     "set": "",
     "color": "BLACK"},

    {"nombre": "MAZO LUFFY (ST-08)",
     "precio": 17990,
     "idioma": Idioma.objects.get(idioma="INGLES"),
     "descripcion": "",
     "url": "https://carduniverse.cl/collections/one-piece-card-game/products/reserva-starter-deck-monkey-d-luffy-st-08",
     "type": Type.objects.get(type="STARTER DECK"),
     "image": Images.objects.get(image="https://m.media-amazon.com/images/I/61w12MF71yL._AC_SL1000_.jpg"),
     "moneda": Moneda.objects.get(moneda="CLP"),
     "set": "",
     "color": "BLACK"},

    {"nombre": "Wings Of The Captain - Booster Box (OP-06)",
     "precio": 95990,
     "idioma": Idioma.objects.get(idioma="INGLES"),
     "descripcion": "",
     "url": "https://carduniverse.cl/collections/one-piece-card-game/products/reserva-display-wings-of-captain-op-06",
     "type": Type.objects.get(type="BOOSTER PACK"),
     "image": Images.objects.get(
         image="https://carduniverse.cl/cdn/shop/files/WingsoftheCaptainpng_600x.png?v=1698620241"),
     "moneda": Moneda.objects.get(moneda="CLP"),
     "set": "OP06",
     "color": ""},

    {"nombre": "Wings Of The Captain - Double Pack (DP-03)",
     "precio": 10990,
     "idioma": Idioma.objects.get(idioma="INGLES"),
     "descripcion": "",
     "url": "https://carduniverse.cl/collections/one-piece-card-game/products/reserva-double-pack-set-vol-3-dp03",
     "type": Type.objects.get(type="BOOSTER PACK"),
     "image": Images.objects.get(
         image="https://carduniverse.cl/cdn/shop/files/DoublePackSetVol.3_DP-03_2_600x.png?v=1698620478"),
     "moneda": Moneda.objects.get(moneda="CLP"),
     "set": "OP06",
     "color": ""},

    {"nombre": "Paramount War - Booster Box (OP-02)",
     "precio": 131990,
     "idioma": Idioma.objects.get(idioma="INGLES"),
     "descripcion": "",
     "url": "https://carduniverse.cl/collections/one-piece-card-game/products/reserva-display-romance-dawn",
     "type": Type.objects.get(type="BOOSTER PACK"),
     "image": Images.objects.get(image="https://m.media-amazon.com/images/I/61MdqVLDEdL._AC_SL1309_.jpg"),
     "moneda": Moneda.objects.get(moneda="CLP"),
     "set": "OP02",
     "color": ""},

    {"nombre": "MAZO YAMATO (ST-09)",
     "precio": 18990,
     "idioma": Idioma.objects.get(idioma="INGLES"),
     "descripcion": "",
     "url": "https://www.geekers.cl/one-piece-starter-deck-09-yamato",
     "type": Type.objects.get(type="STARTER DECK"),
     "image": Images.objects.get(image="https://m.media-amazon.com/images/I/715t8fd83LL._AC_SL1500_.jpg"),
     "moneda": Moneda.objects.get(moneda="CLP"),
     "set": "",
     "color": "YELLOW"},

    {"nombre": "Paramount War - Booster Pack (OP-02)",
     "precio": 5490,
     "idioma": Idioma.objects.get(idioma="INGLES"),
     "descripcion": "",
     "url": "https://www.geekers.cl/one-piece-pillars-of-strength-booster-pack-copiar",
     "type": Type.objects.get(type="BOOSTER PACK"),
     "image": Images.objects.get(image="https://m.media-amazon.com/images/I/71qvgIHlPcL._AC_SL1500_.jpg"),
     "moneda": Moneda.objects.get(moneda="CLP"),
     "set": "OP02",
     "color": ""},

    {"nombre": "Pillars Of Strength - Booster Pack (OP-03)",
     "precio": 5490,
     "idioma": Idioma.objects.get(idioma="INGLES"),
     "descripcion": "",
     "url": "https://www.geekers.cl/one-piece-pillars-of-strength-booster-pack",
     "type": Type.objects.get(type="BOOSTER PACK"),
     "image": Images.objects.get(image="https://m.media-amazon.com/images/I/61SgFEw2SUL._AC_.jpg"),
     "moneda": Moneda.objects.get(moneda="CLP"),
     "set": "OP03",
     "color": ""},

    {"nombre": "MAZO LUFFY (ST-08)",
     "precio": 16990,
     "idioma": Idioma.objects.get(idioma="INGLES"),
     "descripcion": "",
     "url": "https://thirdimpact.cl/producto/one-piece-card-game-st08-monkey-d-luffy/",
     "type": Type.objects.get(type="STARTER DECK"),
     "image": Images.objects.get(image="https://m.media-amazon.com/images/I/715t8fd83LL._AC_SL1500_.jpg"),
     "moneda": Moneda.objects.get(moneda="CLP"),
     "set": "",
     "color": "BLACK"},

    {"nombre": "Wings Of The Captain - Booster Box (OP-06)",
     "precio": 99990,
     "idioma": Idioma.objects.get(idioma="INGLES"),
     "descripcion": "",
     "url": "https://thirdimpact.cl/producto/one-piece-card-game-op06-wings-of-the-captain-booster-box/",
     "type": Type.objects.get(type="BOOSTER PACK"),
     "image": Images.objects.get(
         image="https://carduniverse.cl/cdn/shop/files/WingsoftheCaptainpng_600x.png?v=1698620241"),
     "moneda": Moneda.objects.get(moneda="CLP"),
     "set": "OP06",
     "color": ""},

    {"nombre": "Gift Collection 2023 (GC-01)",
     "precio": 30990,
     "idioma": Idioma.objects.get(idioma="INGLES"),
     "descripcion": "",
     "url": "https://thirdimpact.cl/producto/one-piece-card-game-gb01-gift-box-2023/",
     "type": Type.objects.get(type="BOOSTER PACK"),
     "image": Images.objects.get(image="https://m.media-amazon.com/images/I/61AZext6huL._AC_.jpg"),
     "moneda": Moneda.objects.get(moneda="CLP"),
     "set": "OP04",
     "color": ""},

    {"nombre": "Kingdoms of Intrigue - Double Pack (DP-01)",
     "precio": 11990,
     "idioma": Idioma.objects.get(idioma="INGLES"),
     "descripcion": "",
     "url": "https://thirdimpact.cl/producto/one-piece-card-game-kingdom-of-intrigue-dp01-double-pack-vol-1/",
     "type": Type.objects.get(type="BOOSTER PACK"),
     "image": Images.objects.get(image="https://progaming.cl/wp-content/uploads/2023/09/one-piece-1-1bedba2c-0b01-4660-8f88-f4c26374cb85.jpg"),
     "moneda": Moneda.objects.get(moneda="CLP"),
     "set": "OP04",
     "color": ""},

    {"nombre": "Pillars Of Strength - Booster Box (OP-03)",
     "precio": 119990,
     "idioma": Idioma.objects.get(idioma="INGLES"),
     "descripcion": "",
     "url": "https://thirdimpact.cl/producto/one-piece-card-game-op03-pillars-of-strength/",
     "type": Type.objects.get(type="BOOSTER PACK"),
     "image": Images.objects.get(image="https://m.media-amazon.com/images/I/91Agw8ffdUL._AC_SL1500_.jpg"),
     "moneda": Moneda.objects.get(moneda="CLP"),
     "set": "OP03",
     "color": ""},

    {"nombre": "Paramount War - Booster Box (OP-02)",
     "precio": 109990,
     "idioma": Idioma.objects.get(idioma="INGLES"),
     "descripcion": "",
     "url": "https://thirdimpact.cl/producto/one-piece-card-game-op02-paramount-war/",
     "type": Type.objects.get(type="BOOSTER PACK"),
     "image": Images.objects.get(image="https://m.media-amazon.com/images/I/61MdqVLDEdL._AC_SL1309_.jpg"),
     "moneda": Moneda.objects.get(moneda="CLP"),
     "set": "OP02",
     "color": ""},

    {"nombre": "Kingdoms of Intrigue - Booster Box (OP-04)",
     "precio": 119990,
     "idioma": Idioma.objects.get(idioma="INGLES"),
     "descripcion": "",
     "url": "https://thirdimpact.cl/producto/one-piece-card-game-op04-kingdoms-of-intrigue-booster-box/",
     "type": Type.objects.get(type="BOOSTER PACK"),
     "image": Images.objects.get(image="https://dojiw2m9tvv09.cloudfront.net/29535/product/X_display-op0470111804.jpg?57&time=1700761976.jpg"),
     "moneda": Moneda.objects.get(moneda="CLP"),
     "set": "OP04",
     "color": ""},

    {"nombre": "Pillars Of Strength - Booster Box (OP-03)",
     "precio": 104990,
     "idioma": Idioma.objects.get(idioma="INGLES"),
     "descripcion": "",
     "url": "https://www.playset.cl/producto/display-24-sobres-one-piece-tcg-pillars-of-strength-op-03/",
     "type": Type.objects.get(type="BOOSTER PACK"),
     "image": Images.objects.get(image="https://m.media-amazon.com/images/I/91Agw8ffdUL._AC_SL1500_.jpg"),
     "moneda": Moneda.objects.get(moneda="CLP"),
     "set": "OP03",
     "color": ""},

    {"nombre": "Kingdoms of Intrigue - Double Pack (DP-01)",
     "precio": 10990,
     "idioma": Idioma.objects.get(idioma="INGLES"),
     "descripcion": "",
     "url": "https://www.playset.cl/producto/one-piece-card-game-double-pack-set-vol-1-dp-01/",
     "type": Type.objects.get(type="BOOSTER PACK"),
     "image": Images.objects.get(image="https://progaming.cl/wp-content/uploads/2023/09/one-piece-1-1bedba2c-0b01-4660-8f88-f4c26374cb85.jpg"),
     "moneda": Moneda.objects.get(moneda="CLP"),
     "set": "OP04",
     "color": ""},

    {"nombre": "MAZO LUFFY (ST-08)",
     "precio": 16990,
     "idioma": Idioma.objects.get(idioma="INGLES"),
     "descripcion": "",
     "url": "https://drawn.cl/producto/preventa-juego-de-cartas-one-piece-st08-monkey-d-luffy/",
     "type": Type.objects.get(type="STARTER DECK"),
     "image": Images.objects.get(image="https://m.media-amazon.com/images/I/715t8fd83LL._AC_SL1500_.jpg"),
     "moneda": Moneda.objects.get(moneda="CLP"),
     "set": "",
     "color": "BLACK"},

    {"nombre": "Gift Collection 2023 (GC-01)",
     "precio": 34990,
     "idioma": Idioma.objects.get(idioma="INGLES"),
     "descripcion": "",
     "url": "https://drawn.cl/producto/one-piece-card-game-gift-collection-2023-gc-01/",
     "type": Type.objects.get(type="BOOSTER PACK"),
     "image": Images.objects.get(image="https://m.media-amazon.com/images/I/61AZext6huL._AC_.jpg"),
     "moneda": Moneda.objects.get(moneda="CLP"),
     "set": "OP04",
     "color": ""},

    {"nombre": "Kingdoms of Intrigue - Booster Box (OP-04)",
     "precio": 119990,
     "idioma": Idioma.objects.get(idioma="INGLES"),
     "descripcion": "",
     "url": "https://drawn.cl/producto/preventa-2-one-piece-op04-kingdoms-of-intrigue-booster-box-preventa/",
     "type": Type.objects.get(type="BOOSTER PACK"),
     "image": Images.objects.get(image="https://dojiw2m9tvv09.cloudfront.net/29535/product/X_display-op0470111804.jpg?57&time=1700761976.jpg"),
     "moneda": Moneda.objects.get(moneda="CLP"),
     "set": "OP04",
     "color": ""},

    {"nombre": "Kingdoms of Intrigue - Booster Pack (OP-04)",
     "precio": 5490,
     "idioma": Idioma.objects.get(idioma="INGLES"),
     "descripcion": "",
     "url": "https://drawn.cl/producto/booster-pack-op-04-kingdoms-of-intrigue/",
     "type": Type.objects.get(type="BOOSTER PACK"),
     "image": Images.objects.get(image="https://m.media-amazon.com/images/I/81pEhtjSSVL._AC_SL1500_.jpg"),
     "moneda": Moneda.objects.get(moneda="CLP"),
     "set": "OP04",
     "color": ""}
]

for producto_data in productos_data:
    producto = Producto.objects.create(
        nombre=producto_data["nombre"],
        precio=producto_data["precio"],
        idioma=producto_data["idioma"],
        descripcion=producto_data["descripcion"],
        url=producto_data["url"],
        type=producto_data["type"],
        image=producto_data["image"],
        moneda=producto_data["moneda"],
        set=producto_data["set"],
        color=producto_data["color"]
    )

print("Productos agregados a la base de datos.")
