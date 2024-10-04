class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        if len(skill) == 2:
            return skill[0] * skill[1]
        total = sum(skill)
        teams = len(skill)//2
        if total % teams != 0:
            return -1
        each_team_skill = total//teams
        skill_freq = Counter(skill)
        res = 0

        for sk in skill:
            if skill_freq[sk] == 0:
                continue

            needed = each_team_skill - sk
            if needed in skill_freq and skill_freq[needed] > 0:
                res += sk * needed
                skill_freq[sk] -= 1
                skill_freq[needed] -= 1
            else:
                return -1
            
        return res

        


