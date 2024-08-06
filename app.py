# from flask import Flask, request, render_template,jsonify, make_response
# from flask_cors import CORS
# from instagramy import InstagramUser
# from flask_restful import Api,Resource
# from flask_sqlalchemy import SQLAlchemy
# import os
# import json


# app = Flask(__name__)
# api = Api(app)
# db = SQLAlchemy(app)
# CORS(app)

# application = app

# filename = os.path.dirname(os.path.abspath(__file__))
# database = 'sqlite:///' + os.path.join(filename, 'db.sqlite')
# app.config['SQLALCHEMY_DATABASE_URI'] = database 
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# f = open('question_gemini.json', encoding='utf-8')
# gemini_db = json.load(f)

# f = open('result_gemini.json', encoding='utf-8')
# gemini_result_db = json.load(f)


# f = open('question_pisces.json', encoding='utf-8')
# pisces_db = json.load(f)

# f = open('result_pisces.json', encoding='utf-8')
# pisces_result_db = json.load(f)


# class ZodiakData(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     date_time = db.Column(db.String(100))
#     category = db.Column(db.String(100))
#     browser = db.Column(db.String(300))
#     ip_address = db.Column(db.String(100))
#     score = db.Column(db.String(100))

# db.create_all()

# class ZodiakApi(Resource):
#     def post(self):
#         data_date_time = request.form.get('date_time')
#         data_score = request.form.get('score')
#         data_category = request.form.get('category')
#         data_browser = request.form.get("browser")
#         data_ip_address = request.form.get("ip_address")
        
#         data = ZodiakData(date_time = data_date_time, category=data_category, browser = data_browser, ip_address = data_ip_address, score = data_score)
#         db.session.add(data)
#         db.session.commit()
        
#         return make_response({'msg' : 'Success'},200)
#     def get(self):
#         dataQuery = ZodiakData.query.all()
        
#         output = [
#             {
#             "id" : data.id,
#             "data" : {   
#                 "date_time" : data.date_time,    
#                 "score" : data.score,    
#                 "category" : data.category,    
#                 "browser" : data.browser,    
#                 "ip_address" : data.ip_address,    
#             }
#             } for data in dataQuery
#             ]
#         return make_response(jsonify(output), 200)
    
#     def delete(self):
#         dataQuery = ZodiakData.query.all()
#         for data in dataQuery:
#             db.session.delete(data)
#             db.session.commit()
#         return make_response({'msg' : 'Deleted'},200)
    
# class DelData(Resource):
#     def delete(self, id):
#         dataQuery = ZodiakData.query.get(id)
#         db.session.delete(dataQuery)
#         db.session.commit()
#         return make_response({'msg' : 'Deleted'},200)
    
#     def get(self, id):
#         dataQuery = ZodiakData.query.get(id)
#         output = [
#             {
#             "id" : dataQuery.id,
#             "data" : {   
#                 "date_time" : dataQuery.date_time,    
#                 "score" : dataQuery.score,    
#                 "category" : dataQuery.category,    
#                 "browser" : dataQuery.browser,    
#                 "ip_address" : dataQuery.ip_address,    
#             }
#             } 
#             ]
#         return make_response(jsonify(output), 200)
        
# class QuizPisces(Resource):
#     def get(self):
#         return make_response(jsonify(pisces_db), 200)
    
# class ResultPisces(Resource):
#     def get(self):
#         return make_response(jsonify(pisces_result_db), 200)
        
