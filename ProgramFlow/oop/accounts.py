import datetime
import pytz


class Accounts(object):
    """
    Simple account class
    """

    @staticmethod
    def _current_time():
        """
        This is a static method since no self is used in params
        and it starts with _ which indicates it is not intended to be modified

        in this case we need to annotate it with @staticmethod
        :return: localized utc time
        """
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        """
        Init method is not necessarily a constructor
        since in python the object creation is a two step processing
        first __new__ which calls __init__ method which provides customization to it
        :param name:
        :param balance:
        """
        self._name = name
        self._balance = balance
        self._transaction_list = []
        print(f"Account created for {self._name}")
        self._transaction_list.append((Accounts._current_time(), self._balance))
        self.show_balance()

    def deposit(self, amount: int):
        if amount > 0:
            self._balance += amount
            self.show_balance()
            # self.transaction_list.append((pytz.utc.localize(datetime.datetime.utcnow()), amount))
            self._transaction_list.append((Accounts._current_time(), amount))

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            # self.transaction_list.append((pytz.utc.localize(datetime.datetime.utcnow()), amount))
            self._transaction_list.append((Accounts._current_time(), -amount))
        else:
            print(f'''The amount must be greater than zero 
            or less than or equal to {self._balance} ''')
        self.show_balance()

    def show_balance(self):
        print(f'Balance is {self._balance}')

    def show_transaction(self):
        for date, amount in self._transaction_list:
            if amount > 0:
                tran_type = 'Deposit'
            else:
                tran_type = 'Withdraw'
                # Convert amount to positive
                amount *= -1
            print("{:6} {} on {} local time was {} "
                  .format(amount, tran_type, date, date.astimezone()))


if __name__ == "__main__":
    print('running as main')
    tim = Accounts('Tim', 0)
    tim.show_balance()

    tim.deposit(1000)
    tim.deposit(500)
    tim.withdraw(1000)

    print()
    print("Transaction(s)")
    tim.show_transaction()

    print("*" * 80)
    print()

    steph = Accounts("Steph", 800)
    steph.deposit(100)
    steph.withdraw(200)
    steph.show_balance()
    steph.show_transaction()

    # mangling in python
    '''
    When we start an attribute name with __ python mangles it with class name
    hence __balance becomes _Accounts__balance (verified by "print(steph.__dict__)"
    output {'_name': 'Steph', '_Accounts__balance': 700))
    '''
    print(steph.__dict__)
    # if we really need to do it
    # we can modify the mangled attribute
    # modifying the mangled attribute
    # print('Modifying mangled attribute')
    # steph._Accounts__balance = 40
    # steph.show_balance()
else:
    print('running as module')
