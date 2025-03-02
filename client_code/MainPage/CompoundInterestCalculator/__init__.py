from ._anvil_designer import CompoundInterestCalculatorTemplate
from anvil import *
import anvil.server


class CompoundInterestCalculator(CompoundInterestCalculatorTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.result_card.visible = False
    self.graph_card.visible = False
    # Any code you write here will run before the form opens.

  def mainpage_link_click(self, **event_args):
    open_form('MainPage')

  def compoundinterestcalc_link_click(self, **event_args):
    open_form('MainPage.CompoundInterestCalculator')

  def calculate_compoundinterest_button_click(self, **event_args):
    # get the user inputs
    principal = float(self.principal_textbox.text)
    interest_rate = float(self.interestrate_textbox.text) / 100
    years = int(self.years_textbox.text)
    times_compounded = int(self.timescompounded_textbox.text)

    # calculate the future value based on inputs
    future_value = self.compound_interest(principal, interest_rate, years, times_compounded)

    self.result_label.text = f"The future value of your investment is: ${future_value: .2f}"
    self.result_card.visible = True # the result card is rendered with the result
    graph = anvil.server.call('compound_interest_graph', principal, interest_rate, years, times_compounded)
    self.plot_image.source = graph
    self.graph_card.visible = True  # show the graph card
    
  def compound_interest(self, principal, interest_rate, years, times_compounded):
    amount = principal * (1 + interest_rate / times_compounded) ** (times_compounded * years)
    return amount

  def stocksearchsingular_link_click(self, **event_args):
    open_form('MainPage.StockSearchSingular')

  

