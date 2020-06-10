from observer import AbsObserver


class CurrentKPIs(AbsObserver):
    # open_tickets = -1
    # closed_tickets = -1
    # new_tickets = -1
    
    def __init__(self, kpis):
        self._kpis = kpis
        self._open_tickets = self._kpis.open_tickets
        self._closed_tickets = self._kpis.closed_tickets
        self._new_tickets = self._kpis.new_tickets
        self._kpis.attach(self)
        
    def update(self, value=None):
        self._open_tickets = self._kpis.open_tickets
        self._closed_tickets = self._kpis.closed_tickets
        self._new_tickets = self._kpis.new_tickets
        self._display()
        
    def _display(self):
        print('Current open tickets: {}'.format(self._open_tickets))
        print('New tickets in last hour: {}'.format(self._closed_tickets))
        print('Tickets closed in last hour: {}'.format(self._new_tickets))
        print('*****\n')
