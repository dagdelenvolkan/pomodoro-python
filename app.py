import datetime as dt
import time


class Pomodoro:

    def __init__(self):
        self.second = dt.timedelta(seconds=1)  # Second to count down
        self.Time = dt.timedelta(minutes=25)  # Pomodoro time
        self.short_break = dt.timedelta(
            minutes=5)  # Short-break time
        self.long_break = dt.timedelta(minutes=30)  # Long-break time
        self.Ctime = dt.timedelta()  # Turn based time for count_down function
        self.time_show = dt.timedelta()  # Time for showing after the count_down finish
        self.turn = 1  # Turn Number
        self.pomodoro_count = 0  # Which pomodoro turn is completed
        self.decision = True  # Decision to count_down function loop
        self.message = ''

    def count_down(self):
        """Function that working as a chronometer"""

        while self.decision:
            self.Turn_decision()

            for i in range(int(self.Ctime.total_seconds())):

                self.Ctime -= self.second

                if int(self.Ctime.total_seconds() % 60) < 10 and int(self.Ctime.total_seconds() // 60) >= 10:
                    print(
                        f'{int(self.Ctime.total_seconds()//60)} minutes : 0{int(self.Ctime.total_seconds()%60)} seconds ')
                    time.sleep(1.0)

                elif int(self.Ctime.total_seconds() % 60) >= 10 and int(self.Ctime.total_seconds() // 60) < 10:
                    print(
                        f'0{int(self.Ctime.total_seconds()//60)} minutes : {int(self.Ctime.total_seconds()%60)} seconds ')
                    time.sleep(1.0)

                elif int(self.Ctime.total_seconds() % 60) < 10 and int(self.Ctime.total_seconds()//60) < 10:
                    print(
                        f'0{int(self.Ctime.total_seconds())//60} minutes : 0{int(self.Ctime.total_seconds()%60)} seconds ')
                    time.sleep(1.0)

                elif int(self.Ctime.total_seconds() % 60) >= 10 and int(self.Ctime.total_seconds()//60) >= 10:
                    print(
                        f'{int(self.Ctime.total_seconds())//60} minutes : {int(self.Ctime.total_seconds()%60)} seconds ')
                    time.sleep(1.0)

            self.turn += 1
            print(
                f'You have completed the {self.message}, {int(self.time_show//60)} minutes and {int(self.time_show%60)} seconds working!')

            self.DecisionF()

    def ask(self):
        """This function asks to user, does the user want to keep going pomodoro?"""

        self.decision = input('Do you want to continue? (Y/N): ')
        return self.decision

    def DecisionF(self):
        """This function checks whether the user want to keep going pomodoro or not"""

        if (self.ask() == 'Y'):
            self.decision = True
        else:
            self.decision = False

    def Turn_decision(self):
        """ This function checks the which turn is next: Pomodoro, Short-Break, Long-Break"""

        if self.turn % 2 != 0:
            self.Ctime = self.Time
            self.pomodoro_count += 1
            self.message = f'{self.pomodoro_count} Pomodoro'
            self.time_show = self.Ctime.total_seconds()

        if self.turn % 2 == 0 and self.turn % 8 != 0:
            self.Ctime = self.short_break
            self.message = 'Short Break'
            self.time_show = self.Ctime.total_seconds()

        if self.turn % 8 == 0:
            self.Ctime = self.long_break
            self.message = 'Long Break'
            self.time_show = self.Ctime.total_seconds()

    def run(self):
        """ This function works the pomodoro app"""
        self.count_down()


if __name__ == '__main__':
    app = Pomodoro()
    app.run()
