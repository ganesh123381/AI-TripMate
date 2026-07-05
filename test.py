from tools.tavily_tool import tavily_search
from tools.flight_tool import search_flights
from backend import run_travel_agent


#flights = search_flights("plan 7 days japan trip from germany")
# print(flights)

user_input = input("enter travel request: ")

res = run_travel_agent(
    user_input = user_input,
    thread_id = "test_user")

print("\nFINAL RESPONSE:\n")
print(res)