from cherrypy._cprequest import Request

class AbstractAdapter():
    """An abstract adaptor based on a subset of Google Drive and Dropbox APIs"""
    def get(self, Request):
        """Retrive a file"""
        raise NotImplementedError("Should have implemented this")

    def update(self, Request):
        """Update a exisiting file."""
        raise NotImplementedError("Should have implemented this")
    
    def delete(self, Request):
        """Delete a exisiting file."""       
        raise NotImplementedError("Should have implemented this")
        
    def metadata(self, Request):
    	raise NotImplementedError("Should have implemented this")