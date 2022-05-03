from datetime import datetime
from booking.booking import Booking


bot = Booking()

bot.land_first_page()
bot.preferences_bar()
bot.change_language(language='en-gb')
bot.change_currency(currency='PLN')
bot.select_destination(destination='Dubai')
bot.select_date(check_in='2022-02-20', check_out='2022-02-25')
bot.guests_value(adults=2, children=0, rooms=1, children_age=[])
bot.search_button()
bot.search_result_filters()
