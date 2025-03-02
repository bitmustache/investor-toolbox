from ._anvil_designer import StockSearchComparisonTemplate
from anvil import *
import anvil.server


class StockSearchComparison(StockSearchComparisonTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def mainpage_link_click(self, **event_args):
    open_form('MainPage.StockSearchSingular')

  def compoundinterestcalc_link_click(self, **event_args):
    open_form('MainPage.CompoundInterestCalculator')
    
  def stocksearchsingular_link_click(self, **event_args):
    open_form('MainPage.StockSearchSingular')
    
  def stocksearchcomparison_link_click(self, **event_args):
    open_form('MainPage.StockSearchComparison')

