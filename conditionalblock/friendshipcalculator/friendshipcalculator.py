print("I will tell you your friendship score and how you match together")
yourname = input("Your name: ")
friendsname = input("Your friends name: ")
yourname_lower = (yourname.lower())
friendsname_lower = (friendsname.lower())
together = yourname_lower + friendsname_lower
print(together)
# true_score
t_count = together.count('t')
r_count  = together.count('r')
u_count  = together.count('u')
e_count  = together.count('e')
# friend_score
f_count = together.count('f')
r_count = together.count('r')
i_count = together.count('i')
e_count = together.count('e')
n_count = together.count('n')
d_count = together.count('d')
true_score = t_count + r_count + u_count + e_count
friend_score = f_count + r_count + i_count + e_count + n_count + d_count
print(f"Your friendship score is {true_score}")
print(f"Your friendship score is {friend_score}")
true_score_str = str(true_score)
friend_score_str = str(friend_score)
total = int(true_score_str + friend_score_str)
print(total)
if(total < 10 or total > 90):
  print(f"Your score is {total}, you go together like coke and mentos.")
elif(total > 40 and total < 50):
  print(f"Your score is {total}, you are alright together.")
else:
  print(f"Your score is {total}.")

# 'Mary had a little lamb'.count('a')
# For Friendship Scores less than 10 or greater than 90, the message should be:

# "Your score is x, you go together like coke and mentos."

# For Friendship Scores between 40 and 50, the message should be:

# "Your score is y, you are alright together."

# Otherwise, the message will just be their score. e.g.:

# # "Your score is z."