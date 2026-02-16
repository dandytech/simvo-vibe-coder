# Mini social media system with visible full structures

# Create user profile
user = {
    "username": "alex_dev",
    "followers": 120,
    "is_verified": False,
    "posts": []
}

# Create first post
post_1 = {
    "caption": "Hello world!",
    "likes": 10,
    "comments": [
        "Nice post!",
        "Welcome!"
    ]
}

# Add first post
user["posts"].append(post_1)

# Create second post
post_2 = {
    "caption": "Learning Python dictionaries!",
    "likes": 25,
    "comments": []
}

# Add second post
user["posts"].append(post_2)

# Update activity
user["posts"][1]["likes"] = user["posts"][1]["likes"] + 1
user["posts"][1]["comments"].append("Keep going!")
user["followers"] = user["followers"] + 30

# Print full structures
print("FULL USER DICTIONARY:")
print(user)

print("\nALL POSTS LIST:")
print(user["posts"])

print("\nFIRST POST DICTIONARY:")
print(user["posts"][0])

print("\nSECOND POST DICTIONARY:")
print(user["posts"][1])
