raw_activation_key = input()
command = input()

while command != 'Generate':
    current_command = command.split('>>>')
    if current_command[0] == "Contains":
        if current_command[1] in raw_activation_key:
            print(f'{raw_activation_key} contains {current_command[1]}')
        else:
            print(f'Substring not found!')
    elif current_command[0] == 'Flip':
        start_index = int(current_command[2])
        end_index = int(current_command[3])
        if current_command[1] == 'Upper':
            change = raw_activation_key[start_index:end_index].upper()
            raw_activation_key = raw_activation_key[:start_index] + change + raw_activation_key[end_index:]
            print(raw_activation_key)
        elif current_command[1] == 'Lower':
            change = raw_activation_key[start_index:end_index].lower()
            raw_activation_key = raw_activation_key[:start_index] + change + raw_activation_key[end_index:]
            print(raw_activation_key)
    elif current_command[0] == 'Slice':
        start_index = int(current_command[1])
        end_index = int(current_command[2])
        raw_activation_key = raw_activation_key[:start_index] + raw_activation_key[end_index:]
        print(raw_activation_key)
    command = input()

print(f'Your activation key is: {raw_activation_key}')