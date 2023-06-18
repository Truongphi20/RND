import logging

class my_log():
	def __init__(self, name_file):
		self.logger = logging.getLogger(name_file)							# Set logger object
		file_handler = logging.FileHandler(f'{name_file}.log', mode="w")	    # Set file handler
		stream_handler = logging.StreamHandler()				    		# Set stream handler

		# Set level
		self.logger.setLevel(logging.DEBUG)		

		# Set format
		format_string = '%(levelname)s |%(asctime)s| %(name)s: \n %(message)s\n'+'-'*50
		f_format = logging.Formatter(format_string)

		file_handler.setFormatter(f_format)

		stream_handler.setFormatter(f_format)
		stream_handler.setLevel(logging.DEBUG)

		self.logger.addHandler(file_handler)
		self.logger.addHandler(stream_handler)
