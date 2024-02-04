from django.shortcuts import render

def index(request):
    cards = [
     {"name": "Card title",
     "desc": "This is a wider card with supporting text below as a natural lead-in to additional content. This card has even longer content than the first to show that equal height action.",
     "image_url": "images/gray_bg.jpg",
     "tags": "Чё-то интересное, типа тегов."
     } ,
    {"name": "Card title",
     "desc": "This is a wider card with supporting text below as a natural lead-in to additional content. This card has even longer content than the first to show that equal height action.",
     "image_url": "images/gray_bg.jpg",
     "tags": "Чё-то интересное, типа тегов."
     },
    {"name": "Card title",
     "desc": "This is a wider card with supporting text below as a natural lead-in to additional content. This card has even longer content than the first to show that equal height action.",
     "image_url": "images/gray_bg.jpg",
     "tags": "Чё-то интересное, типа тегов."
     },
    ]

    context = {"title": "Главная страница",
               "cards": cards}

    return render(request, "main/cards.html", context=context)