# class QuizCancer(Resource):
#     def get(self):
#         # dataQuery = QuizZodiak.query.all()
#         # with open('question_pisces.json') as file:
#         #     output = json.load(file)
#         output = [
#         {
#         "image": "https://cretivox.com/zodiac/pisces/q1.gif",
#         "name": "Gue mending tinggal di bulan daripada deket sama orang yang…",
#         "type": "q1",
#         "answers": [
#             {
#                 "answer1": "Gak bisa komitmen",
#                 "val1": 10,
#                 "answer2": "Gak deketin gue duluan",
#                 "val2": 1,
#                 "answer3": "Susah diajak ngobrol",
#                 "val3": 2,
#                 "answer4": "Terlalu perfeksionis",
#                 "val4": 3
#             }
#         ]
#         },
#         {
#         "image": "https://cretivox.com/zodiac/pisces/q2.gif",
#         "name": "Gue rela terjun di ketinggian 500 meter pake baju kodok demi orang yang…",
#         "type": "q2",
#         "answers": [
#             {
#                 "answer1": "Style rambutnya bagus",
#                 "val1": 1,
#                 "answer2": "Keliatannya kreatif, tau seni",
#                 "val2": 10,
#                 "answer3": "Bisa mix and match outfit",
#                 "val3": 2,
#                 "answer4": "Bisa kopral 1000x",
#                 "val4": 3
#             }
#         ]
#         },
#         {
#         "image": "https://cretivox.com/zodiac/pisces/q3.gif",
#         "name": "Gue mau renovasi rumah Atta Halilintar, tapi fasilitas yang wajib ada di rumah itu",
#         "type": "q3",
#         "answers": [
#             {
#                 "answer1": "Tempat gym biar mirip Ade Rai",
#                 "val1": 1,
#                 "answer2": "Ruangan khusus cemilan gue",
#                 "val2": 2,
#                 "answer3": "Kolam renang kali yaa",
#                 "val3": 10,
#                 "answer4": "Ruang buat ngonten",
#                 "val4": 3
#             }
#         ]
#         },
#         {
#         "image": "https://cretivox.com/zodiac/pisces/q4.gif",
#         "name": "Selain bawang bombay, yang bisa bikin pipi gue basah tuh…",
#         "type": "q4",
#         "answers": [
#             {
#                 "answer1": "Crush gue punya pacar baru",
#                 "val1": 1,
#                 "answer2": "Liat pocong gak bisa lompat",
#                 "val2": 2,
#                 "answer3": "Diputusin di tahun kelima pacaran",
#                 "val3": 3,
#                 "answer4": "Kalo sahabat gue kenapa-napa",
#                 "val4": 10
#             }
#         ]
#         },
#         {
#         "image": "https://cretivox.com/zodiac/pisces/q5.gif",
#         "name": "Dateng ke perpustakaan buat jualan, dateng ke gue buat belajar…",
#         "type": "q5",
#         "answers": [
#             {
#                 "answer1": "Atur jadwal kegiatan yang rapih",
#                 "val1": 1,
#                 "answer2": "Jadi pusat perhatian",
#                 "val2": 2,
#                 "answer3": "Masak nasi goreng",
#                 "val3": 3,
#                 "answer4": "Bikin ayang seneng",
#                 "val4": 10
#             }
#         ]
#         },
#         {
#         "image": "https://cretivox.com/zodiac/pisces/q6.gif",
#         "name": "Pas di interview kerja lo ditanyain kelebihan, lo bakal jawab...",
#         "type": "q6",
#         "answers": [
#             {
#                 "answer1": "Bisa salto sambil kayang",
#                 "val1": 1,
#                 "answer2": "Bisa selalu ada buat siapapun",
#                 "val2": 10,
#                 "answer3": "Gak kekurangan duit di akhir bulan",
#                 "val3": 2,
#                 "answer4": "Cakep gue kelebihan gue",
#                 "val4": 3
#             }
#         ]
#         },
#         {
#         "image": "https://cretivox.com/zodiac/pisces/q7.gif",
#         "name": "Apa yang bakal gue lakuin kalo diundang ke Podcast Deddy Corbuzier…",
#         "type": "q7",
#         "answers": [
#             {
#                 "answer1": "Siapin mental aja",
#                 "val1": 1,
#                 "answer2": "Ke dokter kulit biar cakep",
#                 "val2": 2,
#                 "answer3": "Siapin baju dari jauh hari",
#                 "val3": 10,
#                 "answer4": "Langsung daftar bimbel",
#                 "val4": 3
#             }
#         ]
#         },
#         {
#         "image": "https://cretivox.com/zodiac/pisces/q8.gif",
#         "name": "Kalo pas SMA ada razia seragam, gue bakal…",
#         "type": "q8",
#         "answers": [
#             {
#                 "answer1": "Bantuin temen gue selagi bisa",
#                 "val1": 10,
#                 "answer2": "Nyelametin diri sendiri",
#                 "val2": 1,
#                 "answer3": "Ngumpet soalnya penakut",
#                 "val3": 2,
#                 "answer4": "Cepuin temen ke guru",
#                 "val4": 3
#             }
#         ]
#         },
#         {
#         "image": "https://cretivox.com/zodiac/pisces/q9.gif",
#         "name": "Mantan gue ahlinya nyakitin gue, kalo gue ahlinya…",
#         "type": "q9",
#         "answers": [
#             {
#                 "answer1": "Setia sama orang yang nyakitin",
#                 "val1": 1,
#                 "answer2": "Cabut kalo udah gak worth it",
#                 "val2": 2,
#                 "answer3": "Fokus ke masa depan",
#                 "val3": 10,
#                 "answer4": "Nutupin rahasia dari si dia",
#                 "val4": 3
#             }
#         ]
#         },
#         {
#         "image": "https://cretivox.com/zodiac/pisces/q10.gif",
#         "name": "Air susu dibalas air tuba, gue lemah kalo orang yang deketin gue…",
#         "type": "q10",
#         "answers": [
#             {
#                 "answer1": "Jiwa seninya tinggi",
#                 "val1": 10,
#                 "answer2": "Perfeksionis banget",
#                 "val2": 1,
#                 "answer3": "Suka anime",
#                 "val3": 2,
#                 "answer4": "Badannya wangi",
#                 "val4": 3
#             }
#         ]
#         }
#         ]
#         return make_response(jsonify(output), 200)
        
