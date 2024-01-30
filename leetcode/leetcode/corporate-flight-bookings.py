class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        total_seats=[0]*(n+1)
        for first,last,seats in bookings:
            total_seats[first-1]+=seats
            total_seats[last]-=seats
        _sum=0
        for i in range(len(total_seats)):
            _sum+=total_seats[i]
            total_seats[i]=_sum
        total_seats.pop()
        return total_seats