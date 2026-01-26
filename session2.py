# Name: [abhinandan]
# Date: January 22, 2026
# Module 2: Core Fundamentals

# Task - 1: Identity vs. Equality Investigation
x = 256
y = 256
a = 257
b = 257
is_same_identity = a is b
is_same_value = a == b

status = None

print(f"Task 1 Results:\n"
      f"x_id: {id(x)}, y_id: {id(y)}\n"
      f"a_id: {id(a)}, b_id: {id(b)}\n"
      f"Identity (a is b): {is_same_identity}, Value (a == b): {is_same_value}\n"
      f"Status Type: {type(status)}, Status ID: {id(status)}")


# Task - 2: Advanced I/O and Type Casting Pipeline


hourly_rate = float(input("Enter Hourly Rate: "))
hours_worked = int(input("Enter Hours Worked: "))
tax_bracket = float(input("Enter Tax Bracket (e.g., 0.2): "))

gross_pay = hourly_rate * hours_worked
net_pay = gross_pay - (gross_pay * tax_bracket)

print(f"\nValidation: hourly_rate is {type(hourly_rate)}, "
      f"hours_worked is {type(hours_worked)}, "
      f"tax_bracket is {type(tax_bracket)}")

# Task - 3: Precision Engineering with F-Strings
header = "OFFICIAL PAYSLIP"
divider = "=" * 40

print(f"\n{header:=^40}")
print(f"{'Hourly Rate:':<25} ${hourly_rate:>10.3f}")
print(f"{'Hours Worked:':<25}  {hours_worked:>10d}")
print(f"{'Gross Pay:':<25} ${gross_pay:>10.3f}")
print(f"{'Tax Bracket:':<25}  {tax_bracket:>10.3f}")
print(divider)
print(f"{'NET PAY:':<25} ${net_pay:>10.3f}")
print(divider)

# Task - 4: Complex Expressions & Operator Precedence
a, b, c, d, e, f, g = 10.0, 5, 2, 3, 2, 8, 3

result = (a + b * c) / (d ** e) - (f // g)
is_valid = result > 0 and result is not None

print(f"\nTask 4 - Result: {result}")
print(f"Is Valid: {is_valid}")

# Task - 5: Bitwise Permissions & Flag Manipulation
GUEST, USER, ADMIN, SUPERUSER = 1, 2, 4, 8
current_access = GUEST | USER
new_secure_level = ADMIN << 1
has_user_bit = bool(current_access & USER)
current_access = current_access ^ GUEST

print(f"\nTask 5 Bitwise Results:")
print(f"Current Access (Binary): {bin(current_access)}")
print(f"New Secure Level: {new_secure_level}")
print(f"Has User Bit: {has_user_bit}")
