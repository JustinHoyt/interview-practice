def shipWithinDays(self, weights: List[int], days: int) -> int:
    low, high = max(weights), sum(weights)
    while low < high:
        mid = (low + high) // 2
        weight_sofar, days_sofar = 0, 1
        for weight in weights:
            if weight_sofar + weight > mid:
                days_sofar += 1
                weight_sofar = weight
            else:
                weight_sofar += weight
        if days_sofar <= days:
            high = mid
        else:
            low = mid+1
    return low
