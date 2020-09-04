class ResponseMessage:

    def __init__(self, tips=None, msg=None, query=None):
        self.success = True
        self.code = 200
        self.tips = tips
        self.msg = msg
        self.query = query
