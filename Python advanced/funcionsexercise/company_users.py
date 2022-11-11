

def company_users_func():

    command = input()
    company_users = {}

    while command != "End":
        current_info = command.split(" -> ")
        company = current_info[0]
        id = current_info[1]

        if company not in company_users:
            company_users[company] = []
        if id not in company_users[company]:
            company_users[company].append(id)

        command = input()

    for company, id in company_users.items():
        print(f"{company}")
        for id in company_users[company]:
            print(f"-- {id}")

company_users_func()