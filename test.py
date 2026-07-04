from tools.tavily_tool import tavily_search
from tools.flight_tool import search_flights


flights = search_flights("plan 7 days japan trip from germany")
print(flights)