class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        dire = deque()
        radiant = deque()
        n = len(senate)
        for i in range(n):
            if senate[i] == 'D':
                dire.append(i)
            else:
                radiant.append(i)
        while dire and radiant:
            d = dire.popleft()
            r = radiant.popleft()
            if d < r:
                dire.append(d+n)
            else:
                radiant.append(r+n)
        return "Dire" if dire else "Radiant"
        