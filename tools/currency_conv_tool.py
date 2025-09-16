import os
import requests
from typing import List
from utils.currency_converter import CurrencyConverter
from langchain.tools import tool
from dotenv import load_dotenv
import logging




class CurrencyConversionTool:
    def __init__(self):
        load_dotenv()
        self.api_key = os.environ.get("EXCHANGE_RATE_API_KEY")
        self.currency_service = CurrencyConverter(self.api_key)
        self.currency_converter_tool_list = self._setup_tools()

    def _setup_tools(self)-> List:
        """setup all tools for the currency converter tool"""

        @tool
        def convert_currency(amount: float, from_currency: str, to_currency: str):
            """
            Convert a specified amount of money from one currency to another.

            Args:
                amount (float): The amount of money to be converted.
                from_currency (str): The currency code of the original currency (e.g., 'USD', 'EUR').
                to_currency (str): The currency code of the target currency (e.g., 'INR', 'JPY').

            Returns:
                float: The converted amount in the target currency. If the conversion fails, 
                    an exception may be raised or a specific error value returned.
            """
            logging.debug(f"convert_currency tool is invoked")
            return self.currency_service.convert(amount, from_currency, to_currency)
        
        return [convert_currency]
