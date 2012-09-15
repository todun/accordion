class AbstractAdapter(object):
    """An abstract adaptor based on a subset of Google Drive and Dropbox APIs"""
    def get(path):
        """Retrive a file"""
        raise NotImplementedError("Should have implemented this")
        
    def update(path):
        """Update a exisiting file."""
        raise NotImplementedError("Should have implemented this")
    
    def delete(path):
        """Delete a exisiting file."""       
        raise NotImplementedError("Should have implemented this")
        