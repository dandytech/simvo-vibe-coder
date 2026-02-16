# Ecosystem Simulation: Animals evolving over time

# Define species with initial individuals
ecosystem = {
    "rabbits": [
        {"name": "Fluffy", "age": 2, "hunger": 5},
        {"name": "Snowball", "age": 1, "hunger": 3}
    ],
    "foxes": [
        {"name": "Fang", "age": 4, "hunger": 7}
    ],
    "birds": [
        {"name": "Tweety", "age": 1, "hunger": 2}
    ]
}

# Number of simulation days
days = 3

# Simulate each day
for day in range(1, days + 1):
    print(f"\n--- Day {day} ---")

    # Rabbits eat grass
    for rabbit in ecosystem["rabbits"]:
        if rabbit["hunger"] > 0:
            rabbit["hunger"] = rabbit["hunger"] - 2  # eating reduces hunger
        print(f"{rabbit['name']} the rabbit has hunger level {rabbit['hunger']}")

    # Foxes hunt rabbits
    for fox in ecosystem["foxes"]:
        hunted_rabbit = None
        for rabbit in ecosystem["rabbits"]:
            if rabbit["hunger"] > 2:
                hunted_rabbit = rabbit
                break  # hunt only one rabbit per fox per day
        if hunted_rabbit:
            print(f"{fox['name']} the fox hunted {hunted_rabbit['name']}")
            ecosystem["rabbits"].remove(hunted_rabbit)
            fox["hunger"] = max(fox["hunger"] - 3, 0)
        else:
            print(f"{fox['name']} couldn't find a hungry rabbit to hunt")

    # Rabbits reproduce if enough energy (low hunger)
    new_rabbits = []
    for rabbit in ecosystem["rabbits"]:
        if rabbit["hunger"] <= 2:
            baby_name = rabbit["name"] + "_Jr"
            new_rabbits.append({"name": baby_name, "age": 0, "hunger": 1})
            print(f"{rabbit['name']} had a baby rabbit named {baby_name}")
    ecosystem["rabbits"].extend(new_rabbits)

    # Age all animals by 1 day
    for species in ecosystem:
        for animal in ecosystem[species]:
            animal["age"] = animal["age"] + 1

# Final ecosystem status
print("\n--- Final Ecosystem ---")
print(ecosystem)