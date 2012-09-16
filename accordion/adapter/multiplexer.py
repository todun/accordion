

class Multiplexer():
  FileNotFoundExceptionMessage = "The file does not exist."

  @staticmethod
  def read(path):
    f = files.find_one("path": path)
    if f == None:
      raise FileNotFoundException(FileNotFoundExceptionMessage)
    else:
      adapter = Multiplexer.find_adapter(f.service)
      # Find the file whose name is id
      return adapter.read(Multiplexer._get_auth_info(f), f["_id"])

  @staticmethod
  def update(file_object, path):
    f = files.find_one("path": path)
    if f == None:
      f = Multiplexer._add_file(file_object, path)

    adapter = Multiplexer._find_adapter(f['service'])

    return adapter.update(Multiplexer._get_auth_info(f), file_object, f['_id'])

  @staticmethod
  def delete(path):
    f = Multiplexer._get_file(path)
    if f == None:
      raise FileNotFoundException(FileNotFoundExceptionMessage)

    adapter = Multiplexer._find_adapter(f['service'])
    return adapter.delete(Multiplexer._get_auth_info(f), f['_id'])

  @staticmethod
  def metadata(path):
    f = Multiplexer._get_file(path)
    if f == None:
      raise FileNotFoundException(FileNotFoundExceptionMessage)
    adapter = Multiplexer._find_adapter(f['service'])
    return adapter.metadata(Multiplexer._get_auth_info(f), f['id'])

  @staticmethod
  def remaining_space():
    

  @staticmethod
  def total_space():
    pass

  def _add_file(file_object, path):
    """
    Creates a new file object in the collection "files"
    """
    

  def _find_adapter(service):
    """
    Returns an adapter that corresponds to the given service
    """
    pass

  def _get_file(path):
    """
    Returns a dictionary corresponds 
    """
    return files.find_one("path": path)

  def _get_auth_info(f):
    """
    Returns auth_info of the account that is in charge of the give file f
    """
    account = accounts.find_one("_id": f["account_id"])
    return account["auth_info"]