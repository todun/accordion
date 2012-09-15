"""An abstract adaptor based on a subset of Google Drive and Dropbox APIs"""
class AbstractAdapter(object):
  
  @staticmethod
  def read(auth_info, path):
    """Retrive a file"""
    raise NotImplementedError("Should have implemented this")

  @staticmethod
  def update(auth_info, local_path, remote_path, overwrite):
    """Update a exisiting file."""
    raise NotImplementedError("Should have implemented this")
  
  @staticmethod
  def delete(auth_info, path):
    """Delete a exisiting file."""       
    raise NotImplementedError("Should have implemented this")
      

  def metadata(auth_info, path):
    raise NotImplementedError("Should have implemented this")

  def remaining_space(auth_info):
    raise NotImplementedError("Should have implemented this")