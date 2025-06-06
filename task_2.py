class Tester:

    def __init__(self, name):  # пропущен self
        self.name = name
        self.deadline = True

    def work_hard(self, deadline=None):  # учёт параметра deadline, если он != None
        if deadline is not None:
            self.deadline = deadline
        if self.deadline:
            print(self.name, 'Что ж, ещё часок поработаю!')
        else:
            print(self.name, 'Можно отдыхать')

tester_1 = Tester(name='tester_1')
tester_1.work_hard(deadline=False)  # 'tester_1 Можно отдыхать'
tester_2 = Tester(name='tester_2')
tester_2.work_hard(deadline=True)   # 'tester_2 Что ж, ещё часок поработаю!'