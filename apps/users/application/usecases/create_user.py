class CreateUser:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def execute(self, name, email, password):
        return self.user_repository.create(name, email, password)
