#Create a function for upload document
	#if you get uploaded file ,tags,document,date
#process the uploaded file to pdf 
#process the uploaded file to thumbnail
#process the uploaded file to folder with the same name
#extract into images
# uploaded file --> Total number of pages
import os

from datetime import datetime

from db.repository import DocumentRepository
from datetime import datetime
from core.file_manager import file_manager
from core.thumbnail import thumbnail_generator
from core.reader import PDF_reader
PDF_STORAGE = os.path.join("storage","pdf")


class DocumentService:

	def __init__(self):
		self.repo = DocumentRepository()
		self.file_manager = file_manager()
		self.thumnail = thumbnail_generator()
		self.PDF_reader = PDF_reader()

	def uploadDocument(self,uploaded_file,tags,Description,lecture_date = None):
		doc = []
	  #1.save the file
	 
		file_path = self.file_manager.save_file(uploaded_file)
		
	  #2.Generate thumbnail
		thumnail_path = self.thumnail.thumbnail_generator(file_path)
	  #3.Get total pages
		total_pages = self.thumnail.get_total_pages(file_path)
	  #4.Generate images
	
		self.PDF_reader.covert_pdf_to_images(file_path)
	  #5. create uploaded date
		upload_date = datetime.now().strftime("%Y-%m-%d")
	  # 6. #Sve to DB
		doc.append(uploaded_file.name)
		doc.append(file_path)
		doc.append(thumnail_path)
		doc.append(tags)
		doc.append(Description)
		doc.append(upload_date)
		doc.append(lecture_date)
		doc.append(total_pages)
		self.repo.add_document(doc) 