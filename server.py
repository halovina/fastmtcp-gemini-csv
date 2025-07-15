import pandas as pd
from fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Demo")

@mcp.tool()
async def get_csv_data() -> str:
    """
    Reads the content of sales_data.csv and returns it as a string.
    """
    try:
        df = pd.read_csv('sales_data.csv')
        return df.to_string()
    except FileNotFoundError:
        return "Error: sales_data.csv not found."
    
if __name__ == "__main__":
    mcp.run()