# class ResultCancer(Resource):
#     def get(self):
#         pass
        
# class QuizGemini(Resource):
#     def get(self):
#         return make_response(jsonify(gemini_db), 200)
        
# class ResultGemini(Resource):
#     def get(self):
#         return make_response(jsonify(gemini_result_db),200)

# class QuizTaurus(Resource):
#     def get(self):
#         output = [{"test" : "Taurus"}]
#         return make_response(jsonify(output), 200)
        
# class ResultTaurus(Resource):
#     def get(self):
#         pass
        
# class QuizLeo(Resource):
#     def get(self):
#         output = [{"test" : "Leo"}]
#         return make_response(jsonify(output), 200)
        
# class ResultLeo(Resource):
#     def get(self):
#         pass
        
# class QuizAries(Resource):
#     def get(self):
#         output = [{"test" : "Aries"}]
#         return make_response(jsonify(output), 200)
        
# class ResultAries(Resource):
#     def get(self):
#         pass
        
# class QuizScorpio(Resource):
#     def get(self):
#         output = [{"test" : "Scorpio"}]
#         return make_response(jsonify(output), 200)
        
# class ResultScorpio(Resource):
#     def get(self):
#         pass
        
# class QuizCapri(Resource):
#     def get(self):
#         output = [{"test" : "Capri"}]
#         return make_response(jsonify(output), 200)    
        
# class ResultCapri(Resource):
#     def get(self):
#         pass
        
# class QuizSagi(Resource):
#     def get(self):
#         output = [{"test" : "sagitarius"}]
#         return make_response(jsonify(output), 200)  
        
# class ResultSagi(Resource):
#     def get(self):
#         pass
        
# class QuizVirgo(Resource):
#     def get(self):
#         output = [{"test" : "Virgoooo"}]
#         return make_response(jsonify(output), 200)  
    
# class ResultVirgo(Resource):
#     def get(self):
#         pass
    
# class QuizLibra(Resource):
#     def get(self):
#         output = [{"test" : "libra"}]
#         return make_response(jsonify(output), 200)  
        
# class ResultLibra(Resource):
#     def get(self):
#         pass

# api.add_resource(QuizLibra,"/api/zodiak/libra", methods=["GET"]) 
# api.add_resource(QuizVirgo,"/api/zodiak/virgo", methods=["GET"]) 
# api.add_resource(QuizSagi,"/api/zodiak/sagi", methods=["GET"]) 
# api.add_resource(QuizCapri,"/api/zodiak/capri", methods=["GET"]) 
# api.add_resource(QuizScorpio,"/api/zodiak/scorpio", methods=["GET"]) 
# api.add_resource(QuizAries,"/api/zodiak/aries", methods=["GET"]) 
# api.add_resource(QuizLeo,"/api/zodiak/leo", methods=["GET"])        
# api.add_resource(QuizTaurus,"/api/zodiak/taurus", methods=["GET"])
# api.add_resource(QuizCancer,"/api/zodiak/cancer", methods=["GET"])

# #GEMINI
# api.add_resource(QuizGemini,"/api/zodiak/gemini", methods=["GET"])
# api.add_resource(ResultGemini, "/api/zodiak/gemini/result", methods=["GET"])

# #PISCES
# api.add_resource(ResultPisces,"/api/zodiak/pisces/result", methods=["GET"])
# api.add_resource(QuizPisces,"/api/zodiak/pisces", methods=["GET"])

# api.add_resource(ZodiakApi, "/api/zodiak", methods=["GET", "POST","DELETE"])
# api.add_resource(DelData, "/api/zodiak/<id>", methods=["GET","DELETE"])


