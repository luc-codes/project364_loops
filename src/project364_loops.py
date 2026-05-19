#names = ["Judith", "Abel", "Tyson", "Martha", "Beverley", "David", "Anabel"]
#estimated_insurance_costs = [1000.0, 2000.0, 3000.0, 4000.0, 5000.0, 6000.0, 7000.0]
#actual_insurance_costs = [1100.0, 2200.0, 3300.0, 4400.0, 5500.0, 6600.0, 7700.0]

# The above lists are now substituted with three separate csv files for each, which are stored in the data/ folder.
# This information is loaded into the .py file using pandas as below:

import pandas as pd

estimated_df = pd.read_csv("data/estimated_insurance_costs.csv") #what is inside the parenthesis is called a relative path. 
names_df = pd.read_csv("data/names.csv")
actual_df = pd.read_csv("data/actual_insurance_costs.csv")

# Now, let's convert the csv columns to lists:

names = names_df["name"].tolist()
actual_insurance_costs = actual_df["act_costs"].tolist()
estimated_insurance_costs = estimated_df["est_costs"].tolist()


# CREATING A FOR LOOP

# 1) Create a variable total_cost and initialize it to 0. 

total_cost = 0

# 2) Use a for loop to iterate through actual_insurance_costs and add each insurance cost to the variable total_cost. 

for cost in actual_insurance_costs:
  total_cost += cost

print("The total insurance cost considering everyone in the list is " + str(total_cost) + " dollars.")

# 3) After the for loop, create a variable called average_cost that stores the total_cost divided by the length of the actual_insurance_costs list.

average_cost = total_cost / len(actual_insurance_costs)

# 4) Print average_Cost with the following message: 
# Average Insurance Cost: <average_cost> dollars.

print("Average Insurance Cost: " + str(average_cost) + " dollars.")

# USING RANGE IN LOOPS

# 5) For each individual in names, we want to determine whether their insurance cost is above or below average. 
# Write a for loop with variable i that goes from 0 to len(names).

for i in range(len(names)):

# 6)
# Create a variable name, which stores names[i]
# Create a variable insurance_cost, which stores actual_insurance costs[i]
# Print out the insurance cost for each individual, with the following message: The insurance cost for <name> is <insurance_costs> dollars.

  name = names[i]
  insurance_cost = actual_insurance_costs[i]
  print("The insurance cost for " + name + " is " + str(insurance_cost) + " dollars.")

# 7) Click "Save" to see the result.

# 8) Inside of the for loop, use if, elif, else statements after the print statement to check whether the insurance cost is above, below, or equal to the average. Print out messages for each case.

  if insurance_cost > average_cost:
    print("The insurance cost for " + name + " is above average.")
  elif insurance_cost < average_cost:
    print("The insurance cost for " + name + " is below average.")
  else:
    print("The insurance cost for " + name + " is equal to the average.")
# 9) Click "Save" to see the results.

# CREATE A LIST COMPREHENSION

# 10) Using a list comprehensioin, create a new list called updated_estimated_costs, which has each element in estimated_insurance_costs multiplied by 11/10.

updated_estimated_costs = [estimated_cost * 11/10 for estimated_cost in estimated_insurance_costs]

# 11) Print updated_estimated_costs.

print(updated_estimated_costs)

# EXTRA

# 12.1) Convert the first for loop in the code to a while loop. 

total_cost = 0
index = 0

while index < len(actual_insurance_costs):
  total_cost += actual_insurance_costs[index]
  index += 1

print("The total insurance cost considering everyone in the list is " + str(total_cost) + " dollars.")

# How it works:
# index = 0 starts at the first item in the list. 
# while index < len(actual_insurance_costs) keeps looping until the end of the list. 
# actual_insurance_costs[index] accesses each value one at a time. 
# index += 1 moves to the next position in the list. 

# This produces the same result as the original for loop. 

# 12.2) Modify the second for loop so that it also calculates how far above or below the average the estimated insurance cost is. 

print("*************************************************")

for i in range(len(names)):
  name = names[i]
  insurance_cost = actual_insurance_costs[i]
  print("The insurance cost for " + name + " is " + str(insurance_cost) + " dollars.")

  if insurance_cost > average_cost:
    price_difference = insurance_cost - average_cost
    print("The insurance cost for " + name + " is " + str(price_difference) + " dollars above average.")
  elif insurance_cost < average_cost:
    price_difference = average_cost - insurance_cost
    print("The insurance cost for " + name + " is " + str(price_difference) + " dollars below average.")
  else:
    print("The insurance cost for " + name + " is equal to the average.")

