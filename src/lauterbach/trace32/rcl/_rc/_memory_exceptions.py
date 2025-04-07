from ._error import BaseError


class MemoryError(BaseError):
    """This class is deprecated and will be removed in a future version.

    Deprecated:
        Use `MemoryAccessError` instead.
    """

    pass


class MemoryReadError(MemoryError):
    """This class is deprecated and will be removed in a future version.

    Deprecated:
        Use `MemoryReadAccessError` instead.
    """

    pass


class MemoryWriteError(MemoryError):
    """This class is deprecated and will be removed in a future version.

    Deprecated:
        Use `MemoryWriteAccessError` instead.
    """

    pass


class MemoryAccessError(MemoryError):
    """Memory access error"""

    pass


class MemoryReadAccessError(MemoryReadError):
    """Memory read access error"""

    pass


class MemoryWriteAccessError(MemoryWriteError):
    """Memory write access error"""

    pass
