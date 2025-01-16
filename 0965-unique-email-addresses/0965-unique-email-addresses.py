class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_email = []
        for email in emails:
            local, domain = email.split('@')
            local = local.split('+')[0].replace('.', '')
            clean_email = local + '@' + domain
            if clean_email not in unique_email:
                unique_email.append(clean_email)
        
        return len(unique_email)