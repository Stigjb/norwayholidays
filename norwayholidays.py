from pandas.tseries.holiday import AbstractHolidayCalendar, Holiday, EasterMonday, Easter
from pandas.tseries.offsets import Day

class NorwayHolidays(AbstractHolidayCalendar):
    rules = [
        Holiday('Nyttårsdag', month=1, day=1),
        Holiday('Skjærtorsdag', month=1, day=1, offset=[Easter(), Day(-3)]),
        Holiday('Langfredag', month=1, day=1, offset=[Easter(), Day(-2)]),
        EasterMonday,
        Holiday('Arbeidernes internasjonale dag', month=5, day=1),
        Holiday('Grunnlovsdagen', month=5, day=17),
        Holiday('Kristi himmelfartsdag', month=1, day=1, offset=[Easter(), Day(39)]),
        Holiday('1. pinsedag', month=1, day=1, offset=[Easter(), Day(49)]),
        Holiday('2. pinsedag', month=1, day=1, offset=[Easter(), Day(50)]),
        Holiday('1. juledag', month=12, day=25),
        Holiday('2. juledag', month=12, day=26)
    ]