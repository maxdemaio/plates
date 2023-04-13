def is_valid(s):
  if len(s) < 2 or len(s) > 6:
    return False
  # Must start with 2 letters
  if not s[:2].isalpha():
    return False
    
  # Loop over characters in string
  numSeen = False
  for char in s:
    # All chars must be letters or numbers
    if not char.isalnum():
      return False
    # First number found, but it's a 0
    if char.isdigit() and not numSeen and char == "0":
      return False
    # First number found
    if char.isdigit() and not numSeen:
      numSeen = True
    # Numbers cannot be in the middle of a string
    if numSeen and char.isalpha():
      return False
  return True
