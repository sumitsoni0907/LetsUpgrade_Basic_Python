## Project: OTP Generator
# Generate a 6 character OTP

import random as ran     # import random module
import string    # import string module

length = 6     # lengh of PTP
letter = string.ascii_letters + string.digits     # taking all alphabets like captial, small and digits.

otp = ''
for i in range(length):          # looping for generate OTP
  otp += ran.choice(letter)        # Adding random charater from  letter to otp
print("One Time Password(OTP):", otp)       # Print OTP


# Output - 1:

# One Time Password(OTP): aWKz8J

# Output - 2:

# One Time Password(OTP): pwY4ps

# Output - 3:

# One Time Password(OTP): bix8LW
