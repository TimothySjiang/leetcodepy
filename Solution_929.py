class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        result = set()
        for email in emails:
            local, domain = email.split('@')
            if "+" in local:
                local = local[:local.find("+")]
            local = local.replace(".","")
            result.add(local+"@"+domain)
        return len(result)