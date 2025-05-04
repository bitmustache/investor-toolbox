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

  def stockcomparison_button_click(self, **event_args):
    stock_1 = self.stockcomparison_box_1.text.strip().upper()
    stock_2 = self.stockcomparison_box_2.text.strip().upper()
    metal = self.metal_dropdown.selected_value
    start_date = self.stockcomparison_startdate.date
    end_date = self.stockcomparison_enddate.date

    # validate input
    if not stock_1 and not stock_2:
      alert("Please enter at least one stock to compare.")
      return

    if not start_date or not end_date:
      alert("Please select a start and end date.")
      return

    if start_date >= end_date:
      alert("Start date must be before end date.")
      return

      # ensure user chooses one of possible comparison options
      valid_comparison = (stock_1 and stock_2) or (stock_1 and metal in ["Gold", "Silver"]) or (stock_1 and stock_2 and metal in ["Gold", "Silver"])
      if not valid_comparison:
            alert("Comparison requires two stocks, a stock and a metal or two stocks and a metal.")
            return

      self.status_label.text = "Fetching data..."

      try:
        img_base64 = anvil.server.call('get_stock_comparison_graph', stock_1, stock_2, metal, start_date, end_date)

        # if call to backend is successful
        self.stockcomparison_graph_card.visible = True     
        

