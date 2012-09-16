

class Multiplexer():

  @staticmethod
  def read(path):
    f = files.find_one("path": path)
    if f == None:
      raise FileNotFoundException("The file does not exist.")
    else:
      adapter = Multiplexer.find_adapter(f["service"])
      account = accounts.find_one("_id": f["account_id"])
      file_object, metadata = adapter.read(account["auth_info"], f["_id"]) # Find the file whose name is id
      return file_object

  @staticmethod
  def update(file_object, path):
    f = files.find_one("path": path)
    if f == None:
      f = Multiplexer._add_file(file_object, path)

    file_id = f['_id']
    adapter = Multiplexer._find_adapter(f['service'])
    account = accounts.find_one("_id": f["account_id"])

    adapter.update(account["auth_info"], file_object, file_id)

  @staticmethod
  def delete(path):
    f = files.find_one("path": path)

  @staticmethod
  def metadata(path):
    pass

  @staticmethod
  def remaining_space():
    pass

  @staticmethod
  def total_space():
    pass

  def _add_file(file_object, path):
    """
    Creates a new file object in the collection "files"
    """
    pass

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