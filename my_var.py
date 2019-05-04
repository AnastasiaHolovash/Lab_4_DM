from tkinter import *
import random
import networkx as nx
import matplotlib.pylab as pl


class Lab4:

    def create_tabl_random(self, n):
        self.tabl = []
        for i in range(n):
            self.tabl.append([])
            for j in range(n):
                self.tabl[i].append(random.randint(0, 1))
        for i in range(n):
            for j in range(n):
                if i == j:
                    self.tabl[i][j] = 0
                else:
                    self.tabl[i][j] = self.tabl[j][i]
        return self.tabl

    def student(self, nzk=8206):
        self.slave = Toplevel(self.root)
        self.slave.title('Student')
        self.slave.focus_set()
        self.slave.minsize(300, 100)
        self.slave.maxsize(300, 100)
        self.slave['bg'] = 'seashell'
        self.slave.wm_geometry("+600+250")
        Label(self.slave, text='Головаш Анастасія\n'
                               'група ІВ-82\n'
                               'варіант {}'.format(divmod(nzk, 6)[1] + 1),
              justify=LEFT, font="Arial 17 bold", bg='seashell').pack(fill='both')

    def GraphColoring(self, matrix, nodes):
        """
        print(Edges)
        result = {}
        colors = ['red', 'blue', 'yellow', 'green', 'orange', 'springgreen', 'lime', 'olive', 'indigo', 'fuchsia']

        def SortEdges():
            sort_list = {}
            for key in Edges:
                sort_list[key] = len(Edges[key])
            sort2 = sorted(sort_list.items(), key=lambda x: x[1], reverse=True)

            return sort2

        def colorize():
            n = 0

            def removeColor():
                for color in colors:
                    if color not in stackColor: return color
                color = colors[n + 1]
                colors.append(color)
                return color

            for key in sort_list:
                stackColor = []
                for key2 in Edges[key[0]]:
                    if key2 in result: stackColor.append(result[key2])
                color = removeColor()
                result[key[0]] = color
            return result

        sort_list = SortEdges()
        print (colorize())
        return colorize()
        """
        # Максимально допустима кількість кольорів
        cmax = 10
        # n = 9  # кількість вершин графа

        n = nodes
        # Список кольорів вершин
        color = [0 for i in range(n)]
        a = matrix

        def visit(i):
            # Функція вибору фарби для розфарбування вершини з номером i
            def nicecolor():
                w = {0}
                newcol = 0
                for j in range(n):
                    if int(a[i][j]) > 0:
                        w.add(color[j])
                for cm in range(1, cmax):
                    if cm not in w:
                        newcol = cm
                        break
                return newcol

            # код функції visit
            if i == n:
                print("FINAL")  # Якщо всі вершини розфарбовані, то виводимо результат
            else:
                if color[i] == 0:  # Якщо поточна вершина не розфарбована
                    curcol = nicecolor()
                    if curcol > 0:
                        color[i] = curcol  # Якщо неконфліктний, то розфарб. вершину i фарбою c
                        visit(i + 1)  # Рекурсивно викликаємо для наступної вершини

        # Основний код програми
        visit(0)
        for r in range(n):
            print(a[r])
        print()
        print(color)

        colors = ['red', 'blue', 'yellow', 'green', 'orange', 'springgreen', 'lime', 'olive', 'indigo', 'fuchsia']

        color_dict = {a + 1: colors[color[a] - 1] for a in range(n)}
        print(color_dict)
        return color_dict


    def main_window(self):
        self.root = Tk()
        self.root.minsize(700, 300)
        self.root.maxsize(700, 300)
        self.root.title('Завдання (лабораторна №4)')

        def but_bind():
            if len(self.e.get()) == 0:
                Label(self.root, text='*задайте спершу кількість вершин графа', fg='red', font='Arial 12', ) \
                    .grid(column=1, row=4, columnspan=2)
            else:
                self.window2()

        Label(self.root, text='Завдання', font='Arial 16 bold').grid(column=1, row=1)
        Label(self.root, text='Набути теоретичні знання по темі «Розфарбування графів». \n'
                              'Створити програму розфарбування графів \n'
                              'за рекурсивною процедурою послідовного розфарбування.',
              font='Arial 16', bg='ghostwhite', wraplength=800, justify=LEFT, padx=10).grid(column=1, row=2,
                                                                                            columnspan=4)
        Label(self.root, text='Кількість вершин графа  ', font='Arial 14', pady=20, justify=RIGHT).grid(column=1, row=3,
                                                                                                        sticky=E)
        self.e = Entry(self.root, width=5, font='Arial 14')
        self.e.grid(column=2, row=3, sticky=W)
        Button(self.root, text='Задати матрицю суміжності', font='Arial 12', bg='lightblue', command=but_bind).grid(
            column=3, row=3)
        Button(self.root, text='Завдання за варіантом', font='Arial 12', bg='lightblue', command=but_bind).grid(
            column=3, row=5)
        Button(self.root, text='Студент', font='Arial 12 bold', command=self.student, bg='azure').grid(column=1, row=5)
        print("E>>>>>", self.e.get())

        self.root.mainloop()

    def window2(self):
        self.slave2 = Toplevel(self.root)
        self.slave2.title('Задати матрицю суміжності')
        self.slave2.focus_set()
        self.slave2.minsize(400, 400)

        def random_gen():
            tabl = self.create_tabl_random(int(self.e.get()))
            for i in range(int(self.e.get())):
                for j in range(int(self.e.get())):
                    self.list_ent[i][j].insert(END, tabl[i][j])

        for i in range(int(self.e.get()) + 1):
            for j in range(int(self.e.get()) + 1):
                if i == 0:
                    Label(self.slave2, text='{}'.format(j), font='Arial 16 bold', width=3).grid(column=j, row=i,
                                                                                                sticky=W)
                elif j == 0:
                    Label(self.slave2, text='{}'.format(i), font='Arial 16 bold', width=3).grid(column=j, row=i,
                                                                                                sticky=W)
                elif i == 0 and j == 0:
                    Label(self.slave2, text=' ', width=3).grid(column=j, row=i, sticky=W)
        self.list_ent = []
        for i in range(int(self.e.get())):
            self.list_ent.append([])
            for j in range(int(self.e.get())):
                self.list_ent[i].append(Entry(self.slave2, font='Arial 14', width=3))
                self.list_ent[i][j].grid(row=i + 1, column=j + 1, sticky=W)

        print(self.list_ent)

        Label(self.slave2, text='   ').grid(column=2, columnspan=5, row=int(self.e.get()) + 1)
        Button(self.slave2, text='Згенерувати випадково', font='Arial 12', bg='mintcream', command=random_gen) \
            .grid(column=0, columnspan=5, row=int(self.e.get()) + 2)
        Button(self.slave2, text='Показати граф', font='Arial 12', bg='mintcream', width=15, command=self.show_gr) \
            .grid(column=5, row=int(self.e.get()) + 2, columnspan=6)
        Button(self.slave2, text='Показати розфарбований граф', font='Arial 12', bg='mintcream', width=30,
               command=self.show_colored_gr) \
            .grid(column=5, row=int(self.e.get()) + 3, columnspan=6)

    def show_gr(self):
        self.tabl = []
        for i in range(int(self.e.get())):
            self.tabl.append([])
            for j in range(int(self.e.get())):
                self.tabl[i].append(self.list_ent[i][j].get())
        for i in range(int(self.e.get())):
            for j in range(int(self.e.get())):
                if self.tabl[i][i] not in ['0', '1']:
                    Label(self.slave2, text='*перевірте таблицю суміжності\n'
                                            'неправильно введені дані', font='Arial 12', fg='red') \
                        .grid(column=0, row=int(self.e.get()) + 3, columnspan=5)
                    pass

        for i in range(int(self.e.get())):
            for j in range(int(self.e.get())):
                self.list_ent[i][j]['state'] = DISABLED

        pl.figure('Заданий граф')
        self.gr = nx.Graph()
        for i in range(int(self.e.get())):
            self.gr.add_node(i + 1)
        for i in range(int(self.e.get())):
            for j in range(int(self.e.get())):
                if self.tabl[i][j] != '0':
                    self.gr.add_edge(i + 1, j + 1)
        pos = nx.circular_layout(self.gr)
        nx.draw_networkx(self.gr, pos)
        pl.axis('off')
        pl.show()

    def show_colored_gr(self):
        self.tabl = []
        for i in range(int(self.e.get())):
            self.tabl.append([])
            for j in range(int(self.e.get())):
                self.tabl[i].append(self.list_ent[i][j].get())
        for i in range(int(self.e.get())):
            for j in range(int(self.e.get())):
                if self.tabl[i][i] not in ['0', '1']:
                    Label(self.slave2, text='*перевірте таблицю суміжності\n'
                                            'неправильно введені дані', font='Arial 12', fg='red') \
                        .grid(column=1, row=int(self.e.get()) + 3, columnspan=5)
                    pass

        for i in range(int(self.e.get())):
            for j in range(int(self.e.get())):
                self.list_ent[i][j]['state'] = DISABLED

        Edges = dict()
        for i in range(int(self.e.get())):
            edge_list = []
            for j in range(int(self.e.get())):
                if self.tabl[i][j] == '1':
                    edge_list.append(j + 1)
            Edges[i + 1] = edge_list

        pl.figure('Розфарбований граф')
        self.gr = nx.Graph()
        for i in range(int(self.e.get())):
            self.gr.add_node(i + 1)
        for i in range(int(self.e.get())):
            for j in range(int(self.e.get())):
                if self.tabl[i][j] != '0':
                    self.gr.add_edge(i + 1, j + 1)
        pos = nx.circular_layout(self.gr)
        node_colors = Lab4.GraphColoring(self, self.tabl, int(self.e.get())).items()
        nx.draw_networkx(self.gr, pos)
        for i in node_colors:
            nx.draw_networkx(self.gr, pos, nodelist=[i[0]], node_color=i[1])
        pl.axis('off')
        pl.show()


a = Lab4()
a.main_window()
