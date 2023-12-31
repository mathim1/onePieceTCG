import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "onePieceTCG.settings")
django.setup()

from catalog.models import Producto, Type, Images, Idioma, Moneda

imagenes = [
    "https://m.media-amazon.com/images/I/81wCOj9DDTL._AC_SL1500_.jpg",
    "https://m.media-amazon.com/images/I/61jYkdLhbQL._AC_.jpg",
    "https://dojiw2m9tvv09.cloudfront.net/18085/product/X_14990400-81150970565977394773.jpg?71&time=1700763813.jpg",
    "https://m.media-amazon.com/images/I/6117+q-UiiL._AC_.jpg",
    "https://m.media-amazon.com/images/I/61gxrFF2pEL._AC_SL1000_.jpg",
    "https://m.media-amazon.com/images/I/719F3KumP6L._AC_SL1043_.jpg"
]

for imagen in imagenes:
    imagen_obj, created = Images.objects.get_or_create(image=imagen)
    if created:
        print(f"Imagen {imagen_obj.image} agregada a la base de datos.")
    else:
        print(f"Imagen {imagen_obj.image} ya existe en la base de datos.")

productos_data = [

    {"nombre": "MAZO AKAINU (ST-06)", "precio": 0, "idioma": Idioma.objects.get(idioma="JAPONES"),
     "descripcion": "",
     "url": "https://www.amazon.com/-/es/BANDAI-One-Piece-TCG-Cubierta/dp/B0B588N7NW/ref=sr_1_47?__mk_",
     "type": Type.objects.get(type="STARTER DECK"),
     "image": Images.objects.get(image="https://m.media-amazon.com/images/I/81muMg7eGeL._AC_SL1500_.jpg"),
     "moneda": Moneda.objects.get(moneda="USD"),
     "set": "",
     "color": "BLACK"},

    {"nombre": "FAMILY DECK BOX", "precio": 0, "idioma": Idioma.objects.get(idioma="JAPONES"),
     "descripcion": "",
     "url": "https://www.amazon.com/-/es/BANDAI-Entertainment-cartas-familia-japon%C3%A9s/dp/B0BV13PTNF/ref=sr_1_51?__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=18KR1FNCOPFCO&keywords=One+Piece+TCG&qid=1700762277&sprefix=one+piece+tcg%2Caps%2C177&sr=8-51",
     "type": Type.objects.get(type="STARTER DECK"),
     "image": Images.objects.get(image="https://m.media-amazon.com/images/I/91E45IrnyDL._AC_SL1500_.jpg"),
     "moneda": Moneda.objects.get(moneda="USD"),
     "set": "",
     "color": "RED&GREEN&PURPLE"},

    {"nombre": "Gift Collection 2023 (GC-01)",
     "precio": 0,
     "idioma": Idioma.objects.get(idioma="INGLES"),
     "descripcion": "",
     "url": "https://www.amazon.com/-/es/Bandai-Juego-cartas-pieza-coleccionables/dp/B0C7VJ7DMY/ref=sr_1_33?__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=18KR1FNCOPFCO&keywords=One+Piece+TCG&qid=1700762277&sprefix=one+piece+tcg%2Caps%2C177&sr=8-33#customerReviews",
     "type": Type.objects.get(type="BOOSTER PACK"),
     "image": Images.objects.get(image="https://m.media-amazon.com/images/I/61AZext6huL._AC_.jpg"),
     "moneda": Moneda.objects.get(moneda="USD"),
     "set": "OP04",
     "color": ""},

    {"nombre": "MAZO SH LUFFY (ST-01)", "precio": 0, "idioma": Idioma.objects.get(idioma="JAPONES"),
     "descripcion": "",
     "url": "https://www.amazon.co.jp/-/en/BANDAI-ST-01-PIECE-Start-Straw/dp/B09VKTBKMS/ref=sr_1_27?keywords=One+Piece+TCG&qid=1700763031&sr=8-27",
     "type": Type.objects.get(type="STARTER DECK"),
     "image": Images.objects.get(image="https://m.media-amazon.com/images/I/612Tn48L90L._AC_SL1200_.jpg"),
     "moneda": Moneda.objects.get(moneda="JPY"),
     "set": "",
     "color": "RED"},

    {"nombre": "MAZO KIDD (ST-02)", "precio": 0, "idioma": Idioma.objects.get(idioma="JAPONES"),
     "descripcion": "",
     "url": "https://www.amazon.co.jp/-/en/BANDAI-ST-02-PIECE-Start-Generation/dp/B09VKVFQMD/ref=sr_1_44?keywords=One+Piece+TCG&qid=1700763031&sr=8-44",
     "type": Type.objects.get(type="STARTER DECK"),
     "image": Images.objects.get(image="https://m.media-amazon.com/images/I/611-iR6cfpL._AC_SL1200_.jpg"),
     "moneda": Moneda.objects.get(moneda="JPY"),
     "set": "",
     "color": "GREEN"},

    {"nombre": "MAZO KAIDO (ST-04)", "precio": 0, "idioma": Idioma.objects.get(idioma="JAPONES"), "descripcion": "",
     "url": "https://www.amazon.co.jp/-/en/BANDAI-ST-04-PIECE-Card-Start/dp/B09VKWZJWZ/ref=sr_1_61?keywords=One+Piece+TCG&qid=1700763195&sr=8-61",
     "type": Type.objects.get(type="STARTER DECK"),
     "image": Images.objects.get(image="https://m.media-amazon.com/images/I/81fNYpxI1pL._AC_SL1500_.jpg"),
     "moneda": Moneda.objects.get(moneda="JPY"),
     "set": "",
     "color": "PURPLE"},

    {"nombre": "MAZO ONE PIECE RED (ST-05)", "precio": 0, "idioma": Idioma.objects.get(idioma="JAPONES"),
     "descripcion": "",
     "url": "https://www.amazon.co.jp/-/en/Bandai-ST-05-Piece-Card-Start/dp/B09VKS64CD/ref=sr_1_66?keywords=One+Piece+TCG&qid=1700763195&sr=8-66",
     "type": Type.objects.get(type="STARTER DECK"),
     "image": Images.objects.get(image="https://m.media-amazon.com/images/I/71ksCUbPIuL._AC_SL1200_.jpg"),
     "moneda": Moneda.objects.get(moneda="JPY"),
     "set": "",
     "color": "PURPLE"},

    {"nombre": "MAZO YAMATO (ST-09)",
     "precio": 0,
     "idioma": Idioma.objects.get(idioma="JAPONES"),
     "descripcion": "",
     "url": "https://www.amazon.co.jp/-/en/BANDAI-ST-9-PIECE-Start-Yamato/dp/B0BNPFQV8J/ref=sr_1_47?keywords=One+Piece+TCG&qid=1700763031&sr=8-47",
     "type": Type.objects.get(type="STARTER DECK"),
     "image": Images.objects.get(image="https://m.media-amazon.com/images/I/715t8fd83LL._AC_SL1500_.jpg"),
     "moneda": Moneda.objects.get(moneda="JPY"),
     "set": "",
     "color": "YELLOW"},

    {"nombre": "MAZO 3 HERMANOS (ST-13)",
     "precio": 0,
     "idioma": Idioma.objects.get(idioma="JAPONES"),
     "descripcion": "",
     "url": "https://www.amazon.co.jp/-/en/BANDAI-ST-9-PIECE-Start-Yamato/dp/B0BNPFQV8J/ref=sr_1_47?keywords=One+Piece+TCG&qid=1700763031&sr=8-47",
     "type": Type.objects.get(type="STARTER DECK"),
     "image": Images.objects.get(image="https://m.media-amazon.com/images/I/715t8fd83LL._AC_SL1500_.jpg"),
     "moneda": Moneda.objects.get(moneda="JPY"),
     "set": "",
     "color": "YELLOW&BLACK&BLUE&RED"},

    {"nombre": "SET DE 4",
     "precio": 0,
     "idioma": Idioma.objects.get(idioma="JAPONES"),
     "descripcion": "",
     "url": "https://www.amazon.co.jp/-/en/Piece-Card-Game-Start-Deck/dp/B0B3MF5T7P/ref=sr_1_92?keywords=One+Piece+TCG&qid=1700763195&sr=8-92",
     "type": Type.objects.get(type="STARTER DECK"),
     "image": Images.objects.get(image="https://m.media-amazon.com/images/I/61jYkdLhbQL._AC_.jpg"),
     "moneda": Moneda.objects.get(moneda="JPY"),
     "set": "",
     "color": "RED&GREEN&BLUE&PURPLE"},

    {"nombre": "MAZO 3 CAPITANES (ST-10)", "precio": 0, "idioma": Idioma.objects.get(idioma="INGLES"),
     "descripcion": "",
     "url": "https://www.guildreams.com/product/one-piece-tcg-ultra-deck-the-three-captains",
     "type": Type.objects.get(type="STARTER DECK"),
     "image": Images.objects.get(image="https://m.media-amazon.com/images/I/81ZIvaR-uPL._AC_SL1500_.jpg"),
     "moneda": Moneda.objects.get(moneda="CLP"),
     "set": "",
     "color": "RED&PURPLE"},

    {"nombre": "Devil Fruit Collection Vol.1 (DF-01)",
     "precio": 0,
     "idioma": Idioma.objects.get(idioma="INGLES"),
     "descripcion": "",
     "url": "https://www.guildreams.com/product/one-piece-tcg-devil-fruits-collection-vol-1",
     "type": Type.objects.get(type="BOOSTER PACK"),
     "image": Images.objects.get(
         image="https://dojiw2m9tvv09.cloudfront.net/18085/product/X_14990400-81150970565977394773.jpg?71&time=1700763813.jpg"),
     "moneda": Moneda.objects.get(moneda="CLP"),
     "set": "OP03&OP4",
     "color": ""},

    {"nombre": "Kingdoms of Intrigue - Double Pack (DP-01)",
     "precio": 0,
     "idioma": Idioma.objects.get(idioma="INGLES"),
     "descripcion": "",
     "url": "https://elreinodelosduelos.cl/producto/one-piece-card-game-double-pack-set-vol-1-dp-01/",
     "type": Type.objects.get(type="BOOSTER PACK"),
     "image": Images.objects.get(image="https://progaming.cl/wp-content/uploads/2023/09/one-piece-1-1bedba2c-0b01-4660-8f88-f4c26374cb85.jpg"),
     "moneda": Moneda.objects.get(moneda="CLP"),
     "set": "OP04",
     "color": ""},

    {"nombre": "Devil Fruit Collection Vol.1 (DF-01)",
     "precio": 0,
     "idioma": Idioma.objects.get(idioma="INGLES"),
     "descripcion": "",
     "url": "https://elreinodelosduelos.cl/producto/one-piece-card-game-devil-fruits-collection-vol-1-df-01/",
     "type": Type.objects.get(type="BOOSTER PACK"),
     "image": Images.objects.get(
         image="https://dojiw2m9tvv09.cloudfront.net/18085/product/X_14990400-81150970565977394773.jpg?71&time=1700763813.jpg"),
     "moneda": Moneda.objects.get(moneda="CLP"),
     "set": "OP03&OP4",
     "color": ""},

    {"nombre": "MAZO SH LUFFY (ST-01)", "precio": 0, "idioma": Idioma.objects.get(idioma="INGLES"),
     "descripcion": "",
     "url": "https://carduniverse.cl/collections/one-piece-card-game/products/reserva-starter-decks-one-piece-card-game",
     "type": Type.objects.get(type="STARTER DECK"),
     "image": Images.objects.get(image="https://m.media-amazon.com/images/I/612Tn48L90L._AC_SL1200_.jpg"),
     "moneda": Moneda.objects.get(moneda="CLP"),
     "set": "",
     "color": "RED"},

    {"nombre": "MAZO ONE PIECE RED (ST-05)", "precio": 0, "idioma": Idioma.objects.get(idioma="INGLES"),
     "descripcion": "",
     "url": "https://carduniverse.cl/collections/one-piece-card-game/products/reserva-starter-deck-film-edition",
     "type": Type.objects.get(type="STARTER DECK"),
     "image": Images.objects.get(image="https://m.media-amazon.com/images/I/71ksCUbPIuL._AC_SL1200_.jpg"),
     "moneda": Moneda.objects.get(moneda="CLP"),
     "set": "",
     "color": "PURPLE"},

    {"nombre": "MAZO AKAINU (ST-06)", "precio": 0, "idioma": Idioma.objects.get(idioma="INGLES"),
     "descripcion": "",
     "url": "https://carduniverse.cl/collections/one-piece-card-game/products/copia-de-reserva-starter-deck-navy-st-06",
     "type": Type.objects.get(type="STARTER DECK"),
     "image": Images.objects.get(image="https://m.media-amazon.com/images/I/81muMg7eGeL._AC_SL1500_.jpg"),
     "moneda": Moneda.objects.get(moneda="CLP"),
     "set": "",
     "color": "BLACK"},

    {"nombre": "MAZO BIG MOM (ST-07)", "precio": 0, "idioma": Idioma.objects.get(idioma="INGLES"),
     "descripcion": "",
     "url": "https://carduniverse.cl/collections/one-piece-card-game/products/reserva-starter-deck-big-mom-st-07",
     "type": Type.objects.get(type="STARTER DECK"),
     "image": Images.objects.get(image="https://m.media-amazon.com/images/I/81UG8MAcmeL._AC_SL1500_.jpg"),
     "moneda": Moneda.objects.get(moneda="CLP"),
     "set": "",
     "color": "YELLOW"},

    {"nombre": "MAZO 3 CAPITANES (ST-10)", "precio": 0, "idioma": Idioma.objects.get(idioma="INGLES"),
     "descripcion": "",
     "url": "https://carduniverse.cl/collections/one-piece-card-game/products/reserva-ultimate-deck-the-three-captains-st-10",
     "type": Type.objects.get(type="STARTER DECK"),
     "image": Images.objects.get(image="https://m.media-amazon.com/images/I/81ZIvaR-uPL._AC_SL1500_.jpg"),
     "moneda": Moneda.objects.get(moneda="CLP"),
     "set": "",
     "color": "RED&PURPLE"},

    {"nombre": "Romance Dawn - Booster Box (OP-01)",
     "precio": 0,
     "idioma": Idioma.objects.get(idioma="INGLES"),
     "descripcion": "",
     "url": "https://carduniverse.cl/collections/one-piece-card-game/products/reserva-display-romance-dawn-op-01",
     "type": Type.objects.get(type="BOOSTER PACK"),
     "image": Images.objects.get(
         image="https://m.media-amazon.com/images/I/719F3KumP6L._AC_SL1043_.jpg"),
     "moneda": Moneda.objects.get(moneda="CLP"),
     "set": "OP01",
     "color": ""},

    {"nombre": "Pillars of Strength - Booster Box (OP-03)",
     "precio": 0,
     "idioma": Idioma.objects.get(idioma="INGLES"),
     "descripcion": "",
     "url": "https://carduniverse.cl/collections/one-piece-card-game/products/reserva-display-pillars-of-strength-op-03",
     "type": Type.objects.get(type="BOOSTER PACK"),
     "image": Images.objects.get(
         image="https://m.media-amazon.com/images/I/91Agw8ffdUL._AC_SL1500_.jpg"),
     "moneda": Moneda.objects.get(moneda="CLP"),
     "set": "OP03",
     "color": ""},

    {"nombre": "Kingdoms of Intrigue - Booster Box (OP-04)",
     "precio": 0,
     "idioma": Idioma.objects.get(idioma="INGLES"),
     "descripcion": "",
     "url": "https://carduniverse.cl/collections/one-piece-card-game/products/reserva-display-kingdoms-of-intrigue-op-04",
     "type": Type.objects.get(type="BOOSTER PACK"),
     "image": Images.objects.get(
         image="https://dojiw2m9tvv09.cloudfront.net/29535/product/X_display-op0470111804.jpg?57&time=1700761976.jpg"),
     "moneda": Moneda.objects.get(moneda="CLP"),
     "set": "OP04",
     "color": ""},

    {"nombre": "Kingdoms of Intrigue - Double Pack (DP-01)",
     "precio": 0,
     "idioma": Idioma.objects.get(idioma="INGLES"),
     "descripcion": "",
     "url": "https://carduniverse.cl/collections/one-piece-card-game/products/reserva-double-pack-set-volume-1-display-dp01",
     "type": Type.objects.get(type="BOOSTER PACK"),
     "image": Images.objects.get(
         image="https://progaming.cl/wp-content/uploads/2023/09/one-piece-1-1bedba2c-0b01-4660-8f88-f4c26374cb85.jpg"),
     "moneda": Moneda.objects.get(moneda="CLP"),
     "set": "OP04",
     "color": ""},

    {"nombre": "Awakening Of The New Era - Booster Box (OP-05)",
     "precio": 0,
     "idioma": Idioma.objects.get(idioma="INGLES"),
     "descripcion": "",
     "url": "https://carduniverse.cl/collections/one-piece-card-game/products/reserva-display-awakening-of-the-new-era-op-05",
     "type": Type.objects.get(type="BOOSTER PACK"),
     "image": Images.objects.get(
         image="https://m.media-amazon.com/images/I/61gxrFF2pEL._AC_SL1000_.jpg"),
     "moneda": Moneda.objects.get(moneda="CLP"),
     "set": "OP05",
     "color": ""},

    {"nombre": "Awakening Of The New Era - Double Pack (DP-02)",
     "precio": 0,
     "idioma": Idioma.objects.get(idioma="INGLES"),
     "descripcion": "",
     "url": "https://carduniverse.cl/collections/one-piece-card-game/products/reserva-double-pack-set-vol-2-dp02",
     "type": Type.objects.get(type="BOOSTER PACK"),
     "image": Images.objects.get(
         image="https://m.media-amazon.com/images/I/6117+q-UiiL._AC_.jpg"),
     "moneda": Moneda.objects.get(moneda="CLP"),
     "set": "OP05",
     "color": ""},

    {"nombre": "Gift Collection 2023 (GC-01)",
     "precio": 0,
     "idioma": Idioma.objects.get(idioma="INGLES"),
     "descripcion": "",
     "url": "https://carduniverse.cl/collections/one-piece-card-game/products/reserva-gift-collection-2023-gc01",
     "type": Type.objects.get(type="BOOSTER PACK"),
     "image": Images.objects.get(image="https://m.media-amazon.com/images/I/61AZext6huL._AC_.jpg"),
     "moneda": Moneda.objects.get(moneda="CLP"),
     "set": "OP04",
     "color": ""},

    {"nombre": "Devil Fruit Collection Vol.1 (DF-01)",
     "precio": 0,
     "idioma": Idioma.objects.get(idioma="INGLES"),
     "descripcion": "",
     "url": "https://carduniverse.cl/collections/one-piece-card-game/products/reserva-devil-fruits-collection-vol-1",
     "type": Type.objects.get(type="BOOSTER PACK"),
     "image": Images.objects.get(
         image="https://dojiw2m9tvv09.cloudfront.net/18085/product/X_14990400-81150970565977394773.jpg?71&time=1700763813.jpg"),
     "moneda": Moneda.objects.get(moneda="CLP"),
     "set": "OP03&OP4",
     "color": ""},

    {"nombre": "MAZO LUFFY (ST-08)", "precio": 0, "idioma": Idioma.objects.get(idioma="INGLES"), "descripcion": "",
     "url": "https://www.geekers.cl/one-piece-starter-deck-08-monkey-d-luffy",
     "type": Type.objects.get(type="STARTER DECK"),
     "image": Images.objects.get(image="https://m.media-amazon.com/images/I/61w12MF71yL._AC_SL1000_.jpg"),
     "moneda": Moneda.objects.get(moneda="CLP"),
     "set": "",
     "color": "BLACK"},

    {"nombre": "Kingdoms of Intrigue - Double Pack (DP-01)",
     "precio": 0,
     "idioma": Idioma.objects.get(idioma="INGLES"),
     "descripcion": "",
     "url": "https://www.geekers.cl/one-piece-pillars-of-strength-booster-pack-copiar-1",
     "type": Type.objects.get(type="BOOSTER PACK"),
     "image": Images.objects.get(
         image="https://progaming.cl/wp-content/uploads/2023/09/one-piece-1-1bedba2c-0b01-4660-8f88-f4c26374cb85.jpg"),
     "moneda": Moneda.objects.get(moneda="CLP"),
     "set": "OP04",
     "color": ""},

    {"nombre": "Gift Collection 2023 (GC-01)",
     "precio": 0,
     "idioma": Idioma.objects.get(idioma="INGLES"),
     "descripcion": "",
     "url": "https://www.geekers.cl/one-piece-tcg-gc01-gift-collection-2023",
     "type": Type.objects.get(type="BOOSTER PACK"),
     "image": Images.objects.get(image="https://m.media-amazon.com/images/I/61AZext6huL._AC_.jpg"),
     "moneda": Moneda.objects.get(moneda="CLP"),
     "set": "OP04",
     "color": ""},

    {"nombre": "Awakening Of The New Era - Double Pack (DP-02)",
     "precio": 0,
     "idioma": Idioma.objects.get(idioma="INGLES"),
     "descripcion": "",
     "url": "https://thirdimpact.cl/producto/one-piece-card-game-awakening-of-the-new-era-double-pack-vol-2/",
     "type": Type.objects.get(type="BOOSTER PACK"),
     "image": Images.objects.get(
         image="https://m.media-amazon.com/images/I/6117+q-UiiL._AC_.jpg"),
     "moneda": Moneda.objects.get(moneda="CLP"),
     "set": "OP05",
     "color": ""},

    {"nombre": "Pillars Of Strength - Booster Pack (OP-03)",
     "precio": 0,
     "idioma": Idioma.objects.get(idioma="INGLES"),
     "descripcion": "",
     "url": "https://drawn.cl/producto/booster-pack-op-03-pillars-of-strength/",
     "type": Type.objects.get(type="BOOSTER PACK"),
     "image": Images.objects.get(
         image="https://m.media-amazon.com/images/I/61SgFEw2SUL._AC_.jpg"),
     "moneda": Moneda.objects.get(moneda="CLP"),
     "set": "OP03",
     "color": ""},

    {"nombre": "Devil Fruit Collection Vol.1 (DF-01)",
     "precio": 0,
     "idioma": Idioma.objects.get(idioma="INGLES"),
     "descripcion": "",
     "url": "https://drawn.cl/producto/devil-fruits-collection-one-piece/",
     "type": Type.objects.get(type="BOOSTER PACK"),
     "image": Images.objects.get(
         image="https://dojiw2m9tvv09.cloudfront.net/18085/product/X_14990400-81150970565977394773.jpg?71&time=1700763813.jpg"),
     "moneda": Moneda.objects.get(moneda="CLP"),
     "set": "OP03&OP4",
     "color": ""},
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
