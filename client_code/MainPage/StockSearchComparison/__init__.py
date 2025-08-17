from ._anvil_designer import StockSearchComparisonTemplate
from anvil import *
import anvil.server


class StockSearchComparison(StockSearchComparisonTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    self.stockcomparison_graph_card.visible = False
    self.stockcomparison_card.visible = False


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
    '''
    # Validate inputs
    if not stock_1 and not stock_2:
      alert("Please enter at least one stock to compare.")
      return

    if not start_date or not end_date:
      alert("Please select a start and end date.")
      return

    if start_date >= end_date:
      alert("Start date must be before end date.")
      return

    # Check that one of the allowed comparison combinations is chosen
    valid_comparison = (
      (stock_1 and stock_2) or
      (stock_1 and metal in ["Gold", "Silver"]) or
      (stock_1 and stock_2 and metal in ["Gold", "Silver"])
    )

    if not valid_comparison:
      alert("Comparison requires two stocks, a stock and a metal, or two stocks and a metal.")
      return
    '''
    # self.status_label.text = "Fetching data..."

    result = anvil.server.call('get_stock_price_multiple', stock_1, stock_2, metal)

    price_1 = result['price_1']
    price_2 = result['price_2']
    metal_price = result['metal_price']

    self.stockcomparison_card.visible = True
    self.stockcomparison_label.text = (
      f"Price of {result['stock_1']}: {price_1}\n" +
      (f"Price of {result['stock_2']}: {price_2}" if result['stock_2'] else "") +
      (f"Price of {result['metal']}: {metal_price}" if result['metal_price'] else "")
    )
    
    '''
    try:
      img_base64 = anvil.server.call('get_stock_comparison_graph', stock_1, stock_2, metal, start_date, end_date)
      
      # Show result
      self.stockcomparison_graph_card.visible = True
      self.stockcomparison_graph_image.source = f"data:image/png;base64,{img_base64}"
      self.stockcomparison_graph_image.height = '100%'
      self.stockcomparison_graph_image.width = '100%'
      self.status_label.text = f"Comparing {stock_1} vs {stock_2 or ''} {metal or ''} from {start_date} to {end_date}"

    except Exception as e:
      self.status_label.text = f"Error: {str(e)}"
    '''
