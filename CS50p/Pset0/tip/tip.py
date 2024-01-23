dollars = float(input("How much was the meal? ").strip("$"))
percent = float(input("What percentage would you like to tip? ").strip("%")) / 100
print(f"Leave ${dollars*percent:.2f}")
