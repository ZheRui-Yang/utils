from pathlib import Path

import os


def clonetree(src: str, dest: str, callback: "Callable" = None, **kwargs):
    """Clone the whole structute of given source directory, and apply callback on
    any file it meet.

    The directories under 'src` will be copy into `dest` with the same
    hierarchy as `src`.
    The files will not be copied, instead they wiil be pass to callback function.

    Note this function will not check the relationship between `src` and `dest`.
    Therefore, if `dest` is a subdirectory of `src`, it will ruin the hierarchy of
    `src` and may cause some unwanted results.

    Parameters
    ----------
    src: str or PathLike
        The root directory.
    dest: str or PathLike
        A directory to be the new root of hierarchy of `src`.
    callback: function, default None
        A function accepts at least two string as parameters.
        The first parameter is the source path of the file, the second is the new one.
        The default callback will not doing anything.
    **kwargs:
        Any other keyword  arguments will pass directly to callback.
    """
    callback = (lambda *arg, **kwarg: None) if callback is None else callback

    for entry in os.scandir(src):
        destination: Path = Path(dest) / entry.name

        if entry.is_dir():
            os.makedirs(destination, exist_ok=True)
            clonetree(entry.path, destination, callback, *args, **kwargs)
        if entry.is_file():
            callback(entry.path, destination, **kwargs)
