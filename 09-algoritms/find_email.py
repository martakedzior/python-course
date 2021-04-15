list_of_emails = ["From Gregory", "From Adam", "From XXXX"]


def find_email(email, list_of_emails):
    for item in list_of_emails:
        if item == email:
            return True
    return False


find_email("From Gregory", list_of_emails)


de