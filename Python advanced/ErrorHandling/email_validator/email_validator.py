from custom_exceptions import MustContainAtSymbolError, NameTooShortError, InvalidDomainError

valid_domains = {".com", ".bg", ".org", ".net"}

while True:
    command = input()
    if command == "End":
        break
    email_parts = command.split("@")

    if len(email_parts) != 2:
        raise MustContainAtSymbolError("Email must contain @")

    name, domain = email_parts

    if len(name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    domain_end = f".{domain.split('.')[-1]}"

    if domain_end not in valid_domains:
        raise InvalidDomainError(f"Domain must be one of the following: {', '.join(valid_domains)}")

    print("Email is valid")