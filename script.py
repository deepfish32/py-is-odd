def is_odd(n: int) -> bool:
  return bool(n & 1)

if __name__ == "__main__":
  try:
    user_input = input("enter an integer. ")
    number = int(user_input)
    print(f"{is_odd(number)}")
  except ValueError:
    print("not a valid input.")
