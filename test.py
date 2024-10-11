def update_epoch(file_path, increment):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    updated_lines = []
    for line in lines:
        if line.startswith("epoch:"):
            parts = line.split(',')
            epoch_part = parts[0]
            epoch_value = int(epoch_part.split(':')[1])
            new_epoch_value = epoch_value + increment
            parts[0] = f"epoch:{new_epoch_value}"
            updated_line = ','.join(parts)
            updated_lines.append(updated_line)
        else:
            updated_lines.append(line)

    with open(file_path, 'w') as file:
        file.writelines(updated_lines)

# 使用範例
file_path = 'output2.txt'
increment = 256
update_epoch(file_path, increment)
