from datetime import datetime

class JSONFactory():
    """ To create JSON response header. It will contain "status", "create_time" and "payloads". 
    Please reference the class doc for more detail.

    Method(s):
    ---
    createResponse(success: bool, payloads: any)
        Return a JSON response header.

    """

    def __init__(self):      
        create_time =  datetime.now().isoformat()   
        self.base_json = {
            'status': 'not_initialized',
            'create_time': create_time,
            'payloads': []
        }

        self.status_success = 'success'
        self.status_failed = 'failed'


    def createResponse(self, success: bool, payloads) -> dict:
        """ To create a JSON response header. 

        ---
        Args:
            success (bool): The boolean flag indicate if this response shows success
            payload (any): The payload you want to send through the response JSON. dict is recommended.
        
        Returns:
            dict: The JSON response header with the success flag, response create time and payload passed to.

        """

        if success:
            self.base_json['status'] = self.status_success
        else:
            self.base_json['status'] = self.status_failed
        self.base_json['payloads'] = payloads
        return self.base_json