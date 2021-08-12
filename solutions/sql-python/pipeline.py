class Pipeline(object):
    """Class for executing a series of
    SQL commands as a pipeline.
    """
    def __init__(self, conn, ):
        """
        Parameters
        ----------
        conn : SQL connection object
        Returns
        -------
        None
        """
        self.conn = conn
        self.c = conn.cursor()
        self.steps = []

    def add_step(self, query, params=None):
        """Add a query to this pipeline.

        Parameters
        ----------
        query : SQL Query string.
        params : dict of params to format the query with

        Returns
        -------
        None
        """
        self.steps.append((query, params))

    def execute(self):
        """Execute all steps in the pipeline.
        """
        for step, params in self.steps:
            self.c.execute(step, params)

        self.conn.commit()

    def close(self):
        self.conn.close()
