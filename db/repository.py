from db.database import get_connection

from core.model import Document


class DocumentRepository:

    def add_document(self,doc:Document):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            Insert INTO documents(
                    name, path, thumbnail_path, tags, description,
                    upload_date, lecture_date, total_pages   

                       )
            VALUES(?,?,?,?,?,?,?,?)
       """,(
           doc.name,
           doc.path,
           doc.thumbnail_path,
           doc.tags,
           doc.description,
           doc.upload_date,
           doc.lecture_date,
           doc.total_pages
            )
             )
        conn.commit()
        conn.close
    
    def search_Document(self,tags= None,date = None):
        print("repository")
        conn = get_connection()
        cursor = conn.cursor()

        query = "SELECT * FROM documents"

        conditions=[]
        parameters=[]

        if tags:
            print(parameters)
            conditions.append("tags LIKE ?")
            parameters.append(f"%{tags}%")

        if date:
            conditions.append("date LIKE ?")
            parameters.append(date)
        
        if conditions:
            last_part_query = " OR ".join(conditions)
            query += " WHERE " 
            query += last_part_query

        cursor.execute(query,parameters)
        rows= cursor.fetchall()
        conn.close
        
        return [Document(*row) for row in rows]

