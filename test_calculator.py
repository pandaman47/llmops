import os
import logging
from utils.expense_calculator import Calculator
from tools.expense_calculator_tool import CalculatorTool

from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file
logging.basicConfig(
    level=logging.DEBUG,
    format= "%(asctime)s - %(levelname)s - %(message)s",
    filename="test_calci.log",
    filemode="w")

def test_expense_calculator():
    expense_calci = CalculatorTool()

    ### Defining test parameters

    price_per_night = 5000
    total_days = 4
    total_cost = 32000

    
    """List all initialized tools"""
    for index, tool in enumerate(expense_calci.calculator_tool_list):
        logging.debug(f"Tool {index}: {tool.name}")

    input_data = {
        "price_per_night": price_per_night,
        "total_days": total_days
    }
    calci_tool = expense_calci.calculator_tool_list[0]
    logging.debug(f"attempting to call {calci_tool.name} tool")
    total_hotel_costs = calci_tool.invoke(input=input_data)
    print(f"total hotel costs for the trip is {total_hotel_costs} for {total_days} days")
    logging.debug(f"success")


if __name__ == "__main__":
    test_expense_calculator()
