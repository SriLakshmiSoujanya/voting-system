
PARTIES = [
    {"id": 1, "name": "Progressive Alliance"},
    {"id": 2, "name": "National Unity Party"},
    {"id": 3, "name": "Green Future"},
    {"id": 4, "name": "Liberty Front"},
    {"id": 5, "name": "People's Voice"},
]

def display_parties():
    print("\n--- Registered Parties ---")
    for party in PARTIES:
        print(f"  [{party['id']}] {party['name']}")
    print("--------------------------")

def get_party_by_id(party_id):
    for party in PARTIES:
        if party["id"] == party_id:
            return party
    return None

def run_voting():
    votes = {party["id"]: {"total": 0, "valid": 0, "invalid": 0} for party in PARTIES}
    used_ids = set()

    print("============================")
    print("   WELCOME TO VOTING SYSTEM ")
    print("============================")

    while True:
        print("\n--- New Voter ---")

        while True:
            uid = input("Enter your Unique ID Number: ").strip()
            if uid:
                break
            print("  ID cannot be empty. Please try again.")

        while True:
            age_str = input("Enter your Age: ").strip()
            try:
                age = int(age_str)
                if age < 0:
                    print("  Age cannot be negative. Please try again.")
                else:
                    break
            except ValueError:
                print("  Please enter a valid numeric age.")

        invalid_reason = None

        if uid in used_ids:
            invalid_reason = "Duplicate Unique ID"
        elif age < 18:
            invalid_reason = "Age below 18"

        display_parties()

        while True:
            party_id_str = input("Enter the ID of the party you wish to vote for: ").strip()
            try:
                party_id = int(party_id_str)
                if get_party_by_id(party_id):
                    break
                else:
                    print(f"  Invalid party ID '{party_id}'. Please choose from the list above.")
            except ValueError:
                print("  Please enter a numeric party ID.")

        votes[party_id]["total"] += 1

        if invalid_reason:
            votes[party_id]["invalid"] += 1
            print(f"\n  ✗ Vote recorded as INVALID ({invalid_reason}).")
        else:
            votes[party_id]["valid"] += 1
            used_ids.add(uid)
            print(f"\n  ✓ Vote cast successfully for '{get_party_by_id(party_id)['name']}'!")

        while True:
            more = input("\nAre there more voters? (Y/N): ").strip().upper()
            if more in ("Y", "N"):
                break
            print("  Please enter Y or N.")

        if more == "N":
            break

    show_results(votes)

def show_results(votes):
    print("\n")
    print("=" * 72)
    print("                        ELECTION RESULTS                         ")
    print("=" * 72)

    total_valid_votes = sum(v["valid"] for v in votes.values())

    results = []
    for party in PARTIES:
        pid = party["id"]
        v = votes[pid]
        percentage = (v["valid"] / total_valid_votes * 100) if total_valid_votes > 0 else 0.0
        results.append({
            "id": pid,
            "name": party["name"],
            "total": v["total"],
            "valid": v["valid"],
            "invalid": v["invalid"],
            "percentage": percentage,
        })

    results.sort(key=lambda x: x["valid"], reverse=True)

    for i, r in enumerate(results):
        if i == 0:
            if len(results) > 1:
                lead_margin = r["valid"] - results[1]["valid"]
                margin_str = f"+{lead_margin} votes ahead of 2nd"
            else:
                margin_str = "Only party"
        else:
            lead_margin = results[0]["valid"] - r["valid"]
            margin_str = f"{lead_margin} votes behind leader"

        print(f"\n  Party       : {r['name']}")
        print(f"  Total Votes : {r['total']}")
        print(f"  Valid Votes : {r['valid']}")
        print(f"  Invalid     : {r['invalid']}")
        print(f"  Percentage  : {r['percentage']:.2f}%")
        print(f"  Lead Margin : {margin_str}")
        print("  " + "-" * 50)

    print("\n" + "=" * 72)
    if total_valid_votes > 0:
        winner = results[0]
        print(f"  WINNER: {winner['name']} with {winner['valid']} valid vote(s) ({winner['percentage']:.2f}%)")
    else:
        print("  No valid votes were cast.")
    print("=" * 72 + "\n")

if __name__ == "__main__":
    run_voting()
