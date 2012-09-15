class AbstractAdapter(object):
  """An abstract adaptor based on a subset of Google Drive and Dropbox APIs"""
  def get(self, path):
    """Retrive a file"""
    raise NotImplementedError("Should have implemented this")

  def update(self, path):
    """Update a exisiting file."""
    raise NotImplementedError("Should have implemented this")
  
  def delete(self, path):
    """Delete a exisiting file."""       
    raise NotImplementedError("Should have implemented this")
      
  def metadata(self, path):
    raise NotImplementedError("Should have implemented this")