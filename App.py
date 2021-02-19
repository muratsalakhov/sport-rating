from tkinter import *


# Класс приложения.
class App():

    # Очистка окна.
    def clear(app, root):
        list = root.grid_slaves()
        for l in list:
            l.destroy()

    # Меню.
    def MenuShow(app, root):
        app.clear(root)
        root.title("Рейтинг спортсменов")
        root.geometry('430x500+200+100')

        Label(text="РЕЙТИНГ СПОРТСМЕНОВ", pady=10, padx=10,
              justify=CENTER, font=("Verdana", 24)).grid(row=1, pady=20)

        football_button = Button(text="Футбол",
                                 command=lambda: app.FootballShow(root),
                                 justify=CENTER, font=("Verdana", 15),
                                 bg='#ABFF7A', activebackground='#93DB69',
                                 width=15, pady=10).grid(row=2, pady=15)

        basketball_button = Button(text="Баскетбол",
                                   command=lambda: app.BasketballShow(root),
                                   justify=CENTER, font=("Verdana", 15),
                                   bg='#FFB30F', activebackground='#C9590E',
                                   width=15, pady=10).grid(row=3, pady=15)

        hockey_button = Button(text="Хоккей",
                               command=lambda: app.HockeyShow(root),
                               justify=CENTER, font=("Verdana", 15),
                               bg='#4EBBFF', activebackground='#419DD6',
                               width=15, pady=10).grid(row=4, pady=15)

        exit_button = Button(text="Выход",
                             command=lambda: root.withdraw(),
                             justify=CENTER, font=("Verdana", 15),
                             bg='#FF796F', activebackground='#C15B54',
                             width=15, pady=10).grid(row=5, pady=15)
        root.mainloop()

    # Рейтинг футболистов.
    def FootballShow(app, root):

        app.clear(root)
        root.title("Рейтинг футболистов")
        root.geometry('625x680+200+100')

        # Класс ячейки списка.
        class Node:
            def __init__(list, name='None', match=None,
                         goals=None, assists=None,
                         ycards=None, rcards=None,
                         rating=None):
                list.name = name  # имя игрока
                list.match = match  # кол-во матчей
                list.goals = goals  # кол-во голов
                list.assists = assists  # кол-во ассистов
                list.ycards = ycards  # кол-во желтых карточек
                list.rcards = rcards  # кол-во красных карточек
                list.rating = rating  # фамилия игрока
                list.next = None  # ссылка на след. элемент

        # Класс списка.
        class LinkedList:
            def __init__(self):
                self.head = None

            # Вставка нового элемента.
            def appendList(self, name, match, goals,
                           assists, ycards, rcards, rating):
                node = Node(name, match, goals,
                            assists, ycards, rcards, rating)
                if self.head is None:
                    self.head = node
                else:
                    curr = self.head
                    while curr.next is not None:
                        curr = curr.next
                    curr.next = node

            # Вставка сортируя по имени.
            def appendSortedName(self, name, match, goals,
                                 assists, ycards, rcards, rating):
                node = Node(name, match, goals,
                            assists, ycards, rcards, rating)
                curr = self.head
                prev = None
                while curr is not None and curr.name < name:
                    prev = curr
                    curr = curr.next
                if prev is None:
                    self.head = node
                else:
                    prev.next = node
                node.next = curr

            # Вставка сортируя по матчам.
            def appendSortedMatch(self, name, match, goals,
                                  assists, ycards, rcards, rating):
                node = Node(name, match, goals,
                            assists, ycards, rcards, rating)
                curr = self.head
                prev = None
                while curr is not None and curr.match > match:
                    prev = curr
                    curr = curr.next
                if prev is None:
                    self.head = node
                else:
                    prev.next = node
                node.next = curr

            # Вставка сортируя по голам.
            def appendSortedGoals(self, name, match, goals,
                                  assists, ycards, rcards, rating):
                node = Node(name, match, goals,
                            assists, ycards, rcards, rating)
                curr = self.head
                prev = None
                while curr is not None and curr.goals > goals:
                    prev = curr
                    curr = curr.next
                if prev is None:
                    self.head = node
                else:
                    prev.next = node
                node.next = curr

            # Вставка сортируя по голевым передачам
            def appendSortedAssists(self, name, match, goals,
                                    assists, ycards, rcards, rating):
                node = Node(name, match, goals,
                            assists, ycards, rcards, rating)
                curr = self.head
                prev = None
                while curr is not None and curr.assists > assists:
                    prev = curr
                    curr = curr.next
                if prev is None:
                    self.head = node
                else:
                    prev.next = node
                node.next = curr

            # Вставка сортируя по желтым карточкам.
            def appendSortedYcards(self, name, match, goals,
                                   assists, ycards, rcards, rating):
                node = Node(name, match, goals,
                            assists, ycards, rcards, rating)
                curr = self.head
                prev = None
                while curr is not None and curr.ycards > ycards:
                    prev = curr
                    curr = curr.next
                if prev is None:
                    self.head = node
                else:
                    prev.next = node
                node.next = curr

            # Вставка сортируя по красным карточкам.
            def appendSortedRcards(self, name, match, goals,
                                   assists, ycards, rcards, rating):
                node = Node(name, match, goals,
                            assists, ycards, rcards, rating)
                curr = self.head
                prev = None
                while curr is not None and curr.rcards > rcards:
                    prev = curr
                    curr = curr.next
                if prev is None:
                    self.head = node
                else:
                    prev.next = node
                node.next = curr

            # Вставка сортируя по рейтингу.
            def appendSortedRating(self, name, match, goals,
                                   assists, ycards, rcards, rating):
                node = Node(name, match, goals,
                            assists, ycards, rcards, rating)
                curr = self.head
                prev = None
                while curr is not None and curr.rating > rating:
                    prev = curr
                    curr = curr.next
                if prev is None:
                    self.head = node
                else:
                    prev.next = node
                node.next = curr

            # Напечатать список.
            def printList(self):
                curr = self.head
                while curr is not None:
                    print(curr.name)
                    print ("%d->" % curr.match),
                    curr = curr.next
                print ("NULL")

        # Заполнение списка футболистами.
        PLAYERS_COUNT = 20
        List = LinkedList()
        List.appendList("Фернандиньо", 13, 1, 2, 2, 0, 7.49)
        List.appendList("Родриго Де Пауль", 13, 6, 3, 3, 0, 7.52)
        List.appendList("Лукаш Пищек", 8, 1, 2, 0, 0, 7.52)
        List.appendList("Юсуф Атал", 7, 1, 0, 3, 0, 7.53)
        List.appendList("Лерой Сане", 6, 5, 4, 1, 0, 7.55)
        List.appendList("Мохаммед Салах", 13, 7, 3, 0, 0, 7.57)
        List.appendList("Марко Ройс", 12, 8, 4, 1, 0, 7.58)
        List.appendList("Серхио Агуэро", 13, 8, 4, 2, 0, 7.69)
        List.appendList("Себастьен Халлер", 10, 9, 6, 1, 0, 7.69)
        List.appendList("Тежи Саванье", 9, 2, 3, 1, 1, 7.75)
        List.appendList("Эдинсон Кавани", 9, 9, 1, 0, 0, 7.76)
        List.appendList("Сусо", 13, 4, 8, 2, 0, 7.73)
        List.appendList("Давид Сильва", 11, 5, 2, 1, 0, 7.8)
        List.appendList("Эден Азар", 9, 7, 4, 2, 0, 7.9)
        List.appendList("Торган Азар", 12, 8, 5, 1, 0, 7.92)
        List.appendList("Рахим Стерлинг", 11, 7, 6, 1, 0, 7.93)
        List.appendList("Криштиану Роналду", 13, 9, 5, 0, 0, 7.95)
        List.appendList("Килиан Мбаппе", 7, 11, 4, 2, 1, 8.19)
        List.appendList("Неймар", 11, 10, 5, 2, 0, 8.48)
        List.appendList("Лионель Месси", 10, 9, 6, 1, 0, 8.48)

        # Создание таблицы.
        LabelList = []
        for i in range(PLAYERS_COUNT):
            LabelList.append([])
            LabelList[i].append(Label(pady=5, padx=5, justify=CENTER))
            LabelList[i].append(Label(pady=5, padx=5, justify=CENTER))
            LabelList[i].append(Label(pady=5, padx=5, justify=CENTER))
            LabelList[i].append(Label(pady=5, padx=5, justify=CENTER))
            LabelList[i].append(Label(pady=5, padx=5, justify=CENTER))
            LabelList[i].append(Label(pady=5, padx=5, justify=CENTER))
            LabelList[i].append(Label(pady=5, padx=5, justify=CENTER))

        # Заполнение таблицы
        def LabelListReload(List, LabelList):
            current = List.head
            i = 0
            while current is not None:
                LabelList[i][0]['text'] = current.name
                LabelList[i][1]['text'] = current.match
                LabelList[i][2]['text'] = current.goals
                LabelList[i][3]['text'] = current.assists
                LabelList[i][4]['text'] = current.ycards
                LabelList[i][5]['text'] = current.rcards
                LabelList[i][6]['text'] = current.rating
                current = current.next
                i += 1
            for i in range(PLAYERS_COUNT):
                for j in range(7):
                    LabelList[i][j].grid(row=i+3, column=j)

        # Запуск сортировки
        def sorting(list, LabelList, btn):
            ShowList = LinkedList()
            curr = list.head
            while curr is not None:
                if btn == 1:
                    ShowList.appendSortedName(curr.name, curr.match,
                                              curr.goals, curr.assists,
                                              curr.ycards, curr.rcards,
                                              curr.rating)
                elif btn == 2:
                    ShowList.appendSortedMatch(curr.name, curr.match,
                                               curr.goals, curr.assists,
                                               curr.ycards, curr.rcards,
                                               curr.rating)
                elif btn == 3:
                    ShowList.appendSortedGoals(curr.name, curr.match,
                                               curr.goals, curr.assists,
                                               curr.ycards, curr.rcards,
                                               curr.rating)
                elif btn == 4:
                    ShowList.appendSortedAssists(curr.name, curr.match,
                                                 curr.goals, curr.assists,
                                                 curr.ycards, curr.rcards,
                                                 curr.rating)
                elif btn == 5:
                    ShowList.appendSortedYcards(curr.name, curr.match,
                                                curr.goals, curr.assists,
                                                curr.ycards, curr.rcards,
                                                curr.rating)
                elif btn == 6:
                    ShowList.appendSortedRcards(curr.name, curr.match,
                                                curr.goals, curr.assists,
                                                curr.ycards, curr.rcards,
                                                curr.rating)
                else:
                    ShowList.appendSortedRating(curr.name, curr.match,
                                                curr.goals, curr.assists,
                                                curr.ycards, curr.rcards,
                                                curr.rating)
                curr = curr.next
            LabelListReload(ShowList, LabelList)

        # Отображение витжетов
        menu_button = Button(text="Меню",
                             command=lambda: app.MenuShow(root),
                             justify=CENTER, font=("Verdana", 10),
                             padx=17, pady=17)
        menu_button.grid(row=0, column=6)

        Label(text="РЕЙТИНГ ФУТБОЛИСТОВ", pady=10, padx=65,
              justify=CENTER, bg='#ABFF7A',
              font=("Verdana", 24)).grid(row=0, column=0, columnspan=6)

        name_button = Button(text="Имя",
                             command=lambda: sorting(List, LabelList, 1),
                             justify=CENTER, font=("Verdana", 10),
                             pady=3, padx=10, width=25)
        name_button.grid(row=1, column=0)

        match_button = Button(text="Матчи",
                              command=lambda: sorting(List, LabelList, 2),
                              justify=CENTER, font=("Verdana", 10),
                              pady=3, padx=10)
        match_button.grid(row=1, column=1)

        goal_button = Button(text="Голы",
                             command=lambda: sorting(List, LabelList, 3),
                             justify=CENTER, font=("Verdana", 10),
                             pady=3, padx=10)
        goal_button.grid(row=1, column=2)

        assist_button = Button(text="Пасы",
                               command=lambda: sorting(List, LabelList, 4),
                               justify=CENTER, font=("Verdana", 10),
                               pady=3, padx=10)
        assist_button.grid(row=1, column=3)

        yellow_button = Button(text="ЖК",
                               command=lambda: sorting(List, LabelList, 5),
                               justify=CENTER, font=("Verdana", 10),
                               pady=3, padx=10)
        yellow_button.grid(row=1, column=4)

        red_button = Button(text="КК",
                            command=lambda: sorting(List, LabelList, 6),
                            justify=CENTER, font=("Verdana", 10),
                            pady=3, padx=10)
        red_button.grid(row=1, column=5)

        rating_button = Button(text="Рейтинг",
                               command=lambda: sorting(List, LabelList, 7),
                               justify=CENTER, font=("Verdana", 10),
                               pady=3, padx=10)
        rating_button.grid(row=1, column=6)
        sorting(List, LabelList, 7)

    # Рейтинг баскетболистов.
    def BasketballShow(app, root):
        app.clear(root)
        root.title("Рейтинг баскетболистов")
        root.geometry('815x680+200+100')

        # Класс ячейки списка.
        class Node:
            def __init__(list, name='None', team='None', position='None',
                         average=None, summ=None,
                         maximum=None, games=None):
                list.name = name  # имя
                list.team = team  # позиция
                list.position = position  # амплуа
                list.average = average  # кол-во среднее
                list.summ = summ  # кол-во всего очков
                list.maximum = maximum  # кол-во макс за игру
                list.games = games  # кол-во игр
                list.next = None  # ссылка на след. элемент

        # Класс списка.
        class LinkedList:

            def __init__(self):
                self.head = None

            # Вставка в конец списка.
            def appendList(self, name, team, position,
                           average, summ, maximum, games):
                node = Node(name, team, position,
                            average, summ, maximum, games)
                if self.head is None:
                    self.head = node
                else:
                    curr = self.head
                    while curr.next is not None:
                        curr = curr.next
                    curr.next = node

            # Вставка сортируя по имени.
            def appendSortedName(self, name, team, position,
                                 average, summ, maximum, games):
                node = Node(name, team, position,
                            average, summ, maximum, games)
                curr = self.head
                prev = None
                while curr is not None and curr.name < name:
                    prev = curr
                    curr = curr.next
                if prev is None:
                    self.head = node
                else:
                    prev.next = node
                node.next = curr

            # Вставка сортируя по команде.
            def appendSortedTeam(self, name, team, position,
                                 average, summ, maximum, games):
                node = Node(name, team, position,
                            average, summ, maximum, games)
                curr = self.head
                prev = None
                while curr is not None and curr.team < team:
                    prev = curr
                    curr = curr.next
                if prev is None:
                    self.head = node
                else:
                    prev.next = node
                node.next = curr

            # Вставка сортируя по позиции.
            def appendSortedPosition(self, name, team, position,
                                     average, summ, maximum, games):
                node = Node(name, team, position,
                            average, summ, maximum, games)
                curr = self.head
                prev = None
                while curr is not None and curr.position < position:
                    prev = curr
                    curr = curr.next
                if prev is None:
                    self.head = node
                else:
                    prev.next = node
                node.next = curr

            # Вставка сортируя по среднему количеству очков.
            def appendSortedAverage(self, name, team, position,
                                    average, summ, maximum, games):
                node = Node(name, team, position,
                            average, summ, maximum, games)
                curr = self.head
                prev = None
                while curr is not None and curr.average > average:
                    prev = curr
                    curr = curr.next
                if prev is None:
                    self.head = node
                else:
                    prev.next = node
                node.next = curr

            # Вставка сортируя по сумме очков.
            def appendSortedSumm(self, name, team, position,
                                 average, summ, maximum, games):
                node = Node(name, team, position,
                            average, summ, maximum, games)
                curr = self.head
                prev = None
                while curr is not None and curr.summ > summ:
                    prev = curr
                    curr = curr.next
                if prev is None:
                    self.head = node
                else:
                    prev.next = node
                node.next = curr

            # Вставка сортируя по максимальному количеству очков.
            def appendSortedMaximum(self, name, team, position,
                                    average, summ, maximum, games):
                node = Node(name, team, position,
                            average, summ, maximum, games)
                curr = self.head
                prev = None
                while curr is not None and curr.maximum > maximum:
                    prev = curr
                    curr = curr.next
                if prev is None:
                    self.head = node
                else:
                    prev.next = node
                node.next = curr

            # Вставка сортируя по количеству игр.
            def appendSortedGames(self, name, team, position,
                                  average, summ, maximum, games):
                node = Node(name, team, position,
                            average, summ, maximum, games)
                curr = self.head
                prev = None
                while curr is not None and curr.games > games:
                    prev = curr
                    curr = curr.next
                if prev is None:
                    self.head = node
                else:
                    prev.next = node
                node.next = curr

            # Печать списка.
            def printList(self):
                curr = self.head
                while curr is notNone:
                    print(curr.name)
                    print ("%d->" % curr.match),
                    curr = curr.next
                print ("NULL")

        # Заполнение списка баскетболистами.
        PLAYERS_COUNT = 20
        List = LinkedList()
        List.appendList("Кемба Уокер", "Шарлотт Хорнетс", "защитник",
                        22.1, 1770, 47, 80)
        List.appendList("Джимми Батлер", "Миннесота Тимбервулвз", "форвард",
                        22.2, 1307, 39, 59)
        List.appendList("Брэдли Бил", "Вашингтон Уизардс", "защитник",
                        22.6, 1857, 51, 82)
        List.appendList("Лу Уильямс", "Лос-Анджелес Клипперс", "защитник",
                        22.6, 1782, 50,  79)
        List.appendList("Кристапс Порзингис", "Нью-Йорк Никс", "форвард",
                        22.7, 1088, 40, 48)
        List.appendList("Джоэл Эмбиид", "Филадельфия Сиксерс", "центровой",
                        22.9, 1445, 46, 63)
        List.appendList("Демар Дерозан", "Торонто Рэпторс", "защитник",
                        23.0, 1840, 52,  80)
        List.appendList("Виктор Оладипо", "Индиана Пэйсерс", "защитник",
                        23.1, 1735, 47, 75)
        List.appendList("Ламаркус Олдридж", "Сан-Антонио Сперс", "форвард",
                        23.1, 1735, 45, 75)
        List.appendList("Кайри Ирвинг", "Бостон Селтикс", "защитник",
                        24.4, 1466, 47, 60)
        List.appendList("Девин Букер", "Финикс Санз", "защитник",
                        24.9, 1346, 46, 54)
        List.appendList("Демаркус Казинс", "Нью-Орлеан Пеликанс", "форвард",
                        25.2, 1210, 44, 48)
        List.appendList("Расселл Уэстбрук", "Оклахома-Сити Тандер", "защитник",
                        25.4, 2028, 46, 80)
        List.appendList("Кевин Дюрант", "Голден Стэйт Уорриорз", "форвард",
                        26.4, 1793, 50, 68)
        List.appendList("Стивен Карри", "Голден Стэйт Уорриорз", "защитник",
                        26.4, 1346, 49, 51)
        List.appendList("Яннис Адетокунбо", "Милуоки Бакс", "форвард",
                        26.9, 2014, 44, 75)
        List.appendList("Дэмьен Лиллард", "Портленд Трэйл Блэйзерс",
                        "защитник", 26.9, 1962, 50, 73)
        List.appendList("Леброн Джеймс", "Кливленд Кавальерс", "форвард",
                        27.5, 2251, 57, 82)
        List.appendList("Энтони Дэвис", "Нью-Орлеан Пеликанс", "форвард",
                        28.1, 2110, 53, 75)
        List.appendList("Джеймс Харден", "Хьюстон Рокетс", "защитник",
                        30.4, 2191, 60, 72)

        # Создание таблицы.
        LabelList = []
        for i in range(PLAYERS_COUNT):
            LabelList.append([])
            LabelList[i].append(Label(pady=5, padx=5, justify=CENTER))
            LabelList[i].append(Label(pady=5, padx=5, justify=CENTER))
            LabelList[i].append(Label(pady=5, padx=5, justify=CENTER))
            LabelList[i].append(Label(pady=5, padx=5, justify=CENTER))
            LabelList[i].append(Label(pady=5, padx=5, justify=CENTER))
            LabelList[i].append(Label(pady=5, padx=5, justify=CENTER))
            LabelList[i].append(Label(pady=5, padx=5, justify=CENTER))

        # Заполнение таблицы.
        def LabelListReload(List, LabelList):
            current = List.head
            i = 0
            while current is not None:
                LabelList[i][0]['text'] = current.name
                LabelList[i][1]['text'] = current.team
                LabelList[i][2]['text'] = current.position
                LabelList[i][3]['text'] = current.average
                LabelList[i][4]['text'] = current.summ
                LabelList[i][5]['text'] = current.maximum
                LabelList[i][6]['text'] = current.games
                current = current.next
                i += 1
            for i in range(PLAYERS_COUNT):
                for j in range(7):
                    LabelList[i][j].grid(row=i+3, column=j)

        # Сортировка списка.
        def sorting(list, LabelList, btn):
            ShowList = LinkedList()
            curr = list.head
            while curr is not None:
                if btn == 1:
                    ShowList.appendSortedName(curr.name, curr.team,
                                              curr.position, curr.average,
                                              curr.summ, curr.maximum,
                                              curr.games)
                elif btn == 2:
                    ShowList.appendSortedTeam(curr.name, curr.team,
                                              curr.position, curr.average,
                                              curr.summ, curr.maximum,
                                              curr.games)
                elif btn == 3:
                    ShowList.appendSortedPosition(curr.name, curr.team,
                                                  curr.position, curr.average,
                                                  curr.summ, curr.maximum,
                                                  curr.games)
                elif btn == 4:
                    ShowList.appendSortedAverage(curr.name, curr.team,
                                                 curr.position, curr.average,
                                                 curr.summ, curr.maximum,
                                                 curr.games)
                elif btn == 5:
                    ShowList.appendSortedSumm(curr.name, curr.team,
                                              curr.position, curr.average,
                                              curr.summ, curr.maximum,
                                              curr.games)
                elif btn == 6:
                    ShowList.appendSortedMaximum(curr.name, curr.team,
                                                 curr.position, curr.average,
                                                 curr.summ, curr.maximum,
                                                 curr.games)
                else:
                    ShowList.appendSortedGames(curr.name, curr.team,
                                               curr.position, curr.average,
                                               curr.summ, curr.maximum,
                                               curr.games)
                curr = curr.next
            LabelListReload(ShowList, LabelList)

        # Заполнение окна.
        menu_button = Button(text="Меню",
                             command=lambda: app.MenuShow(root),
                             justify=CENTER, font=("Verdana", 10),
                             padx=17, pady=17)
        menu_button.grid(row=0, column=6)

        Label(text="РЕЙТИНГ БАСКЕТБОЛИСТОВ", pady=10, padx=130,
              justify=CENTER, bg='#FFB30F',
              font=("Verdana", 24)).grid(row=0, column=0, columnspan=6)

        name_button = Button(text="Имя",
                             command=lambda: sorting(List, LabelList, 1),
                             justify=CENTER, font=("Verdana", 10),
                             pady=3, padx=10, width=25)
        name_button.grid(row=1, column=0)

        match_button = Button(text="Команда",
                              command=lambda: sorting(List, LabelList, 2),
                              justify=CENTER, font=("Verdana", 10),
                              pady=3, padx=45)
        match_button.grid(row=1, column=1)

        goal_button = Button(text="Позиция",
                             command=lambda: sorting(List, LabelList, 3),
                             justify=CENTER, font=("Verdana", 10),
                             pady=3, padx=10)
        goal_button.grid(row=1, column=2)

        assist_button = Button(text="Среднее",
                               command=lambda: sorting(List, LabelList, 4),
                               justify=CENTER, font=("Verdana", 10),
                               pady=3, padx=10)
        assist_button.grid(row=1, column=3)

        yellow_button = Button(text="Сумма",
                               command=lambda: sorting(List, LabelList, 5),
                               justify=CENTER, font=("Verdana", 10),
                               pady=3, padx=10)
        yellow_button.grid(row=1, column=4)

        red_button = Button(text="Максимум",
                            command=lambda: sorting(List, LabelList, 6),
                            justify=CENTER, font=("Verdana", 10),
                            pady=3, padx=10)
        red_button.grid(row=1, column=5)

        rating_button = Button(text="Игры",
                               command=lambda: sorting(List, LabelList, 7),
                               justify=CENTER, font=("Verdana", 10),
                               pady=3, padx=20)
        rating_button.grid(row=1, column=6)
        sorting(List, LabelList, 7)

    # Рейтинг хоккеистов.
    def HockeyShow(app, root):
        app.clear(root)
        root.title("Рейтинг хоккеистов")
        root.geometry('770x680+200+100')

        # Класс ячейки списка.
        class Node:
            def __init__(list, name='None', team='None', position='None',
                         total=None, goals=None, assists=None,
                         games=None):
                list.name = name  # имя
                list.team = team  # команда
                list.position = position  # амплуа
                list.total = total  # гол+пас
                list.goals = goals  # кол-во голов
                list.assists = assists  # кол-во пасов
                list.games = games  # кол-во игр
                list.next = None  # ссылка на след. элемент

        # Класс списка
        class LinkedList:
            def __init__(self):
                self.head = None

            # Вставка в конец списка.
            def appendList(self, name, team, position,
                           total, goals, assists, games):
                node = Node(name, team, position,
                            total, goals, assists, games)
                if self.head is None:
                    self.head = node
                else:
                    curr = self.head
                    while curr.next is not None:
                        curr = curr.next
                    curr.next = node

            # Вставка сортируя по имени.
            def appendSortedName(self, name, team, position,
                                 total, goals, assists, games):
                node = Node(name, team, position,
                            total, goals, assists, games)
                curr = self.head
                prev = None
                while curr is not None and curr.name < name:
                    prev = curr
                    curr = curr.next
                if prev is None:
                    self.head = node
                else:
                    prev.next = node
                node.next = curr

            # Вставка сортируя по команде.
            def appendSortedTeam(self, name, team, position,
                                 total, goals, assists, games):
                node = Node(name, team, position,
                            total, goals, assists, games)
                curr = self.head
                prev = None
                while curr is not None and curr.team < team:
                    prev = curr
                    curr = curr.next
                if prev is None:
                    self.head = node
                else:
                    prev.next = node
                node.next = curr

            # Вставка сортируя по позиции.
            def appendSortedPosition(self, name, team, position,
                                     total, goals, assists, games):
                node = Node(name, team, position,
                            total, goals, assists, games)
                curr = self.head
                prev = None
                while curr is not None and curr.position < position:
                    prev = curr
                    curr = curr.next
                if prev is None:
                    self.head = node
                else:
                    prev.next = node
                node.next = curr

            # Вставка сортируя по количеству гол+пас.
            def appendSortedTotal(self, name, team, position,
                                  total, goals, assists, games):
                node = Node(name, team, position,
                            total, goals, assists, games)
                curr = self.head
                prev = None
                while curr is not None and curr.total > total:
                    prev = curr
                    curr = curr.next
                if prev is None:
                    self.head = node
                else:
                    prev.next = node
                node.next = curr

            # Вставка сортируя по голам.
            def appendSortedGoals(self, name, team, position,
                                  total, goals, assists, games):
                node = Node(name, team, position,
                            total, goals, assists, games)
                curr = self.head
                prev = None
                while curr is not None and curr.goals > goals:
                    prev = curr
                    curr = curr.next
                if prev is None:
                    self.head = node
                else:
                    prev.next = node
                node.next = curr

            # Вставка сортируя по передачам.
            def appendSortedAssists(self, name, team, position,
                                    total, goals, assists, games):
                node = Node(name, team, position,
                            total, goals, assists, games)
                curr = self.head
                prev = None
                while curr is not None and curr.assists > assists:
                    prev = curr
                    curr = curr.next
                if prev is None:
                    self.head = node
                else:
                    prev.next = node
                node.next = curr

            # Вставка сортируя по играм.
            def appendSortedGames(self, name, team, position,
                                  total, goals, assists, games):
                node = Node(name, team, position,
                            total, goals, assists, games)
                curr = self.head
                prev = None
                while curr is not None and curr.games > games:
                    prev = curr
                    curr = curr.next
                if prev is None:
                    self.head = node
                else:
                    prev.next = node
                node.next = curr

            # Печать списка
            def printList(self):
                curr = self.head
                while curr is not None:
                    print(curr.name)
                    print ("%d->" % curr.match),
                    curr = curr.next
                print ("NULL")

        # Заполнение списка хоккеистов.
        PLAYERS_COUNT = 20
        List = LinkedList()
        List.appendList("Артемий Панарин", "Коламбус Блю Джетс", "нападающий",
                        82, 27, 55, 81)
        List.appendList("Евгений Кузнецов", "Вашингтон Кэпиталз", "нападающий",
                        83, 27, 56, 79)
        List.appendList("Джонни Годро", "Калгари Флэймз", "нападающий",
                        84, 24, 60, 80)
        List.appendList("Микко Рантанен", "Колорадо Эвеланш", "нападающий",
                        84, 29, 55, 81)
        List.appendList("Джон Таварес", "Нью-Йорк Айлендерс", "нападающий",
                        84, 37, 47, 82)
        List.appendList("Якуб Ворачек", "Филадельфия Флайерз", "нападающий",
                        85, 20, 65, 82)
        List.appendList("Мэтью Барзал", "Нью-Йорк Айлендерс", "нападающий",
                        85, 22, 63, 82)
        List.appendList("Брэд Маршан", "Бостон Брюинз", "нападающий",
                        85, 34, 51, 68)
        List.appendList("Стивен Стэмкос", "Тампа-Бэй Лайтнинг", "нападающий",
                        86, 27, 59, 78)
        List.appendList("Александр Овечкин", "Вашингтон Кэпиталз",
                        "нападающий", 87, 49, 38, 82)
        List.appendList("Сидни Кросби", "Питтсбург Пингвинз", "нападающий",
                        89, 29, 60, 82)
        List.appendList("Блейк Уилер", "Виннипег Джетс", "нападающий",
                        91, 23, 68, 81)
        List.appendList("Фил Кессел", "Питтсбург Пингвинз", "нападающий",
                        92, 34, 58, 82)
        List.appendList("Анже Копитар", "Лос-Анджелес Кингз", "нападающий",
                        92, 35, 57, 82)
        List.appendList("Тейлор Холл", "Нью-Джерси Дэвилз", "нападающий",
                        93, 39, 54, 76)
        List.appendList("Натан Маккиннон", "Колорадо Эвеланш", "нападающий",
                        97, 39, 58, 74)
        List.appendList("Евгений Малкин", "Питтсбург Пингвинз", "нападающий",
                        98, 42, 56, 78)
        List.appendList("Никита Кучеров", "Тампа-Бэй Лайтнинг", "нападающий",
                        100, 39, 61, 80)
        List.appendList("Клод Жиру", "Филадельфия Флайерз", "нападающий",
                        102, 34, 68, 82)
        List.appendList("Коннор Макдэвид", "Эдмонд Ойлерз", "нападающий",
                        108, 41, 67, 82)

        # Создание таблицы.
        LabelList = []
        for i in range(PLAYERS_COUNT):
            LabelList.append([])
            LabelList[i].append(Label(pady=5, padx=5, justify=CENTER))
            LabelList[i].append(Label(pady=5, padx=5, justify=CENTER))
            LabelList[i].append(Label(pady=5, padx=5, justify=CENTER))
            LabelList[i].append(Label(pady=5, padx=5, justify=CENTER))
            LabelList[i].append(Label(pady=5, padx=5, justify=CENTER))
            LabelList[i].append(Label(pady=5, padx=5, justify=CENTER))
            LabelList[i].append(Label(pady=5, padx=5, justify=CENTER))

        # Заполнение таблицы.
        def LabelListReload(List, LabelList):
            current = List.head
            i = 0
            while current is not None:
                LabelList[i][0]['text'] = current.name
                LabelList[i][1]['text'] = current.team
                LabelList[i][2]['text'] = current.position
                LabelList[i][3]['text'] = current.total
                LabelList[i][4]['text'] = current.goals
                LabelList[i][5]['text'] = current.assists
                LabelList[i][6]['text'] = current.games
                current = current.next
                i += 1
            for i in range(PLAYERS_COUNT):
                for j in range(7):
                    LabelList[i][j].grid(row=i+3, column=j)

        # Сортировка списка
        def sorting(list, LabelList, btn):
            ShowList = LinkedList()
            curr = list.head
            while curr is not None:
                if btn == 1:
                    ShowList.appendSortedName(curr.name, curr.team,
                                              curr.position, curr.total,
                                              curr.goals, curr.assists,
                                              curr.games)
                elif btn == 2:
                    ShowList.appendSortedTeam(curr.name, curr.team,
                                              curr.position, curr.total,
                                              curr.goals, curr.assists,
                                              curr.games)
                elif btn == 3:
                    ShowList.appendSortedPosition(curr.name, curr.team,
                                                  curr.position, curr.total,
                                                  curr.goals, curr.assists,
                                                  curr.games)
                elif btn == 4:
                    ShowList.appendSortedTotal(curr.name, curr.team,
                                               curr.position, curr.total,
                                               curr.goals, curr.assists,
                                               curr.games)
                elif btn == 5:
                    ShowList.appendSortedGoals(curr.name, curr.team,
                                               curr.position, curr.total,
                                               curr.goals, curr.assists,
                                               curr.games)
                elif btn == 6:
                    ShowList.appendSortedAssists(curr.name, curr.team,
                                                 curr.position, curr.total,
                                                 curr.goals, curr.assists,
                                                 curr.games)
                else:
                    ShowList.appendSortedGames(curr.name, curr.team,
                                               curr.position, curr.total,
                                               curr.goals, curr.assists,
                                               curr.games)
                curr = curr.next
            LabelListReload(ShowList, LabelList)

        # Заполнение окна вижетами
        menu_button = Button(text="Меню", command=lambda: app.MenuShow(root),
                             justify=CENTER, font=("Verdana", 10),
                             padx=17, pady=17)
        menu_button.grid(row=0, column=6)
        Label(text="РЕЙТИНГ ХОККЕИСТОВ", pady=10, padx=150,
              justify=CENTER, bg='#4EBBFF',
              font=("Verdana", 24)).grid(row=0, column=0, columnspan=6)

        name_button = Button(text="Имя",
                             command=lambda: sorting(List, LabelList, 1),
                             justify=CENTER, font=("Verdana", 10),
                             pady=3, padx=10, width=25)
        name_button.grid(row=1, column=0)

        match_button = Button(text="Команда",
                              command=lambda: sorting(List, LabelList, 2),
                              justify=CENTER, font=("Verdana", 10),
                              pady=3, padx=45)
        match_button.grid(row=1, column=1)

        goal_button = Button(text="Позиция",
                             command=lambda: sorting(List, LabelList, 3),
                             justify=CENTER, font=("Verdana", 10),
                             pady=3, padx=10)
        goal_button.grid(row=1, column=2)

        assist_button = Button(text="Гол+Пас",
                               command=lambda: sorting(List, LabelList, 4),
                               justify=CENTER, font=("Verdana", 10),
                               pady=3, padx=10)
        assist_button.grid(row=1, column=3)

        yellow_button = Button(text="Голы",
                               command=lambda: sorting(List, LabelList, 5),
                               justify=CENTER, font=("Verdana", 10),
                               pady=3, padx=10)
        yellow_button.grid(row=1, column=4)

        red_button = Button(text="Пасы",
                            command=lambda: sorting(List, LabelList, 6),
                            justify=CENTER, font=("Verdana", 10),
                            pady=3, padx=10)
        red_button.grid(row=1, column=5)

        rating_button = Button(text="Игры",
                               command=lambda: sorting(List, LabelList, 7),
                               justify=CENTER, font=("Verdana", 10),
                               pady=3, padx=20)
        rating_button.grid(row=1, column=6)
        sorting(List, LabelList, 7)


# Запуск программы.
def Run():
    root = Tk()
    app = App()
    app.MenuShow(root)
    root.mainloop()
