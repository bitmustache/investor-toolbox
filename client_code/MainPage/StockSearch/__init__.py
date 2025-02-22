from ._anvil_designer import StockSearchTemplate
from anvil import *
import anvil.server

class StockSearch(StockSearchTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings
        self.init_components(**properties)
        self.stocksearch_card2.visible = False
        self.stockgraph_card.visible = False

    def mainpage_link_click(self, **event_args):
        open_form('MainPage')

    def compoundinterestcalc_link_click(self, **event_args):
        open_form('MainPage.CompoundInterestCalculator')

    def stocksearch_link_click(self, **event_args):
        open_form('MainPage.StockSearch')

    def stocksearch_button_click(self, **event_args):
        """Runs when the search button is clicked"""
        print("Search button clicked!")  # Debugging output

        # Get the stock symbol from the text box
        symbol = self.stocksearch_box.text.strip().upper()  # Convert to uppercase
        print(f"Symbol entered: {symbol}")  # Debugging output

        if not symbol:
            self.stocksearch_label.text = "Please enter a stock symbol!"
            return

        self.stocksearch_label.text = "Fetching data..."
        
        # Call stock price function
        self.get_stock_data(symbol)

        # Call stock graph function
        self.get_stock_graph(symbol)

    def get_stock_data(self, symbol):
        """Calls the server function to fetch stock price"""
        try:
            print("Calling Uplink function...")  # Debugging output
            stock_data = anvil.server.call('get_stock_price', symbol)

            print(f"Received response: {stock_data}")  # Debugging output
            
            if 'price' in stock_data:
                self.stocksearch_card2.visible = True
                self.stocksearch_label.text = f"Price of {symbol}: ${stock_data['price']}"
        
            else:
                self.stocksearch_label.text = f"Error: {stock_data['error']}"

        except Exception as e:
            self.stocksearch_label.text = f"Error: {str(e)}"
            print(f"Exception occurred: {e}")  # Debugging output

    def get_stock_graph(self, symbol):
        """Fetch stock graph when search is pressed"""
        try:
            print(f"Fetching stock graph for {symbol}...")
            img_base64 = anvil.server.call('get_stock_graph', symbol)

            if isinstance(img_base64, dict) and 'error' in img_base64:
                self.stocksearch_label.text = f"Error: {img_base64['error']}"
            else:
                # Convert base64 to image and display
                self.stockgraph_card.visible = True  # Show graph card
                self.stocksearch_image.source = f"data:image/png;base64,{img_base64}"
                self.stocksearch_image.width = '100%'  # Make image fill the width of the card
                self.stocksearch_image.height = '100%'  # Make image fill the height of the card
                self.stocksearchgraph_label.text = f"Stock Price Progression for {symbol}"
                
        except Exception as e:
            self.stocksearch_label.text = f"Error: {str(e)}"
            print(f"Exception in get_stock_graph: {e}")  # Debugging output






