class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        let_logs = []
        dig_logs = []
       
        for log in logs:
            ans = log.split(" ")
            identifier = ans[0]
           
            if 48 <= ord(ans[1][0]) <= 57:
                dig_logs.append(log)
            else:
                let_logs.append([ans[1:], identifier])
        
        let_logs = sorted(let_logs)
        result = []
        for log in let_logs:
            new = ""
            content, key = log
            new += key + " " + " ".join(content)
            result.append(new)

        result += dig_logs
        return result
        