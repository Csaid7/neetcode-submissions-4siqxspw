class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Step 1: Pair up each car's position with its corresponding speed
        # e.g., position=[10, 8, 0], speed=[2, 4, 1] -> [[10, 2], [8, 4], [0, 1]]
        pairs = [[p, s] for p, s in zip(position, speed)]

        stack = []

        # Step 2: Sort by position in REVERSE order (closest to target -> furthest)
        # The car closest to the target sets the speed bottleneck for cars behind it
        for p, s in sorted(pairs)[::-1]:
            # Step 3: Calculate the time needed for this car to reach the finish line
            # Formula: time = (remaining distance) / speed
            time_to_target = (target - p) / s
            stack.append(time_to_target)

            # Step 4: Check if this car catches up to the fleet in front of it
            # stack[-1] is the current car (further back on the road)
            # stack[-2] is the fleet ahead (closer to target)
            # If current car takes LESS or EQUAL time, it catches up and gets stuck behind it!
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                # Pop current car because it merges into the fleet ahead (stack[-2])
                stack.pop()

        # Step 5: Every remaining item in the stack is a separate, distinct fleet
        return len(stack)