# if __name__ == "__main__":
#     app.run(debug=True)


# url = 'https://www.youtube.com/watch?v=bYvH-RY5e3U'
# id = url.split("=",1)[1]
# thumbnailurl= 'https://img.youtube.com/vi/'+id + '/maxresdefault.jpg'
# print(thumbnailurl)

# from urltitle import URLTitleReader

# reader = URLTitleReader(verify_ssl=True)

# tit = str(reader.title('https://www.youtube.com/watch?v=zx3-JEb9d5k'))
# print(tit)

dataurl = 'https://www.youtube.com/watch?v=7SqNVv98e8Q&list=RD7SqNVv98e8Q&start_radio=1'
id = dataurl.split("=",2)[1]
for ch in id :
    if ch == "&":
        id = id.split("&",)[0]
        print(id)

# thumbnailurl= 'https://img.youtube.com/vi/'+id + '/maxresdefault.jpg'

from flask import Flask, request, render_template,jsonify, make_response
from flask_cors import CORS
from instagramy import InstagramUser
from flask_restful import Api,Resource
from flask_sqlalchemy import SQLAlchemy
import os
import json


app = Flask(__name__)
api = Api(app)
db = SQLAlchemy(app)
CORS(app)

application = app

filename = os.path.dirname(os.path.abspath(__file__))
database = 'sqlite:///' + os.path.join(filename, 'db.sqlite')
app.config['SQLALCHEMY_DATABASE_URI'] = database 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#GEMINI
f = open('question_gemini.json', encoding='utf-8')
gemini_db = json.load(f)

f = open('result_gemini.json', encoding='utf-8')
gemini_result_db = json.load(f)

#PISCES
f = open('question_pisces.json', encoding='utf-8')
pisces_db = json.load(f)

f = open('result_pisces.json', encoding='utf-8')
pisces_result_db = json.load(f)

#CAPRI
f = open('question_capri.json', encoding='utf-8')
capri_db = json.load(f)

f = open('result_capri.json', encoding='utf-8')
capri_result_db = json.load(f)

#LIBRA
f = open('question_libra.json', encoding='utf-8')
libra_db = json.load(f)

f = open('result_libra.json', encoding='utf-8')
libra_result_db = json.load(f)

#SCORPIO
f = open('question_scorpio.json', encoding='utf-8')
scorpio_db = json.load(f)

f = open('result_scorpio.json', encoding='utf-8')
scorpio_result_db = json.load(f)

#TAURUS
f = open('question_taurus.json', encoding='utf-8')
taurus_db = json.load(f)

f = open('result_taurus.json', encoding='utf-8')
taurus_result_db = json.load(f)

#CANCER
f = open('question_cancer.json', encoding='utf-8')
cancer_db = json.load(f)

f = open('result_cancer.json', encoding='utf-8')
cancer_result_db = json.load(f)

#SAGI
f = open('question_sagi.json', encoding='utf-8')
sagi_db = json.load(f)

f = open('result_sagi.json', encoding='utf-8')
sagi_result_db = json.load(f)

#LEO 
f = open('question_leo.json', encoding='utf-8')
leo_db = json.load(f)

f = open('result_leo.json', encoding='utf-8')
leo_result_db = json.load(f)

#VIRGO
f = open('question_virgo.json', encoding='utf-8')
virgo_db = json.load(f)

f = open('result_virgo.json', encoding='utf-8')
virgo_result_db = json.load(f)


class ZodiakData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_time = db.Column(db.String(100))
    category = db.Column(db.String(100))
    browser = db.Column(db.String(300))
    ip_address = db.Column(db.String(100))
    score = db.Column(db.String(100))

db.create_all()

class ZodiakApi(Resource):
    def post(self):
        data_date_time = request.form.get('date_time')
        data_score = request.form.get('score')
        data_category = request.form.get('category')
        data_browser = request.form.get("browser")
        data_ip_address = request.form.get("ip_address")
        
        data = ZodiakData(date_time = data_date_time, category=data_category, browser = data_browser, ip_address = data_ip_address, score = data_score)
        db.session.add(data)
        db.session.commit()
        
        return make_response({'msg' : 'Success'},200)
    def get(self):
        dataQuery = ZodiakData.query.all()
        
        output = [
            {
            "id" : data.id,
            "data" : {   
                "date_time" : data.date_time,    
                "score" : data.score,    
                "category" : data.category,    
                "browser" : data.browser,    
                "ip_address" : data.ip_address,    
            }
            } for data in dataQuery
            ]
        return make_response(jsonify(output), 200)
    
    def delete(self):
        dataQuery = ZodiakData.query.all()
        for data in dataQuery:
            db.session.delete(data)
            db.session.commit()
        return make_response({'msg' : 'Deleted'},200)
    
