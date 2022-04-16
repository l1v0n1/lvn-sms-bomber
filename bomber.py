import services
import streamlit as st


class Application:
	"""
	Main application.
	"""

	def __init__(self):
		"""
		Creates a new application.
		"""

	def nubmer_check(self, number):
		msg = "Спам запущен"
		if len(number) in (10, 11, 12):
			if number[0] == "8":
				number = number[1:]
				st.success(msg)
			elif number[0] == '7':
				number = number[1:]
				st.success(msg)
			elif number[:2] == "+7":
				number = number[2:]
				st.success(msg)
			elif int(len(number)) == 10 and number[0] == 9:
				st.success(msg)
			return number
		else:
			st.error("Номер введен неверно, только РФ номера!")
			return False

	def run(self):
		"""
		Runs a Streamlit application.
		"""

		st.title("LvnBOMBER")
		st.markdown("*Только для РФ!*")
		st.write("Введите номер с кодом страны или без (+7, 8)")

		st.sidebar.title('Соц. сети LvnBOMBER')
		st.sidebar.info('[Телеграм](https://t.me/scumeyka)')

		query = st.text_input("Например: +79993332211")
		sms = st.text_input("Количество смс")
		if query and sms:
			if sms.isdigit():
				number = self.nubmer_check(query)
				if number is False:
					pass
				else:
					services.attack(number, sms)
					st.success('Спам окончен!')
			else:
				st.error('Введите количество смс!')


@st.cache(allow_output_mutation=True)
def create():
	"""
	Creates and caches a Streamlit application.
	Returns:
		Application
	"""

	return Application()


if __name__ == "__main__":

	# Create and run application
	app = create()
	app.run()
