from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import DjangoRegForm, LoginForm
from .models import Toy, Buyer, Basket, Action
import hashlib
import datetime
from random import randint

current_user = 0
current_user_name = ''


def main_page(request):
    '''
    Актуализирует действие акций и цены с учетом временных скидок,
    после чего формирует контекст главной страницы и возвращает рендер ее шаблона
    :param request:
    :return:
    '''
    global current_user, current_user_name
    pn = 'Добро пожаловать в наш игрушечный магазин игрушек!'
    # Актуализируем действие акций на текущую дату
    actions = Action.objects.all()
    for action in actions:
        first_date = datetime.datetime.strptime(
            str(action.first_date), "%Y-%m-%d").date()
        last_date = datetime.datetime.strptime(
            str(action.last_date), "%Y-%m-%d").date()
        if first_date <= datetime.date.today() and last_date >= datetime.date.today():
            action.actual = 1
        else:
            action.actual = 0
        action.save()
    # Актуализируем цены с учетом скидок (не суммируются) на текущую дату
    max_discount = 0
    actions = Action.objects.filter(actual=1)
    for action in actions:
        if action.discont > max_discount:
            max_discount = action.discont
    discount = (100 - max_discount) / 100
    toys = Toy.objects.all()
    for toy in toys:
        toy.actual_cost = float(toy.cost) * float(discount)
        toy.save()
    context = {
        'pn': pn,
        'current_user': current_user,
        'toys': toys,
        'discount': discount}
    return render(request, 'main_page.html', context)


def actions_page(request):
    '''
    Формирует контекст страницы акций и возвращает рендер ее шаблона
    :param request:
    :return:
    '''
    global current_user, current_user_name
    pn = 'Мы кое-что для Вас приготовили!'
    current_date = datetime.date.today()
    actions = Action.objects.filter(
        published=True) & Action.objects.filter(
        last_date__gte=current_date).order_by('last_date')
    context = {'pn': pn, 'current_user': current_user, 'actions': actions}
    return render(request, 'actions.html', context)


def present(request):
    '''
    Подготавливает данные для страницы вручения акционных подарков.
    (категория 4 - это подарки)
    Выбирает случайный подарок из имеющихся в наличии.
    Если в наличии не осталось подарков, приносит извинения
    Возвращает рендер страницы.
    :param request:
    :return:
    '''
    global current_user, current_user_name
    action_id = request.GET.get('action')
    action = Action.objects.filter(id=action_id)
    presents = Toy.objects.filter(
        toy_cat=4) & Toy.objects.filter(
        in_stock__gt=0)
    if len(presents) > 0:
        l = len(presents)
        p = randint(0, l - 1)
        present = presents[p]
        context = {
            'present': present,
            'current_user_name': current_user_name,
            'action': action}
        return render(request, 'present.html', context)
    else:
        context = {'current_user_name': current_user_name}
        return render(request, 'no_present.html', context)


def shop_page(request):
    '''
    Получает из текста GET-запроса категорию игрушек.
    0-категория - игрушки первых двух категорий (мальчишкам и девчонкам)
    Исключает из списка отсутствующие на складе игрушки (in_stock__gt = 0)
    Возвращает рендер шаблона toy_selection.html
    :param request:
    :return:
    '''
    global current_user, current_user_name
    toy_cat = request.GET.get('toy_cat', 0)
    pn = 'Выбери игрушку по своему вкусу!'
    if toy_cat == 0:
        Toys = Toy.objects.filter(in_stock__gt=0).exclude(toy_cat__gt=2)
    else:
        Toys = Toy.objects.filter(
            toy_cat=toy_cat) & Toy.objects.filter(
            in_stock__gt=0)
    context = {'pn': pn, 'Toys': Toys, 'current_user': current_user,
               'current_user_name': current_user_name, 'toy_cat': toy_cat}
    return render(request, 'toy_selection.html', context)