class DelData(Resource):
    def delete(self, id):
        dataQuery = ZodiakData.query.get(id)
        db.session.delete(dataQuery)
        db.session.commit()
        return make_response({'msg' : 'Deleted'},200)
    
    def get(self, id):
        dataQuery = ZodiakData.query.get(id)
        output = [
            {
            "id" : dataQuery.id,
            "data" : {   
                "date_time" : dataQuery.date_time,    
                "score" : dataQuery.score,    
                "category" : dataQuery.category,    
                "browser" : dataQuery.browser,    
                "ip_address" : dataQuery.ip_address,    
            }
            } 
            ]
        return make_response(jsonify(output), 200)

#PISCES        
class QuizPisces(Resource):
    def get(self):
        return make_response(jsonify(pisces_db), 200)
    
class ResultPisces(Resource):
    def get(self):
        return make_response(jsonify(pisces_result_db), 200)

#CANCER        
class QuizCancer(Resource):
    def get(self):
        return make_response(jsonify(cancer_db), 200)
        
class ResultCancer(Resource):
    def get(self):
        return make_response(jsonify(cancer_result_db), 200)

#GEMINI        
class QuizGemini(Resource):
    def get(self):
        return make_response(jsonify(gemini_db), 200)
        
class ResultGemini(Resource):
    def get(self):
        return make_response(jsonify(gemini_result_db),200)

#TAURUS
class QuizTaurus(Resource):
    def get(self):
        # output = [{"test" : "Taurus"}]
        return make_response(jsonify(taurus_db),200)
        
class ResultTaurus(Resource):
    def get(self):
        return make_response(jsonify(taurus_result_db),200)

#LEO        
class QuizLeo(Resource):
    def get(self):
        # output = [{"test" : "Leo"}]
        return make_response(jsonify(leo_db),200)
        
class ResultLeo(Resource):
    def get(self):
        return make_response(jsonify(leo_result_db),200)

#ARIES        
class QuizAries(Resource):
    def get(self):
        output = [{"test" : "Aries"}]
        return make_response(jsonify(output), 200)
        
class ResultAries(Resource):
    def get(self):
        pass

#SCORPIO        
class QuizScorpio(Resource):
    def get(self):
        # output = [{"test" : "Scorpio"}]
        return make_response(jsonify(scorpio_db), 200)
        
class ResultScorpio(Resource):
    def get(self):
        return make_response(jsonify(scorpio_result_db), 200)

#CAPRI        
class QuizCapri(Resource):
    def get(self):
        # output = [{"test" : "Capri"}]
        return make_response(jsonify(capri_db), 200)    
        
class ResultCapri(Resource):
    def get(self):
        return make_response(jsonify(capri_result_db), 200)

#SAGI        
class QuizSagi(Resource):
    def get(self):
        # output = [{"test" : "sagitarius"}]
        return make_response(jsonify(sagi_db), 200)  
        
class ResultSagi(Resource):
    def get(self):
        return make_response(jsonify(sagi_result_db), 200)

#VIRGO        
class QuizVirgo(Resource):
    def get(self):
        # output = [{"test" : "Virgoooo"}]
        return make_response(jsonify(virgo_db), 200) 
    
class ResultVirgo(Resource):
    def get(self):
        return make_response(jsonify(virgo_result_db), 200)

#LIBRA    
class QuizLibra(Resource):
    def get(self):
        # output = [{"test" : "libra"}]
        return make_response(jsonify(libra_db), 200)  
        
class ResultLibra(Resource):
    def get(self):
        return make_response(jsonify(libra_result_db), 200)

#LIBRA (NEW)
api.add_resource(QuizLibra,"/api/zodiak/libra", methods=["GET"])
api.add_resource(ResultLibra, "/api/zodiak/libra/result", methods=["GET"])

#VIRGO (NEW)
api.add_resource(QuizVirgo,"/api/zodiak/virgo", methods=["GET"])
api.add_resource(ResultVirgo, "/api/zodiak/virgo/result", methods=["GET"])

#SAGI (NEW)
api.add_resource(QuizSagi,"/api/zodiak/sagi", methods=["GET"])
api.add_resource(ResultSagi, "/api/zodiak/sagi/result", methods=["GET"])

