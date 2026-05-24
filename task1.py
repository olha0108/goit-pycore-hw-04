def total_salary(path):
    try:
        with open(path, 'r',encoding='utf-8') as fh:
         salaries = [float(line.strip().split(',')[1]) for line in fh if line.strip()]

        return (sum(salaries), sum(salaries) / len(salaries)) if salaries else (0.0, 0.0)
    except FileNotFoundError:
        print("File not found")
        return (0.0, 0.0)

total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")