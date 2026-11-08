while True:
	function_to_run = input("What do you want to calculate? (v:voltage/r:resistance/i:intensity): ")
	match function_to_run:
		case "v" | "voltage":
			while True:
				try:
					resistance = float(input("Resistance: "))
					intensity = float(input("intensity: "))
					break
				except ValueError as e:
					print("The values must be numeric.")
			print(f"Voltage: {resistance * intensity}")
		case "r" | "resistance":
			while True:
				try:
					voltage = float(input("Voltage: "))
					intensity = float(input("Intensity: "))
					break
				except ValueError as e:
					print("The values must be numeric.")
			print(f"Voltage: {voltage / intensity}")
		case "i" | "intensity":
			while True:
				try:
					voltage = float(input("Voltage: "))
					resistance = float(input("Resistance: "))
					break
				except ValueError as e:
					print("The values must be numeric.")
			print(f"Intensity: {voltage / resistance}")
		case _:
			print("The selected function is not valid, please, try again.")
	print()