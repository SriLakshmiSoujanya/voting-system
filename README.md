# CLI Voting System

A simple command-line voting system written in Python that simulates an election with multiple parties, voter validation, and result tabulation.

## Features

- Statically defined list of political parties with unique IDs
- Voter registration via Unique ID and Age
- Vote casting with party selection
- Invalid vote detection (duplicate IDs, underage voters)
- Sorted election results with statistics per party

## Parties

| ID | Party Name |
|----|------------|
| 1 | Progressive Alliance |
| 2 | National Unity Party |
| 3 | Green Future |
| 4 | Liberty Front |
| 5 | People's Voice |

## Requirements

- Python 3.6 or higher
- No external libraries required

## How to Run

```bash
python3 voting_system.py
```

## How It Works

### Voting Process

1. The program prompts each voter to enter:
   - **Unique ID Number** — identifies the voter
   - **Age** — must be 18 or above to cast a valid vote
2. A list of parties with their IDs is displayed.
3. The voter enters the ID of the party they wish to vote for.
4. After each vote, the program asks: **"Are there more voters? (Y/N)"**
   - **Y** — repeats the process for the next voter
   - **N** — ends voting and displays results

### Vote Validation Rules

| Condition | Result |
|-----------|--------|
| Valid Unique ID + Age ≥ 18 | ✓ Valid vote |
| Age < 18 | ✗ Invalid vote |
| Duplicate Unique ID | ✗ Invalid vote (only the first vote counts) |

### Results Display

After voting ends, results are shown **sorted from highest to lowest valid votes**, with the following stats per party:

- **Total Votes** — all votes cast for the party
- **Valid Votes** — votes that passed validation
- **Invalid Votes** — votes that failed validation
- **Vote Percentage** — percentage of valid votes out of total valid votes
- **Lead Margin** — vote difference from the leading party (or lead over 2nd place for the winner)

## Example Session

```
============================
   WELCOME TO VOTING SYSTEM
============================

--- New Voter ---
Enter your Unique ID Number: 1001
Enter your Age: 25

--- Registered Parties ---
  [1] Progressive Alliance
  [2] National Unity Party
  [3] Green Future
  [4] Liberty Front
  [5] People's Voice
--------------------------
Enter the ID of the party you wish to vote for: 3

  ✓ Vote cast successfully for 'Green Future'!

Are there more voters? (Y/N): N

========================================================================
                        ELECTION RESULTS
========================================================================

  Party       : Green Future
  Total Votes : 1
  Valid Votes : 1
  Invalid     : 0
  Percentage  : 100.00%
  Lead Margin : Only party
  --------------------------------------------------
```

## File Structure

```
voting-system/
└── voting_system.py   # Main program
```

## License

This project is open source and free to use.
