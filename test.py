num = 1
output_total = ""
while True:
    result = f"본문{num}"
    output_total += result
    num += 1
    if num == 11:
        break

print(output_total)