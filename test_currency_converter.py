import os
from tools.currency_conv_tool import CurrencyConversionTool
from utils.currency_converter import CurrencyConverter
import logging

from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file
logging.basicConfig(
    level=logging.DEBUG,
    format= "%(asctime)s - %(levelname)s - %(message)s",
    filename="test.log",
    filemode="w")

def test_currency_converter():
    # Initialize the CurrencyConverterTool
    converter_tool = CurrencyConversionTool()

    # Define test parameters
    amount = 100.0  # Amount to convert
    from_currency = 'USD'  # Currency to convert from
    to_currency = 'INR'  # Currency to convert to

    # Perform the conversion
    try:
        #print(converter_tool.currency_converter_tool_list[0])
        input_data = {
        "amount": amount,
        "from_currency": from_currency,
        "to_currency": to_currency
    }
        convert_tool = converter_tool.currency_converter_tool_list[0]
        logging.debug(f"{convert_tool.name} is called")
        #converted_amount = convert_tool.invoke(input=input_data)
        converted_amount = converter_tool.currency_converter_tool_list[0].invoke(input=input_data)
        print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    test_currency_converter()