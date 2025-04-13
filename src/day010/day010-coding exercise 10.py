def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                # Leap year
                return True
            else:
                # Not a leap year
                return False
        else:
            # Leap year
            return True
    else:
        # Not a leap year
        return False


is_leap_year(2024)
