from flask import Flask
from flask import request
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask import Response
import base64

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/sglovelah_image'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)
CORS(app)

class image(db.Model):
    __tablename__ = 'images'

    profileID = db.Column(db.Integer(), primary_key=True, autoincrement=False)
    profileImage = db.Column(db.String(2083), nullable=False)
    data = db.Column(db.LargeBinary, nullable=False)

    def __init__(self, profileID, profileImage, data):
        self.profileID = profileID
        self.profileImage = profileImage
        self.data = data

    def json(self):
        return {"profileid": self.profileID, "profileImage": self.profileImage, "data": self.data}

#upload image
@app.route("/upload/<int:profileID>", methods= ['POST','PUT'])
def upload(profileID):
    ##pass profileID to this function (retrieve from json)
    ##hardcode for now
    if request.method == 'POST':
        # print(request.form)
        file = request.files["profilepic"]
        # print(file)
        newfile = image(profileID, file.filename, file.read())
        db.session.add(newfile)
        db.session.commit()
    if request.method == 'PUT':
        # return jsonify({"message":"hello"})
        # Gets current profile
        currentprofile = image.query.filter_by(profileID=profileID)
        # return currentprofile.get_json())
        # Grabs file from request
        file = request.files["profilepic"]

        # Changes the attributes of the current profile object
        currentprofile.profileImage = file.filename
        currentprofile.data = file.read()

        # Adds back into the database
        try:
            db.session.commit()
            return jsonify({"message":"successful update of image"}) 
        except:
            return jsonify({"message":"Error adding into the database."})
    return jsonify({"message":"successful upload of image"}) 

#retrieve image
@app.route("/getimage/<int:id>")
def retrieve(id):
    ##pass profileID to this function
    ##hardcode for now
    userprofile = image.query.filter_by(profileID=id).first()
    print("************************************************")
    print(userprofile)
    filepic = userprofile.data
    # encoded = base64.b64encode(filepic)
    # return encoded
    ## img src = this response.
    return Response(filepic, mimetype='image/jpeg')
    



if __name__ == "__main__":
    app.run(port=3000,debug=True)
