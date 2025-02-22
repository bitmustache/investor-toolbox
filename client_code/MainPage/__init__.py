from ._anvil_designer import MainPageTemplate
from anvil import *
import anvil.server


class MainPage(MainPageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def mainpage_link_click(self, **event_args):
    open_form('MainPage')
  
  def compoundinterestcalc_link_click(self, **event_args):
    open_form('MainPage.CompoundInterestCalculator')

  def stocksearch_link_click(self, **event_args):
    open_form('MainPage.StockSearch')


  



