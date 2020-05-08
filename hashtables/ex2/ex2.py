#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    sources = {}

    # Create dictionary with key: source and value: destination
    for ticket in tickets:
        sources[ticket.source] = ticket.destination

    # Return array with start as NONE source ticket
    route = [None] * length
    route[0] = sources["NONE"]

    # Checks previous ticket's destination, puts as source of the current ticket
    for i in range(1, len(route)):
        route[i] = sources[route[i-1]]

    return route
