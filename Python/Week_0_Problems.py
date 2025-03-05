value = input("What is your message?")
print(value.lower())

value2 = input("What are you saying?")
value2_slow = value2.replace(" ", "...")
print(value2_slow)

value3 = input("What else are you adding?")
value3_face1 = value3.replace(":)", "🙂")
value3_face2 = value3_face1.replace(":(", "🙁")
print(value3_face2)

value4 = int(input("What is the mass?"))
print(value4 * 300000000 * 300000000)

