from django.core.paginator import Paginator
from django.shortcuts import render

def index(request):
    main_desc = """
    Возможно, многие удивятся, узнав, что термин «аниме» родом вовсе не из Страны восходящего солнца, а из Англии. Ёмкое слово animation немного сократили и присвоили по-настоящему магическому искусству японской мультипликации. Аниме мультфильмы онлайн, в отличии от мультфильмов других стран, занимает другую нишу так как он предназначен в основном на подростковую и взрослую аудиторию. Именно эта многогранность обеспечила ей широчайшую востребованность. Для этого направления характерна уникальная отрисовка персонажей и фон, которая легко узнаётся. Большинство из них основаны на манге, а также виртуальных играх и ранобэ. Когда авторы проектов создают свои творения, они стараются придать графике «первородный» стиль, то есть сохранить непередаваемую графику оригинала. Наш портал предоставляет зрителям список аниме онлайн лучших произведений. Это направление кинематографа можно разбить на четыре части. Первая создаётся только для молодых женщин, вторая для более зрелых представительниц прекрасного пола, третья для неопытных юношей, а четвертая для взрослых мужчин. Дети получают специализированные аниме мультики — комодо.
    В нашем каталоге вы найдете список лучших аниме, разных жанров и на любой вкус. Это и аниме про любовь, и детективы, и экшен, и аниме про демонов, и ужасы, и фэнтези, и приключения... Кроме «полнометражных аниме» картин на сайте представлены также короткометражные и аниме сериалы
    """

    page = int(request.GET.get("page", 1))
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
    {"name": "Card title",
     "desc": "This is a wider card with supporting text below as a natural lead-in to additional content. This card has even longer content than the first to show that equal height action.",
     "image_url": "images/gray_bg.jpg",
     "tags": "Чё-то интересное, типа тегов."
     },
    ]

    paginator = Paginator(cards, 3)
    current_page_card = paginator.page(page)

    context = {"title": "Что-то про аниме",
               "main_desc": main_desc,
               "cards": current_page_card
               }

    return render(request, "main/cards.html", context=context)

