from datetime import datetime
import time


def save_user(user, updated_at=None):
    if updated_at is None:
        updated_at = datetime.now()
    print("ユーザー情報：", user)
    print("更新日：", updated_at)
    # Simulating saving process
    # save(user, updated_at)


# Test cases with delay
user_info1 = {"name": "John", "age": 30, "email": "john@example.com"}
save_user(user_info1)
# Add delay to see the time difference
time.sleep(2)

user_info2 = {"name": "Sarah", "age": 20, "email": "sarah@example.com"}
save_user(user_info2)
# Add delay to see the time difference
time.sleep(2)


# Incorrect usage demonstration (for understanding purposes)
def save_user_incorrect(user, updated_at=datetime.now()):
    print("ユーザー情報：", user)
    print("更新日：", updated_at)
    # Simulating saving process
    # save(user, updated_at)


# Test cases for incorrect usage with delay
save_user_incorrect(user_info1)
# Add delay to see the time difference
time.sleep(2)

save_user_incorrect(user_info2)