def purchase_confirm(request):
    '''
    Подготавливает данные для страницы подтверждения покупки.
    Подбирает случайное прилагательное из списка good_words, чтобы похвалить выбор клиента.
    Ведь "Клиент всегда прав!" ))
    Возвращает рендер шаблона purchase_confirm.html
    :param request:
    :return:
    '''
    global current_user, current_user_name
    toy_id = request.GET.get('toy', 0)
    toy = Toy.objects.filter(id=toy_id)
    toy_title = toy[0].title
    toy_pic_fn = toy[0].picture_min
    toy_cost = toy[0].actual_cost
    user = Buyer.objects.filter(id=current_user)
    balance = user[0].balance
    good_words = [
        "хороший",
        "замечательный",
        "неплохой",
        "стильный",
        "прекрасный",
        "отличный"]
    word_nr = randint(0, len(good_words) - 1)
    good_word = good_words[word_nr]
    context = {
        'current_user_name': current_user_name,
        'balance': balance,
        'toy_id': toy_id,
        'toy_title': toy_title,
        'toy_cost': toy_cost,
        'toy_pic_fn': toy_pic_fn,
        'good_word': good_word}
    return render(request, 'purchase_confirm.html', context)


def basket_page(request):
    '''
    Подготавливает данные для страницы "Корзина"
    Возвращает рендер шаблона basket.html
    Выбор отображаемого рисунка (пустая/полная корзина) и текста заголовка страницы осуществляется на уровне шаблона.
    :param request:
    :return:
    '''
    global current_user, current_user_name
    pn = 'Корзина'
    toys = Basket.objects.filter(buyer_id=current_user)
    context = {
        'pn': pn,
        'current_user': current_user,
        'current_user_name': current_user_name,
        'toys': toys}
    return render(request, 'basket.html', context)


def logout_page(request):
    '''
    Функция выхода из системы.
    Сбрасывает значения переменных current_user и current_user_name.
    Возвращает рендер начальной страницы.
    :param request:
    :return:
    '''
    global current_user, current_user_name
    current_user = 0
    current_user_name = ''
    pn = 'Добро пожаловать в наш игрушечный магазин игрушек!'
    context = {'pn': pn, 'current_user': current_user}
    return render(request, 'main_page.html', context)


def login_page(request):
    '''
    Функция входа в систему, получив GET-запрос, берет информационную структуру формы из класса LoginForm и возвращает
    рендер шаблона login_page.html (т.е. отрисовывает незаполненную форму входа в систему).
    В случае POST-запроса принимает внесенные пользователем данные, производит их валидацию и обрабатывает следующим образом:
    1. ищет указанное имя пользователя в базе данных;
    2а. в случае отсутствия искомого имени возвращает HttpResponse с указанием ошибки;
    2б. если имя найдено, сравнивает значение хэш-функции содержимого поля 'password', со значением в БД;
    3а. в случае совпадения значений обновляет значение переменных current_user и current_user_name и возвращает
        рендер шаблона toy_selection.html (каталог игрушек).
    3б. в случае несовпадения значений возвращает HttpResponse с указанием ошибки;
    :param request:
    :return:
    '''
    global current_user, current_user_name
    pn = 'Мы рады Вас видеть!'
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            pwd_enc = password.encode()
            pwd_hash = hashlib.md5(pwd_enc)
            buyers = Buyer.objects.all()
            user_presents = False
            for buyer in buyers:
                if buyer.name == username:
                    user_presents = True
                    if buyer.psw == pwd_hash.hexdigest():
                        current_user = buyer.id
                        current_user_name = buyer.name
                        pn = 'Выбери игрушку по своему вкусу!'
                        Toys = Toy.objects.filter(in_stock__gt=0)
                        context = {
                            'pn': pn,
                            'Toys': Toys,
                            'current_user': current_user,
                            'current_user_name': current_user_name}
                        return render(request, 'toy_selection.html', context)
                    else:
                        response = 'Ошибка логина или пароля!'
                        return HttpResponse(response)
                    break
            if not user_presents:
                response = 'Данный пользователь не зарегистрирован.'
                return HttpResponse(response)
    else:
        form = LoginForm()
    context = {'pn': pn, 'form': form, 'current_user': current_user}
    return render(request, 'login_page.html', context)


def show_max(request):
    '''
    Функция подготовки данных для отображения страницы детального просмотра товара (как правило анимированного)
    Взывается нажатием кнопки "Посмотреть" на странице каталога.
    Принимает из GET-запроса id игрушки.
    Возвращает рендер шаблона show_max.html.
    :param request:
    :return:
    '''
    toy_id = request.GET.get('toy_id', 0)
    toys = Toy.objects.filter(id=toy_id)
    toy = toys[0]
    pic_fn = str(toy.picture_max)
    return render(
        request, 'show_max.html', {
            'pn': 'Можно рассмотреть повнимательнее...', 'toy_pic': pic_fn})


