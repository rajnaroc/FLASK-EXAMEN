from .models.User import User

class ModelUser:

    @classmethod
    def get_by_id(cls,db,id):
        try: 

            cur = db.connection.cursor()
            cur.execute("SELECT * FROM users WHERE id = %s", (id,))
            data = cur.fetchone()

            if data:
                id = data[0]
                fullname = data[1]
                email = data[3]
                
                user = User(id,fullname,None,email)

                return user
        except Exception as e:
            print(e)

    @classmethod
    def register(cls,db,fullname,email,password):
        try:
            cursor = db.connection.cursor()
            hashed_password = User.hash_password(password)
            cursor.execute("INSERT INTO users VALUES (NULL,fullname,email,password)", (fullname,email,hashed_password))
            db.commit.cursor()

            return True
        except Exception as e:
            print(e)

    @classmethod
    def login(cls,db,email,password):
        try:
            cur = db.connection.cursor()
            cur.execute("SELECT * FROM users WHERE email = %s", (email,))
            data = cur.fetchone()

            if data:
                id = data[0]
                fullname = data[1]
                password = User.check_password(data[2],user.password)
                email = data[3]
                
                if password:
                    user = User(id,fullname,None,email)

                    return user
                return print("error password")
            
        except Exception as e:
            print(e)