#CAPRI (new)
api.add_resource(QuizCapri,"/api/zodiak/capri", methods=["GET"])
api.add_resource(ResultCapri, "/api/zodiak/capri/result", methods=["GET"])

#SCORPIO (NEW)
api.add_resource(QuizScorpio,"/api/zodiak/scorpio", methods=["GET"]) 
api.add_resource(ResultScorpio, "/api/zodiak/scorpio/result", methods=["GET"])

api.add_resource(QuizAries,"/api/zodiak/aries", methods=["GET"]) 

#LEO (NEW)
api.add_resource(QuizLeo,"/api/zodiak/leo", methods=["GET"])  
api.add_resource(ResultLeo, "/api/zodiak/leo/result", methods=["GET"])

#TAURUS (NEW)
api.add_resource(QuizTaurus,"/api/zodiak/taurus", methods=["GET"])
api.add_resource(ResultTaurus, "/api/zodiak/taurus/result", methods=["GET"])

#CANCER (NEW)
api.add_resource(QuizCancer,"/api/zodiak/cancer", methods=["GET"])
api.add_resource(ResultCancer, "/api/zodiak/cancer/result", methods=["GET"])


#GEMINI
api.add_resource(QuizGemini,"/api/zodiak/gemini", methods=["GET"])
api.add_resource(ResultGemini, "/api/zodiak/gemini/result", methods=["GET"])

#PISCES (new)
api.add_resource(ResultPisces,"/api/zodiak/pisces/result", methods=["GET"])
api.add_resource(QuizPisces,"/api/zodiak/pisces", methods=["GET"])

api.add_resource(ZodiakApi, "/api/zodiak", methods=["GET", "POST","DELETE"])
api.add_resource(DelData, "/api/zodiak/<id>", methods=["GET","DELETE"])

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/data/<usrname>')
def data(usrname):
    user = " "
    # usrname = "cretivox"
    # print("https://instagram.com/"+usrname)
    # session_ig = ["48420109999%3AwYTofPNHOHFmPo%3A15%3AAYdePiWOn0bg3xhjxthCXGZ4ogwQzl2hbuT-QFLjbw" , "51669758945%3AQXe1CxsKaeEl0Z%3A14%3AAYcitzOLUpfaaC582rAfRbhWnz_5QSUIPnSNdhQYOQ"]
    # session_id = "51669758945%3AeaoE7wCFnfMUUz%3A20%3AAYeauCt70M82lH0aKr9c-h3ZnUmHS5lgY6fKsNQGyw"
    session_id = "51669758945%3AT6cRjAuTDvy64m%3A2%3AAYfo4rWMoPVENxrFWy35mdoaB69UTqFNxlk5rqNVHw"
    # try:
    #     user = InstagramUser(usrname, sessionid=session_id)
    #     print("user : ", user)
    # except:
    #     print("user : ", user)
    #     return ("failed instagramy")
    user = InstagramUser(username=usrname,sessionid=session_id)
    # print("user : ", user)
    return (usrname)
    # ig_user = user.fullname
    # follower = user.number_of_followers
    # Photo = user.profile_picture_url
    # verified = user.is_verified
    # print("total followers : " + str(user.number_of_followers))
    # # print(user.profile_picture_url)
    
    # data = user.user_data
    # # print(len(data["edge_owner_to_timeline_media"]["edges"]))
    # total_num_likes = 0
    # total_num_comments = 0
    # for i in range(len(data["edge_owner_to_timeline_media"]["edges"])):
    #     total_num_likes += int(data["edge_owner_to_timeline_media"]["edges"][i]["node"]["edge_liked_by"]["count"])
    #     total_num_comments += int(data["edge_owner_to_timeline_media"]["edges"][i]["node"]["edge_media_to_comment"]["count"])
    # # print("total comment : " + str(total_num_comments))
    # # print("total like : " + str(total_num_likes))
    # value = float(total_num_comments/12) + float(total_num_likes/12)
    # ER_account = (value / user.number_of_followers) * 100
    # # print(ER_account)
    
    # # with open('data.json', 'w') as outfile:
    # #     json.dump(data["edge_owner_to_timeline_media"]["edges"], outfile)
    # jsondat = {
    #     "name" : ig_user,
    #     "follower" : follower,
    #     "ER" : ("%.1f" % ER_account),
    # }
    
    # return jsonify(jsondat)



if __name__ == "__main__":
    app.run(debug=True)