from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class LoanCalculatorApp(App):

    def calculate_loan(self, principal, interest_rate, years):
        interest_rate_decimal = interest_rate / 100.0
        total_amount = principal * (1 + interest_rate_decimal * years)
        monthly_payment = total_amount / (years * 12)
        return total_amount, monthly_payment

    def build(self):
        self.principal_input = TextInput(hint_text='Loan Amount', input_filter='float')
        self.interest_rate_input = TextInput(hint_text='Annual Interest Rate', input_filter='float')
        self.years_input = TextInput(hint_text='Loan Duration (in years)', input_filter='int')

        self.result_label = Label(text='')

        calculate_button = Button(text='Calculate', on_press=self.on_calculate)

        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        layout.add_widget(self.principal_input)
        layout.add_widget(self.interest_rate_input)
        layout.add_widget(self.years_input)
        layout.add_widget(calculate_button)
        layout.add_widget(self.result_label)

        return layout

    def on_calculate(self, instance):
        try:
            principal = float(self.principal_input.text)
            interest_rate = float(self.interest_rate_input.text)
            years = int(self.years_input.text)

            total_amount, monthly_payment = self.calculate_loan(principal, interest_rate, years)

            result_text = f'Total Amount to be Repaid: ${total_amount:.2f}\nMonthly Payment: ${monthly_payment:.2f}'
            self.result_label.text = result_text

        except ValueError:
            self.result_label.text = 'Please enter valid numeric values for all inputs'

if __name__ == '__main__':
    LoanCalculatorApp().run()
