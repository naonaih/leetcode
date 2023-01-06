class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        ans_list = set()

        def separate_email(email):
            at_mark_index = email.find('@')
            return email[:at_mark_index], email[at_mark_index + 1:]

        def revise_local_name(local_name):
            list_lc = list(local_name)
            rev_local_name = ''
            for i in list_lc:
                if i == '.':
                    continue
                if i == '+':
                    return rev_local_name
                rev_local_name += i

            return rev_local_name

        for email in emails:
            local_name, domain_name = separate_email(email)
            rev_local_name = revise_local_name(local_name)
            candidate = rev_local_name + '@' + domain_name
            ans_list.add(candidate)

        return len(ans_list)
