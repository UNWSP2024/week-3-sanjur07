# Write a program that asks the user to enter a person's age.  The program should display a message indicating whether the person is an infant, a child, a teenager, or an adult.  Following are the guidelines:
#Function categorize_age(age): 
''' FUNCTION catergorize_age(age):
    IF age is less than or eqaul to 1 THEN
        RETURN "The person is an infant."
    ELSE IF age is greater than 1 AND less than 13 THEN
        RETURN "The person is a child."
    ELSE IF age is greater than or equal to 13 AND less than 20 THEN 
        RETURN "The person is a teenager."
    ELSE
        RETURN "The person is an adult."
    END IF
    END FUNCTION

    PROMPT user to enter the person"s age
    STORE user inut as age

    TRY:
        CONVERT age input to a number
        CALL categorize_age(age)
        DISPLAY the returned message
    IF an error occurs during input conversion
        DISPLAY "Please enter a valid number for the age."
'''
# If the person is 1 year old or less, it should display "infant" (without quotes).
# If the person is older than 1 year, but younger than 13 years, it should display "child".
# If the person is at least 13 years old, but less than 20 years old, it should display "teenager".
# If the person is at least 20 year old, it should display "adult".

def categorize_age(age):
    ageCategory = "TBD"
    if age <= 1:
        ageCategory = "infant."
    elif 1 < age < 13:
        ageCategory = "child."
    elif 13 <= age < 20:
        ageCategory = "teenager."
    else:
        ageCategory = "adult."
    return ageCategory


#### This piece of the code has been done for you,
#### you only need to worry about the actual shipping 
#### charge logic in the weight_conversion function
if __name__ == '__main__':
    # Local variables
    # Get age from the user.
    age = float(input("Enter the person's age: "))
    # Display the age
    ageBucket = categorize_age(age)
    print (ageBucket)