def registration(request):
    '''
    Функция регистрации нового пользователя, получив GET-запрос, берет информационную структуру формы из класса
    DjangoRegForm и возвращает рендер шаблона django_reg.html (т.е. отрисовывает незаполненную форму регистрации).
    В случае POST-запроса принимает внесенные пользователем данные, производит их валидацию и обрабатывает следующим образом:
    1. Проверяет соответствие введенного возраста минимально допустимому (10 лет). В случае несоответствия возвращает
       HttpResponse с указанием ошибки;
    2. Проверяет совпадение содержимого полей "password" и "re_password". В случае несовпадения HttpResponse с указанием
       ошибки;
    3. Просматривает базу данных, сравнивая уже имеющиеся имена пользователей с нововведенным. В случае нахождения
       возвращает HttpResponse с указанием ошибки;
    4. Во всех остальных случаях создает объект класса Buyer (вносит в БД нового пользователя), кодируе введенный пароль
       с помощью алгоритма md5.
    5. Обновляет значение переменных current_user и current_user_name и возвращает рендер шаблона toy_selection.html (каталог игрушек).
    6. Возвращает рендер шаблона toy_selection.html (каталог игрушек).
    :param request:
    :return:
    '''
    global current_user, current_user_name
    pn = 'Use this form for registration.'
    if request.method == 'POST':
        form = DjangoRegForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            password = form.cleaned_data['password']
            re_password = form.cleaned_data['re_password']
            result = False
            if int(age) < 10:
                response = 'Вы слишком молоды для этого сайта!'
            elif password != re_password:
                response = 'Не совпадают введенные пароли!'
            else:
                result = True
            if result:
                buyers = Buyer.objects.all()
                for buyer in buyers:
                    if buyer.name == username:
                        response = 'Пользователь с этим именем уже зареристрирован!'
                        return HttpResponse(response)
                pwd_enc = password.encode()
                pwd_hash = hashlib.md5(pwd_enc)
                Buyer.objects.create(
                    name=username,
                    balance=100,
                    age=age,
                    psw=pwd_hash.hexdigest())
                new_buyer = Buyer.objects.get(name=username)
                current_user = new_buyer.id
                current_user_name = new_buyer.name
                return redirect('http://127.0.0.1:8000/toys/')
            else:
                return HttpResponse(response)
    else:
        form = DjangoRegForm()
    contest = {'pn': pn, 'form': form, 'current_user': current_user}
    return render(request, 'django_reg.html', contest)


def buy_toy(request):
    '''
    Функция покупки игрушки.
    1. Получает id игрушки из GET-запроса.
    2. Создает объект Basket. (Строку в таблице на странице "Корзина" / Запись в БД)
    3. Уменьшает на 1 параметр in_stock (доступное количество) объекта toy (выбранной игрушки).
    4. Уменьшает баланс пользователя на актуальную стоимость приобретенной игрушки.
    Формирует контекст и возвращает рендер шаблона basket.html - текущее состояние корзины пользователя.
    :param request:
    :return:
    '''
    global current_user, current_user_name
    toy_id = request.POST.get('toy_id')
    # Логика обработки покупки игрушки
    toy = (Toy.objects.filter(id=toy_id))[0]
    buyer = Buyer.objects.filter(id=current_user)[0]
    Basket.objects.create(
        buyer_id=buyer, toy_id=toy, toy_name=Toy.objects.get(
            id=toy_id).title, toy_descr=Toy.objects.get(
            id=toy_id).description)
    toy.in_stock = toy.in_stock - 1
    toy.save()
    buyers = Buyer.objects.filter(id=current_user)
    buyer = buyers[0]
    buyer.balance -= toy.actual_cost
    buyer.save()
    pn = 'Корзина'
    toys = Basket.objects.filter(buyer_id=current_user)
    context = {
        'pn': pn,
        'current_user': current_user,
        'current_user_name': current_user_name,
        'toys': toys}
    return render(request, 'basket.html', context)
