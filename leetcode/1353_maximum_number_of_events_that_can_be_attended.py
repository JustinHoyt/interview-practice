from heapq import heappush, heappop

def maxEvents(self, events):
    # sort by first start date
    events.sort(reverse=1)
    end_date_heap = []
    event_count = 0
    day = 0

    while events or end_date_heap:
        start_date = events[-1][0]
        if not end_date_heap:
            day = start_date

        while events and start_date <= day:
            heappush(end_date_heap, events.pop()[1])

        heappop(end_date_heap)
        event_count += 1
        day += 1

        while end_date_heap and end_date_heap[0] < day:
            heappop(end_date_heap)

    return event_count
