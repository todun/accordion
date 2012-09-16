class AbstractAdapter(object):

  @staticmethod
  def read(auth_info, ID):
    """reads a file from the cloud

    Args:
        - ``auth_info``:
            A dictionary containing authorization information
        - ``ID``:
            An ID that identifies the file, and it's the file's name too.

    Returns:
        - A python file object
        - A metadata object, which is a dictionary
    """
    raise NotImplementedError("Should have implemented this")

  @staticmethod
  def update(auth_info, file_object, ID):
    """Upload/update a file to the cloud

    Args:
        - ``auth_info``:
            A dictionary containing authorization information
        - ``file_object``:
            A Python file object
        - ``ID``:
            An ID that identifies the file, and it's the file's name too.

    Returns:
        - A metadata object, which is a dictionary
    """
    raise NotImplementedError("Should have implemented this")

  @staticmethod
  def create_dir(auth_info, ID):
    """Creates a folder

    Args:
        - ``auth_info``:
            A dictionary containing authorization information
        - ``ID``:
            An ID that identifies the folder, and it's the folder's name too.

    Returns:
        - A metadata object, which is a dictionary
    """
    raise NotImplementedError("Should have implemented this")

  @staticmethod
  def delete(auth_info, ID):
    """Deletes a file/directory

    Args:
        - ``auth_info``:
            A dictionary containing authorization information
        - ``ID``:
            An ID that identifies the file, and it's the file's name too.

    Returns:
        - A metadata object, which is a dictionary
    """
    raise NotImplementedError("Should have implemented this")

  @staticmethod
  def metadata(auth_info, ID):
    """Returns a metadata object of the file/folder specified by ID

    Args:
        - ``auth_info``:
            A dictionary containing authorization information
        - ``ID``:
            An ID that identifies the file, and it's the file's name too.

    Returns:
        - A metadata object, which is a dictionary
    """
    raise NotImplementedError("Should have implemented this")

  @staticmethod
  def remaining_space(auth_info):
    """Returns the remaining space of the account associated with auth_info

    Args:
        - ``auth_info``:
            A dictionary containing authorization information

    Returns:
        - The remaining space of the account, in bytes
    """
    raise NotImplementedError("Should have implemented this")

  @staticmethod
  def total_space(auth_info):
    """Returns the total space of the account associated with auth_info

    Args:
        - ``auth_info``:
            A dictionary containing authorization information

    Returns:
        - The total space of the account, in bytes
    """
    raise NotImplementedError("Should have implemented this")

  @staticmethod
  def unused_space(auth_info):
    """Returns the unused space of the account associated with auth_info

    Args:
        - ``auth_info``:
            A dictionary containing authorization information

    Returns:
        - The unused space of the account, in bytes
    """
    return AbstractAdapter.total_space(auth_info) - AbstractAdapter.remaining_space(auth_info)