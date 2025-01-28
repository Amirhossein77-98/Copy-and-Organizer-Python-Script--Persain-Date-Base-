import logging
class TextHandler(logging.Handler):
    def __init__(self, text_widget):
        super().__init__()
        self.text_widget = text_widget

    def emit(self, record):
        msg = self.format(record)
        timestamp, operation = msg.split(' - ')
        timestamp = timestamp.split('.')[0]
        operation_mode, file_name, to, *destination = operation.split(' ')

        if operation_mode == "Your":
            self.text_widget.insert('end', timestamp, 'timestamp')
            self.text_widget.insert('end', ' - ', 'dash')
            self.text_widget.insert('end', operation_mode + ' ', 'operationmode')
            self.text_widget.insert('end', file_name + ' ', 'operationmode')
            self.text_widget.insert('end', to + ' ', 'operationmode')
            self.text_widget.insert('end', ' '.join(destination) + '\n', 'operationmode')
            self.text_widget.see('end')
        else:
            self.text_widget.insert('end', timestamp, 'timestamp')
            self.text_widget.insert('end', ' - ', 'dash')
            self.text_widget.insert('end', operation_mode + ' ', 'operationmode')
            self.text_widget.insert('end', file_name + ' ', 'filename')
            self.text_widget.insert('end', to + ' ', 'to')
            self.text_widget.insert('end', ' '.join(destination) + '\n', 'destination')
            self.text_widget.see('end')