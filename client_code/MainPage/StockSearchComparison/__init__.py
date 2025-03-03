from ._anvil_designer import StockSearchComparisonTemplate
from anvil import *
import anvil.server


class StockSearchComparison(StockSearchComparisonTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    self.stockcomparison_graph_card.visible = False


  def mainpage_link_click(self, **event_args):
    open_form('MainPage.StockSearchSingular')

  def compoundinterestcalc_link_click(self, **event_args):
    open_form('MainPage.CompoundInterestCalculator')
    
  def stocksearchsingular_link_click(self, **event_args):
    open_form('MainPage.StockSearchSingular')
    
  def stocksearchcomparison_link_click(self, **event_args):
    open_form('MainPage.StockSearchComparison')

