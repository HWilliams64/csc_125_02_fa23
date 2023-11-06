# RULES
#
# and => multiplication `*`
# or => addition `+`
# Follow your order of operations (PEMDAS)
# >= 1 => TRUE
# 0 => FALSE

exp_1 = 1 < 2 # => TRUE
exp_2 = 1 > 2 # => FALSE

# TRUE * FALSE => 1 * 0 = 0
exp_3 = exp_1 and exp_2
print(exp_3)

# TRUE + FALSE => 1 + 0 = 1 => TRUE
exp_3 = exp_1 or exp_2
print(exp_3)


#if amount_of_time_waited < 15 or (payment > 0 and desire > 50):
    # Go to class

# amount_of_time_waited < 15 + (0 > 0  * 80 > 50)
# amount_of_time_waited < 15 + (FALSE)
# 5 < 15 + (FALSE)
# TRUE + (FALSE)
# TRUE