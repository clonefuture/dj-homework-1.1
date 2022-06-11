from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, кг': 0.3,
        'сыр, кг': 0.05,
    },
    'butter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }


def omlet(request):
    num = int(request.GET.get('servings', 1))
    oml = {key: value * num for key, value in DATA.get('omlet').items()}
    context = {
        'recipe': oml
    }
    return render(request, 'calculator/index.html', context)


def pasta(request):
    num = int(request.GET.get('servings', 1))
    pas = {key: value * num for key, value in DATA.get('pasta').items()}
    context = {
        'recipe': pas
    }
    return render(request, 'calculator/index.html', context)


def butter(request):
    num = int(request.GET.get('servings', 1))
    but = {key: value * num for key, value in DATA.get('butter').items()}
    context = {
        'recipe': but
    }
    return render(request, 'calculator/index.html', context)
