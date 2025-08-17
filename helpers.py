class LimitedString:
    def __init__(self, min_len=0, max_len=None):
        self.min_len = min_len
        self.max_len = max_len

    def __set_name__(self, owner, name):
        self.private_name = "_" + name

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        if not isinstance(value, str):
            raise TypeError(f"{self.private_name} must be a string")
        if len(value) < self.min_len or (self.max_len and len(value) > self.max_len):
            raise ValueError(f"{self.private_name} must be between {self.min_len} and {self.max_len} characters")
        setattr(obj, self.private_name, value)


class User:
    username = LimitedString(3, 20)

    def __init__(self, username):
        self.username = username


# Example usage
u = User("SaifBayyari")  # ✅
u.username = "a"         # ❌ ValueError
