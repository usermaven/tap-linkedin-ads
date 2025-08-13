#!/usr/bin/env python3
"""Debug script to test LinkedIn API AccountUsers endpoint."""

from urllib.parse import urlencode, quote

# Test different parameter formats
account_id = "YOUR_ACCOUNT_ID"  # Replace with actual account ID
urn = f"urn:li:sponsoredAccount:{account_id}"

# Format 1: List with unencoded URN
params1 = {
    "q": "accounts",
    "accounts": f"List({urn})"
}

# Format 2: List with URL-encoded URN
params2 = {
    "q": "accounts", 
    "accounts": f"List({quote(urn, safe='')})"
}

# Format 3: Just the URN without List wrapper
params3 = {
    "q": "accounts",
    "accounts": urn
}

print("Testing different parameter formats:\n")
print("Format 1 - List with unencoded URN:")
print(f"  Raw params: {params1}")
print(f"  URL encoded: ?{urlencode(params1)}")
print()

print("Format 2 - List with URL-encoded URN inside List:")
print(f"  Raw params: {params2}")
print(f"  URL encoded: ?{urlencode(params2)}")
print()

print("Format 3 - Just URN without List:")
print(f"  Raw params: {params3}")
print(f"  URL encoded: ?{urlencode(params3)}")
print()

# What the actual URL should look like according to LinkedIn docs
print("Expected format according to LinkedIn docs:")
print(f"  ?q=accounts&accounts=List({quote(urn, safe='')})")