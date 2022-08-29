import os


def pickfile(src: str, ext: tuple[str]) -> list[str]:
    """Collect files with specified extension recursively.

    Parameters
    ----------
    src: str or PathLike
        The root directory.
    ext: tuple of str
        The accepted file extension.

    Returns
    -------
    list of str
        A list of relative path to pick-uped files.
    """
    return [
        os.path.join(root, file)
        for root, _, files in os.walk(src)
        for file in files
        if file.lower().endswith(ext)
    ]


def ipickfile(src: str, ext: tuple[str]) -> "generator[str]":
    """Collect files with specified extension recursively.

    Parameters
    ----------
    src: str or PathLike
        The root directory.
    ext: tuple of str
        The accepted file extension.

    Returns
    -------
    A generator of  str
        A generator which generates relative path to pick-uped files each iteration.
    """
    return (
        os.path.join(root, file)
        for root, _, files in os.walk(src)
        for file in files
        if file.lower().endswith(ext)
    )
