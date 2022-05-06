import datetime

get_input = True
dateformat = "%Y/%m/%d, %H:%M"


def date_check(user_input=None):
	try:
		valid_time = datetime.datetime.strptime(user_input, dateformat)
		print("Poprawna wartość.")
		return valid_time

	except ValueError:
		print("Podano zły format daty.")
		return


if __name__ == '__main__':
	while get_input:
		user_date = input("Podaj datę i godzinę zdarzenia w formacie(YYYY/MM/DD, H:M):")

		if user_date == 'quit':
			get_input = False
		else:
			cleaned_date = date_check(user_date)
			cleaned_date = cleaned_date.timestamp()

		if cleaned_date: get_input = False

print(cleaned_date)

def date_count(cleaned_date):
	current_time = datetime.datetime.now()
	time_stamp = current_time.timestamp()
	val = cleaned_date - time_stamp
	print(time_stamp)
	print(val)
	xxx = datetime.datetime.fromtimestamp(val)
	print(xxx)

date_count(cleaned_date)

# data_data = datetime.fromtimestamp(val)
# str_data_data = data_data.strftime(dateformat)
# print(str_data_data)

# if cleaned_date.hour >= 0 or cleaned_date.hour <= 24:
#  print(f"Za {value}")
# elif cleaned_date.hour >> 24 or cleaned_date.hour << 48:
#  print(f"Jutro {value}")
# elif cleaned_date.hour >= 48 or cleaned_date.hour << 72:
#  print(f"Pojutrze {value}")
