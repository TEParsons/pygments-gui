class MissingPackage:
    """ 
    Class which handles a missing dependency. Will raise an import error when dependency 
    is accessed, rather than when it is imported.
    """
    def __init__(self, pkg, context):
        self.pkg = pkg
        self.context = context
    
    def __getattr__(self, attr):
        return self
    
    def __call__(self, *args, **kwargs):
        raise ImportError(
            f"{self.context} requires {self.pkg} to be installed."
        ) 