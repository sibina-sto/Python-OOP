# Ines

def admin_access(ref_func):
    def wrapper(user_obj):
        if user_obj["is_admin"]:
            return ref_func(user_obj)
        raise PermissionError("Only admins can access it")
    return wrapper


user = {"name": "Test", "is_admin": True}
user_not_admin = {"name": "Testov", "is_admin": False}


@admin_access
def read_book_content(user):
    print(f"{user['name']} reads the book content")


def read_product_content(user):
    print(f"{user['name']} reads the book content")

read_product_content(user)
read_product_content(user_not_admin)
