class PermissionDenied(Exception):
    pass


def transfer(db, user: str, source: str, target: str, amount: int) -> None:
    if not isinstance(amount, int) or amount <= 0:
        raise ValueError("amount must be a positive integer")
    if not db.can_operate(user, source):
        raise PermissionDenied(source)
    with db.transaction():
        if amount <= 0:
            raise ValueError("amount must be a positive integer")
        db.debit(source, amount)
        db.credit(target, amount)
