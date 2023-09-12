class CountsBySoH:
    def __init__(self):
        self.healthy = 0
        self.exchange = 0
        self.failed = 0

def count_batteries_by_health(present_capacities):
    counts = CountsBySoH()
    rated_capacity = 120.0  # Assuming rated capacity is always 120 Ah

    for capacity in present_capacities:
        # Calculate SoH for each battery
        soh = (capacity / rated_capacity) * 100

        # Classify batteries based on SoH
        if soh > 80.0:
            counts.healthy += 1
        elif 80.0 >= soh >= 63.0:
            counts.exchange += 1
        else:
            counts.failed += 1

    return counts

def test_bucketing_by_health():
    # Test case 1: All batteries healthy
    present_capacities1 = [120, 118, 119, 115]
    counts1 = count_batteries_by_health(present_capacities1)
    assert counts1.healthy == 4
    assert counts1.exchange == 0
    assert counts1.failed == 0

    # Test case 2: Mix of healthy, exchange, and failed batteries
    present_capacities2 = [115, 118, 80, 95, 91, 72]
    counts2 = count_batteries_by_health(present_capacities2)
    assert counts2.healthy == 2
    assert counts2.exchange == 3
    assert counts2.failed == 1

    # Test case 3: All batteries failed
    present_capacities3 = [50, 45, 30, 20]
    counts3 = count_batteries_by_health(present_capacities3)
    assert counts3.healthy == 0
    assert counts3.exchange == 0
    assert counts3.failed == 4

    # Test case 4: Boundary case - empty array
    present_capacities4 = []
    counts4 = count_batteries_by_health(present_capacities4)
    assert counts4.healthy == 0
    assert counts4.exchange == 0
    assert counts4.failed == 0

    # Test case 5: Boundary case - single battery with full capacity
    present_capacities5 = [120]
    counts5 = count_batteries_by_health(present_capacities5)
    assert counts5.healthy == 1
    assert counts5.exchange == 0
    assert counts5.failed == 0

    print("All test cases passed")

if __name__ == "__main__":
    test_bucketing_by_health()
