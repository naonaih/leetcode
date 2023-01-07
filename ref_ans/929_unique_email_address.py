class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        # hash set to store all unique emails
        ans = set()

        for email in emails:
            # split into local name and domain name
            local, domain = email.split('@')

            # split local by '+' and replace all '.' with ''
            local = local.split('+')[0].replace('.', '')

            # concentrate local, @ and domain
            rev_email = local + '@' + domain

            ans.add(rev_email)

        return len(ans)
